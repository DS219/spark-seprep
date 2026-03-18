from datetime import datetime


def getOutput():
    now = str(datetime.now())
    now = now[8:10]
    now = float(now)
    answer = None
    if now % 2 == 0:
        print("Todays date is an even number")
        answer = "even"
    else:
        print("Todays date is an odd number")
        anser = "off"
    return answer

getOutput()

#  CMD ["/usr/local/bin/python", "main.py"]