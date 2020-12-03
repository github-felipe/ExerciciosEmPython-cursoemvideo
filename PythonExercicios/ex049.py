n = int(input('Digite um valor para ver sua tabuada: '))
print('-=' * 5 + '-')
for c in range(1, 11):
    print(f'{c:2} X {n} = {c * n}')
print('-=' * 5 + '-')
