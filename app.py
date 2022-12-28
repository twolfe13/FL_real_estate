import pandas as pd


### TO DO: Change data to filter out outliers ($1M house)
###        Find out what "Recently Sold" filter means

"""
Realtor.com scrapes APIFY to get data, for recently sold single-family homes in Fort Myers


Add a URL for each PAGE to be scraped to Apify (10-15 should be)

SEARCH CRITERIA: 
- 2-3 bedrooms.  Single family home. 
- Filter = SOLD properties ONLY 
- Geographic Area: only Fort Myers area near us... should be about 10-15 pages of results for the search

"""


"""
# Create Dataframe from CSV
csv_df = pd.read_csv('CSVs/csv_realtor')
########################
"""
######### September 5th, Dataset #1 #########

# Read the Realtor.com JSON data into a Pandas object, Create data frame
sept_realtor_data = pd.read_json('Sept_1-data.json', orient='records')
#print(sept_realtor_data)


######### October 4th, Dataset #2 #########

# Read the Realtor.com JSON data into a Pandas object, Create data frame
oct_realtor_data = pd.read_json('Oct_1-data.json', orient='records')
#print(oct_realtor_data)

######### November 7th, Dataset #3 #########

nov_realtor_data = pd.read_json('Nov_1-data.json', orient='records')
#print(nov_realtor_data)

######### December 9th, Dataset #4 #########

dec_realtor_data = pd.read_json('Dec_1-data.json', orient='records')

"""
DATA INSPECTION
"""


# See all column names in a list format 
columns = list(sept_realtor_data.columns)  
#print(columns)

# Check how many missing values of COLUMNS only
columns_null = sept_realtor_data.isnull().sum()
#print(columns_null)

# Check the TOTAL number of all missing values in the data, in a single number 
columns_null_total = sept_realtor_data.isnull().sum().sum()
#print(columns_null_total)

# Check the data types of all columns
data_types = sept_realtor_data.dtypes
#print(data_types)


# Full inspection of the data, with memory usage
data_info = sept_realtor_data.info()
#print(data_info)

"""
Last sold price logic
"""

# Set data for Month of lastSoldPrice (Sept, Oct....)
last_sold_price = sept_realtor_data['lastSoldPrice'] 
print(last_sold_price)

# Identify which houses were sold for over $1M.  
## For September data, using describe.() we observe 486 "False" out of 500 count, leaving 14 who must be over $1M
sept_realtor_data['lastSoldPrice'] = sept_realtor_data['lastSoldPrice'] > 1000000
last_sold_price = sept_realtor_data['lastSoldPrice'].sort_values(ascending=False) 
print(last_sold_price.describe())


# Calculate the mean total last sold price
total_sold = last_sold_price.mean()
#print(total_sold)
#
total_sold_median = last_sold_price.median()
#print(total_sold_median)

url = sept_realtor_data['url']
#print(url)

summary = sept_realtor_data.describe() 
#print(summary)
