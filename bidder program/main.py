import art

bids = {}
def collect_bids():
    name = input("What is your name?: ").capitalize()
    actual_bid = int(input("What is your bid?: $"))
    bids[name] = actual_bid
def compare_bids(bidders):
    highest_bidder_value = max(bids.values())
    highest_bidder_key = ""
    for key in bids:
        if bids[key] == highest_bidder_value:
            highest_bidder_key = key
    print(f"The winner is {highest_bidder_key} with a bid of ${highest_bidder_value}")

print(art.logo)
collect_bids()
still_bidding = True
while still_bidding:
    more_bidders = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if more_bidders == "yes":
        print("\n" * 20)
        collect_bids()
    else:
        compare_bids(bids)
        still_bidding = False


