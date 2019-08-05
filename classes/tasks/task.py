class Pub():
    def __init__(self, pub_name, cuisine_type):
        self.pub_name = pub_name
        self.cuisine_type = cuisine_type

    def describe_pub(self):
        print('Pub name: ' + self.pub_name +
              '\nCuisine type: ' + self.cuisine_type)

    def open_pub(self):
        print(self.pub_name + ' is now opened')


pub = Pub('Irish pub', 'cuisine')
pub.describe_pub()
pub.open_pub()
