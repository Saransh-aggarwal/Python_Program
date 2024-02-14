class CreateProduct:
    def __init__(self, Product_name, Base_Price, Available_Quantity):
        self.Product_name = Product_name
        self.Base_Price = Base_Price
        self.Available_Quantity = Available_Quantity

A = CreateProduct("A", 100, 100)
B = CreateProduct("B", 50, 200)
C = CreateProduct("C", 200, 50)

def Add_Product(cart, Product_name, Base_Price, Selected_Quantity):
    cart.append([Product_name, Base_Price, Selected_Quantity, Base_Price * Quantity])
    return cart

def check_quantity(Selected_Product, Quantity):
    if Quantity < Selected_Product.Available_Quantity:
        Selected_Product.Available_Quantity -= Quantity
        return True
    else:
        return False

def display_menu(Products):
    print("\nMain Menu")
    for i in range(len(Products)):
        print(f"{list(Products.keys())[i]}. Product {list(Products.values())[i].Product_name}")
    print("4. Exit")

cart = []
while True:
    Products = {1: A, 2: B, 3: C}
    display_menu(Products)
    Selected_Product = int(input("Enter your choice: "))
    if Selected_Product == 4:
        break
    Quantity = int(input("Quantity: "))

    if not check_quantity(Products.get(Selected_Product), Quantity):
        break
    else:
        Add_Product(cart, Products.get(Selected_Product).Product_name, Products.get(Selected_Product).Base_Price,
                    Quantity)
for i in cart:
    print(f" Product name = {i[0]}\n Base price = {i[1]} \n Quantity = {i[2]} \n Final Price = {i[3]} \n")
