import random

POPULATION_SIZE = 100
METODOLOGIAS = 5;
GENE_SIZE = 5

# cria uma população inicial com genes aleatórios
def create_population():
    population = []
    for i in range(POPULATION_SIZE):
        gene = [random.randint(0, 1) for j in range(GENE_SIZE)]
        population.append(gene)
    return population

population = create_population()

print(population)