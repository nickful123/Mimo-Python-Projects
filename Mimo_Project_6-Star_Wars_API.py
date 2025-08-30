import requests

################################################

def fetch_data(option):
  url = f"https://swapi.mimo.dev/api/{option}/"
  data = []
  
  try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print()
    print(f"Successfully fetched {len(data)} entities: ")
    print()
  except requests.HTTPError as e:
    print(f"Error while fetching data: {e}")
    return None
  return data

################################################

print(f"Please choose an entity type:\n(People, Planets, etc)")
option = input().strip().lower()
#print(option)

################################################

data = fetch_data(option)

if data:
  for entity in data:
    print(entity["name"])
else:
  print("Unable to download data")
