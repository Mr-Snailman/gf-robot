import pygame
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("GoodMorning.ogg")
pygame.mixer.music.play()

playing = pygame.mixer.music.get_busy()
while (playing == 1):
  playing = pygame.mixer.music.get_busy()
