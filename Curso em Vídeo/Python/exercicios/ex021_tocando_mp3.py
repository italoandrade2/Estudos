# Aula 08 - Exercício 21 - Tocando um MP3
# Italo Andrade Costa
# 23/09/2026

import pygame

pygame.mixer.init()
pygame.mixer.music.load(str(input('Digite o caminho completo do arquivo MP3 a ser reproduzido: ')))
pygame.mixer.music.play()

input('Pressione ENTER para interromper...')

pygame.mixer.music.stop
