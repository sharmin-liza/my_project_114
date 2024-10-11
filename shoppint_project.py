class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

class Customer(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart.append((product, quantity))
            print(f"Added {quantity} of {product.name} to cart.")
        else:
            print(f"Sorry, only {product.stock} of {product.name} available.")

    def place_order(self, shop):
        for product, quantity in self.cart:
            if product.stock >= quantity:
                order = Order(self, product, quantity)
                shop.process_order(order)
            else:
                print(f"Cannot place order for {product.name}, insufficient stock.")
        self.cart = []  # Empty cart after placing order

class Seller(User):
    def __init__(self, email, password):
        super().__init__(email, password)
        self.products = []

    def add_product(self, name, price, stock):
        product = Product(name, price, stock)
        self.products.append(product)
        print(f"Product {name} added to your store.")

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity

class Shop:
    def __init__(self):
        self.customers = []
        self.sellers = []
        self.products = []

    def register_customer(self, email, password):
        customer = Customer(email, password)
        self.customers.append(customer)
        print(f"Customer account for {email} created.")
        return customer

    def register_seller(self, email, password):
        seller = Seller(email, password)
        self.sellers.append(seller)
        print(f"Seller account for {email} created.")
        return seller

    def add_product(self, seller, product):
        self.products.append(product)
        print(f"Product {product.name} added to shop by {seller.email}")

    def show_products(self):
        available_products = [p for p in self.products if p.stock > 0]
        if available_products:
            for product in available_products:
                print(f"{product.name}: ${product.price} ({product.stock} in stock)")
        else:
            print("No products available.")

    def process_order(self, order):
        product = order.product
        if product.stock >= order.quantity:
            product.stock -= order.quantity
            print(f"Order placed for {order.quantity} of {product.name}. Stock remaining: {product.stock}.")
        else:
            print(f"Order failed: Insufficient stock for {product.name}.")

# Example usage

shop = Shop()

# Registering a customer
customer = shop.register_customer("customer1@example.com", "password123")

# Registering a seller
seller = shop.register_seller("seller1@example.com", "password456")

# Seller adding products
seller.add_product("Laptop", 1000, 5)
seller.add_product("Smartphone", 700, 10)

# Adding products to shop
for product in seller.products:
    shop.add_product(seller, product)

# Customer viewing products
shop.show_products()

# Customer adds product to cart and places an order
customer.add_to_cart(seller.products[0], 2)  # Adding 2 Laptops to cart
customer.place_order(shop)

# Shop displays products after order is placed
shop.show_products()
