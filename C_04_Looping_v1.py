
# initialize ticket numbers
max_tickets = 5
tickets_sold = 0

while tickets_sold < max_tickets:
    name = input("Name: ")

    # if the name is exit code, break out of loop
    if name == "xxx":
        break

    tickets_sold += 1

if tickets_sold == max_tickets:
    print(f"You have sold all the tickers (ie: {max_tickets} tickets)")
else:
    print(f"You have sold {tickets_sold} / {max_tickets} tickets.")