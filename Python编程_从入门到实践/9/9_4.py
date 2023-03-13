class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f'餐馆{self.restaurant_name}的特色菜是{self.cuisine_type}!')
        print(f'一共有{self.number_served}人就餐')
    
    def set_number_served(self, number_served):
        self.number_served += number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

    def open_restaurant(self):
        print(f'{self.restaurant_name}正在营业')

restaurant = Restaurant('山河屯', '东北铁锅炖')
restaurant.set_number_served(20)
restaurant.increment_number_served(30)
restaurant.describe_restaurant()
restaurant.open_restaurant()