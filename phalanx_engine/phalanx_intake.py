import os, re, csv
from pypdf import PdfReader

# ARCHITECT PATHING: Dynamically find the folder where this script lives
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "Phalanx_Data")
output_csv = os.path.join(base_dir, "phalanx_portfolio.csv")

def run_intake():
    portfolio = []
    if not os.path.exists(data_dir): 
        os.makedirs(data_dir)
        print(f"Created directory: {data_dir}. Drop your PDFs there.")
        return
        
    files = [f for f in os.listdir(data_dir) if f.endswith(".pdf")]
    for file in files:
        try:
            path = os.path.join(data_dir, file)
            reader = PdfReader(path)
            text = reader.pages[0].extract_text()
            agency = re.search(r"(?:CONTRACT|SOLICITATION|Agency):\s*([A-Z]+)", text).group(1)
            value = re.search(r"\$([0-9,.]+)", text).group(1)
            portfolio.append({"Agency": agency, "Value": value, "Source": file})
        except: continue
        
    if portfolio:
        with open(output_csv, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Agency", "Value", "Source"])
            writer.writeheader()
            writer.writerows(portfolio)
    print(f"INTAKE COMPLETE: {len(portfolio)} records processed.")

if __name__ == "__main__": run_intake()
