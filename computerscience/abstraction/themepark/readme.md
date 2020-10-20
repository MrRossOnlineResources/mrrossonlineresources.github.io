# Theme Park

Five friends are going to a theme park for a day. Upon entry they are told that the different rides have different requirements for age and height. To go on Stealth you must be 1.25 meters tall and over 14 years old; whereas to ride on The Wickerman you must be over 1.35 meters tall and over 13 Years old. Amy is 13 years old and 1.2m tall, Charlie is 14 years old and 1.3m tall, Ben is 13 and is 1.35m tall and finally Daphne is 14 years old and 1.35m tall. Write an algorithm in Psuedo Code that will tell you who can ride on which rides.

Below is the code written in Python, use this and the paragraph above to write the algorithm in Psuedo Code

```
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
```
