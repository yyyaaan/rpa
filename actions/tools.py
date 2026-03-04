""""tools to be shared"""
import cv2
import numpy as np
from time import sleep
from PIL.Image import Image

class Tools:

    def __init__(self, delay: int = 5, debug: bool=False):
        self.delay = delay
        self.debug = debug

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
    