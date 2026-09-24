# Aula 08 - Desafio 21 - Reprodução de Arquivo MP3
# Italo Andrade Costa
# 23/06/2026

import pygame

pygame.mixer.init()
pygame.mixer.music.load(str(input('Digite o caminho do arquivo MP3 a ser reproduzido: ')))
pygame.mixer.music.play()

input('Pressione Enter para parar...')

pygame.mixer.music.stop()