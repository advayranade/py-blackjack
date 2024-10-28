from colorama import Fore, Back, Style


def win_check(total_money, cards_total, bet):
  cards_total = 21
  if cards_total == 21:
    print(Fore.GREEN + "You are the winner!")
    print("Your bet has been doubled!")
    print(Style.RESET_ALL)
    total_money += int(bet)
    return True 
  elif cards_total > 21:
    print("You are the loser!")
    print("Your bet has been has been taken by the dealer!")
    total_money -= int(bet)
    print(total_money)
    return False
  elif cards_total < 21:
    print("You are still under 21. ")
    return "under 21"

  50
  