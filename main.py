# ===============================
# TASK 1 - Discount Function
# ===============================

def apply_discount(price, discount_percent=5):
    if discount_percent > 60:
        discount_percent = 60
    return price - (price * discount_percent / 100)


# ===============================
# TASK 2 - Recursive Factorial
# ===============================

def factorial(n):
    if n < 0:
        print("Error: Factorial not defined for negative numbers.")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# ===============================
# TASK 3 - GST Lambda
# ===============================

gst = lambda price: price + (0.18 * price)


# ===============================
# TASK 6 - Combined Utility
# ===============================

def process_prices(prices):
    discounted_prices = list(map(lambda x: x * 0.90, prices))
    filtered_prices = list(filter(lambda x: x > 300, discounted_prices))
    return discounted_prices, filtered_prices


# ===============================
# TASK 7 - Menu Functions
# ===============================

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


# ===============================
# MAIN EXECUTION
# ===============================

if __name__ == "__main__":

    # Task 1 Test
    print("Discount Test:", apply_discount(1000, 10))
    print("Default Discount Test:", apply_discount(500))

    # Task 2 Test
    print("Factorial 5:", factorial(5))
    print("Factorial 0:", factorial(0))
    factorial(-3)

    # Task 3 Test
    print("GST on 100:", gst(100))

    # Task 6 Test
    d, f = process_prices([100, 500, 900, 50, 750])
    print("Discounted:", d)
    print("Filtered (>300):", f)

    # Menu
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
            print("Invalid choice.")