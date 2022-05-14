import requests


class StarWarsAPI:
  def __init__(self, character):
    '''
    Initializes the URL for the star wars API
    '''
    self.url = f'https://www.swapi.tech/api/people/{character}'
  def get(self):
    '''
    Uses the get and json methods of requests to gain access to the data of the API
    '''
    r = requests.get(self.url)
    response = r.json()
    if response.get('result'):
      return response['result']
    else:
      return None
  