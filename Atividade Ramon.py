import sys
# #Verifica qual número é o maior entre 3 variaveis nomeadas de v1 - v2 -v3
# v1 = int(input('Primeiro Valor: '))
# v2 = int(input('Segundo Valor: '))
# v3 = int(input('Terceiro Valor: '))
# if v1 > v2 and v1 > v3:
#      print('O maior número é {}'.format(v1))
# elif v2 > v1 and v2 > v3:
#      print('O maior número é {}'.format(v2))
# else:
#      print('O maior número é {}'.format(v3))
# print('Final do programa')

# #Verifica se o número é impar ou pá.
# v1 = int(input('Entre com o 1° valor: '))
# v2 = int(input('Entre com o 2° valor: '))
# resto_v1 = v1 % 2
# resto_v2 = v2 % 2
# if resto_v1 == 0 or resto_v2 == 0: #Também pode colocar "or not resto_v2 > 0 - também irá funcionar, or not funciona para validar se a informação é verdadeira ou não.
#   print('Um número par foi informado.')
# else:
#    print('Nenhum número informado é par.')

#Diz se o número é multiplo de 3:
# v = int(input('Digite o número para saber se ele é múltiplo de 3: '))
# if ((v % 3) == 0):
#     print('O número é divivel por 3.')
# else:
#     print('O número não é divivivel por 3.')

#Verifica a idade do usuario
# nome = input('Digite o seu nome: ')
# idade = int(input('Digite o ano que você nasceu: '))
# ano = 2023 - idade
# if (ano < 18):
#     maenome = input('Por você ser menor de idade, por favor digite o nome da sua mãe: ')
# else:
#     sys.exit(print(f'Olá {nome}, agradeço por ter entrado no nosso esquema de piramide.'))
# print(f'Olá {nome}, iremos cobrar a Sraº {maenome} por uma resposta por deixar você entrar em um site adulto.')

#Pega um número e o retorna o dobro caso seja positivo e o triplo se for negativo.
# v1 = int(input('Digite o número: '))
# if v1 >= 0:
#     po = v1 ** 2
#     print(f'Seu número é positivo: {po}')
# else:
#     ne = v1 ** 3
#     print(f'Seu número ele é negativo: {ne}')