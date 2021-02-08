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
#	print('Locate At', x, y)
	return x, y

def ScreenToPosition(x, y):
	longitude = x / imageWidth * (R - L) + L
	latitude = y / imageHeight * (D - U) + U
#	print('Screen At', longitude, latitude)
	return longitude, latitude

pygame.init()

sourceImage = Image.open(sourceImageFile)
imageWidth, imageHeight = sourceImage.size

screen = pygame.display.set_mode((imageWidth, imageHeight))
pygameImage = pygame.image.load(sourceImageFile).convert_alpha()
updateFrame = pygame.time.Clock()
screen.blit(pygameImage, (0, 0))

for date in range(1, 62):
	dataFile = open(str(date) + '.csv')

	# redraw screen image for each data file
#	screen.blit(pygameImage, (0, 0))
	pygame.display.update()

	line = dataFile.readline()	# read csv title
	line = dataFile.readline()
	while line:
		latitude, longitude, brightness, scan, track, acq_date, acq_time, satellite, confidence, version, bright_t31, frp, daynight = line.split(',')
		
#		print(longitude, latitude, frp, confidence)
		screenX, screenY = PositionToScreen(float(longitude), float(latitude))

		radius = float(frp)
		if radius >= 30: radius = 30
		alpha = float(confidence)
		if not(screenX >= 0 and screenX <= imageWidth and screenY >= 0 and screenY <= imageHeight):
			line = dataFile.readline()
			continue
		
#		print(longitude, latitude, frp, confidence)
		tempSurface = screen.convert_alpha()
		pygame.draw.circle(tempSurface, (200, 0, 0), (screenX, screenY), radius, width=0)

		tempSurface.set_alpha(alpha / 100 * 255)
		screen.blit(tempSurface, (0, 0))
		pygame.display.update()
		line = dataFile.readline()
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
		
	updateFrame.tick(5)
	
print('Complete!')

while True:
	for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
