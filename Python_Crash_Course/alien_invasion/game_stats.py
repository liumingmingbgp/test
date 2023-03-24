class GameStats:
    '''跟踪游戏的统计信息'''
    def __init__(self, ai_game):
        '''初始化统计信息'''
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit