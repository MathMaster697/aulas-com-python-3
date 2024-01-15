# Importa a biblioteca pandas e a apelida como pd para facilitar a referência posterior no código.
import pandas as pd

# Cria um DataFrame a partir da lista de dados.
data = [1, 2, 3]
df = pd.DataFrame(data)

# Imprime o DataFrame com uma única coluna contendo os dados da lista.
print(df)

# Explicação sobre o DataFrame:
# Um DataFrame é uma estrutura de dados tabular do pandas, semelhante a uma tabela em um banco de dados ou uma planilha do Excel.
# Neste caso, o DataFrame é construído a partir da lista de dados, e ele tem uma única coluna contendo os valores 1, 2 e 3.
