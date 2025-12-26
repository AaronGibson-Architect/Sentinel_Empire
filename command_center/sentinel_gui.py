import os
from git import Repo

# ARCHITECT PATHING
base_dir = os.path.dirname(os.path.abspath(__file__))
repo = Repo(base_dir)

def execute_pulse(message="chore: system synchronized"):
    """Stages only tracked files, respecting the .gitignore shield."""
    try:
        # Stage all changes that aren't ignored
        repo.git.add(u=True) # Adds modified/deleted files
        repo.git.add('.')    # Adds new files NOT in .gitignore
        
        if repo.is_dirty():
            repo.index.commit(message)
            origin = repo.remote(name='origin')
            origin.push()
            print(f"PULSE SUCCESS: {message}")
        else:
            print("PULSE SKIPPED: No new architectural changes.")
    except Exception as e:
        print(f"PULSE ERROR: {e}")

if __name__ == "__main__":
    execute_pulse("feat: architecture hardened and synchronized")