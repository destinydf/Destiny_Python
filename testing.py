print("Hey there")
print(2 ** 3 ** 2)


x =  -1 # hardcode your test data here
x = float(x)
# write your code here
print("y =", (3*x**3)-(2*x**2)+(3*x-1))


fnam = input("May I have your first name, please? ")
lnam = input("May I have your last name, please? ")
print("Thank you.")
print("\nYour name is " + fnam + " " + lnam + ".")


print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")


option1 = float(input("Enter a value here:"))# input a float value for variable a here
option2 = float(input("Enter a value here:"))# input a float value for variable b here

# output the result of addition here
print(option1+option2)
# output the result of subtraction here
print(option1-option2)
# output the result of multiplication here
print(option1*option2)
# output the result of division here
print(option1/option2)
print("\nThat's all, folks!")



x = float(input("Enter value for x: "))

# Write your code here.

print("y =", 1/(x+(1/(x+(1/(x+(1/x)))))))
