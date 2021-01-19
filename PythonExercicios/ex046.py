import pygame
from time import sleep
from emoji import emojize
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex046.mp3')
print('Os show de fogos de artifício começará em:')
for c in range(10, -1, -1):
    print(str(c) + '...')
    sleep(1)
pygame.mixer.music.play(loops=0, start=0)
print(emojize('COMEÇOU!!! :fireworks: :fireworks: :fireworks: :fireworks:', use_aliases=True))
sleep(5)
