x = input('me fala alguma coisa ')
print('o \033[4;34mtipo primitivo\033[m disso é', type(x))
print('ele \033[1;35mestá\033[m em \033[4;34mminúsculo\033[m?', x.isupper())
print('ele \033[1;35mestá\033[m em \033[4;34mmaiúsculo\033[m?', x.islower())
print('está \033[4;34mcapitalizada\033[m?', x.istitle())
print('só tem \033[4;34mespaços\033[m?', x.isspace())
print('ele é um \033[4;34mdígito\033[m?', x.isdigit())
print('ele é \033[4;1;34mprintable\033[m?', x.isprintable())
print('ele é \033[4;1;34midentifier\033[m?', x.isidentifier())
print('ele é um \033[4;34mnúmero\033[m?', x.isnumeric())
print('ele é \033[4;34malfabético\033[m?', x.isalpha())
print('ele é \033[4;34malphanumérico?', x.isalnum())
