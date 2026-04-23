import subprocess
import os

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

def open_app(app_name_or_file):
    """
    Opens an application or a file using xdg-open.
    """
    return run_command(f"xdg-open {app_name_or_file}")

def close_app(process_name):
    """
    Closes an application using pkill.
    """
    return run_command(f"pkill -f {process_name}")

def focus_window(window_title):
    """
    Focuses a window by title using wmctrl.
    """
    return run_command(f"wmctrl -a '{window_title}'")

def list_windows():
    """
    Lists all open windows using wmctrl.
    """
    return run_command("wmctrl -l")
