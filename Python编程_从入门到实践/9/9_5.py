class User():
    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        self.full_name = f'{self.first_name}{self.last_name}'
        print(f"{self.full_name} is {self.age} years old, living in {self.city}")

    def greet_user(self):
        print(f"welcome {self.full_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User('tian', 'lifang', 'langfang', 30)
user1.describe_user()
user1.greet_user()
print('尝试三次登录')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"\t登录次数: {user1.login_attempts}")
print(f'重置登录次数。。。。。。')
user1.reset_login_attempts()
print(f'\t登录次数: {user1.login_attempts}')