import pygame
import random
import sys
from pygame.locals import*
import time
import math

pygame.init() 
pygame.mixer.init()
GameDisplay = pygame.display.set_mode([1000,500])                                       #Set up the screen to windowed mode 
pygame.display.set_caption("Project: DG")                                              #Set Caption for window name

Backgrouds = ['DetectiveRoom.jpg']
Backgroud = pygame.image.load(Backgrouds[0])

def startingScreen():
    Backgroud = pygame.image.load(Backgrouds[0])    
    pygame.Surface.blit(GameDisplay,Backgroud,BackgroudRect)  
    
while not exit: 
    startingScreen()
    


pygame.quit()                                                                         #Unintialize Pygame
sys.exit()                                                                            #Close the game window