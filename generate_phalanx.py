import os
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Set the absolute path to avoid logic breaks
# Using 'os.path.expanduser' ensures it finds YOUR Documents folder automatically
base_path = os.path.join(os.path.expanduser("~"), "Documents", "Sentinel_Empire", "Phalanx_Data")

def ensure_directory():
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"[*] Created missing directory: {base_path}")

def create_contract_pdf(id_num):
    filename = f"Contract_Test_{id_num:03d}.pdf"
    file_path = os.path.join(base_path, filename)
    
    # Generate Mock Metadata
    agency = random.choice(["DOD", "NASA", "GSA", "HHS", "DOE"])
    value = f"${random.randint(100000, 2000000):,}"
    
    c = canvas.Canvas(file_path, pagesize=letter)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 750, f"GOVERNMENT CONTRACT: {agency}-ALPHA-{id_num}")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 730, f"Total Value: {value}")
    c.drawString(100, 710, f"Status: SIMULATED DATA FOR STRESS TEST")
    
    c.drawString(100, 680, "Statement of Work:")
    c.setFont("Helvetica", 10)
    c.drawString(100, 665, "The contractor shall provide automated systems maintenance")
    c.drawString(100, 650, "and infrastructure support for the Sentinel_Empire framework.")
    
    c.save()
    return filename

if __name__ == "__main__":
    ensure_directory()
    print(f"[!] Beginning Level 3 Deployment: Generating 50 Mock Contracts...")
    for i in range(1, 51):
        name = create_contract_pdf(i)
        if i % 10 == 0:
            print(f"    - Progress: {i}/50 files generated.")
    print(f"\n[SUCCESS] Phalanx_Data is now populated at: {base_path}")