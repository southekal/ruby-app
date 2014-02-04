from bs4 import BeautifulSoup
import requests
import argparse
import time


servers = ['http://www.reddit.com']

for server in servers:
	r = requests.get(server)
	soup = BeautifulSoup(r.text)

	print 'Header H1:', soup.h1
	print 'Header H2:', soup.h2

	for link in soup.find_all('a'):
		print link.get('href')