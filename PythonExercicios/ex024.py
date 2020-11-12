cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(f'A sua cidade é: {cidade}. Ela começa com o nome Santo? {"santo" in cidade[:5].lower()}')
