# Robotic Process Automation

Monorepo (`uv` workspace) with multiple modules, see `pyproject.toml` files in root and src folders

## AutoGUI for direct control on windows apps, see /autogui

## Modern Browser Automation

### Hybrid mode: Local Browser + Container Python Runtime

Quick start the dev env, by start the dev contaienr in VSCode (or others)

```
uv run browser-automation
# or
uv run python -m browser_automation.mains
```

```
# any reachable web
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=$HOME/Lab/z-debug-profile

"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome_debug" --no-first-run

# chrome://inspect/#remote-debugging
# localhost:92222/json/version
```


## Recomendation to Review

The short answer is **not yet**. While you have the metadata (name, version, dependencies) and the build backend set up correctly, your current `pyproject.toml` doesn't actually tell Python or your tools that `main.py` is the "start point" of the application.

To turn your project into a runnable command (e.g., typing `browser-automation` in your terminal), you need to add a **Project Script** entry point.

### **1. The Missing Piece: `[project.scripts]`**

Add this section to your `pyproject.toml`. This maps a command name to a specific function inside your code.

```toml
[project.scripts]
# command-name = "package_name.module:function"
browser-automation = "browser_automation.main:main"
```

* **`browser-automation`**: This is the command you'll type in the terminal.
* **`browser_automation.main`**: This points to `src/browser_automation/main.py`.
* **`:main`**: This tells Python to execute a function named `def main():` inside that file.

---

### **2. Updated `pyproject.toml` (Recommended)**

Here is your configuration with the entry point and a few "Modern 2026" standard additions (like the README and explicit source inclusion for Hatchling):

```toml
[project]
name = "browser-automation"
version = "0.1.0"
description = "Scalable Agentic Browser Automation"
readme = "README.md"  # Recommended for documentation
requires-python = ">=3.14"
dependencies = [
    "browser-use>=0.12.6",
    "pydantic-settings>=2.13.1",
]

# This is the "Start Point" configuration
[project.scripts]
browser-automation = "browser_automation.main:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/browser_automation"] # Explicitly tells Hatch where the code is
```

---

### **3. Expected Folder Structure**

For this config to work, your files must be laid out in the "Source Layout" style, which is the industry standard for 2026:

```text
.
├── pyproject.toml
├── README.md
├── .venv/
└── src/
    └── browser_automation/   <-- Note the underscore
        ├── __init__.py       <-- Required to make it a package
        ├── main.py           <-- Must contain: def main(): ...
        └── utils.py
```



---

### **4. How to run it now?**

Once you have added the `[project.scripts]` section and performed a `uv sync`, you have two ways to start your project:

**A. The "Project Command" Way (Best for Dev/Tools)**
Since you defined the script, you can run:
```bash
uv run browser-automation
```
*`uv` will automatically look at your `pyproject.toml`, find the `main:main` mapping, and execute it.*

**B. The "Module" Way (Standard Python)**
If you don't want to use the script entry point yet, you can always run it as a module:
```bash
uv run python -m browser_automation.main
```

### **One Quick Check: Does your `main.py` have a function?**
Ensure your `src/browser_automation/main.py` looks something like this:

```python
def main():
    print("Agentic Browser starting...")
    # Your logic here


if __name__ == "__main__":
    main()
```

Without the `def main():` function, the `[project.scripts]` entry point will throw an error when you try to run it. 

Do you already have a `main()` function defined, or are you currently running code at the top-level of the file?