import tkinter as tk
from datetime import datetime, timezone
import os
import sys

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "keypress_log.txt")
os.makedirs(LOG_DIR, exist_ok=True)

def now_iso_utc():
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")

def safe_write(line: str):
    # Append with a small flush to reduce data loss on crash
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)
        f.flush()
        try:
            os.fsync(f.fileno())
        except Exception:
            pass

def format_event(event):
    ts = now_iso_utc()
    char = event.char if event.char and event.char.isprintable() else ""
    keysym = event.keysym
    return f"{ts}\tkeysym={keysym}\tchar={repr(char)}\n"

def on_key(event):
    # Guard: don't log if window is not focused (shouldn't fire then, but double-check)
    if root.focus_displayof() is None:
        return
    line = format_event(event)
    safe_write(line)
    status_var.set(f"Last key: {event.keysym} at {now_iso_utc()}")

def clear_logs():
    try:
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
        status_var.set("Log cleared.")
    except Exception as e:
        status_var.set(f"Error clearing log: {e}")

def open_log_folder():
    try:
        if sys.platform.startswith("win"):
            os.startfile(os.path.abspath(LOG_DIR))
        elif sys.platform == "darwin":
            os.system(f"open {os.path.abspath(LOG_DIR)}")
        else:
            os.system(f"xdg-open {os.path.abspath(LOG_DIR)}")
    except Exception as e:
        status_var.set(f"Unable to open folder: {e}")

# ---------- UI ----------
root = tk.Tk()
root.title("Safe In-App Key Logger — Authorized Use Only")
root.geometry("700x420")

intro = (
    "This application logs keystrokes ONLY while this window is focused.\n"
    "Use for testing/learning on machines you own or where you have explicit permission.\n"
    "DO NOT log passwords, PINs, or other people's input without written consent."
)
tk.Label(root, text=intro, wraplength=680, justify="left").pack(padx=12, pady=10)

text = tk.Text(root, height=12)
text.pack(fill="both", expand=True, padx=12, pady=(0,8))
text.insert("end", "Click here and type — keystrokes will be logged to logs/keypress_log.txt\n")

status_var = tk.StringVar(value="Focus the window and type. Logs saved to logs/keypress_log.txt")
tk.Label(root, textvariable=status_var, anchor="w").pack(fill="x", padx=8)

btn_frame = tk.Frame(root)
btn_frame.pack(fill="x", padx=8, pady=8)
tk.Button(btn_frame, text="Clear Log", command=clear_logs).pack(side="left")
tk.Button(btn_frame, text="Open Logs Folder", command=open_log_folder).pack(side="left", padx=6)

root.bind_all("<Key>", on_key)
def on_focus_in(_=None):
    status_var.set("Focused: logging enabled (only while focused).")
def on_focus_out(_=None):
    status_var.set("Not focused: logging paused.")
root.bind("<FocusIn>", on_focus_in)
root.bind("<FocusOut>", on_focus_out)

if __name__ == "__main__":
    root.mainloop()

