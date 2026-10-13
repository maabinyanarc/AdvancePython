class Car:
    pass

# Below we create three cars from our class of Car
car1 = Car()
car2 = Car()
car3 = Car()

print(car1, car2, car3)

# Below we give our objects some attributes
car1.brand = "Toyota"
car1.model = "Camry"

print("car1: ", car1.brand)

# Above we use the dot notation to access the items of an object.

car2.brand = "Honda"
car2.model = "Civic"
print("car2: ", car2.brand, car2.model)

# Create the attribute of objects three of the car.

car3.brand = "BMW"
car3.model = "X6"
print("car3: ", car3.brand, car3.model)