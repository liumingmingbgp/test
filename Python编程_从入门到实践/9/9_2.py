class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'Restaurant name is : {self.restaurant_name}')
        print(f'Cuisine type is : {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is opening now!')

restaurant1 = Restaurant('山河屯', '东北铁锅炖')
restaurant2 = Restaurant('松叶', '烤鸭')
restaurant3 = Restaurant('东来顺', '铜锅涮肉')
restaurants = [restaurant1, restaurant2, restaurant3]

for i in restaurants:
    i.describe_restaurant()

    
