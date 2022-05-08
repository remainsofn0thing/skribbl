from .game import Game

class Player(object):
    def __init__(self, ip: str, name: str):
        self.game=None
        self.ip = ip
        self.name = name
        self.score = 0

    def update_score(self, x: int):
        self.score += x

    def guess(self, guess: str):
        pass

    def disconnect(self):
        pass

    def get_ip(self):
        return self.ip

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name
