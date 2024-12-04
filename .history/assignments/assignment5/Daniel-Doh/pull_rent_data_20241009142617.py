import requests
import pandas as pd

# Define the API endpoint and SQL query
api_url = "https://data.cdc.gov/resource/cjae-szjv.json"
sql_query = "?$query=SELECT state_name, county_name, aqi_value, aqi_category WHERE state_name = 'California' LIMIT 10"

# Make the request to the API
response = requests.get(api_url + sql_query)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON into a list of records
    data = response.json()

    # Convert the list of records to a DataFrame for easier handling
    df = pd.DataFrame(data)

    # Display the data
    print(df)

else:
    print(f"Error: Unable to fetch data. Status code {response.status_code}")
