class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append(MenuItem(name, price))

    def display_menu(self):
        print("\nRestaurant Menu:")
        for item in self.items:
            print(item)

    def get_item(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None


class Order:
    def __init__(self):
        self.ordered_items = []

    def add_to_order(self, item, quantity):
        for i, (existing_item, existing_quantity) in enumerate(self.ordered_items):
            if existing_item.name == item.name:
                self.ordered_items[i] = (existing_item, existing_quantity + quantity)
                print(f"Updated {item.name} quantity to {existing_quantity + quantity}.")
                return
            self.ordered_items.append((item, quantity))
        print(f"{quantity}x {item.name} added to order.")

    def calculate_bill(self):
        total = sum(item.price * quantity for item, quantity in self.ordered_items)
        return total

    def display_order(self):
        print("\nYour Order:")
        for item, quantity in self.ordered_items:
            print(f"{quantity}x {item.name} - ${item.price * quantity:.2f}")
        print(f"Total Bill: ${self.calculate_bill():.2f}")

    def remove_from_order(self, item_name):
        for i, (item, quantity) in enumerate(self.ordered_items):
            if item.name.lower() == item_name.lower():
                del self.ordered_items[i]
                print(f"{item_name} removed from order.")
                return
        print("Item not found in order!")
    
    def select_payment_method(self):
        print("Select Payment Method : 1. Cash, 2. Credit Card, 3.UPI")
        choice =input("Enter your choice (1/2/3):\n")
        methods={"1":"Cash","2":"Credit Card","3":"UPI"}
        print(f"Payment mode is {methods[choice]}")

menu = Menu()
menu.add_item("Burger", 10)
menu.add_item("Pizza", 20)
menu.add_item("Pasta", 30)
menu.add_item("Soda", 40)
menu.display_menu()
order = Order()
while True:
    item_name = input("Enter the item name to order (or 'done' to finish) (or 1 to remote any item): ")
    if item_name=="1":
        data=input("Enter the item name to remove from your list :")
        order.remove_from_order(data)
        item_name = input("Enter the item name to order (or 'done' to finish) (or 1 to remote any item): ")
    if item_name.lower() == 'done':
        order.select_payment_method()
        break
    quantity = int(input(f"Enter the quantity for {item_name}: "))
    order.add_to_order(menu.get_item(item_name), quantity)

order.display_order()
