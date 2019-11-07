#!/usr/bin/env python3

import requests

class HHBot(object):
	def __init__(self, employer_name, industry):
		self.vacancies_list = []
		self.employer_name  = employer_name
		self.industry       = industry

	def get_employer_id(self):
		url       = 'https://api.hh.ru/suggests/companies?text=' + self.employer_name
		result    = requests.get(url)
		employers = result.json()

		for employer in employers['items']:
			for industry in employer['industries']:
				if (industry['name'].count(self.industry) > 0):
					return employer['id']


	def print_vacancies(self):
		employer_id = self.get_employer_id()
		url = 'https://api.hh.ru/vacancies'

		for page in range(10):
			par = {'employer_id': employer_id, 'per_page':'10', 'page':page}
			result = requests.get(url, params = par)
			vacancy_json = result.json()
			self.vacancies_list.append(vacancy_json)

		for vacancy in self.vacancies_list:
			vacancy_items = vacancy['items']
			for vacancy_item in vacancy_items:
				if vacancy_item['employer']['name'] != None:
					vacancy_name   = vacancy_item['name']
					employer       = vacancy_item['employer']['name']
					requirement    = vacancy_item['snippet']['requirement']
					responsibility = vacancy_item['snippet']['responsibility']
					vacancy_info   = "{0}\n{1}\n{2}\n{3}\n".format(vacancy_name, employer,
														requirement, responsibility)
					print(vacancy_info)



if __name__ == '__main__':
	bot = HHBot('MERA', 'Разработка программного обеспечения')
	bot.print_vacancies()