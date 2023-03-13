class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f'Restaurant name is : {self.restaurant_name}')
        print(f'Cuisine type is : {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is opening now!')

restaurant = Restaurant('山河屯', '东北铁锅炖')
print(restaurant.restaurant_name)
restaurant.describe_restaurant()
restaurant.open_restaurant()