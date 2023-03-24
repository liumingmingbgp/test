class Seetings:
    '''存储游戏中所有的设置的类'''
    def __init__(self):
        '''初始化游戏的设置'''
        self.screen_width = 900
        self.screen_heigh = 600
        self.bg_color = (230, 230,230)

        # 飞船设置        
        self.ship_speed = 0.09
        self.ship_limit = 2

        # 子弹设置
        self.bullet_speed = 0.07
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60,60)
        self.bullet_allowed = 3

        self.alien_speed = 0.05
        self.fleet_drop_speed = 50
        # 1表示向右，-1表示向左
        self.fleet_direction = 1  
