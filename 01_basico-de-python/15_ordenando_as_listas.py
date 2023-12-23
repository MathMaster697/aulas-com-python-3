# Criando uma lista de carros desordenada.
carros = ['bmw', 'honda', 'fiat', 'nissan', 'mclaren', 'toyota']

# Ordenando a lista de carros em ordem alfabética (altera a lista original).
carros.sort()

# Imprimindo a lista de carros ordenada.
print(carros)

# Reatribuindo a lista de carros à sua forma original.
carros = ['bmw', 'honda', 'fiat', 'nissan', 'mclaren', 'toyota']

# Imprimindo a mensagem indicando a lista original.
print("Essa é a lista original: ")
# Imprimindo a lista de carros original.
print(carros)

# Imprimindo a mensagem indicando a lista em ordem específica (não altera a lista original).
print("\nEssa é a lista em ordem específica: ")
# Imprimindo a lista de carros ordenada sem alterar a lista original.
print(sorted(carros))

# Imprimindo a mensagem indicando a lista original novamente.
print("\nEssa é a lista original de novo: ")
# Imprimindo a lista de carros original (sem alterações).
print(carros)
