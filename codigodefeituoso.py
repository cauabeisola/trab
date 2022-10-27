from random import randint
from time import sleep
import os
perguntas = ['Quantos anos duram a faculdade de programador?\nR: 3 anos.', 'Com que idade deve-se começar a programar?\nR: A idade ideal para aprender a programar é a partir dos 7 anos de idade', 'Qual a média do salário de um programador?\nR: R$ 2.800,00', 'Qual titulação recebe quem faz programação?\nR: Programador', 'Qual a linguagem de programação mais famosa?\nR: Phyton', 'O que é uma variável?\nR: É um espaço em disco que se atribui um valor', 'O que é um algoritmo?\nR:  É um conjunto de instruções, como uma receita de bolo.', 'Quais os principais tipos de variáveis?\nR: int, float, string e boolean.', 'O que é um fluxograma?\nR: O fluxograma ilustra as etapas, sequências e decisões de um processo ou fluxo de trabalho', 'Quais são os 3 tipos de algoritmos?\nR: A descrição narrativa, o fluxograma e o pseudocódigo ', 'Quais as 3 cidades no Brasil que mais tem vagas na área da programação?\nR: São paulo, Rio de janeiro e Porto alegre', 'Em que parte da empresa se usa desenvolvimento de sistemas?\nR: Em uma empresa, atua no segmento da Segurança da Informação e Tecnologia.', 'Onde os desenvolvedores são mais requisitados?\nR: Na área de computação e programação', 'Tem banca avaliadora no curso de avaliação?\nR: O superior sim, e técnico não', 'Os cursos de desenvolvimento são reconhecido pelo MECR?\nR: sim e são bem reconhecidos', 'O curso de programação tem estágio obrigatório?\nR: Não é necessário fazer estágio', 'Os cursos ofertados são presenciais ou à distância?\nR: Podem ser EAD ou presenciais', 'Tempo de duração do curso de programação?\nR: 2 a 3 anos de curso', 'Qual a carga horária de quem faz curso de programação?\nR: 40 horas por semana', 'Quais são as matérias que um programador deve saber?\nR: Matemática em geral']
perguntas_feitas = []
jogador = []
def clear():
    os.system('clear')
while True:
    try:
        qt_jogadores = int(input('Quantos jogadores são?: '))
    except:
        print('Erro, caractere inválido')
    else:
        break
for c in range(qt_jogadores):
    jogador.append([str(input(f'Qual o nome do {c+1}º jogador?: ')), 0])
c = 0
while len(perguntas_feitas) < 19:
    try:
        nmr_escolhido = randint(0, 19)
        if c > 0:
            for d in perguntas_feitas:
                if d == str(nmr_escolhido):
                    erro()
    except:
        continue
    else:
        clear()
        try:
            while True:
                cont = 0
                try:
                    clear()
                    print(perguntas[nmr_escolhido])
                    for e in jogador:
                        print(f'{cont} - ', e[0])
                        cont += 1
                    jogador_da_vez = int(input('Qual o jogador da vez?[digite alguma letra para encerrar o jogo]: '))
                    if jogador_da_vez > qt_jogadores - 1 or jogador_da_vez < 0:
                        erro()
                    acrt = int(input('Ele acertou?:\n1-Sim\n2-Não\n'))
                    if acrt != 1 and acrt != 2:
                        erro()
                except:
                    if isnumeric(jogador_da_vez):
                        print('Opção inválida, ou caractere inválido.')
                        sleep(2)
                        continue
                else: 
                    break
            if acrt == 1:
                jogador[jogador_da_vez][1] += 1
        except:
            break
            print('Caractere inválido!')
        perguntas_feitas.append(f'{nmr_escolhido}')
    c += 1
clear()
print('Resultado:')
for j in range(len(jogador)):
    print(f'\n{j} - ', end='')
    for k in jogador[j]:
        print(k, end=' ')
maior = 0
ganhador = []
for l in range(0, len(jogador)):
    if jogador[l][1] > maior:
        ganhador.append(jogador[l][0])
        maior = jogador[l][1]
for l in range(0, len(jogador)):
    if jogador[l][1] == maior and jogador[l][0] not in ganhador:
        ganhador.append(jogador[l][0])
if len(ganhador) == 1:
    print(f'O ganhador foi {ganhador[0]}, com {maior} pontos¹')
else:
    print(f'\nOs ganhadores foram ', end='')
    for n in ganhador:
        print(n, end=', ')
    print(f'com {maior} ponto(s)!')
