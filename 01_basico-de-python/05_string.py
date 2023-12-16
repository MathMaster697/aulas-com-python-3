# Um método é uma ação que o Python pode executar em um dado. O ponto (.) após meu_nome no meu_nome.title() comunica ao Python que o método title() deve trabalhar na variável meu_nome. Todo método é seguido por um conjunto de parênteses, já que os métodos geralmente precisam de informações adicionais para realizar suas tarefas. Essas informações são fornecidas entre parênteses. A função title() não precisa de nenhuma informação adicional, logo seus parênteses estão vazios.

meu_nome = "matheus elegância"
print(meu_nome.title()) # O método .title() deixa as letras iniciais maiúsculas
print(meu_nome.upper()) # O método .upper() deixa todas as letras maiúsculas
print(meu_nome.lower()) # O método .lower() deixa todas as letras minúsculas

# meu_nome.title(): title() é um método que transforma a primeira letra de cada palavra em maiúscula. No caso do seu nome, "matheus elegância", o método title() fará com que a primeira letra de cada palavra seja maiúscula: "Matheus Elegância".

# meu_nome.upper(): upper() é um método que transforma todas as letras em maiúsculas. Se aplicado ao seu nome, "matheus elegância", o método upper() deixará todas as letras em maiúsculas: "MATHEUS ELEGÂNCIA".

# meu_nome.lower(): lower() é um método que transforma todas as letras em minúsculas. Quando usado em "matheus elegância", o método lower() deixará todas as letras em minúsculas: "matheus elegância".

# Esses métodos são como "ferramentas" que podem ser usadas em strings para modificar ou manipular o texto de maneiras específicas, facilitando o processamento e a formatação dos dados conforme necessário. Exemplo