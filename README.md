# Robotic Process Automation

> Please use dev container.

Monorepo (`uv` workspace) with multiple modules, see `pyproject.toml` files in root and src folders.

```
uv sync --all-packages
uv run autogui
uv run browser_automation
```

## AutoGUI for direct control on windows apps, see /autogui

## Modern Browser Automation

```
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=$HOME/Lab/z-debug-profile
```