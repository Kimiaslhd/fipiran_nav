import csv
import os
from .core import fetch_date_range

def fetch_csv(start_date, end_date, file_path=None):
    if file_path is None:
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop, f"fipiran_data_{start_date}_to_{end_date}.csv")
    
    data = fetch_date_range(start_date, end_date)
    
    if not data:
        print("No data found")
        return None
    
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        headers = list(data[0].keys())
        writer.writerow(headers)
        
        for record in data:
            writer.writerow(record.values())
    
    print(f"Saved {len(data)} records to: {file_path}")
    return file_path