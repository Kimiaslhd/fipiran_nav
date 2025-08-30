# fipiran-nav

Simple Python library to fetch Iranian fund NAV data from Fipiran API.

## Installation

```bash
pip install fipiran-nav
```


## Usage
Save a CSV file on your Desktop by calling `fipiran_nav.fetch_csv()` with start and end dates. For example:
```python
fipiran_nav.fetch_csv("2025-01-01", "2025-01-05")
```
