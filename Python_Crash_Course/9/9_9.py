class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f'{self.year}{self.make}{self.model}'
        return long_name.title()
    
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!" )

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
    
    def descrbie_battery(self):
        print(f'This car has a {self.battery_size}-KWh battery.')

    def get_range(self):
        if self.battery_size==75:
            range = 260
        elif self.battery_size==100:
            range = 315
        print(f'This car can go approximately {range} miles on a full charge.')

    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            print('Upgrade the battery to 100 KWh.')
        else:
            print('The battery is already upgraded.')

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'roadster', '2019')
my_tesla.battery.descrbie_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.upgrade_battery()
