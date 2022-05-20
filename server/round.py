import time as t
from _thread import *
import threading
from .game import Game
from .chat import Chat


class Round(object):

    def __init__(self, word, player_drawing, players, game):
        """
        init object
        :param word: str
        :param player_drawing: player_drawing
        :param players: Player[]
        """
        self.word = word
        self.player_drawing = player_drawing
        self.player_guessed = list()
        self.skips = 0
        self.player_scores = {player: 0 for player in players}
        self.time = 75
        self.game=game
        self.chat = Chat(self)
        threading.Timer(1,self.time_thread)

    def skip(self):
        """
        returns true if round skipped threshold met
        :return:bool
        """
        self.skips += 1
        if self.skips > len(self.players) - 2:
            return True
        return False

    def get_scores(self):
        """
        :return:all player scores
        """
        return self.scores

    def get_score(self, player):
        """
        gets players scores
        :param player:Player
        :return:int
        """
        if player in self.player_scores:
            return self.player_scores[player]
        else:
            raise Exception("player not in score list playrs")

    def time_thread(self):
        """
        runs in thread to keeptrack of time
        :return:None
        """
        self.time -= 1
        if self.time <= 0:
            self.end_round("Time is up")

    def guess(self, player, wrd):
        """
        :returns bool if player got guess correct
        :param player: Player
        :param wrd: str
        :return: bool
        """
        correct = wrd == self.word
        if correct:
            self.player_guessed.append(player)
            # TODO implements scoring system there

    def player_left(self, player):
        """
        removes player that left from scores and list
        :param player:Player
        :return:None
        """
        if player in self.player_scores:
            del self.player_scores[player]
        if player in self.player_guessed:
            self.player_guessed.remove(player)
        if player == self.player_drawing:
            self.end_round("Drawing player leaves")

    def end_round(self, msg):
        self.game.round_ended()
