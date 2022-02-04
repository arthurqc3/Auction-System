from replit import clear
from art import logo

print(logo)

bid_finished = False
bidders = {}

def highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""

  for bidder in bidding_record:
    bid_amount = int(bidding_record[bidder])
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bid_finished:

  name = input("Qual é o seu nome?:\n")
  bid = input("Qual é a sua oferta?:\n")
  bidders[name] = bid

  next_person = input("Existe outro ofertantes? digite 'sim' ou 'nao':\n").lower()
  clear()

  if next_person == "nao":
    bid_finished = True
    highest_bidder(bidders)
  elif next_person == "sim":
    clear()