class User():
    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age
        self.login_attempts = 0
        

    def describe_user(self):
        self.full_name = f'{self.first_name} {self.last_name}'
        print(f"{self.full_name} is {self.age} years old, living in {self.city}")

    def greet_user(self):
        print(f"welcome {self.full_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, city, age):
        super().__init__(first_name, last_name, city, age)
        self.privileges = Privileges()    

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_privileges(self):
        print(f'The administrator have the following privileges:')
        if self.privileges:
            for privilege in self.privileges:
                print(f'-{privilege}')
        else:
            print('This user has no privileges.')

root = Admin('Tom', 'Hankes', 'Huston', '45')
root.describe_user()
root.privileges.show_privileges()
root_privileges = ['can add post','can delete post','can ban user']
root.privileges.privileges= root_privileges
root.privileges.show_privileges()



