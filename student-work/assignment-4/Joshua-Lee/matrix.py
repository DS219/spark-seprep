#!/usr/bin/env python3
import random
import time
GREEN="\033[92m"
RESET="\033[0m"

characters="01ABCDEFGHO@#$%&!"

print("This is my cool looking matrix")
time.sleep(1)
for i in range(25):
    line="".join(
        random.choice(characters + "   ")
        for _ in range(60)
    )
    print(GREEN + line + RESET)
    time.sleep(0.1)

print("End of my weird looking matrix!")

