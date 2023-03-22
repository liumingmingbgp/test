class Seetings:
    '''存储游戏中所有的设置的类'''
    def __init__(self):
        '''初始化游戏的设置'''
        self.screen_width = 900
        self.screen_heigh = 600
        self.bg_color = (230, 230,230)
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60,60)
        
