import fipiran_nav

# Test 1: Basic CSV
print("Test 1: Basic CSV")
path = fipiran_nav.fetch_csv("2025-01-15", "2025-01-16")
print(f"Saved to: {path}\n")

# Test 2: Raw data
print("Test 2: Raw data")
data = fipiran_nav.fetch_date_range("2025-01-15", "2025-01-15")
print(f"Got {len(data)} records\n")

# Test 3: Date range
print("Test 3: Date range")
dates = fipiran_nav.get_all_dates("2025-01-01", "2025-01-05")
print(f"Dates: {dates}")