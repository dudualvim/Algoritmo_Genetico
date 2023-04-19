import random

nomes = [
    'Ana', 'Beto', 'Carla', 'Daniel', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Julia',
    'Karla', 'Lucas', 'Mariana', 'Nelson', 'Olivia', 'Paulo', 'Quezia', 'Rafael', 'Sabrina', 'Tiago',
    'Ursula', 'Victor', 'Walter', 'Xuxa', 'Yasmin', 'Zuleika', 'Alice', 'Bruno', 'Cecilia', 'Diego',
    'Elaine', 'Felipe', 'Giovanna', 'Hugo', 'Isabel', 'Joana', 'Kleber', 'Leticia', 'Marcos', 'Nadia',
    'Otavio', 'Patricia', 'Quiteria', 'Renata', 'Sergio', 'Tatiana', 'Umberto', 'Vanessa', 'Wagner',
    'Ximena', 'Yuri', 'Zelia', 'Alfredo', 'Beatriz', 'Camila', 'Dario', 'Eliane', 'Fernando', 'Graziela',
    'Horacio', 'Isadora', 'Jonas', 'Katia', 'Leandro', 'Mirela', 'Nilton', 'Orlando', 'Priscila',
    'Quirino', 'Ricardo', 'Sueli', 'Tadeu', 'Ugo', 'Vera', 'Wilma', 'Xande', 'Yolanda', 'Zeca',
    'Aline', 'Bernardo', 'Catarina', 'Davi', 'Esther', 'Fabio', 'Glenda', 'Henrique', 'Iara', 'Jorge',
    'Maytê','Thainá', 'Jair','Arlindo','Algusto','Neide','Heloísa','Hortencia','Bianca','Marcelino','Yuri','Kayke'
]
random.shuffle(nomes)

metodos_de_ensino = {
    'introvertido': ['aulas_online', 'estudo_individual'],
    'extrovertido': ['aulas_em_grupo', 'aprendizagem_cooperativa'],
    'ambivertido': ['aulas_online', 'aulas_em_grupo'],
    'proativo': ['projetos_praticos', 'estudo_orientado'],
    'estudioso': ['aulas_teóricas', 'estudo_orientado']
}

def gerar_aluno(nome):
    personalidade = random.choice(['introvertido', 'extrovertido', 'ambivertido', 'proativo', 'estudioso'])
    nota = random.randint(0, 100)
    metodo_ensino = random.choice(metodos_de_ensino[personalidade])
    return {'nome': nome, 'personalidade': personalidade, 'nota': nota, 'metodo_ensino': metodo_ensino}

def selecao_roleta(populacao):
    total_nota = sum(aluno['nota'] for aluno in populacao)
    
    valor_escolhido = random.uniform(0, total_nota)
    acumulado = 0
    for aluno in populacao:
        acumulado += aluno['nota']
        if acumulado >= valor_escolhido:
            return aluno

def crossover(pai1, pai2):
    filho1 = {
        'personalidade': random.choice([pai1['personalidade'], pai2['personalidade']]),
        'nota': (pai1['nota'] + pai2['nota']) // 2, #1quebra
        'metodo_ensino': random.choice([pai1['metodo_ensino'], pai2['metodo_ensino']])
    }
    filho2 = {
        'personalidade': random.choice([pai1['personalidade'], pai2['personalidade']]),
        'nota': (pai1['nota'] + pai2['nota']) // 2,
        'metodo_ensino': random.choice([pai1['metodo_ensino'], pai2['metodo_ensino']])
    }
    return filho1, filho2

def mutacao(aluno, iteracao):
    if random.random() < 0.05: # Probabilidade de mutação de 5%
        aluno['personalidade'] = random.choice(['introvertido', 'extrovertido', 'ambivertido', 'proativo', 'estudioso'])
        aluno['nota'] = random.randint(0, 100)
        aluno['metodo_ensino'] = random.choice(metodos_de_ensino[aluno['personalidade']])
        print(f"Mutação ocorreu na iteração {iteracao} para o aluno {aluno}")

def algoritmo_genetico(populacao, geracoes):
    for iteracao in range(geracoes):
        nova_populacao = []
        for i in range(len(populacao) // 2):
            pai1 = selecao_roleta(populacao)
            pai2 = selecao_roleta(populacao)
            filho1, filho2 = crossover(pai1, pai2)
            mutacao(filho1, iteracao)
            mutacao(filho2, iteracao)
            nova_populacao.append(filho1)
            nova_populacao.append(filho2)
        populacao = nova_populacao

    return populacao

# Parâmetros do algoritmo
populacao_inicial = [gerar_aluno(nomes[i]) for i in range(100)]

numero_de_geracoes = 5

# Executar o algoritmo genético
populacao_final = algoritmo_genetico(populacao_inicial, numero_de_geracoes)

# Exibir resultados
print("População inicial:")
for aluno in populacao_inicial:
    print(aluno)

print("\nPopulação final:")
for aluno in populacao_final:
    print(aluno)

# Encontrar o melhor método de ensino para cada personalidade
melhores_metodos = {}
for personalidade, metodos in metodos_de_ensino.items():
    melhor_metodo = None
    melhor_nota_media = -1
    for metodo in metodos:
        notas = [aluno['nota'] for aluno in populacao_final if aluno['personalidade'] == personalidade and aluno['metodo_ensino'] == metodo]
        if len(notas) > 0:
            nota_media = sum(notas) / len(notas)
            if nota_media > melhor_nota_media:
                melhor_nota_media = nota_media
                melhor_metodo = metodo
    melhores_metodos[personalidade] = melhor_metodo

# Exibir o melhor método de ensino para cada personalidade
print("\nMelhores métodos de ensino:")
for personalidade, melhor_metodo in melhores_metodos.items():
    print(f"Personalidade {personalidade}: {melhor_metodo}") ##2quebra
        # Encontrar o melhor método de ensino com base na nota média geral
metodos_nota_media = {}
for aluno in populacao_final:
    metodo = aluno['metodo_ensino']
    if metodo not in metodos_nota_media:
        metodos_nota_media[metodo] = {'soma_notas': 0, 'total_alunos': 0}
    
    metodos_nota_media[metodo]['soma_notas'] += aluno['nota']
    metodos_nota_media[metodo]['total_alunos'] += 1

melhor_metodo = {}
melhor_nota_media = -1
for metodo, info in metodos_nota_media.items():
    nota_media = info['soma_notas'] / info['total_alunos']
    if nota_media > melhor_nota_media:
        melhor_nota_media = nota_media
        melhor_metodo = metodo

# Exibir o melhor método de ensino com base na nota média geral
print(f"\nMelhor método de ensino geral: {melhor_metodo} com nota média de {melhor_nota_media:.2f}")