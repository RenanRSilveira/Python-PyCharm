from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar uma nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo!
        cabeçalho('PESSOAS CADASTRADAS')
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: ').strip().upper())
        while not nome.isalpha():
            nome = str(input('Nome: ').strip().upper())
        idade = leiaInt('Idade: ')
        cadastro(arq, nome, idade)

    elif resposta == 3:
        print(linha())
        print('Saindo do sistema... Até logo'.center(42))
        print(linha())
        break
    else:
        print('\033[31mERRO. Digite um valor válido\033[m')






