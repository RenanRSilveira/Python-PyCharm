from ex115.lib.interface import *



def arquivoExiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'w+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        a = open(nome, 'r')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
    finally:
        a.close()


def cadastro(aqr, nome='desconhecido', idade = 0):
    try:
        a = open(aqr, 'a')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            n = 37 - len(nome)
            a.write(f'{nome} {idade:>{n}} anos\n')
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado!')
            a.close()
