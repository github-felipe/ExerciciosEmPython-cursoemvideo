from math import sin, cos, tan, radians
n = int(input('Digite um ângulo: '))
radians(n)
print(f'Ângulo: {n:}, Seno: {sin(radians(n)):.2f}, Cosseno: {cos(radians(n)):.2f}, Tangente: {tan(radians(n)):.2f}')
