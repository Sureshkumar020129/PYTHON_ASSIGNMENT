print("36.	Create a dictionary of 5 products and their prices. Print all products whose price is greater than ₹1,000.")
products = {
    "Product 1": 1500,
    "Product 2": 800,
    "Product 3": 2000,
    "Product 4": 1200,
    "Product 5": 900
}
print("Products with price greater than ₹1,000:")
for product, price in products.items():
    if price > 1000:
        print(product + ":", price)