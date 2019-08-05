class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print('-' + self.first_name +
              '\n-' + self.last_name +
              '\n-' + str(self.age))

    def greet_user(self):
        print('Hello, ' + self.first_name)


user = User('user1', 'user_last_name', 100)
user.describe_user()
user.greet_user()