def replay(playing):
  play = input("Do you want to play again?")
  if play.lower() == "no":
    playing = False
    return playing
  elif play.lower() == "yes":
    playing = 'restart'