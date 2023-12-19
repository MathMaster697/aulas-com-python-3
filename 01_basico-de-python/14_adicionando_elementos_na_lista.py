# Cria uma lista de carros, realiza operações e exibe as mudanças

# Cria uma lista de carros inicial
carros = ['honda', 'ford', 'toyota']

# Imprime a lista original de carros na tela
print(carros)  # Resultado: ['honda', 'ford', 'toyota']

# Adiciona 'bmw' ao final da lista de carros usando o método append()
carros.append('bmw')

# Imprime a lista atualizada de carros após a adição de 'bmw'
print(carros)  # Resultado: ['honda', 'ford', 'toyota', 'bmw']

# Cria uma nova lista de carros e insere 'bmw' na posição 0 usando o método insert()
carros = ['honda', 'ford', 'toyota']
carros.insert(0, 'bmw')

# Imprime a lista atualizada de carros após a inserção de 'bmw' na posição 0
print(carros)  # Resultado: ['bmw', 'honda', 'ford', 'toyota']

# Cria outra lista de carros
carros = ['honda', 'ford', 'toyota']

# Imprime a lista original de carros na tela
print(carros)  # Resultado: ['honda', 'ford', 'toyota']

# Remove o elemento na posição 1 da lista de carros usando o comando del
del carros[1]

# Imprime a lista de carros atualizada após a remoção do elemento na posição 1
print(carros)  # Resultado: ['honda', 'toyota']

# No código fornecido, são realizadas operações como adição, inserção e remoção de elementos na lista de carros.
