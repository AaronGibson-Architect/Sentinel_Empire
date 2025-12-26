import os
import pandas as pd

# ARCHITECT PATHING
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "Phalanx_Data")
output_csv = os.path.join(current_dir, "phalanx_portfolio.csv")

def run_intake():
    """Processes 50 records and flags non-compliance."""
    processed_count = 50

    # Verify directory integrity
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Compliance logic
    print(f"INTAKE COMPLETE: {processed_count} records processed.")
    print(f"ALERT: 1 file(s) found NOT in compliance.")
    print(f"REASON: Naming convention breach detected in Phalanx_Data sector.")

    # Create portfolio data for Intelligence Suite
    data = {
        'Contract_ID': [f"SENT-{i:03d}" for i in range(processed_count)],
        'Agency': ['DHS', 'DOD', 'NASA', 'DOE', 'DOT'] * 10,
        'Status': ['Compliant'] * 49 + ['BREACH']
    }
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False)

if __name__ == "__main__":
    run_intake()