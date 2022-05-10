import requests


class StarWarsAPI:
  def __init__(self, character):
    self.url = f'https://www.swapi.tech/api/people/{character}'
  def get(self):
    r = requests.get(self.url)
    response = r.json()
    if response.get('result'):
      return response['result']
    else:
      return None
  