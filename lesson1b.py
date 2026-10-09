mynumber = 10
number2 = 10
sum = mynumber + number2
print("The sum of the numbers is:", sum)

# 3. List : A is a collection of items that are inside of square brackets

"""A list is mutable i.e you change the contents of the list. You can add/append alter a list in different ways."""

mylist = ["Russia", "Ukraine", "UK", "Belarus", "Italy", "Germany"]
print(mylist)
print(type(mylist))

mylist.append("Denmark")
mylist.append("Poland")
print(mylist)

# it reverses the ordering of the list 
mylist.reverse()
print(mylist)

# sort function it is used to rearrage based on Alphabetical order
mylist.sort()
print(mylist)

# pop : you can remove based on a given index
mylist.pop(3)
print(mylist)

# remove : Based on the name of an item
mylist.remove("Poland")
print(mylist)

# Extend : used to add multiple items at once
mylist.extend(["Portugal", "Switzerland"])
print(mylist)

# Insert : add an item to a list at a specific index
mylist.insert(0,"Finland")
print(mylist)

# create two list with three items each and join them together to form one big list
list1 = ["tomato", "pepper", "onion"]
list2 = ["hen", "dog", "cat"]
thelist = list1 + list2
print(thelist)
print(type(thelist))

# 4 : Tuple : This is an immutable type of a list : It is unchangable. The way you define a tuple at first it remains the same upto the end.

presidents = ("Uhuru", "Ruto", "Yoweri", "Mnagangwa", "Ramaphosa")
print(presidents)
print(type(presidents))

# Note : Below code will bring an error:
# presidents.append("Suluhu")
# print(presidents)

presidents.pop(2)
print(presidents)