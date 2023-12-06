import os

continue_auction = True
auction_list = []

while continue_auction:
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))
  auction_list.append({"name": name, "bid": bid})
  another_bidder = input("Is there another bidder? ")
  if another_bidder == "no":
    continue_auction = False
  os.system("cls")

highest_bid = 0
winner = "no one"
for bidders in auction_list:
  if bidders["bid"] > highest_bid:
    highest_bid = bidders["bid"]
    winner = bidders["name"]

print(f"The winner is {winner} with a bid of ${highest_bid}.")
