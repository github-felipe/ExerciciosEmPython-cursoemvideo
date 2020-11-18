from math import sin, cos, tan, radians
n = int(input('Digite um ângulo: '))
radians(n)
print(f'Ângulo: \033[32m{n:}\033[m, Seno: \033[35m{sin(radians(n)):.2f}\033[m, Cosseno: \033[35m{cos(radians(n)):.2f}\033[m, Tangente: \033[35m{tan(radians(n)):.2f}\033[m')
