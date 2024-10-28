def face_card_to_int(card):
  if card in ["Jack", "Queen", "King"]:
    card = 10
  elif card == "Ace":
    card = 11
  return card
