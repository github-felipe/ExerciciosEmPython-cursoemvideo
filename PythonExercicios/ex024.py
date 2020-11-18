cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(f'A sua cidade é: \033[34m{cidade}\033[m. Ela começa com o nome Santo? \033[33m{"santo" in cidade[:5].lower()}\033[m')
