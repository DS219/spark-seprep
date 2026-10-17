#!/usr/bin/env python3
import time
from datetime import datetime

print("Hello from my Python container!")
print("Today is", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

print("Counting down...")
for number in range(5, 0, -1):
    print(number)
    time.sleep(1)   

print("Done! Goodbye!")