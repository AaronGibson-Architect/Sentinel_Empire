import tkinter as tk
from tkinter import scrolledtext
import subprocess
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

def run_script(script_name):
    script_path = os.path.join(base_dir, script_name)
    command = f"python \"{script_path}\""
    
    log_display.insert(tk.END, f"\n> EXECUTING: {script_name}...\n")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.stdout: log_display.insert(tk.END, result.stdout)
    if result.stderr: log_display.insert(tk.END, f"LOG ERROR: {result.stderr}")
    log_display.see(tk.END)

root = tk.Tk()
root.title("SENTINEL_EMPIRE: COMMAND CENTER")
root.geometry("600x500")
root.configure(bg="#1a1a1a")

tk.Label(root, text="SENTINEL_EMPIRE OPS CENTER", fg="#00ff00", bg="#1a1a1a", font=("Consolas", 16, "bold")).pack(pady=10)

btn_style = {"font": ("Consolas", 10), "width": 25, "bg": "#333", "fg": "white"}

tk.Button(root, text="[1] RUN INTAKE", command=lambda: run_script("phalanx_intake.py"), **btn_style).pack(pady=5)
tk.Button(root, text="[2] GENERATE VISUALS", command=lambda: run_script("phalanx_visualizer.py"), **btn_style).pack(pady=5)
# Add this button in the 'btn_style' section
tk.Button(root, text="[3] DEPLOY PULSE (GIT)", 
          command=lambda: run_script("git_pulse.py"), 
          **btn_style).pack(pady=5)
log_display = scrolledtext.ScrolledText(root, width=70, height=15, bg="black", fg="#00ff00")
log_display.pack(pady=10)
log_display.insert(tk.END, "SYSTEM ONLINE. AWAITING ARCHITECT COMMANDS...\n")

root.mainloop()
