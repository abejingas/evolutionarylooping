from moviepy.video.io.VideoFileClip import VideoFileClip
from src.main.function import FrameDistance
from src.main.population import Population
from src.main.selector import TournamentSelector
import logging

logging.basicConfig(level=logging.DEBUG)

def run():
    logging.info("getting clip...")
    clip = VideoFileClip("src/main/resources/hamac.mp4")
    min_d = 1.5
    max_d = 3
    threshold = 50
    logging.info("creating fitness object...")
    fitness_object = FrameDistance(clip, min_d, max_d)

    start_population = 20
    elites = 2
    elite_recombinations = 0
    recombination_percentage = 0.7
    mutation_percentage = 0.1
    selector = TournamentSelector(start_population)
    max_generations = 1000

    logging.info("generating population...")
    population = Population(start_population, fitness_object, min_d, max_d)

    generations = 0
    while generations < max_generations and population.generation.best().get_y() > threshold:
        logging.info("Generation {0}".format(generations))
        population.next_generation(elites,
                                   elite_recombinations,
                                   recombination_percentage,
                                   mutation_percentage,
                                   selector)
        logging.info("Best: {0}".format(population.generation.best()))
        generations += 1