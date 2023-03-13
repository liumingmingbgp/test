class User():
    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age

    def describe_user(self):
        self.full_name = f'{self.first_name}{self.last_name}'
        print(f"{self.full_name} is {self.age} years old, living in {self.city}")

    def greet_user(self):
        print(f"welcome {self.full_name}!")

user1 = User('张', '三', '北京', '30')
user2 = User('李', '四', '上海', '34')
user3 = User('王', '五', '深圳', '26')
users = [user1, user2, user3]

for i in users:
    i.describe_user()
    i.greet_user()
