# Task 7 - Mini Problem: Menu Using Functions

def add_price(prices_list):
    price = float(input("Enter price to add: "))
    prices_list.append(price)
    print("Price added successfully.")

def get_average_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return sum(prices_list) / len(prices_list)

def get_max_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return max(prices_list)


prices = []

while True:
    print("\n1 -> Add price")
    print("2 -> Show average price")
    print("3 -> Show highest price")
    print("q -> Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_price(prices)
    elif choice == "2":
        print("Average price:", get_average_price(prices))
    elif choice == "3":
        print("Highest price:", get_max_price(prices))
    elif choice == "q":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")