# Importa a biblioteca pandas e a apelida como pd para facilitar a referência posterior no código.
import pandas as pd

# Cria um DataFrame a partir de uma lista de listas com dados e especifica os nomes das colunas.
data = [
    ['Matheus', 25],
    ['Jefferson', 20],
    ['Fernando', 25],
    ['Dejair', 17]
]

# Especifica os nomes das colunas: 'Nome' e 'Idade'
df = pd.DataFrame(data, columns=['Nome', 'Idade'])

# Imprime o DataFrame com duas colunas, 'Nome' e 'Idade'.
print(df)