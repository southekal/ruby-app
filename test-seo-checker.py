from bs4 import BeautifulSoup
import requests
import argparse
import time

#class TestSEOChecker():

def test_seoscript ():
	servers = ['http://www.reddit.com']

	for server in servers:
		r = requests.get(server)
		soup = BeautifulSoup(r.text)

		print soup.h1
		print soup.h2
		assert soup.h1.text
		assert soup.h2.text

		for link in soup.find_all('a'):
			print link.get('href')

def test_evens():
    for i in range(0, 5):
        yield check_even, i, i*3

def check_even(n, nn):
	print n % 2, nn % 2
	assert n % 2 == 0 or nn % 2 == 0