import requests

url = 'https://firms2.modaps.eosdis.nasa.gov/map/#t:adv;' \
	+ 'd:2020-01-01..2020-01-31;l:viirs,modis_a,modis_t,1,2,3,4,5,6,7,8,9,10,11,12;' \
	+ '@-213.8,-36.4,7z'

res = requests.get(url)

if res.status_code == 200:
	print(res.url)