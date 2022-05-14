import requests

class YesNoAPI:
  def __init__(self):
    '''
    Initializes the URL for the Yes or No API
    '''
    self.url = 'https://yesno.wtf/api'
  def get(self):
    '''
    Uses the get and json methods of requests to gain access to the data of the API
    '''
    r = requests.get(self.url)
    response = r.json()
    if response.get('answer'):
      return response['answer']
    else:
      return None