import pandas as pd
import matplotlib.pyplot as plt
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base_dir, "phalanx_portfolio.csv")

def generate_report():
    if not os.path.exists(csv_path): 
        print("Error: No portfolio data found. Run Intake first.")
        return
        
    df = pd.read_csv(csv_path)
    df['Value'] = df['Value'].replace(r'[\$,]', '', regex=True).astype(float)
    summary = df.groupby('Agency')['Value'].sum()
    
    plt.figure(figsize=(10, 6))
    summary.plot(kind='bar', color='#9b59b6', edgecolor='black')
    plt.title('Sentinel_Empire: Portfolio Distribution', fontsize=14)
    plt.ylabel('Total Contract Value ($)')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__": generate_report()
