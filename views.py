from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Probability:
    def is_displayed(self):
        return self.player.role() == 'A'


class Graph(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Probability,
    Positive,
    ResultsWaitPage,
    Results
]
