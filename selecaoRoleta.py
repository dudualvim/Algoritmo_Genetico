import random

def selecionar_por_roleta(populacao):
    fitness_total = sum([ind.fitness for ind in populacao])
    valor_roleta = random.uniform(0, fitness_total)
    fitness_atual = 0
    for ind in populacao:
        fitness_atual += ind.fitness
        if fitness_atual >= valor_roleta:
            return ind

class Individuo:
    def __init__(self, fitness):
        self.fitness = round(fitness, 2)

populacao = [Individuo(fitness=random.uniform(0, 1)) for _ in range(100)]
pai1 = selecionar_por_roleta(populacao)
pai2 = selecionar_por_roleta(populacao)

print("Resultado Roleta: {:.2f}".format(pai1.fitness))

