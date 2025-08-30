import requests
from datetime import datetime, timedelta

def get_all_dates(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    
    dates = []
    current = start
    while current <= end:
        dates.append(current.strftime('%Y-%m-%d'))
        current += timedelta(days=1)
    return dates

def fetch_api_data(date_str):
    url = f"https://fund.fipiran.ir/api/v1/fund/fundcompare?date={date_str}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, verify=False, timeout=30)
        if response.status_code == 200:
            data = response.json()
            if 'items' in data:
                return data['items']
        return []
    except:
        return []

def fetch_date_range(start_date, end_date):
    dates = get_all_dates(start_date, end_date)
    all_data = []
    
    for date_str in dates:
        print(f"Fetching {date_str}...")
        items = fetch_api_data(date_str)
        for item in items:
            item['fetch_date'] = date_str
        all_data.extend(items)
    
    return all_data