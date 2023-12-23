# Lista de usuários banidos
usuarios_banidos = ['joão', 'jonathan', 'diego', 'lucas', 'diogo', 'jefferson', 'dejair', 'otávio', 'nathan', 'ana']

# Solicita ao usuário para inserir o nome
usuario = input("Por favor, insira seu nome: ")

# Verifica se o nome do usuário (em letras minúsculas) NÃO está na lista de usuários banidos
if usuario.lower() not in usuarios_banidos:
    # Se o nome não estiver na lista de banidos, permite postar uma resposta
    print(f"{usuario.title()}, você pode postar uma resposta se desejar.")
else:
    # Se o nome estiver na lista de banidos, informa que não pode postar uma resposta
    print(f"{usuario.title()}, você não pode postar uma resposta, pois está BANIDO!")
