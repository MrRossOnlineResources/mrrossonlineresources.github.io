
def coffeeMachine():

    input("Wake up the machine - enter any key")

    print("Heating Water")

    coffee = 0
    while coffee < 25 or coffee > 125:
        coffee = int(input("How much coffee would you like? (ml)"))

    print(str(coffee) + "ml of Coffee")

    milkwater = ""
    while milkwater != "no":

        milkwater = input("Would you like to add Milk or Water? (milk, water or no)")

        if milkwater == "milk":
            milktype = "none"
            milkquantity = 0
            while milktype != "hot" and milktype != "cold" and milktype != "hot frothed" and milktype != "cold frothed":
                milktype = input("What type of milk would you like, hot milk, cold milk, hot frothed milk or cold frothed milk? (hot, cold, hot frothed, cold frothed)")
            while milkquantity < 25 or milkquantity > 125:
                milkquantity = int(input("How much milk would you like? (ml)"))
            print(str(milkquantity) + "ml of " + milktype + " milk")

        elif milkwater == "water":
            watertype = "none"
            waterquantity = 0
            while watertype != "hot" and watertype != "cold":
                watertype = input("Would you like hot or cold water? (hot, cold)")
            while waterquantity < 25 or waterquantity > 125:
                waterquantity = int(input("How much water would you like? (ml)"))
            print(str(waterquantity) + "ml of " + watertype + " water")

        else:
            print("Entry not valid - options are 'milk', 'water' or 'no'")

    syrupsugar = ""
    while syrupsugar != "no":

        syrupsugar = input("Would you like to add Syrup or Sugar? (syrup, sugar or no)")

        if syrupsugar == "syrup":
            syruptype = "none"
            while syruptype != "vanilla" and syruptype != "caramel" and syruptype != "cinnamon" and syruptype != "chocolate":
                syruptype = input("What flavour syrup would you like, vanilla, caramel, cinnamon or chocolate?")
            print(syruptype + " Syrup")

        elif syrupsugar == "sugar":
            sugarquantity = 0
            while sugarquantity < 1 or sugarquantity > 5:
                sugarquantity = int(input("How much sugar would you like? (cubes)"))
            print(str(sugarquantity) + "Cubes of Sugar")

        else:
            print("Entry not valid - options are 'syrup', 'sugar' or 'no'")

    complete = input("Your order is complete - enter any key to continue or enter 'cancel' to cancel")

    if complete == "cancel":
        print("Cancelled")
        coffeeMachine()

    else:
        print("Coffee Ready")

while True:
    coffeeMachine()

