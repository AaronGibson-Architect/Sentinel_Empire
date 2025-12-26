import os
import time

# ARCHITECT PATHING
base_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(base_dir, "Phalanx_Data")

def run_reflex_loop():
    """Level 4 Protocol: Deduplicated Integrity Monitoring."""
    print("RCT SIDECAR: MONITORING PERIMETER...")
    reported_breaches = set() # Track already reported files
    
    while True:
        if os.path.exists(data_folder):
            files = os.listdir(data_folder)
            malformed = [f for f in files if not f.startswith("Contract_Test")]
            
            for asset in malformed:
                if asset not in reported_breaches:
                    print(f"\n!!! RCT ALERT: CRITICAL DATA BREACH !!!")
                    print(f"MALFORMED ASSET DETECTED: {asset}")
                    print("STATUS: AWAITING REPAIR PROTOCOL...")
                    reported_breaches.add(asset) # Mark as reported
                    
            # Reset memory if the file is fixed/removed
            reported_breaches = {f for f in reported_breaches if f in files}
            
        time.sleep(2) # Maintain high-speed pulse

if __name__ == "__main__":
    run_reflex_loop()