# Lista de heróis
herois = ['homem de ferro', 'doutor estranho', 'capitão américa', 'thor', 'hulk', 'viuva negra']

# Loop for utilizado para percorrer cada item na lista de heróis
for heroi in herois:  # Para cada item na lista herois, faça o seguinte:
    # 'heroi' é uma variável temporária que recebe cada item da lista 'herois' por vez
    # A função .title() é usada para colocar a primeira letra de cada palavra em maiúscula
    
    # Imprime uma frase agradecendo cada herói por seu ato heroico
    print(f"{heroi.title()}, fez um bélissimo ato heróico nesse dia!")
    # Imprime uma mensagem indicando que você está ansioso pelo próximo ato do herói
    print(f"Não posso esperar para ver o próximo, {heroi.title()}.\n")

# Fora do loop, uma mensagem de agradecimento geral
print("Obrigado por salvarem a todos")
