# Create a MenuItem class
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

# Create a Menu class
class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_menu(self):
        print("Menu:")
        for item in self.items:
            print(item)

# Create menu items
pizza = MenuItem("Pizza", 8.99)
burger = MenuItem("Burger", 5.49)
drink = MenuItem("Soda", 1.99)

# Create a menu and add items to it
menu = Menu()
menu.add_item(pizza)
menu.add_item(burger)
menu.add_item(drink)

# Display the menu
menu.show_menu()
