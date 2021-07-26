from global_data import *
import pickle
import csv
import numpy as np
import itertools
import subprocess
import math

un_data_files = get_un_data_files()
un_data_fields = get_un_data_fields()
gallup_happiness_data_file = get_gallup_happiness_data_file()
gallup_happiness_data_field = get_gallup_happiness_data_field()
who_data_file = get_who_data_file()
who_relevant_data_fields = get_who_relevant_data_fields()
OECD_data_files = get_OECD_data_files()
OECD_data_fields = get_OECD_data_fields()
percent_population_fields = get_percent_population_fields()
percent_gdp_fields = get_percent_gdp_fields()
percent_death_fields = get_percent_death_fields() 
percent_birth_fields = get_percent_birth_fields()

class Country :

	def __init__ (self, country_name):

		self.name = country_name
		self.__dict__["GDP in current prices (millions of US dollars)"] = 0
		self.__dict__["Population mid-year estimates (millions)"] = 0

		print(f"creating {country_name} ...")

		for file in ("../data/data_files/SYB63_1_202009_Population, Surface Area and Density.csv", "../data/data_files/SYB63_230_202009_GDP and GDP Per Capita.csv"):
			with open(file, 'r+') as f:

				reader = csv.reader(f,delimiter=',')

				next(reader)
				next(reader)

				for row in reader:
					if row[1] == country_name and row[3] == "Population mid-year estimates (millions)":
						self.__dict__["Population mid-year estimates (millions)"] = float(row[4])

					if row[1] == country_name and row[3] == "GDP in current prices (millions of US dollars)":
						self.__dict__["GDP in current prices (millions of US dollars)"] = float(row[4])
			f.close()

		for file_number,file in enumerate(un_data_files):

			with open(file, 'r+', encoding='iso-8859-1') as f:

				reader = csv.reader(f, delimiter = ',')

				next(reader)
				next(reader)

				for row in reader:

					name = row[1]
					year = row[2]
					field = row[3]
					value = row[4]

					if name == country_name and value != '':
						self.__dict__[field] = float(value)

		with open(who_data_file, 'r+') as f:

			reader = csv.reader(f, delimiter = ',')

			next(reader)
			next(reader)
			next(reader)
			next(reader)

			for row in reader:

				name = row[0]
				field = row[2]
				value = row[62]

				if name == country_name and field in who_relevant_data_fields and value != '':
					self.__dict__[field] = float(value)

					

		with open(gallup_happiness_data_file, 'r+') as f:

			reader = csv.reader(f, delimiter = ',')

			next(reader)

			for row in reader:

				name = row[0]
				year = row[2]
				value = float(row[3])

				if (name == country_name) and (year == '2017' or year == '2018'):
					self.__dict__[gallup_happiness_data_field] = value

		for i,file in enumerate(OECD_data_files):
			with open(file, 'r+') as f:

				reader = csv.reader(f, delimiter = ',')

				next(reader)

				for row in reader:
					name = row[0]
					field = OECD_data_fields[i]
					value = float(row[6])

					if name == country_name:
						self.__dict__[field] = value
						#print(f"{field}: {value}")

	def divide_percent_fields(self):

		for field,value in self.__dict__.items():
			if (field in percent_population_fields):
				self.__dict__[field] = 100 * self.__dict__[field] / self.__dict__["Population mid-year estimates (millions)"]

			elif (field in percent_gdp_fields):
				self.__dict__[field] = 100 * self.__dict__[field] / self.__dict__["GDP in current prices (millions of US dollars)"]

			elif (field in percent_birth_fields):
				self.__dict__[field] = 100 * self.__dict__[field] / self.__dict__["Birth rate, crude (per 1,000 people)"]

			elif (field in percent_death_fields):
				self.__dict__[field] = 100 * self.__dict__[field] / self.__dict__["Death rate, crude (per 1,000 people)"]

		[print(key,':',value) for key, value in self.__dict__.items()]

	def multiply_percent_fields(self):

		for field,value in self.__dict__.items():
			if (field in percent_population_fields):
				self.__dict__[field] = self.__dict__[field] * self.__dict__["Population mid-year estimates (millions)"] * .01

			elif (field in percent_gdp_fields):
				self.__dict__[field] = self.__dict__[field] * self.__dict__["GDP in current prices (millions of US dollars)"] * .01

			elif (field in percent_birth_fields):
				self.__dict__[field] = self.__dict__[field] * self.__dict__["Birth rate, crude (per 1,000 people)"] * .01

			elif (field in percent_death_fields):
				self.__dict__[field] = self.__dict__[field] * self.__dict__["Death rate, crude (per 1,000 people)"] * .01

		[print(key,':',value) for key, value in self.__dict__.items()]


	def __str__(self):
		output = "{:<90} | {:<30}".format('Attribute', 'Value') + "\n"
		print("-"*120)
		for field,value in self.__dict__.items():
			output += "{:<90} | {:<30}".format(field, value) + "\n"

		return output
























