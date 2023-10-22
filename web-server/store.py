import requests

def get_categories():
  r = requests.get('https://api.escuelajs.co/api/v1/categories')
  print('>> request status code:', r.status_code)
  return r

def to_json(text):
  categories = text.json()

  for item in categories:
    print(item['name'])
  return categories