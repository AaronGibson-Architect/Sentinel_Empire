import subprocess, requests, sys, os
MODEL = "qwen2.5-coder:7b"
API = "http://localhost:11434/api/generate"

def fix_code(bad_code, error):
    prompt = f"Fix this Python code based on the error. RETURN ONLY CODE.\n\nCODE:\n{bad_code}\n\nERROR:\n{error}"
    try:
        res = requests.post(API, json={"model": MODEL, "prompt": prompt, "stream": False})
        return res.json()['response'].replace("```python", "").replace("```", "").strip()
    except: return None

if __name__ == "__main__":
    target = sys.argv[1]
    with open(target, 'r') as f: content = f.read()
    print(f"[*] Running {target}...")
    proc = subprocess.run(["python", target], capture_output=True, text=True)
    if proc.returncode != 0:
        print(f"[!] Crash Detected. Engaging AI Reflex...")
        fixed = fix_code(content, proc.stderr)
        if fixed:
            with open(f"repaired_{target}", 'w') as f: f.write(fixed)
            print(f"[+] Fixed code saved to repaired_{target}")
    else: print("[*] Script ran successfully.")
