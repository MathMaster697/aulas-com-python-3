# Apesar disso, o valor 'bmw' deve ser exibido em letras maiúsculas. O código a seguir percorre uma lista de nomes de carros com um loop for e procura o valor 'bmw'. Sempre que for 'bmw', o valor será exibido com todas as letras maiúsculas em vez de ser exibido com a primeira letra maiúscula:

# Cria uma lista de carros com quatro elementos.
carros = ['audi', 'bmw', 'subaru', 'toyota']

# Inicia um loop "for" para percorrer a lista de carros.
for carro in carros:
    # Verifica se o carro atual é igual a 'bmw'.
    if carro == 'bmw':
        # Se for 'bmw', transforma o nome em letras maiúsculas e imprime.
        print(carro.upper())
    else:
        # Se não for 'bmw', transforma o nome com a primeira letra maiúscula e imprime.
        print(carro.title())

# O loop "for" termina, e o programa encerra.
        
# Neste exemplo, o loop verifica primeiro se o valor atual de carro é 'bmw'. Se for, o valor é exibido em letras maiúsculas. Se carro for diferente de 'bmw', o valor será exibido com a primeira letra maiúscula:
# Audi 
# BMW 
# Subaru 
# Toyota        