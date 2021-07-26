from global_data import *
import pickle
import os

from Country import Country

'''initialize variables'''

country_file = os.path.join('..','data', 'country_objects', 'countrydata.txt')
unitedstates_file = os.path.join('..','data', 'country_objects','unitedstates.txt')

''' create Country objects '''

countries = []
for donor in donors:
	country = Country(donor)
	countries.append(country)
	print(country)

with open(country_file, 'wb') as f:
	pickle.dump(countries,f)
	f.close()

with open(unitedstates_file, 'wb') as f:
    pickle.dump(Country('United States of America'),f)
    f.close()