class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + ' miles on it')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can not roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# define child-class
class ElectricCar(Car):
    # __init__ gets info required for creating an instance 'Car'???
    def __init__(self, make, model, year):
        '''
            super().__init__ helps Python to fetch child with parent.
            It tells Python call Car's __init__ method, for getting ElectricCar all Car's attributes
        '''
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
