shopping_cart = {}
while True:
    food_product =input("Enter product: ")
    price = int(input("Enter price: "))
    shopping_cart[food_product] = price
    continue_user = input('Do you want to add more [Y/N]: ').strip().upper()
    if continue_user == "N":
        break
    else:
        continue
total = 0
for items in shopping_cart:
    total += shopping_cart[items]
    print(f"item: {items} R{shopping_cart[items]}")
    print("Current price: R" + str(total))
    