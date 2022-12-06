class Vehicle:
    brand_name = 'BMW'

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_price(cls, name, price):
        # ind_price = dollar * 76
        # create new Vehicle object
        return cls(name, (price * 75))

    def show(self):
        print(self.name, self.price)

class Car(Vehicle):
    def average(self, distance, fuel_used):
        mileage = distance / fuel_used
        print(self.name, 'Mileage', mileage)

bmw_us = Car('BMW X5', 65000)
bmw_us.show()

# # class method of parent class is available to child class
# # this will return the object of calling class
# bmw_ind = Car.from_price('BMW X5', 65000)
# bmw_ind.show()

# # check type
# print(type(bmw_ind))