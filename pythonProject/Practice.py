import random

# guess = 0
# number = random.randint(1, 10)
#
# while guess != number:
#     print("Guess a number 1 - 10: ")
#     guess = int(input())
#     if guess == number:
#         print("You win!")
#     elif guess > number:
#         print("Too high. Guess again")
#     else:
#         print("Too low. Guess again.")

# miles = float(input("Enter miles driven:\t\t\t"))
# gallons = float(input("Enter gallons of gas used:\t"))
# cost_per_gal = float(input("Enter cost per gallon:\t\t"))
#
# miles_per_gal = round(miles / gallons, 1)
# total_cost = round(gallons * cost_per_gal, 1)
# cost_per_mile = round(total_cost / miles, 1)
#
# print("Miles Per Gallon: \t\t" + str(miles_per_gal))
# print("Total Gas Cost: \t\t" + str(total_cost))
# print("Cost Per Mile: \t\t\t" + str(cost_per_mile))

# print("Enter 3 test scores")
# print("======================")
# score1 = int(input("Enter test score: "))
# score2 = int(input("Enter test score: "))
# score3 = int(input("Enter test score: "))
#
# total_score = score1 + score2 + score3
# average = total_score // 3
# print("======================")
# print("Your Scores: \t", score1, score2, score3)
# print("Total Score: \t" + str(total_score))
# print("Average Score: \t" + str(average))

print("The Area and Perimeter program")
print()
length = int(input("Please enter the length: "))
width = int(input("Please enter the width: "))
print()
area = length * width
perimeter = 2 * (length + width)

print("Area =", area)
print("Perimeter =", perimeter)
print()
print("Thanks for using this program!")
