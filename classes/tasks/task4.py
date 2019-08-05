class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print('-' + self.first_name +
              '\n-' + self.last_name +
              '\n-' + str(self.age))

    def greet_user(self):
        print('Hello, ' + self.first_name)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def get_login_attempts(self):
        return self.login_attempts


user = User('user1', 'user_last_name', 100)

for i in range(3):
    user.increment_login_attempts()
print(user.get_login_attempts())

user.reset_login_attempts()
print(user.get_login_attempts())
