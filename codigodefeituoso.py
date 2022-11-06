from random import randint
from time import sleep
import os
perguntas = ['Quantos anos duram a faculdade de programador?\nR: 3 anos.', 'Com que idade deve-se começar a programar?\nR: A idade ideal para aprender a programar é a partir dos 7 anos de idade', 'Qual a média do salário de um programador?\nR: R$ 2.800,00', 'Qual titulação recebe quem faz programação?\nR: Programador', 'Qual a linguagem de programação mais famosa?\nR: Phyton', 'O que é uma variável?\nR: É um espaço em disco que se atribui um valor', 'O que é um algoritmo?\nR:  É um conjunto de instruções, como uma receita de bolo.', 'Quais os principais tipos de variáveis?\nR: int, float, string e boolean.', 'O que é um fluxograma?\nR: O fluxograma ilustra as etapas, sequências e decisões de um processo ou fluxo de trabalho', 'Quais são os 3 tipos de algoritmos?\nR: A descrição narrativa, o fluxograma e o pseudocódigo ', 'Quais as 3 cidades no Brasil que mais tem vagas na área da programação?\nR: São paulo, Rio de janeiro e Porto alegre', 'Em que parte da empresa se usa desenvolvimento de sistemas?\nR: Em uma empresa, atua no segmento da Segurança da Informação e Tecnologia.', 'Onde os desenvolvedores são mais requisitados?\nR: Na área de computação e programação', 'Tem banca avaliadora no curso de avaliação?\nR: O superior sim, e técnico não', 'Os cursos de desenvolvimento são reconhecido pelo MECR?\nR: sim e são bem reconhecidos', 'O curso de programação tem estágio obrigatório?\nR: Não é necessário fazer estágio', 'Os cursos ofertados são presenciais ou à distância?\nR: Podem ser EAD ou presenciais', 'Tempo de duração do curso de programação?\nR: 2 a 3 anos de curso', 'Qual a carga horária de quem faz curso de programação?\nR: 40 horas por semana', 'Quais são as matérias que um programador deve saber?\nR: Matemática em geral']
perguntas_feitas = []
jogador = []
def clear():
    os.system('clear')
c = 0
while len(perguntas_feitas) < 19:
    try:
        nmr_escolhido = randint(0, 19)
        if c > 0:
            for d in perguntas_feitas:
                if d == int(nmr_escolhido):
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
                    jogador_da_vez = int(input('Continuar?\n[1] Sim\n[2] Não\n>>'))
                    if jogador_da_vez > 2 or jogador_da_vez < 1:
                        erro()
                except:
                    if isnumeric(jogador_da_vez):
                        print('Opção inválida, ou caractere inválido.')
                        sleep(2)
                        continue
                else: 
                    if jogador_da_vez == 1:
                        break
                    else:
                        quit()
        except:
            break
            print('Caractere inválido!')
        perguntas_feitas.append(f'{nmr_escolhido}')
    c += 1
clear()
