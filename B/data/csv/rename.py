import os
path = 'F:/Projects/2021-2 数学建模美赛/MCM-ICM-2021/B/data/csv'

num = 1

for file in os.listdir(path):
	name = file[:-3]
	t = file[-3:]
	print(t)
	if t == 'csv':
		os.rename(os.path.join(path, file), os.path.join(path, str(num) + '.' + t))
		num += 1