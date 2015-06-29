from src.main.function import FrameDistance, GeneticFrameDistance
from src.main.population import Population, GeneticPopulation
from src.main.selector import TournamentSelector, ParentSelector
import moviepy.editor as mpy
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


class LoopingGifFinder(object):

    def __init__(self,
                 clip,
                 min_d=None,
                 max_d=None,
                 threshold=None,
                 max_gen=None,
                 popsize=None,
                 elites=None,
                 elite_recombinations=None,
                 recombination_rate=None,
                 mutation_rate=None):
        self.clip = mpy.VideoFileClip(clip).resize(width=20)
        self.min_d = 1.5 if min_d is None else min_d
        self.max_d = 5 if max_d is None else max_d
        self.threshold = 40 if threshold is None else threshold
        self.max_gen = 50 if max_gen is None else max_gen
        self.popsize = 20 if popsize is None else popsize
        self.elites = 2 if elites is None else elites
        self.elite_recombinations = 0 if elite_recombinations is None else elite_recombinations
        self.recombination_rate = 0.7 if recombination_rate is None else recombination_rate
        self.mutation_rate = 0.8 if mutation_rate is None else mutation_rate
        self.fitness_object = FrameDistance(self.clip, self.min_d, self.max_d)
        self.selector = TournamentSelector(self.popsize)
        self.population = None

        logging.info("Parameters: \n" +
                     "\tmin_d:                  {0}\n".format(self.min_d) +
                     "\tmax_d:                  {0}\n".format(self.max_d) +
                     "\tthreshold:              {0}\n".format(self.threshold) +
                     "\tmax_gen:                {0}\n".format(self.max_gen) +
                     "\tpopsize:                {0}\n".format(self.popsize) +
                     "\telites:                 {0}\n".format(self.elites) +
                     "\telite_recombinations:   {0}\n".format(self.elite_recombinations) +
                     "\trecombination_rate:     {0}\n".format(self.recombination_rate) +
                     "\tmutation_rate:          {0}".format(self.mutation_rate)
                     )

    def run(self):
        logging.info("generating population...")
        self.population = Population(self.popsize, self.fitness_object, self.min_d, self.max_d)
        generations = 0
        logging.info("starting...")

        # Run first generation without elitism
        self.population.next_generation(0, 0, self.recombination_rate, self.mutation_rate, self.selector)
        best_value = self.population.generation.individuals[0].get_y()
        logging.info("Generation {0}: \n {1}".format(generations, self.population.generation))
        generations += 1

        # Run next generations with elitism
        while generations < self.max_gen and best_value > self.threshold:
            self.population.next_generation(self.elites,
                                            self.elite_recombinations,
                                            self.recombination_rate,
                                            self.mutation_rate,
                                            self.selector)
            logging.info("Generation {0}: \n{1}".format(generations, self.population.generation))
            best_value = self.population.generation.individuals[0].get_y()
            generations += 1

        for i in range(10):
            self.population.next_final_generation(self.recombination_rate, self.selector)
            logging.info("Final Generation {0}: \n{1}".format(i, self.population.generation))

        logging.info("Best clips: \n{0}".format(self.population.generation))

    def results_to_gif(self, prefix):
        for i in range(10):
            self.clip.subclip(*self.population.generation.individuals[i].x).write_gif("{0}_{1}.gif".format(prefix, i))


class GeneticGifFinder(object):

    def __init__(self,
                 clip,
                 min_d=None,
                 max_d=None,
                 threshold=None,
                 max_gen=None,
                 popsize=None,
                 mutation_rate=None,
                 elites=None):
        self.clip = mpy.VideoFileClip(clip).resize(width=20)
        self.min_d = 1 if min_d is None else min_d
        self.max_d = 5 if max_d is None else max_d
        self.threshold = 40 if threshold is None else threshold
        self.max_gen = 50 if max_gen is None else max_gen
        self.popsize = 20 if popsize is None else popsize
        self.mutation_rate = 0.001 if mutation_rate is None else mutation_rate
        self.elites = 1 if mutation_rate is None else elites
        self.f = GeneticFrameDistance(self.clip, self.min_d, self.max_d)
        self.selector = ParentSelector(self.popsize)
        self.population = None

    def run(self):
        logging.info("generating population...")
        self.population = GeneticPopulation(self.popsize, self.f)
        generations = 0
        logging.info("starting...")

        # Run first generation without elitism
        self.population.next_generation(self.mutation_rate, self.selector)
        logging.info("Generation {0}: \n{1}".format(generations, self.population.generation))
        best_value = self.population.generation.individuals[0].get_y()
        generations += 1

        while generations < self.max_gen and best_value > self.threshold:
            self.population.next_generation(self.mutation_rate, self.selector, self.elites)
            logging.info("Generation {0}: \n{1}".format(generations, self.population.generation))
            best_value = self.population.generation.individuals[0].get_y()
            generations += 1

        logging.info("Best clips: \n{0}".format(self.population.generation))
        logging.info("Everything that happened: \n{0}".format(self.population.generations))

    def results_to_gif(self, prefix):
        for i in range(10):
            self.clip.subclip(
                self.f.gene_to_frames(
                    self.population.generation.individuals[i].x)
            ).write_gif("{0}_{1}.gif".format(prefix, i))
