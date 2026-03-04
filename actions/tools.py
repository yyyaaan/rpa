""""tools to be shared"""
import cv2
import numpy as np
from base64 import b64encode
from io import BytesIO
from json import loads
from time import sleep

from dotenv import load_dotenv
from openai import OpenAI
from PIL.Image import Image,  Resampling

load_dotenv()

class Tools:
    """utility class"""

    def __init__(self, delay: int = 5, debug: bool=False):
        self.model = "gpt-4o"
        self.delay = delay
        self.debug = debug
        try:
            self.llm_client = OpenAI()
        except Exception as e:
            print("LLM client initiation failed", e)
            self.llm_client = None

    def delay_with_msg(self, msg: str = None, delay: int = None):
        """simple delay with message and countdown"""
        delay = delay or self.delay
        print(msg or "delaying")
        for i in range(delay):
            print(f"{delay - i:>5}", end="\r")
            sleep(1)
        print(" ")


    def check_image_existence(self, screenshot: Image, local_path: str) -> tuple:
        """
        matching screenshot to the portion that specified by local_path
        returns confidence: float, (x, y)
        """
        screen_np = np.array(screenshot)
        screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)        
        template = cv2.imread(local_path, 0)
        
        tW, tH = template.shape[::-1]
        best_match = None
        
        # saling from 50% to 150% of the screen's size
        for scale in np.linspace(0.5, 1.5, 20):
            resized_w = int(screen_gray.shape[1] * scale)
            resized_h = int(screen_gray.shape[0] * scale)
            resized = cv2.resize(screen_gray, (resized_w, resized_h))
            
            # Ratio to convert back (for coord computation)
            ratio = screen_gray.shape[1] / float(resized_w)
            if resized.shape[0] < tH or resized.shape[1] < tW:
                continue

            result = cv2.matchTemplate(resized, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            if best_match is None or max_val > best_match['confidence']:
                best_match = {
                    'confidence': max_val,
                    'location': max_loc,
                    'ratio': ratio
                }

        if best_match:
            # Get the top-left corner in original screen coordinates
            startX = int(best_match['location'][0] * best_match['ratio'])
            startY = int(best_match['location'][1] * best_match['ratio'])
            
            # Calculate the center of the template in original screen coordinates
            centerX = startX + int((tW * best_match['ratio']) / 2)
            centerY = startY + int((tH * best_match['ratio']) / 2)
            print(f"matching {local_path.split("/")[-1]}, {best_match['confidence']:.2f}", (centerX, centerY)) if self.debug else None
            return best_match['confidence'], (centerX, centerY)
        
        print("no matching found") if self.debug else None
        return 0, (0, 0)
    
    def get_coord_from_llm(self, screenshot: Image, target_element: str) -> tuple:
        """
        use LLM multimodal to find coordinates for item describe in target_element
        return (centerX, centerY)
        """

        orig_width, orig_height, img_str = self.__screenshot_to_base64(screenshot)

        prompt = (
            f"Locate the '{target_element}' in this screenshot."
            "At best accuracy, return the center coordinates as relative percentages between 0.0 and 1.0. "
            "Respond ONLY JSON object containing 'x' and 'y'. Example: {\"x\": 0.52, \"y\": 0.89}"
        )        
        
        print(f"Ussing LLM to locate: '{target_element}'...") if self.debug else None
        
        try:    
            response = self.llm_client.chat.completions.create(
                model=self.model,
                response_format={"type": "json_object"}, # Forces the LLM to return strict JSON
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_str}"}}
                        ]
                    }
                ]
            )
            
            # 4. Parse JSON and map back to the original screen dimensions
            result_str = response.choices[0].message.content
            result = loads(result_str)
            
            rel_x, rel_y = result.get("x", 0.0), result.get("y", 0.0)            
            final_x, final_y = int(rel_x * orig_width), int(rel_y * orig_height)
            
            if self.debug:
                print(f"LLM found it! Relative: (x:{rel_x}, y:{rel_y}) -> Screen Pixels: ({final_x}, {final_y})")
                
            return (final_x, final_y)
            
        except Exception as e:
            if self.debug:
                print(f"LLM extraction failed: {e}")
            return (0, 0)

    def __screenshot_to_base64(self, screenshot: Image, max_dim: int = 1024) -> str:
        """convert screenshot to base64, returns orig_width, orig_height, img_str"""
        orig_width, orig_height = screenshot.size

        max_dim = 1024
        ratio = min(max_dim / orig_width, max_dim / orig_height)
        new_size = (int(orig_width * ratio), int(orig_height * ratio))        
        resized_img = screenshot.resize(new_size, Resampling.LANCZOS)

        buffered = BytesIO()
        resized_img.save(buffered, format="JPEG")
        img_str = b64encode(buffered.getvalue()).decode("utf-8")
        return orig_width, orig_height, img_str