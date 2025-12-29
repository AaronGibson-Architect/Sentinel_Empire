import requests
import datetime

# Sentinel Pulse: Daily Gov Harvest
KEYWORDS = ["SDVOSB", "13 CFR 128", "Subcontracting"]
DATE = datetime.date.today().isoformat()

def harvest_regulations():
    url = f"https://www.federalregister.gov/api/v1/documents.json?conditions[publication_date][is]={DATE}&conditions[term]={KEYWORDS[0]}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        # SOVEREIGN LOGIC: Write result to a physical text file in the Harvest folder
        harvest_path = f"C:/Users/13144/Documents/Sentinel_Empire/Harvest/REG_{DATE}.txt"
        with open(harvest_path, "w") as f:
            for doc in data.get('results', []):
                f.write(f"ALERT: New Regulation Found - {doc['title']}\n")
                f.write(f"Link: {doc['html_url']}\n\n")
            print(f"Harvest complete. File generated: {harvest_path}")
    else:
        print(f"Error connecting to Federal Register: {response.status_code}")

harvest_regulations()