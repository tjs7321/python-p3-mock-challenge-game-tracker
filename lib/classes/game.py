from classes.result import Result


class Game:

    all = []

    def __init__(self, title):
        self.title = title
        Game.all.append(self)

    def results(self):
        return [res for res in Result.all if res.game == self]

    def players(self):
        return [res.player for res in Result.all if res.game == self]

    def average_score(self, player):
        scores = []
        for result in Result.all:
            if result.game == self and result.player == player:
                scores.append(result.score)
        if len(scores) == 0:
            return -5000
        else:
            return sum(scores)/len(scores)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, 'title'):
            raise Exception("Cannot change title of the Game.")
        elif isinstance(new_title, str) and 0 < len(new_title):
            self._title = new_title
        else: raise Exception("Title must be string greater than 0 characters.")
