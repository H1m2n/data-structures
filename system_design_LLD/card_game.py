# Requirements ->
# Design a card game by considering the following assumptions:
#
# There should be more than one method of cards distribution such as even distribution, uneven distribution, etc.
# There are multiple situations which could be considered as a winning situation:
# One who finishes all his cards early.
# One who earns the maximum points at the last.
from tokenize import String

from abc import abstractmethod


class X:
    @abstractmethod
    def fuc1(self):
        raise NotImplementedError


class Card:
    def __init__(self, card_id, card_name):
        self.card_id = card_id
        self.card_name = card_name


class CardDistribution:
    def __init__(self, card_obj: Card):
        self.card_obj = card_obj

    def even_distribution(self):
        pass

    def uneven_distribution(self):
        pass


class Player:
    def __init__(self, player_id, player_name):
        self.player_id = player_id
        self.player_name = player_name


class WinningRule:
    def is_all_card_finished(self, player_obj: Player, card_count: int) -> bool:
        pass

    def is_max_point_earned(self):
        pass
