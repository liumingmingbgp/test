import pygame

class Ship:
    '''管理飞船的类'''
    def __init__(self, ai):
        '''初始化飞船并设置初始位置'''
        self.screen = ai.screen
        self.screen_rect = ai.screen.get_rect()

        # 加载飞船图像并获取其外接矩形    
        self.image = pygame.image.load('/images/ship.bmp')
        self.rect = self.image.get_rect()

        # 将飞船放在屏幕中央
        self.rect.midbottom = self.screen_rect.midbottom

def blitme(self):
    '''在指定位置绘制飞船'''
    self.screen.blit(self.image, self.rect)