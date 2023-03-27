# Simples Calculadora de Média de nota.
nota1 = int(input('Nota 1° Bimestre: '))
if nota1 > 10:
    nota1 = int(input('Nota digitada errada, tente novamente: '))
nota2 = int(input('Nota 2° Bimestre: '))
if nota2 > 10:
    nota2 = int(input('Nota digitada errada, tente novamente: '))
nota3 = int(input('Nota 3° Bimestre: '))
if nota3 > 10:
    nota3 = int(input('Nota digitada errada, tente novamente: '))
nota4 = int(input('Nota 4° Bimestre: '))
if nota4 > 10:
    nota4 = int(input('Nota digitada errada, tente novamente: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('A Média é: {}'.format(media))
if media < 7.0:
    print('O Aluno está com a média baixa.')
else:
    print('O Aluno está aprovado por média.')