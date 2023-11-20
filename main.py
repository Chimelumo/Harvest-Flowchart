def main():
  #Starts the app
  try:
      userName = input("Chimelumo ")
      userName = userName
  except Exception as ourException:
      print( "Ooops an error occured", ourException )
  else:
      print( userName )
# Entering the username.
  playAgain = True
# Asking the user if they want to play again.
  while playAgain == True:
    myFavoriteCrops = ["apple", "corn", "cherry"]
    print(myFavoriteCrops)
    print("Welcome to the app")
    thislist = ["day 1", "day 2", "day 3"]
    print(len(thislist))
    crop = "apple"
    print(f"The chosen crop is {crop}")
    crop = "corn"
    print(f"Now the chosen crop is {crop}")
    crop1 = input("What crop do you like: ")
    if crop1 == "apple":
      print("I like apples")
    elif crop1 == "cherry":
      print("I like cherries")
    elif crop1 == "corn":
      print("I like corn") 
    season = ["spring", "summer", "fall", "winter"]
    if season == "spring":
      print("Woohooo!!!! We have enough crops")
    elif season == "winter":
      print("Oh no we don't have enough food")

    playAgain = input("Do you want to play again. Enter y or n: ")
    if playAgain == 'n':
      print("Thanks for playing")
      
    elif playAgain == 'y':
      print("Let's play again")
      main()

main()
