import random


def draw_card(deck, draw_number):
  hand = []
  for i in range(draw_number):
    if deck:
      hand.append(deck.pop())
    else:
      break
  return hand, deck

def create_deck():
  suits = ["♥", "♦", "♣", "♠"]
  ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  deck = []
  for suit in suits:
    for rank in ranks:
      deck.append((suit, rank))
  return deck

def show_card(card):
  space = " "
  if len(card[1]) == 2:
    space = ""
  print (f"""
  +-------+
  |{card[1]}     {space}|
  |       |
  |   {card[0]}   |
  |       |
  |{space}     {card[1]}|
  +-------+
  """)


deck = create_deck()

while len(deck) > 0:
  draw_choice = input("How many cards would you like to draw: ")
  if draw_choice.isdigit() and int(draw_choice) <= 52:
    draw_choice = int(draw_choice)
    hand, deck = draw_card(deck, draw_choice)
    for card in hand:
      show_card(card)
  else:
    print("Please enter a number")
    print()

print("We are out of cards")
