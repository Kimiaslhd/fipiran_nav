# fipiran-nav

Simple Python library to fetch Iranian fund NAV data from Fipiran API.

## Installation
type this line in your Command prompt, to install the library:
```bash
pip install fipiran-nav
```


## Usage
After instaling the library, you can simply use command/python to choose you desired date range, and have a saved CSV file on your Desktop (or chosen directory) by calling `fipiran_nav.fetch_csv("{start_date_str}","{end_date_str}")` with start and end dates, which should be in the format yyyy-mm-dd. 

as an example, after Installation, you can type these simple lines in your command prompt to have a csv file containing the data for 2025-01-01 until 2025-01-05, saved on your desktop:
```bash
python
fipiran_nav.fetch_csv("2025-01-01", "2025-01-05")
```
