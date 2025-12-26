import os
import pandas as pd
from git import Repo

# ARCHITECT PATHING: Locate root
base_dir = os.path.dirname(os.path.abspath(__file__))
repo = Repo(base_dir, search_parent_directories=True)
csv_path = os.path.join(base_dir, "phalanx_portfolio.csv")

def generate_intelligence_report():
    """Converts local CSV data into a README-ready status update."""
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        # Convert to Markdown table for the GitHub display
        md_report = df.to_markdown(index=False)
        with open(os.path.join(base_dir, "SYSTEM_STATUS.md"), "w") as f:
            f.write(f"# EMPIRE OPS: LIVE INTELLIGENCE\n\nGenerated: 2025-12-25\n\n{md_report}")
        return True
    return False

def execute_pulse(commit_msg="chore: automated system pulse"):
    """Stages, commits, and pushes updates to Sentinel_Empire."""
    try:
        generate_intelligence_report()
        repo.git.add(A=True)  # Stage all changes
        repo.index.commit(commit_msg)
        origin = repo.remote(name='origin')
        origin.push()
        print(f"PULSE SUCCESS: Repository synchronized.")
    except Exception as e:
        print(f"PULSE FAILURE: {str(e)}")

if __name__ == "__main__":
    execute_pulse("feat: architecture synchronized via autonomous pulse")