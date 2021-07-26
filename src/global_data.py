''' Problem specific data '''

inputs = (
	"GDP in current prices (millions of US dollars)",
	"Population mid-year estimates (millions)",
	"Urban population (percent)",
	"Students enrolled in tertiary education (thousands)",
	"International migrant stock: Both sexes (number)"
)

outputs = (
	"Death rate, crude (per 1,000 people)",
	"Birth rate, crude (per 1,000 people)",
	"Immunization, measles (percent of children ages 12-23 months)",
	"Immunization, DPT (percent of children ages 12-23 months)",
	"Number of neonatal deaths",
	"Number of under-five deaths",
	"Number of infant deaths",
	"Survival to age 65, male (percent of cohort)",
	"Survival to age 65, female (percent of cohort)",
	"Life expectancy at birth, male (years)",
	"Life expectancy at birth, total (years)",
	"Life expectancy at birth, female (years)",
	"Domestic private health expenditure per capita (current US$)",
	"Out-of-pocket expenditure per capita (current US$)",
	"Current health expenditure (percent of GDP)",
	"Prevalence of current tobacco use (percent of adults)",
	"Health personnel: Physicians (number)",
	"Health personnel: Nurses and midwives (number)",
	"Health personnel: Dentists (number)",
	"Maternal mortality ratio (deaths per 100,000 population)",
	"Cantril happiness scale (0 to 10)",
	"GDP in current prices (millions of US dollars)",
	"Population mid-year estimates (millions)"
)

donors = [ # OECD countries with public healthcare and at least an 8 human development index according to https://worldpopulationreview.com/country-rankings/first-world-countries
	"Australia",
	"Austria",
	"Belgium",
	"Canada",
	"Chile",
	"Czechia",
	"Denmark",
	"Estonia",
	"Finland",
	"France",
	"Germany",
	"Greece",
	"Hungary",
	"Iceland",
	"Ireland",
	"Israel",
	"Italy",
	"Japan",
	"Latvia",
	"Lithuania",
	"Luxembourg",
	"Netherlands",
	"New Zealand",
	"Norway",
	"Poland",
	"Portugal",
	"Republic of Korea",
	"Slovakia",
	"Slovenia",
	"Spain",
	"Sweden",
	"Switzerland",
	"United Kingdom",
]

# first_world_democracies = [ # democracies determined by countries with at least a democracy score of 6 according to https://worldpopulationreview.com/countries/democracy-countries/ and at least a .8 human development index according to https://worldpopulationreview.com/country-rankings/first-world-countries
# 	"Argentina",
# 	"Australia",
# 	"Austria",
# 	"Belgium",
# #	"Brazil",	# commented countries have index above 7.5
# 	"Bulgaria",
# 	"Canada",
# 	"Chile",
# #	"Colombia",
# #	"Costa Rica",
# 	"Croatia",
# 	"Cyprus",
# 	"Czechia",
# 	"Denmark",
# #	"Ecuador",
# 	"Estonia",
# 	"Finland",
# 	"France",
# 	"Germany",
# 	"Greece",
# 	"Hong Kong",
# 	"Hungary",
# 	"Iceland",
# 	"Ireland",
# 	"Israel",
# 	"Italy",
# 	"Japan",
# 	"Latvia",
# 	"Lithuania",
# 	"Luxembourg",
# 	"Malaysia",
# 	"Malta",
# #	"Mexico",
# 	"Netherlands",
# 	"New Zealand",
# 	"Norway",
# #	"Panama",
# #	"Peru",
# 	"Poland",
# 	"Portugal",
# 	"Republic of Korea",
# 	"Romania",
# #	"Serbia",
# 	"Singapore",
# 	"Slovakia",
# 	"Slovenia",
# 	"Spain",
# #	"Sri Lanka",
# 	"Sweden",
# 	"Switzerland",
# #	"Trinidad and Tobago",
# #	"Ukraine",
# 	"United Kingdom",
# 	"United States of America",
# 	"Uruguay",
# ]

# public_healthcare = [ # countries with universal healthcare determined by https://worldpopulationreview.com/countries/countries-with-universal-healthcare/
# 	"Albania",
# 	"Algeria",
# 	"Andorra",
# 	"Antigua and Barbuda",
# 	"Argentina",
# 	"Australia",
# 	"Austria",
# 	"Bahamas",
# 	"Bahrain",
# 	"Barbados",
# 	"Belarus",
# 	"Belgium",
# 	"Belize",
# 	"Bhutan",
# 	"Bolivia",
# 	"Bosnia and Herzegovina",
# 	"Botswana",
# 	"Brazil",
# 	"Brunei",
# 	"Bulgaria",
# 	"Burkina Faso",
# 	"Canada",
# 	"Chile",
# 	"China",
# 	"Colombia",
# 	"Cook Islands",
# 	"Costa Rica",
# 	"Croatia",
# 	"Cuba",
# 	"Cyprus",
# 	"Czechia",
# 	"Denmark",
# 	"Ecuador",
# 	"Eritrea",
# 	"Estonia",
# 	"Fiji",
# 	"Finland",
# 	"France",
# 	"Gabon",
# 	"Georgia",
# 	"Germany",
# 	"Ghana",
# 	"Greece",
# 	"Guernsey",
# 	"Guyana",
# 	# "Hong Kong",
# 	"Hungary",
# 	"Iceland",
# 	"Iran",
# 	"Israel",
# 	"Italy",
# 	"Jamaica",
# 	"Japan",
# 	"Jersey",
# 	"Kazakhstan",
# 	"Kiribati",
# 	"Kuwait",
# 	"Latvia",
# 	"Liechtenstein",
# 	"Lithuania",
# 	"Luxembourg",
# 	"Macau",
# 	"Macedonia",
# 	"Malaysia",
# 	"Maldives",
# 	"Malta",
# 	"Mauritius",
# 	"Mexico",
# 	"Moldova",
# 	"Monaco",
# 	"Montenegro",
# 	"Namibia",
# 	"Netherlands",
# 	"New Zealand",
# 	"Oman",
# 	"Pakistan",
# 	"Palau",
# 	"Panama",
# 	"Paraguay",
# 	"Peru",
# 	"Poland",
# 	"Portugal",
# 	"Qatar",
# 	"Republic of Korea",
# 	"Romania",
# 	"Russia",
# 	"Rwanda",
# 	"Saint Lucia",
# 	"Samoa",
# 	"San Marino",
# 	"Saudi Arabia",
# 	"Serbia",
# 	"Seychelles",
# 	"Singapore",
# 	"Slovakia", 
# 	"Slovenia",
# 	"Spain",
# 	"Sri Lanka",
# 	"Sweden",
# 	"Switzerland",
# 	"Thailand",
# 	"Timor-Leste",
# 	"Tonga",
# 	"Trinidad and Tobago",
# 	"Tunisia",
# 	"Turkey",
# 	"Tuvalu",
# 	"Ukraine",
# 	"United Arab Emirates",
# 	"United Kingdom",
# 	"Uruguay",
# 	"Uzbekistan",
# 	"Vanuatu",
# 	"Venezuela",
# 	"Zambia"
# ]

''' Data references '''

''' UN Data '''

un_data_files = (
"../data/data_files/SYB63_1_202009_Population, Surface Area and Density.csv",
"../data/data_files/SYB63_327_202009_International Migrants and Refugees.csv",
"../data/data_files/SYB63_230_202009_GDP and GDP Per Capita.csv",
"../data/data_files/SYB63_309_202009_Education.csv",
"../data/data_files/SYB63_329_202009_Labour Force and Unemployment.csv",
"../data/data_files/SYB63_328_202009_Intentional Homicides and Other Crimes.csv",
"../data/data_files/SYB63_285_202009_Research and Development Staff.csv",
"../data/data_files/SYB63_286_202009_GDP on R&D.csv",
"../data/data_files/SYB63_315_202009_Water and Sanitation Services.csv",
"../data/data_files/SYB63_314_202009_Internet Usage.csv",
"../data/data_files/SYB62_246_201907_Population Growth, Fertility and Mortality Indicators.csv",
"../data/data_files/SYB63_325_202009_Expenditure on Health.csv",
"../data/data_files/SYB63_154_202009_Health Personnel.csv",
"../data/data_files/SYB61_253_Population Growth Rates in Urban areas and Capital cities.csv"
)

un_data_fields = (
("Population mid-year estimates (millions)", "Population mid-year estimates for males (millions)", "Population mid-year estimates for females (millions)", "Sex ratio (males per 100 females)", "Population aged 0 to 14 years old (percentage)", "Population aged 60+ years old (percentage)","Population density"),
("International migrant stock: Both sexes (number)", "International migrant stock: Both sexes (% total population)", "International migrant stock: Male (% total Population)", "International migrant stock: Female (% total Population)"),
("GDP in current prices (millions of US dollars)", "GDP per capita (US dollars)", "GDP in constant 2010 prices (millions of US dollars)", "GDP real rates of growth (percent)"),
("Students enrolled in primary education (thousands)", "Gross enrollment ratio - Primary (male)", "Gross enrollment ratio - Primary (female)"),
("Labour force participation - Total", "Unemployment rate - Total", "Labour force participation - Male", "Unemployment rate - Male", "Labour force participation - Female", "Unemployment rate - Female"),
("Intentional homicide rates per 100,000", "Percentage of male and female intentional homicide victims, Male", "Percentage of male and female intentional homicide victims, Female"),
("R & D personnel: Total (number in full-time equivalent)", "R & D personnel: Researchers - total (number in full-time equivalent)", "R & D personnel: Researchers - women (number in full-time equivalent)", "R & D personnel: Other supporting staff - total (number in full-time equivalent)", "R & D personnel: Total (number in full-time equivalent)"),
("Gross domestic expenditure on R & D: as a percentage of GDP (%)"),
("Safely managed drinking water sources, total (Proportion of population with access)", "Safely managed sanitation facilities, total (Proportion of population with access)"),
("Percentage of individuals using the internet",),
("Urban population (percent)",)
)

''' Gallup Cantril Scale Data '''

gallup_happiness_data_file = '../data/data_files/happiness-cantril-ladder.csv'
gallup_happiness_data_field = 'Cantril happiness scale (0 to 10)'

''' WHO Health Statistics '''

who_data_file = '../data/data_files/API_8_DS2_en_csv_v2_2057265.csv'

who_relevant_data_fields = (
"Death rate, crude (per 1,000 people)",
"Birth rate, crude (per 1,000 people)",
"Mortality rate, infant (per 1,000 live births)",
"Mortality rate, infant, female (per 1,000 live births)",
"Incidence of tuberculosis (per 100,000 people)",
"Diabetes prevalence (percent of population ages 20 to 79)",
"Immunization, measles (percent of children ages 12-23 months)",
"Immunization, DPT (percent of children ages 12-23 months)",
"Mortality rate, neonatal (per 1,000 live births)",
"Mortality rate, under-5, male (per 1,000 live births)",
"Mortality rate, under-5, female (per 1,000 live births)",
"Mortality rate, under-5 (per 1,000 live births)",
"Number of neonatal deaths",
"Cause of death, by non-communicable diseases (percent of total)",
"Number of under-five deaths",
"Cause of death, by injury (percent of total)",
"Number of infant deaths",
"Survival to age 65, male (percent of cohort)",
"Survival to age 65, female (percent of cohort)",
"Life expectancy at birth, male (years)",
"Life expectancy at birth, total (years)",
"Life expectancy at birth, female (years)",
"Domestic private health expenditure per capita (current US$)",
"Out-of-pocket expenditure per capita (current US$)",
"Current health expenditure (percent of GDP)",
"Prevalence of current tobacco use (percent of adults)",
"Population ages 20-24, female (percent of female population)",
"Population ages 20-24, male (percent of male population)"
)

''' OECD Data '''

OECD_data_files = (
'../data/data_files/DP_LIVE_20052021201814414.csv',
)

OECD_data_fields = (
'Obesity',
)

''' Accounting for Percents '''

percent_population_fields = (
"Population aged 0 to 14 years old (percentage)", "Population aged 60+ years old (percentage)",
"GDP per capita (US dollars)",
"Labour force participation - Total", "Unemployment rate - Total",
"Safely managed drinking water sources, total (Proportion of population with access)", "Safely managed sanitation facilities, total (Proportion of population with access)",
"Percentage of individuals using the internet",
"Population annual rate of increase (percent)",
"Total fertility rate (children per women)",
"Infant mortality for both sexes (per 1,000 live births)",
"Maternal mortality ratio (deaths per 100,000 population)",
"Death rate, crude (per 1,000 people)",
"Birth rate, crude (per 1,000 people)",
"Incidence of tuberculosis (per 100,000 people)",
"Diabetes prevalence (percent of population ages 20 to 79)",
"Immunization, measles (percent of children ages 12-23 months)",
"Immunization, DPT (percent of children ages 12-23 months)",
"Survival to age 65, male (percent of cohort)",
"Survival to age 65, female (percent of cohort)",
"Domestic private health expenditure per capita (current US$)",
"Out-of-pocket expenditure per capita (current US$)",
"Prevalence of current tobacco use (percent of adults)",
"Safely managed sanitation facilities, total (Proportion of population with access)",
"Urban population (percent)",
"Population ages 20-24, female (percent of female population)",
"Population ages 20-24, male (percent of male population)",
"Cantril happiness scale (0 to 10)",
"Life expectancy at birth, male (years)",
"Life expectancy at birth, total (years)",
"Life expectancy at birth, female (years)",
"Obesity",
"Death rate, crude (per 1,000 people)",
"Birth rate, crude (per 1,000 people)",
"Immunization, measles (percent of children ages 12-23 months)",
"Immunization, DPT (percent of children ages 12-23 months)",
"Survival to age 65, male (percent of cohort)",
"Survival to age 65, female (percent of cohort)",
"Life expectancy at birth, male (years)",
"Life expectancy at birth, total (years)",
"Life expectancy at birth, female (years)"
)

percent_gdp_fields = (
"Gross domestic expenditure on R & D: as a percentage of GDP (%)", 
"Domestic general government health expenditure",
"Current health expenditure (percent of GDP)"
)

percent_death_fields = (
"Cause of death, by non-communicable diseases (percent of total)",
"Cause of death, by injury (percent of total)"
)

percent_birth_fields = (
"Mortality rate, infant (per 1,000 live births)",
"Mortality rate, infant, female (per 1,000 live births)",
"Mortality rate, neonatal (per 1,000 live births)",
"Mortality rate, under-5, male (per 1,000 live births)",
"Mortality rate, under-5, female (per 1,000 live births)",
"Mortality rate, under-5 (per 1,000 live births)"
)


''' functions '''

def get_un_data_files():
	return un_data_files

def get_un_data_fields():
	return un_data_fields

def get_gallup_happiness_data_file():
	return gallup_happiness_data_file 

def get_gallup_happiness_data_field():
	return gallup_happiness_data_field

def get_who_data_file():
	return who_data_file

def get_who_relevant_data_fields():
	return who_relevant_data_fields

def get_OECD_data_files():
	return OECD_data_files

def get_OECD_data_fields():
	return OECD_data_fields

def get_percent_population_fields():
	return percent_population_fields

def get_percent_gdp_fields():
	return percent_gdp_fields

def get_percent_death_fields():
	return percent_death_fields 

def get_percent_birth_fields():
	return percent_birth_fields

def get_inputs():
	return inputs 

def get_outputs():
	return outputs

def get_donors():
	return donors 
