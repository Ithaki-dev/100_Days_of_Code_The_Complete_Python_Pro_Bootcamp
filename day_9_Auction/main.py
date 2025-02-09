#this program is a simple auction program that takes in bids from users and stores them in a dictionary
import art
import os
print(art.logo)
more_bidders = "yes"
auction = {}
while more_bidders == "yes":
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    auction[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    os.system('cls')    
    

if more_bidders == "no":
    total_bid = [bid for bid in auction.values()]
    highest_bid = max(total_bid)
    winner = ""
    for key in auction:
        if auction[key] == highest_bid:
            winner = key
            print(f"The winner is {winner} with a bid of ${highest_bid}")


