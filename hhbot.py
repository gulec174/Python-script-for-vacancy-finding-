#!/usr/bin/env python3

import requests

def getCompanyID():
	url = 'https://api.hh.ru/suggests/companies?text=MERA'
	r = requests.get(url)
	e = r.json()
	for x in e['items']:
		for z in x['industries']:
			if (z['name'].count('Разработка программного обеспечения') > 0):
				return x['id']


def printVacancies(companyID):
	x = []
	url = 'https://api.hh.ru/vacancies'

	for i in range(10):
		par = {'employer_id': companyID, 'per_page':'10', 'page':i}
		r = requests.get(url, params = par)
		e = r.json()
		x.append(e)
	for j in x:
		y = j['items']
		for i in y:
			if i['employer']['name'] != None:
				print(i['name'])
				print(i['employer']['name'])
				print(i['snippet']['requirement'])
				print(i['snippet']['responsibility'])
				print('\n')


if __name__ == '__main__':
	mera_id = getCompanyID()
	printVacancies(mera_id)