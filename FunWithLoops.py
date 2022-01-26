print("Hey there")
print(2 ** 3 ** 2)


#Checking to see if the number entered is larger than 100
n = int(input("Enter a number here: "))
if n < 100:
    print(False)
elif n>= 100:
    print(True)
    



# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)






# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than current largest_number
# and update largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than current largest_number
# and update largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)




#Alterntely I can use a Python built-in function called max()
# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)





flower = input("Enter a flower: ")

if flower == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
else:
    print("No, I want a big Spathiphyllum!")
    print("Spathiphyllum! Not ", flower ,"!")




"""
if the citizen's income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents (this was the so-called tax relief)
if the income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
Your task is to write a tax calculator.
"""

#User will enter income as a float
income = float(input("Enter the annual income: "))


if income < 85528:
    tax = (income * .18) - 556.02
elif income > 85528:
    tax = .32*(income-85528) + 14839.02
tax = round(tax, 0)

if tax < 0:
    print("The tax is: 0.0 thalers")
else:
    print("The tax is:", tax, "thalers")









"""
Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

if the year number isn't divisible by four, it's a common year;
otherwise, if the year number isn't divisible by 100, it's a leap year;
otherwise, if the year number isn't divisible by 400, it's a common year;
otherwise, it's a leap year.
"""

year = int(input("Enter a year: "))
#User enters year	


#Loop that will check based on calculations and remainder is it is a leap year or not
if year <= 1580:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year!")



