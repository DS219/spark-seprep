#!/usr/bin/env python3

import time
import sys

def countdown(n):
    print(f"Starting countdown from {n}...")
    for i in range(n, 0, -1):
        print(f"  {i}...")
        time.sleep(0.5)
    print("Liftoff!")

def main():
    print("=" * 40)
    print("  Welcome to the Countdown Launcher!")
    print("=" * 40)
    print()
    countdown(5)
    print()
    print("Mission complete. Have a great day!")

if __name__ == "__main__":
    main()
