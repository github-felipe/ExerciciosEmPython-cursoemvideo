cidade = str(input('Digite o nome de uma cidade: ')).strip()
cidade = cidade.upper()
cidade = cidade.split()
print(f'A sua cidade começa com santo? {"SANTO" in cidade[0]}')
