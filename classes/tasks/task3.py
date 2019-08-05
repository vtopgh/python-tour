class Pub():
    def __init__(self, pub_name, cuisine_type):
        self.pub_name = pub_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_pub(self):
        print('Pub name: ' + self.pub_name +
              '\tCuisine type: ' + self.cuisine_type +
              '\tNumber served: ' + str(self.number_served))

    def open_pub(self):
        print(self.pub_name + ' is now opened')

    def set_number_served(self, served_customers):
        self.number_served = served_customers

    def increment_number_served(self, served_customers):
        self.number_served += served_customers


pub = Pub('Irish pub', 'cuisine')
pub.describe_pub()
pub.open_pub()

print('Number served customers: ' + str(pub.number_served))
pub.number_served = 1
print('Number served customers: ' + str(pub.number_served))
pub.set_number_served(5)
print('Number served customers: ' + str(pub.number_served))
pub.increment_number_served(10)
print('Number served customers: ' + str(pub.number_served))
