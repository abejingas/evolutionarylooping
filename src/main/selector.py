from abc import ABCMeta, abstractmethod
from math import ceil

from src.main.generation import Generation


class Selector(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def select(self, generation):
        pass


class TournamentSelector(Selector):

    def __init__(self, max_population, tournament_rounds = None):
        self.max_population = max_population
        if not tournament_rounds:
            self.tournament_rounds = int(ceil(max_population * 0.2))
        else:
            if tournament_rounds < 1:
                self.tournament_rounds = int(ceil(max_population * tournament_rounds))
            else:
                self.tournament_rounds = tournament_rounds

    def select(self, generation):
        ranking = []
        for player1 in generation.individuals:
            defeats = 0
            for _ in range(self.tournament_rounds):
                player2 = generation.retrieve_partner(player1)
                if player2 < player1:
                    defeats += 1
            ranking.append((defeats, player1))
        ranking.sort()
        selected_generation = Generation()
        selected_generation.individuals = [individual for defeats, individual in ranking[:self.max_population]]
        return selected_generation
