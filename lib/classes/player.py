from classes.result import Result


class Player:
    all = []

    def __init__(self, username):
        self.username = username
        Player.all.append(self)

    def results(self):
        return [res for res in Result.all if res.player == self]

    def games_played(self):
        return [res.game for res in Result.all if res.player == self]

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([res.game for res in self.results() if res.game == game])

    @classmethod
    def highest_scored(cls, game):
        best_player = cls.all[0]
        if len(cls.all) == 0:
            return None
        for player in cls.all:
            if game.average_score(player) > game.average_score(best_player):
                best_player = player
        return best_player
                

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username
        else: raise Exception("Username must be string between 2 and 16 characters.")
