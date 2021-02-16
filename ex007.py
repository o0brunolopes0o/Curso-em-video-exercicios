n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
s = n1 + n2
m = (n1 + n2) /2

print('A soma da primeira nota {:.1f} \nE da segunda nota {:.1f}\nDeu um total de soma {:.1f}\nCom uma média final de {:.1f} \n' .format(n1, n2, s, m))

if m >= 7:
    print('O aluno(a) está Aprovado')
else:
    print('O aluno(a) está Reprovado')