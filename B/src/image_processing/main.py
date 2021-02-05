import sys
import math
from PIL import Image

smallImage = Image.open('source.png')
sourceImage = Image.open('source.png')

def Grey2Value(colorGrey):
	r, g, b, a = colorGrey
	return 1 - (r + g + b) // 3 / 255

wText = open('data.csv', mode='w')
width, height = sourceImage.size

smallWidth, smallHeight = smallImage.size
for j in range(smallHeight):
	for i in range(smallWidth):
		value = Grey2Value(smallImage.getpixel((i, j)))
		wText.write(str(value) + ', ')
	wText.write('\n')
