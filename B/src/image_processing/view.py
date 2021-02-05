import sys
import math
from PIL import Image
import pygame
from pygame.locals import *

smallImage = Image.open('small.png')
sourceImage = Image.open('source.png')
width, height = sourceImage.size
smallWidth, smallHeight = smallImage.size
print('FLAG')

screen = pygame.display.set_mode((width * 2, height * 2))
updateFrameRate = pygame.time.Clock()
screen.fill((255, 255, 255))
print('FLAG')

def Grey2Value(colorGrey):
	r, g, b, a = colorGrey
	return 1 - (r + g + b) // 3 / 255

for j in range(smallHeight):
	for i in range(smallWidth):
		value = Grey2Value(smallImage.getpixel((i, j)))
		if value != 0:
			red = smallImage.getpixel((i, j))[0]
			pygame.draw.rect(screen, (255, red, red, 255), (i*20-15, j*20-15, 15, 15))
print('FLAG')
pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
