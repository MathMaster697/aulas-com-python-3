# Definindo variáveis para o primeiro e último nome
primeiro_nome = "matheus"
ultimo_nome = "elegância"

# Combinando o primeiro e o último nome para formar um nome completo usando f-string
nome_completo = f"{primeiro_nome} {ultimo_nome}"  # f-string para combinar variáveis
# Mostrando na tela o nome completo
print(nome_completo)

# Definindo variáveis para o nome e a idade
nome = "Davi"
idade = "40"

# Criando uma frase usando f-string, inserindo o nome e a idade na frase
frase = f"Olá, meu nome é {nome} e tenho {idade} anos"  # f-string para criar uma frase
# Exibindo a frase na tela
print(frase)

# Definindo variáveis para o primeiro nome, nome do meio e último nome
primeiro_nome = "matheus"
nome_do_meio = "guimarães"
ultimo_nome = "elegância"

# Combinando os três nomes usando f-string e transformando a primeira letra de cada palavra em maiúscula
nome_completo = f"{primeiro_nome} {nome_do_meio} {ultimo_nome}"  # f-string para combinar os nomes
# Exibindo o nome completo em formato de título
print(f"Olá, {nome_completo.title()}")

# Combinando os três nomes usando concatenação de strings tradicional
nome_completo = primeiro_nome + " " + nome_do_meio + " " + ultimo_nome
# Exibindo o nome completo em formato de título com uma exclamação no final
print("Olá, " + nome_completo.title() + "!")

# Explicação sobre f-strings
# Uma f-string permite inserir variáveis diretamente no texto usando o formato f"{variavel}".
# Ela simplifica a formatação de strings, tornando o código mais limpo e legível.
# As f-strings não são um método, mas uma funcionalidade do Python para facilitar a formatação de strings.

