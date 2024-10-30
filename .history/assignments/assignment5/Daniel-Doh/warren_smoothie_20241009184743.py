# Every morning I get breakfast at Warren Dining Hall even though I live in Fenway. Why? Because I'm a sucker for smoothies.
# However, sometimes Warren provides some nasty smoothies, particularly the smoothie with ginger in it.
# I will build a python script that scrapes the smoothie name from warren's dining hall menu website.
# Ideally, this would then be sent to my email or text, but I

from bs4 import BeautifulSoup
import requests


def get_random_joke():
    response = requests.get('https://www.bu.edu/dining/location/warren/#menu')
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Now you can use BeautifulSoup to extract data from the HTML
        all_titles = soup.find_all("h3", class_="nutrition-title")
        print(type(all_titles))
    else:
        print("Failed to fetch the page:", response.status_code)


get_random_joke()
