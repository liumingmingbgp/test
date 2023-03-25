class Seetings:
    '''存储游戏中所有的设置的类'''
    def __init__(self):
        '''初始化游戏的静态设置'''
        self.screen_width = 900
        self.screen_heigh = 600
        self.bg_color = (230, 230,230)

        # 飞船设置        
        self.ship_limit = 2

        # 子弹设置        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60,60)
        self.bullet_allowed = 3

        # 外星人下移速度
        self.fleet_drop_speed = 50
        
        # 游戏速度的增加量
        self.speedup_scale =1.1

        self.initialize_dynamic_settings()  

    def initialize_dynamic_settings(self):
        '''初始化随游戏进行而变化的设置'''
        self.ship_speed = 0.09
        self.bullet_speed = 0.07
        self.alien_speed = 0.05
        # 1表示向右，-1表示向左
        self.fleet_direction = 1

        # 计分
        self.alien_point = 50 

    def increase_speed(self):
        '''加快速度'''
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
