from time import sleep
from emoji import emojize
print('Os show de fogos de artifício começará em:')
for c in range(10, -1, -1):
    print(str(c) + '...')
    sleep(1)
print(emojize('COMEÇOU!!! :fireworks: :fireworks: :fireworks: :fireworks:', use_aliases=True))
