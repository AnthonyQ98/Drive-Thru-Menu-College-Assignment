print("1) Entree")
print("2) Side Dish")
print("3) Drinks")
menu = input("Please select the menu you wish to go to (number):")

tofu = 3.49
cajun = 4.59
buffalo = 3.99
rainbow = 2.99
riceCracker = 0.79
fries = 0.69
zucchini = 1.09
brownRice = 0.59
cafeMocha = 1.99
cafeLatte = 1.99
espresso = 2.49
oolongTea = 0.99

if menu == "1":
    print("Please select from the following:")
    print("1) Tofu Burger")
    print("2) Cajun Chicken")
    print("3) Buffalo Wings")
    print("4) Rainbow Fillet")
    selected = input("Pick a number from the above menu:")
    if selected == "1":
        order = "Tofu Burger"
        price = 3.49
    elif selected == "2":
        order = "Cajun Chicken"
        price = 4.59
    elif selected == "3":
        order = "Buffalo Wings"
        price = 3.99
    elif selected == "4":
        order = "Rainbow Fillet"
        price = 2.99
    quantity = int(input("How many would you like: "))
elif menu == "2":
    print("Please select from the following:")
    print("1) Rice Cracker")
    print("2) No-Salt Fries")
    print("3) Zucchini")
    print("4) Brown Rice")
    selected = input("Pick a number from the above menu:")
    if selected == "1":
        order = "Rice Cracker"
        price = 0.79
    elif selected == "2":
        order = "No-Salt Fries"
        price = 0.69
    elif selected == "3":
        order = "Zucchini"
        price = 1.09
    elif selected == "4":
        order = "Brown Rice"
        price = 0.59
    quantity = int(input("How many would you like: "))
else:
    print("Please select from the following:")
    print("1) Café Mochar")
    print("2) Café Latte")
    print("3) Espresso")
    print("4) Oolong Tea")
    selected = input("Pick a number from the above menu:")
    if selected == "1":
        order = "Café Mochar"
        price = 1.99
    elif selected == "2":
        order = "Café Latte"
        price = 1.99
    elif selected == "3":
        order = "Espresso"
        price = 2.49
    elif selected == "4":
        order = "Oolong Tea"
        price = 0.99
    quantity = int(input("How many would you like: "))

totalBill = quantity * price


print("You have ordered", quantity, order, "and your total bill is €" + str(round(totalBill, 2)))

if menu == "1" or menu == "2":
    print("Enjoy your food, have a nice day!")
else:
    print("Enjoy your drinks, have a nice day!")