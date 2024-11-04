# print("The Miles Per Gallon program")
# while True:
#     print()
#     miles = float(input("Enter miles driven:\t\t\t"))
#     gallons = float(input("Enter gallons of gas used:\t"))
#     cost_per_gal = float(input("Enter cost per gallon:\t\t"))
#
#     miles_per_gal = round(miles / gallons, 2)
#     total_cost = round(gallons * cost_per_gal, 1)
#     cost_per_mile = round(total_cost / miles, 1)
#
#     print()
#     print("Miles Per Gallon: \t\t" + str(miles_per_gal))
#     print("Total Gas Cost: \t\t" + str(total_cost))
#     print("Cost Per Mile: \t\t\t" + str(cost_per_mile))
#     print()
#     choice = input("Get entries for another trip (y/n)? ")
#
#     if choice.lower() == "n":
#         break

# print("The Test Scores program")
# menu = "y"
# while menu.lower() == 'y':
#     test_score = ""
#     total_score = 0
#     counter = 0
#     print("Enter test scores")
#     print("Enter 'end' to end input")
#     print("======================")
#     while True:
#         test_score = (input("Enter test score: "))
#         if test_score.lower() == "end":
#             break
#         test_score = int(test_score)
#         if test_score >= 0 and test_score <= 100:
#             total_score += test_score
#             counter += 1
#         else:
#             print("Test score must be from 0 through 100. Try again.")
#
#     average = int(total_score / counter)
#     print("======================")
#     print("Total Score :", total_score)
#     print("Average Score: ", average)
#     print()
#
#     menu = input("Enter another set of test scores (y/n)?")
#     print()

print("Welcome to the Future Value Calculator")
print()
menu = "y"
while menu == "y":

    monthly_investment = int(input("Enter monthly investment: \t\t"))

    if monthly_investment <= 0:
        print("Entry must be greater than 0. Please try again.")
        continue
    yearly_interest_rate = int(input("Enter yearly interest rate: \t"))
    if yearly_interest_rate > 0 or yearly_interest_rate <= 15:
        pass
    else:
        print("Entry must be greater than 0 and less than or equal to 15.\nPlease try again.")


    years = int(input("Enter number of years:\t\t\t"))
    if years <= 0 or years > 50:
        print("Entry must be greater than 0 and less than or equal to 50. \nPlease try again.")
        continue

    monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
        if (i+1) % 12 == 0:
            print("Year = ", ((i % 12) + 1), " Future Value = ", round(future_value, 2))

    menu = input("Continue (y/n)?")



