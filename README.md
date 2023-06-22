# Florida Real Estate Market Analysis project


# What it does 

APIFY scrapes realtor.com to get data, for recently sold single-family homes in Fort Myers.  Returns data in a specific geographical area defined by coordinates (via Google Maps on realtor.com).  In this project, an area in Fort Myers area is examined.

Add a URL for each PAGE to be scraped to Apify (10-15 pages should be)

SEARCH CRITERIA: 
- 2-3 bedrooms.  Single family home. 
- Filter = SOLD properties ONLY 
- Geographic Area: only Fort Myers area near us... should be about 10-15 pages of results for the search

- Last Sold Analysis logic: to analyze the current market
-- Average Last Sold

# CSV Dataset method: 

Create Dataframe from CSV
csv_df = pd.read_csv('CSVs/csv_realtor')

# JSON Dataset method: 

Read the Realtor.com JSON data into a Pandas object, Create data frame
sept_realtor_data = pd.read_json('Sept_1-data.json', orient='records')
#print(sept_realtor_data)

