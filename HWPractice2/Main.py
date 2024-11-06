#Exact Change
cents = int(input("Enter the total amount of change: "))

if cents // 100 > 0:
    dollars = cents // 100
    cents -= dollars * 100
    print("Dollars: \t" + str(dollars))
if cents // 25 > 0:
    quarters = cents // 25
    cents -= quarters * 25
    print("Quarters: \t" + str(quarters))
if cents // 10 > 0:
    dimes = cents // 10
    cents -= dimes * 10
    print("Dimes: \t\t" + str(dimes))
if cents // 5 > 0:
    nickels = cents // 5
    cents -= nickels * 5
    print("Nickels: \t" + str(nickels))
if cents > 0:
    print("Pennies: \t" + str(cents))

#Format Name


#Lucky Numbers