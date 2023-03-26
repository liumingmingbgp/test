import sys
from time import sleep
import pygame
from settings import Seetings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
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

        # 创建一个存储游戏统计信息的实例,创建记分牌
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # 创建按钮实例
        self.play_button = Button(self, 'PLAY')

    def _chect_events(self):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()                    
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        '''在玩家单击PLAY按钮时开始游戏'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()

            # 清空剩余子弹和外星人
            self.aliens.empty()
            self.bullets.empty()

            # 创建新的一群外星人并让飞船居中
            self._create_fleet()
            self.ship.center_ship()

            # 隐藏鼠标
            pygame.mouse.set_visible(False)

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
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        '''检测子弹和外星人的碰撞并删除外星人和子弹'''
        # 检查是否有子弹击中了外星人，并删除子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_point * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        # print(collisions)
        if not self.aliens:
            # 删除所有子弹并新建一群外星人
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # 提高等级
            self.stats.level += 1
            self.sb.prep_level()

    def _check_aliens_bottom(self):
        '''检测是否有外星人到达了屏幕底部'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_aliens(self):
        '''检查是否有外星人位于屏幕边缘并更新外星人的位置'''
        self._check_fleet_edges()
        self.aliens.update()

        # 检测外星人和飞船之间的碰撞
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        # 调用函数检测是否有外星人到达屏幕底端
        self._check_aliens_bottom()

    def _ship_hit(self):
        '''响应飞船被外星人撞到'''
        if self.stats.ship_left > 0:
            # 飞船数量减1
            self.stats.ship_left -= 1
            # 清空余下的外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人并将飞船放到底部中央
            self._create_fleet()
            self.ship.center_ship()

            # 暂停
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

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

    def _check_fleet_edges(self):
        '''有外星人到达屏幕边缘时采取的措施'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        '''将整群外星人下移并改变方向'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        '''更新屏幕上的图像并切换到新屏幕'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # 显示得分
        self.sb.show_score()

        # 如果游戏处于非活动状态就绘制PLAY按钮
        if not self.stats.game_active:
            self.play_button.draw_button()
            
        pygame.display.flip()

    def run_game(self):
        '''开始游戏的主循环'''
        while True:
            self._chect_events()

            if self.stats.game_active:
                self.ship.update()            
                self._update_bullets()
                self._update_aliens()  

            self._update_screen()

if __name__ == '__main__':
    '''创建游戏实例并运行游戏'''
    ai = AlienInvasion()
    ai.run_game()