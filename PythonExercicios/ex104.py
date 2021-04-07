def leiaint(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = float(num)
            if num.is_integer():
                num = int(num)
                break
        print('\033[31mERRO! Digite um NÚMERO INTEIRO, por favor.\033[m')
    return num


n = leiaint('Digite um número inteiro: ')
print(f'O número digitado foi: {n}')
