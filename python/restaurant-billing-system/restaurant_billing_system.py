import time

menu = {
    "pizza": 300,
    "burger": 150,
    "fries": 90,
    "nuggets": 120,
    "diet coke": 40,
    "coke": 30,
    "water": 15
}


class Order:
    def __init__(self):
        self.items = {}   # {"pizza": {"price": 300, "qty": 2}, ...}

    def add_item(self, name, price, quantity):
        if name in self.items:
            self.items[name]["qty"] += quantity
        else:
            self.items[name] = {"price": price, "qty": quantity}

    def get_total(self):
        total = 0
        for name, details in self.items.items():
            total += details["price"] * details["qty"]
        return total


def show_menu():
    print("\nmenu")
    for dish, price in menu.items():
        time.sleep(0.3)
        print(f"{dish} - ₹{price}")


def take_order():
    order = Order()
    while True:
        show_menu()
        dish = input("Enter dish name or 'exit' to finish: ")
        if dish.lower() == "exit":
            break
        if dish in menu:
            qty = int(input(f"Enter quantity for {dish}: "))
            order.add_item(dish, menu[dish], qty)
            print(f"Added {qty} x {dish}")
        else:
            print("Item not on the menu, try again.")
    return order


def save_receipt(name, order):
    with open("receipt.txt", "w",encoding="utf-8") as file:
        file.write(f"Receipt for {name}\n")
        file.write("--------------------------------\n")
        for dish, details in order.items.items():
            file.write(f"{dish} x{details['qty']} - ₹{details['price'] * details['qty']}\n")
        file.write("--------------------------------\n")
        file.write(f"Total: ₹{order.get_total()}\n")


name = input("Enter your name: ")
customer_order = take_order()

print("--------------------------------------------")
print(f"{name}, your total amount is ₹{customer_order.get_total()}")
print("--------------------------------------------")

save_receipt(name, customer_order)
print("Receipt saved to receipt.txt")