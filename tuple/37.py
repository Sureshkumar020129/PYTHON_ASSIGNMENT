print("37.	Create a list of tuples containing product name, price, and quantity. Calculate the total value of each product")
products = [
    ("Laptop", 1000, 5),
    ("Mouse", 25, 10),
    ("Keyboard", 75, 7),
    ("Monitor", 300, 3),
    ("Headphones", 100, 8)
]

for product in products:
    name, price, quantity = product
    total_value = price * quantity
    print(f"{name}: Total Value = ${total_value}")