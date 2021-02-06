import os, sys

data = open('data.csv')

while data:
	y, x, z = data.readline().split(',')
