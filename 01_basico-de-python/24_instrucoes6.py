# Este programa verifica a idade para votar usando a biblioteca 'termcolor' para imprimir em cores.

# Para instalar a biblioteca 'termcolor', você pode usar o pip no terminal ou prompt de comando:
# pip3 install termcolor

from termcolor import colored  # Importa a função 'colored' da biblioteca 'termcolor'

while True:  # Inicia um loop que continuará até quebrar explicitamente
    idade = int(input("Por favor, insira sua idade (ou digite 0 para sair): "))  # Pede ao usuário para inserir a idade

    if idade == 0:  # Verifica se a idade digitada é 0
        print("Obrigado por usar o nosso programa, tchau!")  # Imprime uma mensagem de agradecimento e termina o programa

    if idade >= 18:  # Verifica se a idade é maior ou igual a 18
        print(colored("Você é velho o suficiente para votar!", "blue"))  # Imprime uma mensagem em azul indicando que a pessoa pode votar
        print(colored("Você já se registrou hoje?", "blue"))  # Pergunta se a pessoa já se registrou para votar hoje

    else:  # Caso a idade não seja maior ou igual a 18
        print(colored("Desculpe, você é muito jovem para poder votar.", "red"))  # Imprime uma mensagem em vermelho indicando que a pessoa é muito jovem para votar
        print(colored("Por favor, registre-se para votar quando completar 18 anos.", "red"))  # Incentiva a pessoa a se registrar para votar quando fizer 18 anos
