#HINT: You can call clear() to clear the output in the console.

#The bids dictionary is where we add our name and bid but note that it will be cleared if another person has to enter their name and bid. So it wont store the data.
#The bidding_record dictionary will keep a record of all bids entered. 
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
	highest_bid = 0
	winner = ""
	for bidder in bidding_record:
		bid_amount = bidding_record[bidder]
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder
	print(f"The winner is {winner} with a bid of ${highest_bid}")
	
while  not bidding_finished:
	name = input ("What is your name? ")
	price = int(input("What is your bid? $ "))
	bids[name] = price
	
	should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")
	if should_continue == "no":
		bidding_finished = True
		find_highest_bidder(bids)
	elif should_continue == "yes":
		bids.clear()
	
