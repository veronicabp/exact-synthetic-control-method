from global_data import *
import pickle
import csv
import numpy as np
import itertools
import subprocess
import math
import sys
import os

from Country import Country

'''initialize variables'''

country_file = os.path.join('..','data', 'country_objects', 'countrydata.txt')
unitedstates_file = os.path.join('..','data', 'country_objects','unitedstates.txt')

inputs = get_inputs()

''' Functions'''

def one_dimension_array (data,length,attributes):
	array = np.zeros(shape=(length,))
	for n in range(length):
		array[n] = data.__dict__[attributes[n]]
	return array

def two_dimension_array (data, length, width, attributes):
	array = np.zeros(shape=(length,width))
	for m in range(width):
		for n in range(length):
			array[n][m] = data[m].__dict__[attributes[n]]
	return array

def open_file(file_name):
	with open(file_name, 'rb') as fp:
		p = pickle.load(fp)
	return p

###############################################################################

''' open Country objects '''

united_states_data = open_file(unitedstates_file)
countries_data = open_file(country_file)

united_states_data.multiply_percent_fields()
for country in countries_data:
	country.multiply_percent_fields()


'''create numpy arrays'''

M = len(inputs)
N = len(countries_data)

united_states = one_dimension_array(united_states_data, M, inputs)
countries = two_dimension_array(countries_data, M, N, inputs)

''' create countries string list'''

countries_string_list = []

for count,country_np in enumerate(countries):
	countries_string_list.append('')

	for data in country_np:
		countries_string_list[count] = countries_string_list[count] + str(data) + ' '

	countries_string_list[count] = countries_string_list[count] + "-" + str(united_states[count]) + ' '

''' permute string list '''

permutations = list(itertools.permutations(countries_string_list))

''' run c++ program '''

executable_path = os.path.join('..','cpp_dines_algorithm', 'Dines')

for count,permutation in enumerate(permutations):

	arg = ''
	for country_string in permutation:
		arg = arg + country_string + "|"
	arg = arg[:-1]

	print(count)
	# print(arg)

	subprocess.call([executable_path,arg,str(count)])
























