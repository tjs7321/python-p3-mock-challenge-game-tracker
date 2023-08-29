class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if isinstance(new_score, int) and 1 <= new_score <= 5000:
            self._score = new_score
        else: raise Exception("Score must be integer between 1 and 5000.")

    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        from classes.player import Player
        if isinstance(new_player, Player):
            self._player = new_player
        else: raise Exception('Player must be Player instance.')

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        from classes.game import Game
        if isinstance(new_game, Game):
            self._game = new_game
        else: raise Exception('Game must be Game instance.')
