party = int(input("How many people are in your party?"))

for person in range(party):
    name = input("Enter Name")
    age = int(input("Enter Age"))
    height = float(input("Enter Height"))

    if age >= 14 and height >= 1.35:
        print(name + ", you can ride on both 'The Wickerman' and 'Stealth'")
    elif age >= 14 and height >= 1.25:
        print(name + ", you can ride on 'Stealth'")
    elif age >= 13 and height >= 1.35:
        print(name + ", you can ride on 'The Wickerman'")
    else:
        print("Sorry " + name + ", you are not permitted to ride on our rides today")
