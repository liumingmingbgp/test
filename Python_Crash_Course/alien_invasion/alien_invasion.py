import sys
import pygame
from settings import Seetings
from ship import Ship

class AlienInvasion:
    '''管理游戏资源和行为的类'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.settings = Seetings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_heigh))
        pygame.display.set_caption('Alien Invasion') 

        self.ship = Ship(self)

    def _chect_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = True         # 向右移动飞船
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.type == pygame.K_LEFT:
                        self.ship.moving_left = False

    def _update_screen(self):
         '''更新屏幕上的图像并切换到新屏幕'''
         self.screen.fill(self.settings.bg_color)
         self.ship.blitme()
         pygame.display.flip()

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._chect_events()
            self.ship.update() 
            self._update_screen()

if __name__ == '__main__':
    '''创建游戏实例并运行游戏'''
    ai = AlienInvasion()
    ai.run_game()