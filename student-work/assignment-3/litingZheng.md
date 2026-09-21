# Liting Zheng

Hi, my name is Liting and my favorite programing language is Python because I enjoy the convience with a lot of library

## Example code

```
import json
import ssl
import certifi
import tkinter as tk
from datetime import datetime
from queue import Empty, Queue
from threading import Thread
from urllib.parse import quote
from urllib.request import urlopen

CITY = "Boston"  # Leave blank for approximate IP location.
REFRESH_MS = 10 * 60 * 1000  # Refresh weather every 10 minutes.
results = Queue()

window = tk.Tk()
window.title("Today's Day and Weather")
window.geometry("500x300")

date_label = tk.Label(window, font=("Arial", 18))
date_label.pack(pady=20)
weather_label = tk.Label(window, text="Loading weather...", font=("Arial", 14),wraplength=400)
weather_label.pack(pady=10)
status_label = tk.Label(window, text="", font=("Arial", 10), wraplength=460)
status_label.pack(pady=10)


def update_date():
    date_label.config(text=datetime.now().strftime("%A, %B %d, %Y"))
    window.after(1000, update_date)


def fetch_weather():
    try:
        url = f"https://wttr.in/{quote(CITY, safe='')}?format=j1"
        context = ssl.create_default_context(cafile=certifi.where())
        with urlopen(url, timeout=15, context=context) as response:
            data = json.load(response)
        current = data["current_condition"][0]
        location = CITY or data["nearest_area"][0]["areaName"][0]["value"]
        description = current["weatherDesc"][0]["value"]
        report = (f"{location}: {description}\n"
                  f"{current['temp_C']} °C / {current['temp_F']} °F")
        results.put((report, "Fetched at " + datetime.now().strftime("%H:%M:%S")))
    except (OSError, ValueError, KeyError, IndexError, TypeError) as error:
        results.put(("Weather unavailable.", f"{error}\nRetrying in 10 minutes."))


def refresh_weather():
    Thread(target=fetch_weather, daemon=True).start()
    window.after(REFRESH_MS, refresh_weather)


def show_results():
    # Only the main thread updates Tkinter widgets.
    try:
        report, status = results.get_nowait()
        weather_label.config(text=report)
        status_label.config(text=status)
    except Empty:
        pass
    window.after(200, show_results)


update_date()
refresh_weather()
show_results()
window.mainloop()


```

### Code Explanation

This Python example opens a window showing today's weekday, date, and current
weather in Celsius and Fahrenheit. The date follows your computer's local time
and updates every second, including after midnight. Weather refreshes on startup
and every 10 minutes while the window is open. Failed requests display an error
and retry at the next refresh.

Weather comes from [wttr.in](https://github.com/chubin/wttr.in). Leave `CITY` empty
to use your approximate location based on your public IP address, or set it to a
city such as `"Boston"`. An internet connection is required for weather updates.

To run it, run `python3 weather_popup.py` in a terminal. Use Python 3 with Tkinter installed;
`python3 -m tkinter` can check whether Tkinter is available. Close the window to
stop the program and its automatic updates.

