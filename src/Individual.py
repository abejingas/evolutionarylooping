
class Individual(object):

    def __init__(self, x, function):
        self.x = x
        self.function = function
        self.y = self.function(x)

    def recombine(self, partner):
        # TODO write recombination method
        pass

    def mutate(self):
        # TODO write mutation method
        pass

    def __lt__(self, other):
        return self.y < other.y

    def __str__(self):
        return 'x: [' + (', '.join(map(str, self.x))) + '], y: ' + str(self.y)