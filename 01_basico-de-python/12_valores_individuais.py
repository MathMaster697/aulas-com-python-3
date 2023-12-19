# Cria uma lista de heróis e gera uma mensagem com o primeiro herói em título

herois = ['homem de ferro', 'doutor estranho', 'batman', 'capitão américa']

# Cria uma mensagem que contém o primeiro herói da lista, com a primeira letra de cada palavra em maiúscula (título)
mensagem_dos_herois = f"Meu primeiro herói é o {herois[0].title()}"

# Imprime a mensagem contendo o primeiro herói da lista com a primeira letra de cada palavra em maiúscula
print(mensagem_dos_herois)  # Resultado: 'Meu primeiro herói é o Homem De Ferro'

# No código fornecido, a f-string {herois[0].title()} pega o primeiro elemento da lista ('homem de ferro'),
# e o método .title() transforma a primeira letra de cada palavra para maiúscula na mensagem exibida.
