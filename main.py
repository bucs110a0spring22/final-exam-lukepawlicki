import requests
import starwarsAPI

def main():
  print("=====This Program Takes an Inputted Star Wars Character and Changes\n his/her Name to a Random Name=======================================")
  check = "NO"
  while check == "NO":
    character = int(input("Choose a number between 1 and 83: "))
    swAPI = starwarsAPI.StarWarsAPI(character = character)
    results = swAPI.get()
    print(results['properties']['name'])
    check = input("Type YES if you would like to keep this character, Type NO if you want a new character: ") 
    
  



main()