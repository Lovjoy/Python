one = "one "
two = "two "
three = "three "
four = "four "
five = "five "
six = "six "
seven = "seven "
eight = "eight "
nine = "nine "
ten = "ten "
eleven = "eleven "
twelve = "twelve "
thirteen = "thirteen "
fourteen = "fourteen "
fifteen = "fifteen "
sixteen = "sixteen "
seventeen = "seventeen "
eighteen = "eighteen "
nineteen = "nineteen "
twenty = "twenty "
thirty = "thirty "
forty = "forty "
fifty = "fifty "
sixty = "sixty "
seventy = "seventy "
eighty = "eighty "
ninty = "ninty "
hundred = "hundred "
thousand = "thousand "
for i in range(1, 1001):
    if i // 1000 == 1:
        print(one + thousand, end="")
    if i // 100 == 9:
        print(nine + hundred, end="")
    if i // 100 == 8:
        print(eight + hundred, end="")
    if i // 100 == 7:
        print(seven + hundred, end="")
    if i // 100 == 6:
        print(six + hundred, end="")
    if i // 100 == 5:
        print(five + hundred, end="")
    if i // 100 == 4:
        print(four + hundred, end="")
    if i // 100 == 3:
        print(three + hundred, end="")
    if i // 100 == 2:
        print(two + hundred, end="")
    if i // 100 == 1:
        print(one + hundred, end="")
    if 89 < i % 100 < 100:
        print(ninty, end="")
    if 79 < i % 100 < 90:
        print(eighty,end="")
    if 69 < i % 100 < 80:
        print(seventy, end="")
    if 59 < i % 100 < 70:
        print(sixty, end="")
    if 49 < i % 100 < 60:
        print(fifty, end="")
    if 39 < i % 100 < 50:
        print(forty, end="")
    if 29 < i % 100 < 40:
        print(thirty, end="")
    if 19 < i % 100 < 30:
        print(twenty, end="")
    if i % 100 == 19:
        print(nineteen, end="")
    if i % 100 == 18:
        print(eighteen, end="")
    if i % 100 == 17:
        print(seventeen, end="")
    if i % 100 == 16:
        print(sixteen, end="")
    if i % 100 == 15:
        print(fifteen, end="")
    if i % 100 == 14:
        print(fourteen, end="")
    if i % 100 == 13:
        print(thirteen, end="")
    if i % 100 == 12:
        print(twelve, end="")
    if i % 100 == 11:
        print(eleven, end="")
    if i % 100 == 10:
        print(ten, end="")
    if i % 10 % 10 == 9 and i % 100 != 19:
        print(nine, end="")
    if i % 10 % 10 == 8 and i % 100 != 18:
        print(eight, end="")
    if i % 10 % 10 == 7 and i % 100 != 17:
        print(seven, end="")
    if i % 10 % 10 == 6 and i % 100 != 16:
        print(six, end="")
    if i % 10 % 10 == 5 and i % 100 != 15:
        print(five, end="")
    if i % 10 % 10 == 4 and i % 100 != 14:
        print(four, end="")
    if i % 10 % 10 == 3 and i % 100 != 13:
        print(three, end="")
    if i % 10 % 10 == 2 and i % 100 != 12:
        print(two, end="")
    if i % 10 % 10 == 1 and i % 100 != 11:
        print(one, end="")
    print()
