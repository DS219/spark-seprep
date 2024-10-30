from bs4 import BeautifulSoup
import requests


def get_random_joke():
    response = requests.get('https://www.bu.edu/dining/location/warren/#menu')
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Now you can use BeautifulSoup to extract data from the HTML
        title = soup.title.string
        print(title)
    else:
        print("Failed to fetch the page:", response.status_code)


get_random_joke()
