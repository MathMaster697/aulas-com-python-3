# Importando a biblioteca openpyxl para manipulação de planilhas do Excel
import openpyxl

# Abrindo uma planilha existente chamada 'alunos.xlsx'
planilha = openpyxl.load_workbook('alunos.xlsx')

# Selecionando uma folha específica da planilha, neste caso, a folha chamada 'Alunos'
folha = planilha['Alunos']

# Atualizando o conteúdo da célula na coluna C e linha 2 para 'Python Avançado'
folha['C2'] = 'Python Avançado'

# Salvando as alterações na planilha com um novo nome 'alunos_atualizado.xlsx'
planilha.save('alunos_atualizado.xlsx')
