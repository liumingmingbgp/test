class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f'{self.restaurant_name}的特色菜是{self.cuisine_type}!')
    
    def set_number_served(self, number_served):
        self.number_served += number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

    def open_restaurant(self):
        print(f'{self.restaurant_name}正在营业')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='Ice_Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []
    def show_flavors(self):
        print('以下口味可选：')
        for flavor in self.flavors:
            print(f"-{flavor.title()}")

ice_creame_shop = IceCreamStand('妍妍冰淇淋店')
ice_creame_shop.describe_restaurant()

ice_creame_shop.flavors=['香草味', '草莓味', '榴莲味']
ice_creame_shop.show_flavors()