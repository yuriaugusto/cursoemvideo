# faça um programa em python que abra e reproduza o áudio de um arquivo mp3

#importando o módulo
import pygame
# primeiro precisamos iniciar o pygame:
pygame.init()

pygame.mixer.music.load(r'/home/yuri/Documentos/Python/CursoEmVideo/Desafios/d021.mp3')
pygame.mixer.music.play()
input('Tocando o som.')

