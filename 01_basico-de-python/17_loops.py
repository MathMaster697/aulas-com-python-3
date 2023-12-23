# Lista de julgadores
julgadores = ['sansão', 'debora', 'gideão']

# Loop for utilizado para percorrer cada item na lista de julgadores
for juizes in julgadores:  # Para cada item na lista julgadores, faça o seguinte:
    # 'juizes' é uma variável temporária que recebe cada item da lista 'julgadores' por vez
    # A função .title() é usada para colocar a primeira letra de cada palavra em maiúscula
    # O comando f-string permite inserir variáveis dentro de strings formatadas
    print(f"{juizes.title()}, foi um grande juíz usado por Deus!")
    # Imprime uma frase para cada julgador, utilizando o nome em formato de título
