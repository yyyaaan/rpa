# rpa

RPA solution demo in Python with Spotify on Windows.

TL;DR

> Use `pyautogui` package and keyboard shortcuts to achieve the goal. `opencv` based image matching provide vision aid only when needed. LLM implemented as a toy prototype.

Not vibe-coded, but consulted Gemini for ideas. Python structure and coding style is 100% myself.

## Assumptions

Runing on Windowns 11, and Python 3.13 installation. Virtual environments recommended but not mandantory.

In the dev, a remote VM is provisioned to help simplify screen scaling and other local specifications.

Docker container environment, for obvious reason, not supported. For MacOS, consider alternative approach like Apple Script.

## Quick Start

```
# Bash or Command Prompt [not powershell]
.\venv\Scripts\activate
pip install pyautogui opencv-python pyscreeze pillow numpy python-dotenv openai
python main.py
```

## Memo on RPA with Windows App

- keyboard shortcuts are the power tools
- maximized window may help vision approach
- LLM, can help identify the state and possible coords for button, but need more refinements
