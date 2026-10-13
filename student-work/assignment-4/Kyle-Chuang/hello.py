distance = float(input("Distance in miles: "))
time = float(input("Time in minutes: "))

if distance <= 0 or time <= 0:
    print("Distance and time must be greater than zero.")
else:
    pace_seconds = round(time * 60 / distance)
    minutes = pace_seconds // 60
    seconds = pace_seconds % 60

    print(f"Average pace: {minutes}:{seconds:02d} per mile")