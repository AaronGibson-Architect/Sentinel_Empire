import os
import pandas as pd
import matplotlib.pyplot as plt

# ARCHITECT PATHING: Reaching across the modular structure
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
csv_path = os.path.join(root_dir, "phalanx_engine", "phalanx_portfolio.csv")

def generate_visuals():
    """Generates visual intelligence from air-gapped data."""
    if not os.path.exists(csv_path):
        print("Error: No portfolio data found. Run Intake first.")
        return

    try:
        # Load the data from the engine sector
        df = pd.read_csv(csv_path)
        
        if df.empty:
            print("Error: Portfolio dataset is empty.")
            return

        # Simple Viz for the Demo: Distribution by Category
        # (Replace 'Agency' with whatever column you are extracting)
        df['Agency'].value_counts().plot(kind='bar', color='purple')
        plt.title("Sentinel_Empire: Portfolio Distribution")
        plt.xlabel("Agency Sector")
        plt.ylabel("Contract Count")
        plt.tight_layout()
        
        # Save locally to maintain air-gap security
        plt.savefig(os.path.join(root_dir, "portfolio_summary.png"))
        print("INTELLIGENCE SUITE: VISUALS GENERATED SUCCESSFULLY.")
        plt.show()

    except Exception as e:
        print(f"VISUALIZER ERROR: {str(e)}")

if __name__ == "__main__":
    generate_visuals()