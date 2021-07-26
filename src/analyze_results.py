from global_data import *
import pickle
import csv
import numpy as np
import itertools
import subprocess
import math
import sys
import os
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate
from textwrap3 import wrap
from scipy.stats import pearsonr

from Country import Country

'''initialize variables'''

country_file = os.path.join('..','data', 'country_objects', 'countrydata.txt')
unitedstates_file = os.path.join('..','data', 'country_objects','unitedstates.txt')

percent_population_fields = get_percent_population_fields()
percent_gdp_fields = get_percent_gdp_fields()
percent_death_fields = get_percent_death_fields() 
percent_birth_fields = get_percent_birth_fields()

''' Problem Specific Data '''

inputs = get_inputs()
outputs = get_outputs()

''' functions '''

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

def factorial(n):
	sol = 1
	for i in range(1,n+1):
		sol = sol*i
	return sol

def save_results(weights, country_data, united_states_data):

	total_weight = 0
	for i in range(len(weights)) :
		total_weight += float(weights[i])

	synth_us = [0]*(len(outputs))

	for i,field in enumerate(outputs):
		for j,country in enumerate(countries_data):
			synth_us[i] += country.__dict__[field] * float(weights[j])

	output_array = np.zeros(shape=(len(outputs),))

	for i, field in enumerate(outputs):
		output_array[i] = ( (united_states_data.__dict__[field] - synth_us[i])/united_states_data.__dict__[field] ) * 100

	return output_array, synth_us

###############################################################################

''' open Country objects '''

united_states_data = open_file(unitedstates_file)
countries_data = open_file(country_file)

united_states_data.multiply_percent_fields()
for country in countries_data:
	country.multiply_percent_fields()

''' global variables '''

number_of_inputs = len(inputs)
number_of_countries = len(countries_data)
number_of_solutions = math.factorial(number_of_inputs)
number_of_outputs = len(outputs)

''' get SCM solution data '''

scm_weights = []
scm_solution_path = os.path.join('..', 'data', 'scm_solution.csv')
with open(scm_solution_path, 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		scm_weights.append(float(row[0]))

scm_solution = [0]*(len(outputs))

total_weight = 0
for w in scm_weights:
	total_weight += float(w)

for i, attr in enumerate(outputs):
	for j,country in enumerate(countries_data):
		scm_solution[i] += country.__dict__[attr] * scm_weights[j]

''' build numpy arrays with solution data '''

percent_difference_per_solution = np.zeros(shape=(number_of_solutions,number_of_outputs))
synth_us_per_solution = np.zeros(shape=(number_of_solutions,number_of_outputs))
weights = np.zeros(shape=(number_of_solutions,number_of_countries))

for i in range(number_of_solutions):
	file_name = "../solutions/solution_" + str(i) + ".txt"

	weight_vector = [""]
	with open(file_name, "r+") as f:
		sol = f.read()
		j = 0
		for index in range(len(sol)):
			character = sol[index]

			if character == " ":
				j += 1
				weight_vector.append("")

			else:
				weight_vector[j] += character

		f.close()
	weight_vector = weight_vector[:-2]

	weights[i] = weight_vector
	percent_difference_per_solution[i],synth_us_per_solution[i] = save_results(weight_vector,countries_data, united_states_data)

percent_difference_per_output = percent_difference_per_solution.transpose()
synth_us_per_output = synth_us_per_solution.transpose()

''' divide by percent fields '''

for i, synth_us_solution in enumerate(synth_us_per_output):
	if outputs[i] in percent_population_fields:
		for j, val in enumerate(synth_us_solution):
			synth_us_per_output[i][j] = 100 * synth_us_per_output[i][j] / getattr(united_states_data, 'Population mid-year estimates (millions)')
		
		scm_solution[i] = 100 * scm_solution[i] / getattr(united_states_data, 'Population mid-year estimates (millions)')

	if outputs[i] in percent_gdp_fields:
		for j, val in enumerate(synth_us_solution):
			synth_us_per_output[i][j] = 100 * synth_us_per_output[i][j] / getattr(united_states_data, 'GDP in current prices (millions of US dollars)')
		
		scm_solution[i] = 100 * scm_solution[i] / getattr(united_states_data, 'GDP in current prices (millions of US dollars)')

	# if outputs[i] in percent_birth_fields:
	# 	for j, val in enumerate(synth_us_solution):
	# 		synth_us_per_output[i][j] = 100 * synth_us_per_output[i][j] / getattr(united_states_data, 'Birth rate, crude (per 1,000 people)')
		
	# 	scm_solution[i] = 100 * scm_solution[i] / getattr(united_states_data, 'Birth rate, crude (per 1,000 people)')

	# if outputs[i] in percent_death_fields:
	# 	for j, val in enumerate(synth_us_solution):
	# 		synth_us_per_output[i][j] = 100 * synth_us_per_output[i][j] / getattr(united_states_data, 'Death rate, crude (per 1,000 people)')
		
	# 	scm_solution[i] = 100 * scm_solution[i] / getattr(united_states_data, 'Death rate, crude (per 1,000 people)')

united_states_data.divide_percent_fields()
for country in countries_data:
	country.divide_percent_fields()

''' numpy array for OECD average '''
OECD_average = np.zeros(shape=(number_of_outputs,))

for i, attr in enumerate(outputs):
	print('\n',attr)
	print('---------')
	for country in countries_data:
		print(f'{country.name}: {getattr(country, attr)}')
		OECD_average[i] += getattr(country, attr)
	OECD_average[i] = OECD_average[i]/number_of_countries
	print(f'\nAverage:{OECD_average[i]}')

	if attr == 'Population mid-year estimates (millions)':
		OECD_population = OECD_average[i] 

''' create figures '''

# Create weights figure
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "Times New Roman"
hfont = {'fontname':'Times New Roman'}

plt.figure(1)
plt.xticks(rotation=90)
colors = sns.color_palette("ch:s=.25,rot=-.25", as_cmap=False, n_colors=number_of_solutions)
plt.tight_layout()

country_names = [country.name for country in countries_data]

# Plot weights from ESCM solution
for i in range(number_of_solutions):
	plt.plot(country_names, weights[i], marker = 'o', linewidth=0.7, color=colors[i])

# Plot weights from SCM solution
plt.plot(country_names, scm_weights, marker = 'o', linewidth=0.7, color='r', label='SCM solution')

output_path = os.path.join('..','figures','weights.png')
plt.legend()
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# Create differences figure
plt.figure(2)
fig, ax = plt.subplots()

labels = [output for output in outputs if output not in inputs]
label_indexes = [i for i, output in enumerate(outputs) if output not in inputs]

width = 0.8
y = np.arange(len(labels))
means = [sol.mean() for i, sol in enumerate(percent_difference_per_output) if i in label_indexes]
error = [sol.std() for i, sol in enumerate(percent_difference_per_output) if i in label_indexes]

ax.barh(y, means, width, xerr=error, align='center', color = colors[int(round(number_of_solutions/2))])
ax.set_xlabel('Percent Difference (United States - Synthetic United States)')
ax.set_yticks(y+width/2)
ax.set_yticklabels(labels)

for label in ax.get_yticklabels():
	label.set_fontsize(5)

output_path = os.path.join('..','figures','percent_difference.png')
plt.savefig(output_path, dpi=300, bbox_inches="tight")

''' Print tables '''

# Compare United States and Synthetic United States
print("{:<80} {:<30} {:<30}".format('Attribute', 'Mean Difference (Percent)', 'Standard Deviation (Percent)'))
for i,attribute in enumerate(outputs):
	print("{:<80} {:<30} {:<30}".format(attribute, "{:0.2f}".format(percent_difference_per_output[i].mean()), "{:0.2f}".format(percent_difference_per_output[i].std())))
print()

# Compare different models (accounting for population)
us_population = getattr(united_states_data, 'Population mid-year estimates (millions)')

print("{:<80} {:<30} {:<30} {:<30} {:<30}".format('Attribute', 'United States', 'ESCM United States', 'SCM United States', 'OECD Average'))
for i,attribute in enumerate(outputs):
	if attribute not in inputs:
		if attribute not in percent_population_fields:
			print("{:<80} {:<30} {:<30} {:<30} {:<30}".format(attribute + '(per 1,000 people)', "{:0.2f}".format(united_states_data.__dict__[attribute]/us_population), "{:0.2f}".format(synth_us_per_output[i].mean()/us_population), "{:0.2f}".format(scm_solution[i]/us_population), "{:0.2f}".format(OECD_average[i]/OECD_population)))
		else:
			print("{:<80} {:<30} {:<30} {:<30} {:<30}".format(attribute, "{:0.2f}".format(united_states_data.__dict__[attribute]), "{:0.2f}".format(synth_us_per_output[i].mean()), "{:0.2f}".format(scm_solution[i]), "{:0.2f}".format(OECD_average[i])))
