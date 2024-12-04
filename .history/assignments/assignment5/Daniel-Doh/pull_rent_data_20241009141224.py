import urllib.parse
import urllib.request
import json


def main():
    try:
        base_url = "https://data.boston.gov/api/3/action/datastore_search_sql?"
        sql_query = 'SELECT COUNT(*) from "dc615ff7-2ff3-416a-922b-f0f334f085d0"'
        encoded_sql_query = urllib.parse.quote_plus(sql_query)

        # Construct the full URL by appending the encoded query
        full_url = f"{base_url}sql={encoded_sql_query}"

        print(f"Fetching total length from: {full_url}")
        fileobj = urllib.request.urlopen(full_url)
        response_dict = json.loads(fileobj.read())
    except Exception as e:
        print("Error: ", e)


if __name__ == '__main__':
    main()
