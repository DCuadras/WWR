shop_cart = []

print()
print("""------------Shopping List------------")
Choose a number for the action you would like to do:
1: Add to Cart
2: Remove from Cart
3: View Cart
0: Exit Cart
""")

option = int(input("Enter an Option "))

while option != 0:
    if option == 1:
        item = input("What would you like to buy? ")
        shop_cart.append[item]
        print("{item} has been added to the cart.")
    elif option == 2:
        del(shop_cart[item])
    
    elif option == 3:
        for item in shop_cart:
            print(item, ":", shop_cart[item])
    
    elif option != 0:
        print("You didn't enter a valid option")
    option = int(input("Enter an option: "))
else:
    print("Shopping Cart Now Closed, Thank You For Shopping With Us!")


