import requests
import csv
import util
import os
from datetime import datetime
import time
util.p('INFO', 'All Libraries imported')

# define sites
sites = {
	'amazon': 'https://amazon.de',
	'bing': 'https://bing.de',
	'unitymedia': 'https://unitymedia.de',
	'google-de': 'https://google.de',
	'google-com': 'https://google.com',
	'fritzbox': 'http://fritz.box',
	'localhost': 'http://localhost'
	
}
for site in sites:
	util.p(site, sites[site])

bad_chars = [
	'\u2028'
]

# recreate file
inp = 'y'  #input('Recreate data file? (y/n)\n')
if inp.lower() == 'y':
	os.remove('data.csv')
	with open('data.csv', 'w') as data_file:
		csv_writer = csv.writer(data_file, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
		tmp = []
		for s in sites:
			tmp.append(s)
		csv_writer.writerow(['time'] + tmp)

# check sites
while True:
	if int(round(time.time() * 1000)) % 600000 < 1000:
		util.pp('INFO', 'testing sites...  ')

		tmp = []

		for site in sites:
			status_code = 0
			text = None
			try:
				req = requests.get(sites[site], timeout=10)
				status_code = req.status_code
				tmp.append(status_code)
				if status_code != 200:
					text = str(req.text)
			except Exception as e:
				status_code = -1
				tmp.append(status_code)

			# save bad file
			if text != None:
				with open('errors/' + util.getTime(format="%Y-%m-%d_%H-%M-%S") + '_' + site + '_' + str(status_code) + '.html', "w") as text_file:
					for bc in bad_chars:
						text = text.replace(bc, '')
					text_file.write(text)

		# print to console
		out = [str(datetime.now())[:19]] + tmp
		util.p('TEST', str(out))

		# write to file
		with open('data.csv', 'a') as f:
			csv_writer = csv.writer(f, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
			csv_writer.writerow(out)
		time.sleep(0.999)