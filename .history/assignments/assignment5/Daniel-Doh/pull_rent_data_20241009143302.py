from urllib.request import urlopen


def get_random_joke():
    BASE_URL = "https://dad-joke-api.apps.codewizardshq.com"
    endpoint = "/random/jokes"
    request_url = f"{BASE_URL}{endpoint}"

    with urlopen(request_url) as response:
        joke = response.read()
    print(joke)


get_random_joke()
