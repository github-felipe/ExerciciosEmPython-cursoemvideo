notas = str(input('Digite as suas duas notas: ')).strip()
n1 = float(notas.split()[0])
n2 = float(notas.split()[1])
média = (n1 + n2) / 2
if média < 5:
    print('Você foi \033[31mREPROVADO(A)\033[m!')
elif média < 7:
    print('Você está de recuperação, se esforce que você consegue!!')
else:
    print(f'Você foi \033[36mAPROVADO(A)\033[m com média {média:.1f}!')
