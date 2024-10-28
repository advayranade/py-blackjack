import random
from time import sleep as pause
from win_check import win_check
from constants import cards, suits
from face_to_int import face_card_to_int as fci
from replay import replay
from colorama import Fore, Back, Style

playing = True
total_money = 100
while playing:
  print(Fore.BLUE + "Hi! Welcome to Blackjack!")
  pause(1.5)
  print("I am your dealer & host, Advay")
  pause(1.5)
  print("First, I will shuffle the deck...")
  print("Shuffling...")
  pause(2)
  shuffle = random.shuffle(cards)
  print("Before we give you your cards, please bet!")
  bet = input(f"You have ${total_money} right now. How much would you like to bet? ")
  print(Style.RESET_ALL)
  while int(bet) > int(total_money):
    print("Your bet exceeded the maximum amount. Please bet again. ")
    bet = input(
      f"You have ${total_money} right now. How much would you like to bet? ")
  if int(bet) < 5:
    print("Your bet went below the minimum amount. Please bet again. ")
    bet = input(
      f"You have ${total_money} right now. How much would you like to bet? ")
  print("I will give you your cards!")
  print("Your cards are ...")
  num_1 = random.choice(cards)
  num_2 = random.choice(cards)
  print(Back.YELLOW + num_1 + " of " + random.choice(suits))
  print(Back.YELLOW + num_2 + " of " + random.choice(suits))
  print(Style.RESET_ALL)
  print("My card is ..")
  dealer_num = random.choice(cards)
  print(dealer_num + " of " + random.choice(suits))
  
  # Change Face Card to Integer
  num_1 = fci(num_1)
  num_2 = fci(num_2)
  
  cards_total = int(num_1) + int(num_2)
  print(Back.YELLOW + f'Your total right now is {cards_total}.')
  print(Style.RESET_ALL)
  action = input(
      "What would you like to do? \n Hit (h) \n Double Down (d) \n Stay (s)? \n Answer here (one letter only): "
  )
  print(action)
  win = False or "under 21"
  while cards_total <= 21:
      if action.lower() == "h":
          num = random.choice(cards)
          card = num + " of " + random.choice(suits)
          print(Back.YELLOW + f"your new card is the {card}")
          print(Style.RESET_ALL)
          num = fci(num)
          cards_total += int(num)
          print(f"Your new total is {cards_total}")
          win = win_check(total_money, cards_total, bet)
          
          if win == "under 21":
              action = input(
                  "What would you like to do next? \n Hit (h) \n Double Down (d) \n Stay (s)? \n Answer here (one letter only): "
              )
          else: 
            rep = replay(playing)
            if rep == 'restart':
              raise StopIteration
      elif action.lower() == "s":
          print(
              "You have now chosen to stay. The dealer will reveal his other card. "
          )
          num_5 = random.choice(cards)
          new_card_dealer = num_5 + " of " + random.choice(suits)
          num_5 = fci(num_5)
          dealer_num = fci(dealer_num)
          dealer_total = int(num_5) + int(dealer_num)
          print("His card is the " + new_card_dealer)
          print("The dealer's total is " + str(dealer_total))
          if dealer_total > 21:
              print("The dealer loses! ")
              print("Your bet will be doubled!")
              total_money += int(bet)
              rep = replay(playing)
              if rep == 'restart':
                break
                raise StopIteration
          elif dealer_total < 21:
              action = "h_dealer"
          elif dealer_total == 21:
              print("The dealer wins!")
              total_money -= int(bet)
              print(total_money)
              rep = replay(playing)
              if rep == 'restart':
                raise StopIteration
      elif action.lower() == "h_dealer":
          new_card_num = random.choice(cards)
          card = new_card_num + " of " + random.choice(suits)
          print(f"The dealer's new card is the {card}")
          new_card_num = fci(new_card_num)
          dealer_total += int(new_card_num)
          print(f"The dealer's new total is {dealer_total}")
          if dealer_total > 21:
              print("The dealer loses! ")
              print("Your bet will be doubled!")
              total_money += int(bet)
              rep = replay(playing)
              if rep == 'restart':
                raise StopIteration
          elif dealer_total < 21:
              action = "h_dealer"
          elif dealer_total == 21:
              print("The dealer wins!")
              total_money -= int(bet)
              print(total_money)
              rep = replay(playing)
              if rep == 'restart':
                raise StopIteration
                          
      elif action.lower() == "d":
        print(f"Your bet has been doubled because of your confidence you have now bet {int(bet)*2} instead of {bet}")
        bet = int(bet)*2
        action = "only_action"
      elif action.lower() == "only_action":
        action = input(
                  "What would you like to do next? \n Hit (h) \n Double Down (d) \n Stay (s)? \n Answer here (one letter only): "
              )
