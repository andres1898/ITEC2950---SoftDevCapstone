import requests

url = "https://api.nobelprize.org/2.1/nobelPrizes?nobelPrizeYear=1990&nobelPrizeCategory=pea"

response = requests.get(url)

print(response.text)
print(response.headers)
print(response.status_code)