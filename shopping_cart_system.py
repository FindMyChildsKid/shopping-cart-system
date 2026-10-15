# Getting today's date
from datetime import date
today = date.today()

# Creating products and prices
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2, 2.5, 1.5, 3, 1, 5]

# Creating empty shopping cart
shopping_cart = []

# Choice 1
def viewProducts():
    print("========== AVAILABLE PRODUCTS ==========")
    print()
    for i in range(6):
        print(str(i+1) + ". " + format(products[i], "10s") + "$" + format(prices[i], ".2f"))

# Choice 2
def addProduct():
    print("Which product would you like to add?")
    print()
    for i in range(6):
        print(str(i+1) + ". " + products[i])
    print()
    while True:
        product_number = int(input("Enter product number: ")) - 1
        if product_number < 0 or product_number > 5:
            print()
            print("Invalid product!")
            print("Please choose a number between 1 and 6.")
        else:
            break
    print()
    shopping_cart.append(products[product_number])
    print(products[product_number] + " was added to your cart!")

# Choice 3
def removeProduct():
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty!")
        print("There is nothing to remove.")
    else:
        print("========== YOUR SHOPPING CART ==========")
        print()
        for i in range(len(shopping_cart)):
            print(str(i+1) + ". " + shopping_cart[i])
        print()
        print("Which item would you like to remove?")
        while True:
            item_number = int(input("Enter item number: ")) - 1
            if item_number < 0 or item_number >= len(shopping_cart):
                print("Not a valid item number.")
            else:
                break
        print()
        print(shopping_cart[item_number] + " was removed from your cart!")
        shopping_cart.pop(item_number)

# Choice 4
def viewShoppingCart():
    if len(shopping_cart) == 0:
        print("Shopping cart is empty.")
        print()
    else:
        print("========== YOUR SHOPPING CART ==========")
        print()
        for i in range(len(shopping_cart)):
            print(str(i+1) + ". " + format(shopping_cart[i], "10s") + "$" + format(prices[products.index(shopping_cart[i])], ".2f"))
        print()
        print("Total Items: " + str(len(shopping_cart)))

# Choice 5
def viewCurrentTotal():
    print("========== CURRENT TOTAL ==========")
    print()
    total = 0
    for i in range(len(shopping_cart)):
        print(format(shopping_cart[i], "10s") + "$" + format(prices[products.index(shopping_cart[i])], ".2f"))
        total += prices[products.index(shopping_cart[i])]
    print()
    print(format("Subtotal:", "10s") + "$" + format(total, ".2f"))

# Choice 6:
def checkout():
    if len(shopping_cart) == 0:
        print("Cannot checkout. Shopping cart is empty")
    else:
        print("========== CHECKOUT ==========")
        print()
        print("Date: " + str(today))
        print()
        total = 0
        for i in range(len(shopping_cart)):
            total += prices[products.index(shopping_cart[i])]
        print(format("Subtotal: ", "15s") + "$" + format(total, ".2f"))
        if total >= 40:
            discount = 15
        elif total >= 20:
            discount = 10
        elif total >= 10:
            discount = 5
        else:
            discount = 0
        print(format("Discount", "15s") + str(discount) + "%")
        amount_saved = total * discount / 100
        print(format("Amount Saved", "15s") + "$" + format(amount_saved, ".2f"))
        print()
        final = total - amount_saved
        print(format("Final Total:", "15s") + "$" + format(final, ".2f"))
        print()
        print("Thank you for shopping!")

# Main system
while True:
    print("========== SMART SHOPPING CART ==========")
    print()
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Shopping Cart")
    print("5. View Current Total")
    print("6. Checkout")
    print()

    # Choice
    choice = int(input("Enter your choice: "))

    if choice == 1:
        viewProducts()
    elif choice == 2:
        addProduct()
    elif choice == 3:
        removeProduct()
    elif choice == 4:
        viewShoppingCart()
    elif choice == 5:
        viewCurrentTotal()
    elif choice == 6:
        checkout()
        break