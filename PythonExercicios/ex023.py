n1 = int(input('Digite um número entre 0 e 9999 '))
n2 = n1 + 10000
n2 = str(n2)
print(f'Unidade: {n2[4]}')
print(f'Dezena: {n2[3]}')
print(f'Centena: {n2[2]}')
print(f'Milhar: {n2[1]}')
#Também poderia ser feito usando a regra matemática de se dividir um número por 10 o resto da divisão (%) é o algarismo das unidades, ai era só eu fazer a divisão inteira do n1 dependendo de qual algarismo eu quero pegar: n1 // 100 % 10 = o algarismo da centena.
