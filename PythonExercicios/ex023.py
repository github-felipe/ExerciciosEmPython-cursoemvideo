n1 = int(input('Digite um número entre 0 e 9999 '))
n2 = n1 + 10000
n2 = str(n2)
print(f'Unidade: \033[35m{n2[4]}\033[m')
print(f'Dezena: \033[35m{n2[3]}\033[m')
print(f'Centena: \033[35m{n2[2]}\033[m')
print(f'Milhar: \033[35m{n2[1]}\033[m')
#Também poderia ser feito usando a regra matemática de se dividir um número por 10 o resto da divisão (%) é o algarismo das unidades, ai era só eu fazer a divisão inteira do n1 dependendo de qual algarismo eu quero pegar: n1 // 100 % 10 = o algarismo da centena.
