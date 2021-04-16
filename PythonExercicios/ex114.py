import urllib.request as url
try:
    info = url.urlopen('http://pudim.com.br')
except Exception:
    print('\033[31mO site pudim não está disponível no momento :(\033[m')
else:
    print('\033[34mO site pudim está disponível :)\033[m')
