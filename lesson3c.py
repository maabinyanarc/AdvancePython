# Iterative/looping statements.
# Looping is the process of doing a task repetitively until a certain condition is met. In python we have two main looping structures i.e for looping and while loop.

# 1. For loop.
for greeting in range(5):
    print("Hello, ", greeting)

print("==========================")
# Below we give a pre-defined range of values
for x in range(1, 10):
    print("The value of x is: ", x)

print("==========================")
# Below is an example that shows a range with some given steps
for y in range(11, 50, 2):
    print("The value of y is: ", y)

print("==========================")
# By use of the for loop, prompt the user to enter a number three times.
for x in range(3):
    number = int(input("Enter a number: "))
    print("The number is: ", number)
