# Conditional statement.
# if...else statement.
 
# number = int(input("Enter your number: "))

# if number > 0:

#    print("The number is positive.")
#else:
#    print("The number is negative.")   

print("=================================")

# create a dictionary with student's details like name, email, admission No and password. Prompt the student to enter the password for him to be able to access the student portal. By use of an if statement, check whether the entered password is correct to navigate him to the portal otherwise if the password entered is incorrect, pass a message to block the student from accessing the student portal.

#student_details = {
#   "email" : "christina1@gmail.com",
#    "admissionNo" : 590038,
#    "password" : "chris$45mm"
#   }
#password = (input("Enter your password: "))

#if password == student_details["password"]:
#    print("login password successful!")
#else: 
#    print("incorrect password, block!")    

print("=================================")

# combining the logical and the comparison operators together.
age = int(input("Enter your current age: "))
has_id = True

if age >= 18 and has_id:
    print("You can join us for function.")
else:
    print("Sorry, you do not qualify to join us.")    

print("============================================")

# Below is an example of a nested if statement:
if age >= 18:
    if has_id:
        print("You qualify. You can joing us")
    else:
        print("You don't qualify because you need an ID")
else:
    print("You don't qualify because you are under age") 

print("==========================================")

# By use of a nested if statement, check whether a person is allowed to drive a vehicle or not. For a person to be able to drive a vehicle, he need to be 18 or above years of age and has a valid driver's license.

age = int(input("Enter your current age: "))
has_valid_dl = True
if age >= 18:
    if has_valid_dl:
        print("You are qualified to drive a vehile.")
    else:
        print("You don't qualify because you need a valid driver's license'.")
else:
    print("You don't qualify to drive, you are under age.")        



