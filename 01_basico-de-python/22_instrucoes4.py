# Solicita ao usuário para inserir sua idade e converte para um número inteiro
idade = int(input("Por favor, insira a sua idade: "))

# Verifica se a idade inserida é maior ou igual a 18
if idade >= 18:
    # Se a idade for maior ou igual a 18, imprime uma mensagem dizendo que pode votar
    print("Você é velho o suficiente para poder votar!")
    # Além disso, pergunta se a pessoa já se registrou para votar
    print("Você já se registrou para poder votar?")
else:
    # Se a idade for menor que 18, imprime uma mensagem dizendo que ainda é muito jovem para votar
    print("Desculpe, você é muito jovem para poder votar!")
    # Também sugere que a pessoa se registre para votar quando tiver 18 anos
    print("Por favor, registra-se para votar quando tiver 18 anos!")
