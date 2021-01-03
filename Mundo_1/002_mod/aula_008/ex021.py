import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("/home/pv/Documents/Curso_python_cursoemvideo/Mundo_1/002_mod/aula_008/solemn.mp3")
pygame.mixer.music.play()
pygame.event.wait()
pygame.kil