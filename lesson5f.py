# We can parameters to the constructor as demostrated below

class Farmer:
    def __init__(self, name, litres, price):
        self.name = name
        self.litres = litres
        self.price = price
    def calculate_payment(self):
        return self.litres * self.price   

# From the above, we can be able to create different objects with different details
farmer1 = Farmer("John", 50, 55)
farmer2 = Farmer("Mary", 38, 55)
farmer3 = Farmer("Joseph", 70, 55)


print("farmer1 :", farmer1.name, farmer1.litres, "He is going to be paid:", farmer1.calculate_payment())
print("farmer2 :", farmer2.name, farmer2.litres, "He is going to be paid:", farmer2.calculate_payment())
print("farmer3 :", farmer3.name, farmer3.litres, "He is going to be paid:", farmer3.calculate_payment())



        