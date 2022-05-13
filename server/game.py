from .player import Player
from .board import Board
from .round import Round


class Game(object):

    def __init__(self, id, players, thread):
        """
        init the game
        once player threshold is met
        :param id: int
        :param players:list
        """
        self.id = id
        self.players = players
        self.words_used = list()
        self.round = None
        self.board = Board()
        self.player_draw_ind = 0  # will be inc when round_ended
        self.connected_thread = thread
        self.start_new_round()

    def start_new_round(self):
        """
        Starts a new round with a new wrod
        :return: None
        """
        self.round = Round(self.get_word(), self.players[self.player_draw_ind], self.players, self)
        self.player_draw_ind += 1

        if self.player_draw_ind >= len(self.players):
            self.round_ended()
            self.end_game()

    def player_guess(self, player, guess):
        """
        makes the player guess the word
        :param player:Player
        :param guess:Str
        :return:bool
        """
        return self.round.guess(player, guess)

    def player_disconnected(self, player):
        """
        call to clean up objects when player disconnects
        :param player: Player
        :raises: Exception()
        """
        pass

    def skip(self):
        """inc the round skips if skips are grater than trheshold  starts new round
        :return:NOne"""
        if self.round:
            new_round = self.round.skip()
            if new_round:
                self.round_ended()
        else:
            raise Exception("No round started yet")

    def round_ended(self):
        """
        if round ends call this
        :return: None
        """
        self.start_new_round()
        self.board.clear()
        pass

    def end_game(self):
        """
        ends the game
        :return:
        """
        # TODO воплотить
        pass

    def update_board(self, x, y, color):
        """
        calls update method on board
        :param x: int
        :param y: int
        :param color:(int,int,int)
        :return:None
        """
        if not self.board():
            raise Exception("boardd not created")
        self.board.update(x, y, color)
        pass

    def get_word(self):
        """
        gives word that hasn't been used
        :return:str
        """
        # TODO get some list words from somwhere
        pass
