from .game import Game


class Player(object):
    def __init__(self, ip: str, name: str):
        """
        init the player obj
        :param ip: str
        :param name:str
        """
        self.game = None
        self.ip = ip
        self.name = name
        self.score = 0

    def set_game(self, game):
        """
        sets the player game association
        :param game:Game
        :return: None
        """
        self.game = game

    def update_score(self, x: int):
        """
        updates a players socre
        :param x: int
        :return: None
        """
        self.score += x

    def guess(self, wrd):
        """
        makes a player guess
        :param wrd: str
        :return: bool
        """
        return self.game.player_guess(self, wrd)

    def disconnect(self):
        """
        call to disconnet player
        :return:
        """
        pass

    def get_ip(self):
        """
        gets player ip address
        :return:str
        """
        return self.ip

    def get_score(self):
        """
        get player score
        :return: int
        """
        return self.score

    def get_name(self):
        """
        get player name
        :return: str
        """
        return self.name
