class Cafe:
    def __init__(self):
        # Menu with different prices
        self.menu_items = {
            "yellow tea": 2.5,
            "oolong tea": 2.0,
            "americano": 3.5,
            "red-eye coffee": 3.0,
            "nitro cold brew": 4.0,
        }

        # Initial stock
        self.stock = {
            "yellow tea": 10,
            "oolong tea": 10,
            "americano": 10,
            "red-eye coffee": 10,
            "nitro cold brew": 10
        }

        # Total sales
        self.total_sales = 0.0

        # Placeholder for customer name
        self.guest_name = ""

    def show_menu(self):
        """Display the menu with items and their prices."""
        print("\n---- Cafe Menu ----")
        for item, price in self.menu_items.items():
            print(f"{item.title()}: ${price:.2f}")
        print("--------------------\n")

    def accept_order(self):
        """Accept and process the customer's order."""
        self.show_menu()
        order_item = input(f"{self.guest_name}, what would you like to order? ").lower()

        if order_item in self.menu_items:
            if self.stock[order_item] > 0:
                quantity = int(input("How many would you like? "))
                if quantity <= self.stock[order_item]:
                    self.process_order(order_item, quantity)
                else:
                    print(f"Sorry, only {self.stock[order_item]} {order_item}(s) in available.")
            else:
                print(f"Sorry, we're out of {order_item}.")
        else:
            print(f"Sorry, {order_item} is not on the menu.")

    def process_order(self, item, quantity):
        """Calculate cost, confirm order, and update sales and stock."""
        cost = self.menu_items[item] * quantity
        print(f"Your order: {quantity} {item}(s) for ${cost:.2f}")
        confirmation = input("Would you like to proceed with the order? (yes/no) ").lower()

        if confirmation == "yes":
            self.total_sales += cost
            self.stock[item] -= quantity
            print(f"Thank you, {self.guest_name}. Your order for {quantity} {item}(s) has been placed.")
        else:
            print("Order cancelled.")

    def show_sales(self):
        """Display the total sales amount."""
        print(f"\nTotal Sales: ${self.total_sales:.2f}")

    def show_stock(self):
        """Display the current stock levels."""
        print("\n--- Stock Levels ---")
        for item, quantity in self.stock.items():
            print(f"{item.title()}: {quantity}")
        print("--------------------\n")

    def start(self):
        """Main loop to interact with the customer."""
        self.guest_name = input("Welcome to  lex Cafe! May I have your name? ").capitalize()
        print(f"Hello, {self.guest_name}! It's great to have you here.")

        while True:
            print(f"\n{self.guest_name}, please choose an option:")
            print("1. Place an order")
            print("2. View Sales")
            print("3. View Stock")
            print("4. Exit")

            choice = input("Please select an option: ")

            if choice == "1":
                self.accept_order()
            elif choice == "2":
                self.show_sales()
            elif choice == "3":
                self.show_stock()
            elif choice == "4":
                print(f"Thank you for visiting lex cafe, {self.guest_name}. See you next time!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    cafe = Cafe()
    cafe.start()
class Cafe:
    def __init__(self):
        # Menu with different prices
        self.menu_items = {
            "yellow tea": 2.5,
            "Oolong tea": 2.0,
            "americano": 3.5,
            "red-eye coffee": 3.0,
            "nitro cold brew": 4.0,
        }

        # Initial stock
        self.stock = {
            "yellow tea": 10,
            "Oolong tea": 10,
            "americano": 10,
            "red-eye coffee": 10,
            "nitro cold brew": 10
        }

        # Total sales
        self.total_sales = 0.0

        # Placeholder for customer name
        self.guest_name = ""

    def show_menu(self):
        """Display the menu with items and their prices."""
        print("\n---- Cafe Menu ----")
        for item, price in self.menu_items.items():
            print(f"{item.title()}: ${price:.2f}")
        print("--------------------\n")

    def accept_order(self):
        """Accept and process the customer's order."""
        self.show_menu()
        order_item = input(f"{self.guest_name},Hello,what would you like to order? ").lower()

        if order_item in self.menu_items:
            if self.stock[order_item] > 0:
                quantity = int(input("How many would you like? "))
                if quantity <= self.stock[order_item]:
                    self.process_order(order_item, quantity)
                else:
                    print(f"Sorry, we only have {self.stock[order_item]} {order_item}(s) in stock.")
            else:
                print(f"Sorry, we're out of {order_item}.")
        else:
            print(f"Sorry, {order_item} is not on the menu.")

    def process_order(self, item, quantity):
        """Calculate cost, confirm order, and update sales and stock."""
        cost = self.menu_items[item] * quantity
        print(f"Your order: {quantity} {item}(s) for ${cost:.2f}")
        confirmation = input("Would you like to proceed with the order? (yes/no) ").lower()

        if confirmation == "yes":
            self.total_sales += cost
            self.stock[item] -= quantity
            print(f"Thank you, {self.guest_name}. Your order for {quantity} {item}(s) has been placed.")
        else:
            print("Order cancelled.")

    def show_sales(self):
        """Display the total sales amount."""
        print(f"\nTotal Sales: ${self.total_sales:.2f}")

    def show_stock(self):
        """Display the current stock levels."""
        print("\n--- Stock Levels ---")
        for item, quantity in self.stock.items():
            print(f"{item.title()}: {quantity}")
        print("--------------------\n")

    def start(self):
        """Main loop to interact with the customer."""
        self.guest_name = input("Welcome to lex Cafe! May I have your name? ").capitalize()
        print(f"Hello, {self.guest_name}! It's great to have you here.")

        while True:
            print(f"\n{self.guest_name}, please choose an option:")
            print("1. Place an order")
            print("2. View Sales")
            print("3. View Stock")
            print("4. Exit")

            choice = input("Please select an option: ")

            if choice == "1":
                self.accept_order()
            elif choice == "2":
                self.show_sales()
            elif choice == "3":
                self.show_stock()
            elif choice == "4":
                print(f"Thank you for visiting lex cafe, {self.guest_name}. See you next time!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    cafe = Cafe()
    cafe.start()
