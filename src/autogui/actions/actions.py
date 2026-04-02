"""action set"""
import pyautogui

from os import system
from random import uniform
from time import sleep

from .tools import Tools

class Actions:
    """wrapping class for gui automation tasks"""

    threshold = 0.8
    vision_use_llm_over_opencv = False  # so far OpenCV >> LLM

    def __init__(self, delay: int = 9, vision_mode: bool = False, debug: bool = True):
        self.delay = delay
        self.debug = debug
        self.vision_mode = vision_mode
        self.tools = Tools(self.delay, self.debug)


    def play_spotify_playlist(self, playlist_name):
        """the entry script"""

        if self.vision_mode:
            pyautogui.alert(text='Automatcion will start with vision. Click OK to start.', title='Get Ready', button='OK')

        # startup with system command
        system("start spotify:")
        self.__wait_for_logged_in_spotify()

        # interactive approach that uses openCV and simple Alert
        if self.vision_mode:
            if self.vision_use_llm_over_opencv:
                coord = self.tools.get_coord_from_llm(pyautogui.screenshot(), "header search box")
            else:
                _, coord = self.tools.check_image_existence(pyautogui.screenshot(), "./assets/home_header.png")
            pyautogui.moveTo(*coord, duration=uniform(0.5, 2))
            self.tools.delay_with_msg("let's try click on header", 3)
            pyautogui.click(coord)
            self.tools.delay_with_msg("clicked", 3)

        # search with hot key
        pyautogui.hotkey('ctrl', 'k')
        self.tools.delay_with_msg("wait for search box show up")
        pyautogui.write(playlist_name, interval=uniform(0.01, 0.5))
        
        pyautogui.screenshot('x_searching.png') if self.debug else None

        # shift-enter to play!
        self.tools.delay_with_msg("wait for search results")
        pyautogui.hotkey('shift', 'enter')
        pyautogui.screenshot('x_playing.png') if self.debug else None

        # open playlist
        self.tools.delay_with_msg("prepare to show playlist")
        pyautogui.hotkey('enter')

        # check results
        self.tools.delay_with_msg("ready, prepare to verify results")
        final_screenshot = pyautogui.screenshot()
        conf, coord = self.tools.check_image_existence(final_screenshot, "./assets/expected_outcome.png")
        result_opencv = f'OpenCV is {conf*100:.1f}% that the results are achieved'
        result_llm = "LLM evaluation: " + self.tools.check_results_with_llm(final_screenshot)
        print(result_opencv)
        print(result_llm)
        if self.vision_mode:
            pyautogui.moveTo(*coord, duration=uniform(0.5, 1.5))
            pyautogui.alert(
                text=result_opencv + "  " + result_llm,
                title='Automation Completed',
                button='OK'
            )


    def __wait_for_logged_in_spotify(self):
        """"utility to check if spotify is logged in"""
        self.tools.delay_with_msg("starting spotify...")
        self.tools.delay_with_msg("hold on... starting spotify...")
        
        pyautogui.screenshot('x_startup.png') if self.debug else None
        screen = pyautogui.screenshot()
        confidence, coord = self.tools.check_image_existence(screen, "./assets/login_button.png")
        if confidence > self.threshold:
            print("stopping")
            pyautogui.click(coord)
            pyautogui.alert(text='Spotify not logged in. Please copmlete login', title='Login Required', button='OK')
            raise Exception("Spotify is not logged in. Please complete login and retry")
