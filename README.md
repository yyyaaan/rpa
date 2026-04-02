# Robotic Process Automation

There are two flavors provided

## AutoGUI for direct control on windows apps, see /autogui

## Modern Browser Automation

### Hybrid mode: Local Browser + Container Python Runtime

```
# any reachable web
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=$HOME/Lab/z-debug-profile

"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\temp\chrome_debug" --no-first-run

# chrome://inspect/#remote-debugging
# localhost:92222/json/version
````


