import requests, requests_html, scrapy, urllib3, bs4, fake_useragent, gspread, pandas, selenium, stem

page = requests.get('https://scraping.binarynightowl.com/test_install.html')
print(page.text)
