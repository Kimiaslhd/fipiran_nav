# fipiran-nav

Simple Python library to fetch Iranian fund NAV data from Fipiran API.

## Installation

```bash
pip install fipiran-nav
```


## Usage
You can save a CSV file to your Desktop by calling `fipiran_nav.fetch_csv("{start_date_str}","{end_date_str}")` with start and end dates, which should be in the format yyyy-mm-dd. For example:
```python
fipiran_nav.fetch_csv("2025-01-01", "2025-01-05")
```
