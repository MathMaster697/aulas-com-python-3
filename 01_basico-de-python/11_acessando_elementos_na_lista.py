# Cria uma lista de heróis em minúsculas e imprime dois elementos da lista após transformá-los em título

herois = ['homem de ferro', 'doutor estranho', 'batman', 'capitão américa']

# Imprime o terceiro elemento da lista (índice 2) após transformar a primeira letra em maiúscula (título)
print(herois[2].title())  # Resultado: 'Batman'

# Imprime o segundo elemento da lista (índice 1) após transformar a primeira letra em maiúscula (título)
print(herois[1].title())  # Resultado: 'Doutor Estranho'

# Em Python, os índices de lista começam em 0, então herois[2] refere-se ao terceiro elemento ('batman'),
# e herois[1] refere-se ao segundo elemento ('doutor estranho').
# O método .title() transforma a primeira letra de cada palavra para maiúscula.
