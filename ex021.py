"""
import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input('Agora você escuta?')
"""

from playsound import playsound
playsound('ex021.mp3')
