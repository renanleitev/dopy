import pyautogui as pg
import pyperclip as pc
from time import sleep

lista = ['A', 'aplicativo: ', 'D', 'documento: ',
         'M', 'musica: ', 'P', 'pasta: ', 'F', 'foto: ',
         'V', 'video: ']


def funcao_nome(ask):
    nome = input('Nome: ')
    print(f'{nome} adicionado com sucesso.')
    # Para digitar caracteres especiais => encoding='utf-8'
    with open('listaprograma.txt', 'a', encoding='utf-8') as file_programa:
        file_programa.write(lista[lista.index(ask)+1])
        file_programa.write(nome)
        file_programa.write('\n')


try:
    with open('listaprograma.txt', 'x'):
        pass
    print("""
Bem vindo ao sistema de automação Pydo.
Com apenas um click, automatize tarefas repetitivas,
abra programas, arquivos, músicas, vídeos e pastas.
Obs: A ordem de inicialização irá ocorrer conforme as opções escolhidas.
Iniciando... Arquivo de configuração criado.
Para alterar as configurações:
a) Abra o arquivo "listaprograma.txt" e altere o nome do item desejado.
b) Delete o arquivo "listaprograma.txt" e inicie de novo o Pydo.""")
    while True:
        print("""
[A] => Aplicativos
[D] => Documentos
[M] => Músicas
[P] => Pastas
[F] => Fotos
[V] => Vídeos""")
        pergunta = input('Digite a opção que deseja ou digite [N] para encerrar: ').upper().strip() # noqa
        if pergunta == 'N':
            break
        elif pergunta not in lista:
            print('Digite uma opção válida.')
            continue
        else:
            funcao_nome(pergunta)
            continue
    with open('listaprograma.txt', 'r') as file_programa:
        print('Ordem de inicialização:')
        for conta, item in enumerate(file_programa, start=1):
            print(f'{conta}: {item}')
        print('Saindo... Reinicie o Pydo para automatizar as tarefas.') # noqa
except Exception:
    with open('listaprograma.txt', 'r', encoding='utf-8') as file_programa:
        for programa in file_programa:
            if programa.isspace() is True:
                pass
            pc.copy(programa)
            sleep(0.5)
            pg.press('win')
            sleep(0.5)
            pg.hotkey('ctrl', 'v')
            sleep(0.5)
            pg.press('enter')
            sleep(2)
