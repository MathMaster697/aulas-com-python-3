# Importando o módulo openpyxl

import openpyxl # Para baixar pip install openpyxl

# Abrindo uma planilha existente com o nome 'alunos.xlsx' e atribuindo a variável 'planilha'
planilha = openpyxl.load_workbook('alunos.xlsx')

# Selecionando uma folha da planilha 'planilha' com o nome 'Alunos' e atribuindo a variável 'folha'
folha = planilha['Alunos']

# Lendo o valor da célula 'A2' da folha 'folha' e atribuindo a variável 'dados'
dados = folha['A2'].value

# Escrevendo o valor 26 na célula 'B2' da folha 'folha'
folha['B2'] = 55
folha['B3'] = 30
folha['B4'] = 38

# Salvando a planilha com o nome 'alunos_atualizado.xlsx'
planilha.save('alunos_atualizado.xlsx')
