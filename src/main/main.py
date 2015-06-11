import moviepy.editor as mpy
from src.main.function import FrameDistance
from src.main.population import Population
from src.main.selector import TournamentSelector
import logging

logging.basicConfig(level=logging.INFO)

def run():
    logging.info("getting clip...")
    clip = mpy.VideoFileClip("src/main/resources/hamac.mp4")
    clip = clip.resize(width=20)
    min_d = 1.5
    max_d = 3
    threshold = 20
    logging.info("creating fitness object...")
    fitness_object = FrameDistance(clip, min_d, max_d)

    start_population = 20
    elites = 2
    elite_recombinations = 0
    recombination_percentage = 0.7
    mutation_percentage = 0.3
    selector = TournamentSelector(start_population)
    max_generations = 1000

    logging.info("generating population...")
    population = Population(start_population, fitness_object, min_d, max_d)

    generations = 0

    logging.info("starting...")

    # Run first generation without elitism
    population.next_generation(0, 0, recombination_percentage, mutation_percentage, selector)
    generations += 1
    best_value = population.generation.individuals[0].get_y()
    logging.info("Generation {0}: \n {1}".format(generations, population.generation))

    # Run next generations with elitism
    while generations < max_generations and best_value > threshold:
        population.next_generation(elites,
                                   elite_recombinations,
                                   recombination_percentage,
                                   mutation_percentage,
                                   selector)
        logging.info("Generation {0}: \n {1}".format(generations, population.generation))
        best_value = population.generation.individuals[0].get_y()
        generations += 1
