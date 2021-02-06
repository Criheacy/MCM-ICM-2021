import sys
import math
from PIL import Image
import pygame
from pygame.locals import *

sourceImageFile = 'accurate_map.png'

U, L = (-33.869074, 140.955635)
D, R = (-39.134965, 151.209086)

def PositionToScreen(longitude, latitude):
	x = (longitude - L) / (R - L) * imageWidth
	y = (latitude - U) / (D - U) * imageHeight
	print('Locate At', x, y)
	return x, y

def ScreenToPosition(x, y):
	longitude = x / imageWidth * (R - L) + L
	latitude = y / imageHeight * (D - U) + U
	print('Screen At', longitude, latitude)
	return longitude, latitude

pygame.init()

sourceImage = Image.open(sourceImageFile)
imageWidth, imageHeight = sourceImage.size

screen = pygame.display.set_mode((imageWidth, imageHeight))
pygameImage = pygame.image.load(sourceImageFile).convert_alpha()
screen.blit(pygameImage, (0, 0))

x, y = PositionToScreen(145, -35)

pygame.draw.rect(screen, (255, 0, 0, 255), (x - 5, y - 5, 10, 10))

pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				x, y = event.pos
				pygame.draw.rect(screen, (0, 0, 0, 255), (x - 5, y - 5, 10, 10))
				pygame.display.update()
				longitude, latitude = ScreenToPosition(x, y)
