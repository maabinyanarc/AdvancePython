"""A dictionary in python is a data type that stores value in terms of key-value pair. The key of a dictionary need to be unique or immutable while the value of the dictionary can be an integer, string, list, tuple or even another dictionary. A dictionary is introduced by a use of a curly braces."""

phonebook = {
    "Jena" : 25477452542,
    "Bena" : 25663214621,
    "Tina" : 25754212112,
}

print("My phonebook dictionary is: ", phonebook)

# To access the values of a dictionary we use the key
print("Tina's phone number: ", phonebook["Tina"])

print("=====================")

player = {
    "name" : "Messi",
    "age" : 39,
    "teams" : ["Miami", "PSG", "Argentina"],
    "more" : {
        "children" : 3,
        "networth" : 4.5,
        "citizenship" : ("US", "Spain", "Argentina")
    }
}

# Task: Print out Argentina
print(player["more"]["citizenship"][2])

print("============================")

student_profile = {
    "name" : "Brian",
    "age" : 18,
    "subjects" : ["Python", "Database", "Networking"],
    "detais" : {
        "phone" : 254712345678,
        "location" : "Nairobi",
        "marks" : {
            "Python" : 85,
            "Database" : 78,
            "Networking" : 90
        }
    }

}

# Task 1: Print the student name.
print("The student name: ", student_profile["name"])

# Task 2: Print Databse from the subject list. 
print(student_profile["subjects"][1])

# Task 3: Print the student phone number.
print("Studen's phone number is: ", student_profile["detais"]["phone"])

# Task 4: Print the student location. 
print("student's location is: ", student_profile["detais"]["location"])

# Task 5: Print the student Python mark.
print("student's Python mark is: ", student_profile["detais"]["marks"]["Python"])

# Task 6: Print the student's Networking mark.
print("student's Networking mark is: ", student_profile["detais"]["marks"]["Networking"])

print("=========================================")

# Boolen - It evaluates toeither True or False
isSunny = True
isRaining = False

print("Is today sunny in Nairobi? ", isSunny)
print(type(isSunny))
