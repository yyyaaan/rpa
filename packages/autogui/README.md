# rpa with `pyautogui` for Windows

> The script may not work inside containers; it expects to see the Windows directly.

RPA solution demo in Python with Spotify on Windows. Not vibe-coded, but AI-empowered. Python structure and coding style is 100% myself.

> __TL;DR__ Use `pyautogui` package and keyboard shortcuts to achieve the goal. `opencv` based image matching provide vision aid only when needed. LLM implemented as a concept verification only.

![Demo](assets/demo.gif)

Foucsing on idea-verifying and targeting for production structure; maybe slightly overweighted as an ealy prototype, some implemtation may be redundant.

## Assumptions

Runing on Windowns 11, and Python 3.13 installation. Virtual environments recommended but not mandantory.

__A Windows Virtual Machine is highly recommended__ to simplify screen scaling and other specifications, in addition to environment isolation, networking and security boundary. The `rdp` file can include keys to lock screen size that greatly improves solution reliability. See example at `example.rdp`

## Quick Start

```
# Bash
source .venv/scripts/activate
python main.py --delay 5 --debug
```

First time run to install pacakges with `pip install -r requirements.txt`. The dependency tree is derived from `pip install pyautogui opencv-python pyscreeze pillow numpy python-dotenv openai`.

## Keyboard Shortcut, OpenCV and LLM

For this task, keyboard shortcut is clear winner.

OpenCV delivers reasonable result. LLM, using "fast" model like gpt-4o can hardly deliver advantage in absence of further refinement.

Providing that the workflow is deterministic and UI is static, the OpenCV is expected to be sufficent.

In result verification, LLM deems to be a reliable and flexible way.


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

If it will be rollout,
- package management, at minimal with piptools
- lint, styling and better parametrization
- telemetry and logging (replacing image saving and print)
- queue system implementation
- retry logic with the whole flow
