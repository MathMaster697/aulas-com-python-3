# Lista de heróis
herois = ['homem de ferro', 'doutor estranho', 'capitão américa', 'thor', 'hulk', 'viuva negra']

# Loop for utilizado para percorrer cada item na lista de heróis
for heroi in herois:  # Para cada item na lista herois, faça o seguinte:
    # 'heroi' é uma variável temporária que recebe cada item da lista 'herois' por vez
    # A função .title() é usada para colocar a primeira letra de cada palavra em maiúscula
    print(heroi.title())  # Imprime o nome do herói com a primeira letra de cada palavra em maiúscula
# Em essência: 
# O loop for é usado para percorrer itens em uma lista (ou qualquer sequência) e executar uma ação para cada item dessa lista.

# Na linha for heroi in herois:, cada parte significa o seguinte:

# for: Indica o início de um loop. 
# heroi: É uma variável temporária que representa cada item da lista herois enquanto percorremos a lista.
# in: É uma palavra-chave que indica a associação da variável temporária aos itens da lista.
# herois: É a lista em que queremos iterar, ou seja, os itens que queremos percorrer.