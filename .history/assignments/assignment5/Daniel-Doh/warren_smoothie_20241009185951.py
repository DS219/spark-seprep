from bs4 import BeautifulSoup
import requests


def get_random_joke():
    response = requests.get('https://www.bu.edu/dining/location/warren/#menu')
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Now you can use BeautifulSoup to extract data from the HTML
        all_smoothies = soup.find_all(
            "h3", class_="nutrition-title",  string=lambda text: "Smoothie" in text)
        for smoothie in all_smoothies:
            print(smoothie.text)
    else:
        print("Failed to fetch the page:", response.status_code)


get_random_joke()
