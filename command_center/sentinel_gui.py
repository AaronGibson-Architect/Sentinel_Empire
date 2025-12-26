import tkinter as tk
from tkinter import scrolledtext
import subprocess
import os
import threading
import time

# ARCHITECT PATHING
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
last_action_time = 0

def launch_rct():
    """Starts the Level 4 Sidecar in stealth mode."""
    rct_path = os.path.join(base_dir, "phalanx_engine", "sentinel_rct.py")
    process = subprocess.Popen(
        ["python", "-u", rct_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        shell=True,
        creationflags=0x08000000 
    )

    def stream_alerts():
        for line in process.stdout:
            if "RCT ALERT" in line:
                log_display.insert(tk.END, f"{line}\n")
                log_display.see(tk.END)
    
    threading.Thread(target=stream_alerts, daemon=True).start()

def run_script(script_name, folder="", log_verb="ANALYZING"):
    """Level 4 Execution Logic with Verified Verbiage."""
    global last_action_time
    current_time = time.time()
    
    # 5-second hard lockout for hardware noise
    if (current_time - last_action_time) < 5.0:
        return
    
    last_action_time = current_time

    def task():
        try:
            btn_intake.config(state="disabled")
            btn_viz.config(state="disabled")
            btn_git.config(state="disabled")
            
            path = os.path.join(base_dir, folder, script_name)
            log_display.insert(tk.END, f"\n[SYSTEM] {log_verb}: {script_name}...\n")
            log_display.see(tk.END)
            
            result = subprocess.run(f"python \"{path}\"", shell=True, capture_output=True, text=True)
            
            if result.stdout:
                log_display.insert(tk.END, result.stdout)
            if result.stderr:
                log_display.insert(tk.END, f"\n[CRITICAL ERROR]: {result.stderr}")
            
            log_display.see(tk.END)
        finally:
            root.update_idletasks()
            btn_intake.config(state="normal")
            btn_viz.config(state="normal")
            btn_git.config(state="normal")

    threading.Thread(target=task).start()

# GUI INITIALIZATION
root = tk.Tk()
root.title("SENTINEL_EMPIRE: COMMAND CENTER")
# FIX: Removed extra 0 from width
root.geometry("600x500") 
root.configure(bg="#121212")

title_label = tk.Label(root, text="SENTINEL_EMPIRE OPS CENTER", fg="#00FF00", bg="#121212", font=("Courier", 16, "bold"))
title_label.pack(pady=10)

btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack(pady=10)

btn_intake = tk.Button(btn_frame, text="[1] RUN INTAKE", width=25, 
                       command=lambda: run_script("phalanx_intake.py", "phalanx_engine", "ANALYZING"))
btn_intake.pack(pady=5)

btn_viz = tk.Button(btn_frame, text="[2] GENERATE VISUALS", width=25, 
                    command=lambda: run_script("phalanx_visualizer.py", "intelligence_suite", "VISUALIZING"))
btn_viz.pack(pady=5)

btn_git = tk.Button(btn_frame, text="[3] DEPLOY PULSE (GIT)", width=25, 
                    command=lambda: run_script("git_pulse.py", "", "PULSING"))
btn_git.pack(pady=5)

log_display = scrolledtext.ScrolledText(root, width=70, height=15, bg="black", fg="#00FF00", font=("Courier", 10))
log_display.pack(pady=10)

log_display.insert(tk.END, "SENTINEL EMPIRE ONLINE. RCT SIDECAR ACTIVE...\n")
launch_rct()

root.mainloop()