shopping_cart = []


print("-----------------------------------------")
print("------Shopping List------")
print()
print()
print("""---Menu---
Apples
Bananas
Milk
Cheese
Juice
""")




print("What would you like to buy? ")
print("Enter 'DONE' to stop adding items to the cart")

while True:
    new_item = input("item: ")

    if new_item == "DONE":
        break

    shopping_cart.append(new_item)

print()
print("Here is your cart:")

for item in shopping_cart:
    print(item)

print()
print("-----------------------------------------")