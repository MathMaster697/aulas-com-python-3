# Importa a biblioteca openpyxl para manipular arquivos Excel
import openpyxl # Para baixar, escreva isso no terminal: pip install openpyxl

# Carrega o arquivo Excel - substitua o caminho do arquivo com uma mensagem mais geral
# "Aqui você pode colocar o caminho do arquivo que está na pasta do seu computador"
planilha_excel = openpyxl.load_workbook(r'C:\Aqui\você\coloca\o\caminho\onde está o arquivo no seu computador\doces.xlsx')

# Obtém os nomes das planilhas no arquivo Excel
nomes_das_planilhas = planilha_excel.sheetnames

# Imprime os nomes das planilhas
print(nomes_das_planilhas)
