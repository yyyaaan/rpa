# rpa

RPA solution demo in Python with Spotify on Windows.

> __TL;DR__ Use `pyautogui` package and keyboard shortcuts to achieve the goal. `opencv` based image matching provide vision aid only when needed. LLM implemented as a toy prototype.

Not vibe-coded, but consulted Gemini for ideas. Python structure and coding style is 100% myself.

## Assumptions

Runing on Windowns 11, and Python 3.13 installation. Virtual environments recommended but not mandantory.

__A Windows Virtual Machine is highly recommended__ to simplify screen scaling and other specifications, in addition to environment isolation, networking and security boundary. The `rdp` file can include keys to lock screen size that greatly improves solution reliability. See example at `example.rdp`

## Quick Start

```
# Bash or Command Prompt [not powershell]
.\venv\Scripts\activate
pip install pyautogui opencv-python pyscreeze pillow numpy python-dotenv openai
python main.py
```

## Features

Mainly use keyboard shortcut to navigate the app with reasonable (maybe excessive) delay.

Controll gate with OpenCV, by pixel-to-pixel matching with scaling, is implemented, provides meaningful vision check. In `main.py`, setting `vision_mode=True` for `Action` class will display interactive elements and visualize a few tasks.

Experinmental implementation with LLM to locate button and conduct visual check, but not used in the default flow.

## Memo on RPA with Windows App

- keyboard shortcuts are the power tools
- maximized window may help vision approach
- LLM, can help identify the state and possible coords for button, but need more refinements


## Ideas and Improvemennts

- Error handling and result check shall be greatly improved
- Remote VM security to be enhanced, in terms of netowrking and authentication
- LLM implementation to be reviewed carefully and use RBAC as much as possible