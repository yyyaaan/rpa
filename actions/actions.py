"""action set"""
import os
import time
import pyautogui

class Actions:
    """wrapping class for gui automation tasks"""
    debug = True
    esclate_to_llm = False

    def __init__(self, delay: int = 10):
        self.delay = delay

    def __delay__(self):
        print("delaying")
        for i in range(self.delay):
            print(self.delay - i)
            time.sleep(1)
        print(" ")

    def __wait_for_logged_in_spotify(self):
        self.__delay__()
        self.__delay__()
        if self.debug:
            pyautogui.screenshot('x_startup.png')
        try:
            login_btn = pyautogui.locateOnScreen('./assets/login_button.png', confidence=0.5)
            if login_btn is not None:
                raise Exception("Spotify must be logged in already.")
        except:
            pass


    def play_spotify_playlist(self, playlist_name):
        print(f"Opening Spotify to play: {playlist_name}")
        
        # startup
        os.system("start spotify:")
        self.__wait_for_logged_in_spotify()

        # search with hot key
        pyautogui.hotkey('ctrl', 'k')
        self.__delay__()
        pyautogui.write(playlist_name, interval=0.2)
        if self.debug:
            pyautogui.screenshot('x_searching.png')

        # shift-enter to play!
        self.__delay__()
        pyautogui.hotkey('shift', 'enter')
        if self.debug:
            pyautogui.screenshot('x_playing.png')

        # open playlist
        self.__delay__()
        pyautogui.hotkey('enter')


    def __no_run(self):
        # wait a while after type, and it will be selected
        # pyautogui.press('down')
        time.sleep(self.delay)
        pyautogui.press('enter')
        if self.debug:
            pyautogui.screenshot('x_playlist.png')

        # Wait for the playlist page to render
        # start playing... no shortcut???
        time.sleep(self.delay)
        pyautogui.press('enter')
        if self.debug:
            pyautogui.screenshot('x_playing.png')
