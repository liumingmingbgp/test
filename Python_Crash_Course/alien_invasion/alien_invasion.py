import sys
import pygame
from settings import Seetings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def _chect_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()                    
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)

    def _check_key_down_events(self, event):
        '''响应按键'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True 
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_up_events(self, event):
        '''响应按键松开'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False     

    def _fire_bullet(self):
        '''创建一颗子弹并加入编组bullets'''
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet) 

    def _update_bullets(self):
        '''更新子弹的位置并删除消失的子弹'''
        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        '''更新外星人的位置'''
        self.aliens.update()

    def _create_fleet(self):
        '''创建一群外星人'''
        # 创建一个外星人并计算一行可以容纳多少外星人 外星人的间距为外星人宽度
        
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        avilavle_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = avilavle_space_x // (2 * alien_width)

        # 计算屏幕可容纳多少行外星人
        ship_height = self.ship.rect.height
        avilavle_space_y = self.settings.screen_heigh - (3 * alien_height) - ship_height
        number_rows = avilavle_space_y // (2 * alien_height)
        
        # 创建外星人群
        for row_number in range(number_rows):
            for alien_nubmer in range(number_aliens_x):
                self._create_alien(alien_nubmer, row_number)           

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        '''更新屏幕上的图像并切换到新屏幕'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
            
        pygame.display.flip()

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._chect_events()
            self.ship.update()            
            self._update_bullets()
            self._update_aliens()            
            self._update_screen()

if __name__ == '__main__':
    '''创建游戏实例并运行游戏'''
    ai = AlienInvasion()
    ai.run_game()