from art import logo

print(logo)

print("Welcome to Blind Auction!")

bid_amount = {}

bid_more = True
while bid_more:
    name = input("Please enter your name: ")
    bid = int(input("Kindly enter your bid amount: $"))

    bid_amount[name] = bid

    # print(bid_amount)

    another_bidder = input("Are there more people to bid? Type y for Yes or any key for No: ").lower()
    if not another_bidder == 'y':
        bid_more = False

highest = 0
for key in bid_amount:
    find_highest = bid_amount[key]
    if find_highest > highest:
        highest = find_highest
# print(highest)

# print(bid_amount)

print(max(bid_amount, key=bid_amount.get))