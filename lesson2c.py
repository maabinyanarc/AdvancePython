# Conditional statements
# by the use of an if statement, create a python program that evaluates whether a person can donate blood based on the age and weight. If the age is greater than 15 and the weight is greater than 51, the person can donate blood otherwise the person cannot.
 
age = 14
weight = 50

if age > 15 and weight > 51:
    print("cannot donate blood")
else:
    print("can donate blood")

# how do you pick user input from the terminal.
# we use the input function to pick user input from the terminal

age = int(input("kindly enter your age: "))


print("The entered is: ", age)
print("The data type of age is: ", type(age))


