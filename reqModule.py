import requests
r = requests.get("https://financialmodelingprep.com/api/v3/cik-search/Berkshire?apikey=demo")
print(r.text)
print(r.status_code)