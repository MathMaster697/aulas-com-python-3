# Aqui, nós estamos importando a biblioteca tkinter para podermos criar a interface gráfica
# Quando utilizamos o "as" significa que estamos dando um "apelido" para a biblioteca.
import tkinter as tk
# Nessa linha, nós estamos importando a classe "messagebox" da biblioteca "tkinter" para mostrar as caixas de dialógo de mensagm ao usuário.
from tkinter import messagebox
# Função que vamos utilizar para verificar a idade do usuário
def verificar_idade():
	# Aqui, vamos obter a idade de entrada de texto e vamos converter para um número inteiro.
	idade = int(entrada_idade.get())

	# Verifica se a idade é maior ou igual a 18 anos
	if idade >= 18:
		# Aqui vai aparecer uma mensagem de informação com um ícone.
		messagebox.showinfo("Mensagem do programa", "Você é velho o suficiente para votar!", icon='info')
	else:
		# Aqui vai aparecer uma mensagem com um ícone de aviso.
		messagebox.showinfo("Mensagem do programa", "Desculpe, você é muito jovem para poder votar.", icon='warning')
# Estamos agora criando uma função para validar o que o usuário está colocando na entrada (Caixa de entrada).		
def validar_entrada(novo_valor):
	# Nós estamos verificando se o novo valor é uma string VAZIA ou é digitos
	if novo_valor == "" or novo_valor.isdigit():
		return True
	else:
		return False

# Aqui, criamos uma janela
janela = tk.Tk()
# Define o título da janela
janela.title("Verificar Idade")
# Aqui, nós definimos as dimensões da janela (Largura x Altura)
janela.geometry("400x100")
# Estamos criando um rótulo (uma mensagem) e uma entrada de idade na nossa janela
rotulo = tk.Label(janela, text="Por favor, coloque sua idade: ")
# Estamos empacotando o rotulo na janela para exibição
rotulo.pack()
# Estamos aqui agora configurando uma váriavel para "rastrear" a idade.
idade_var = tk.StringVar()
# Aqui, nós criamos uma caixa de entrada para a idade
entrada_idade = tk.Entry(janela, textvariable=idade_var)
# Estamos configurando a validação para permitir APENAS números inteiros 
entrada_idade.config(validate="key", validatecommand=(janela.register(validar_entrada), "%P"))
# Empacotando a caixa de entrada na janela
entrada_idade.pack()
# Criamos um botão para verificar a idade
verificar_botao = tk.Button(janela, text="Verificar a idade", command=verificar_idade)
# Empacota o botão na janela para que ele possa aparecer
verificar_botao.pack()
# Loop da interface gráfica
janela.mainloop()