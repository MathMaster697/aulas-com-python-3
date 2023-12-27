# Este é um programa simples que verifica a idade para votar.

while True:  # Inicia um loop que continuará até quebrar explicitamente
    idade = int(input("Por favor, coloque a sua idade (Ou digite 0 para sair): "))  # Pede ao usuário para inserir a idade

    if idade == 0:  # Verifica se a idade digitada é 0
        print("Obrigado por usar o programa. Tchau tchau!")  # Imprime uma mensagem de agradecimento
        break  # Sai do loop

    if idade >= 18:  # Verifica se a idade é maior ou igual a 18
        print("Você é velho o suficiente para votar!")  # Imprime uma mensagem indicando que a pessoa pode votar
        print("Você já se registrou para votar?")  # Pergunta se a pessoa já se registrou para votar

    else:  # Caso a idade não seja maior ou igual a 18
        print("Desculpe, você é muito jovem para poder votar.")  # Imprime uma mensagem indicando que a pessoa é muito jovem para votar
        print("Por favor, registre-se para votar quando completar 18 anos.")  # Incentiva a pessoa a se registrar para votar quando fizer 18 anos
