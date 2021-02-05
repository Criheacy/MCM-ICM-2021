import os
path = 'F:/Projects/2021-2 数学建模美赛/MCM-ICM-2021/B/data/txt'

for file in os.listdir(path):
	os.rename(os.path.join(path, file), os.path.join(path, file.split('.')[0] + '.csv'))