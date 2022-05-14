import starwarsAPI
import yesnoAPI

def main():
  print("=====This program simulates a fight between 2 Star Wars characters, with the help of a random Yes/No Generator============================")
  num1 = int(input("Choose a number between 1 and 83: "))
  num2 = int(input("Choose another number between 1 and 83: "))
  character1 = starwarsAPI.StarWarsAPI(character = num1)
  results1 = character1.get()
  character2 = starwarsAPI.StarWarsAPI(character = num2)
  results2 = character2.get()
  fighter1 = results1['properties']['name']
  fighter2 = results2['properties']['name']
  print(f"\n The Fight is Between {fighter1} and {fighter2}")
  ynAPI = yesnoAPI.YesNoAPI() 
  yesorno = ynAPI.get()
  if yesorno == 'yes':
    print("\n The fight will be won by the taller competitor")
    height1 = int(results1['properties']['height'])
    height2 = int(results2['properties']['height'])
    if height1 > height2:
      print(f'\n{fighter1} Wins!')
    else:
      print(f'\n{fighter2} Wins!')
  else:
    print("\n The fight will be won by the heavier competitor")
    weight1 = int(results1['properties']['mass'])
    weight2 = int(results2['properties']['mass'])
    if weight1 > weight2:
      print(f'{fighter1} Wins!')
    else:
      print(f'{fighter2} Wins!')
      
    
main()

