#!/usr/bin/env python3
import random

def format_time(seconds):
    mins = int(seconds // 60)
    secs = seconds % 60
    return f"{mins}:{secs:05.2f}" if mins else f"{secs:.2f}"

def generate_splits(target_time, num_laps=4):
    strategies = {
        "negative_split": [1.03, 1.01, 0.99, 0.97],
        "even_pace": [1.0, 1.0, 1.0, 1.0],
        "front_load": [0.96, 0.98, 1.02, 1.04],
    }
    avg_split = target_time / num_laps
    print("=" * 50)
    print("D1 SWIM SPLIT ANALYZER")
    print("=" * 50)
    print(f"\nTarget Time: {format_time(target_time)} ({num_laps}x50 race)")
    print(f"Average Split: {format_time(avg_split)}\n")
    for name, multipliers in strategies.items():
        print(f"Strategy: {name.replace('_', ' ').title()}")
        print("-" * 35)
        total = 0
        for i, mult in enumerate(multipliers):
            split = avg_split * mult + random.uniform(-0.1, 0.1)
            total += split
            bar = "#" * int(split / avg_split * 20)
            print(f"  Lap {i+1}: {format_time(split):>8}  {bar}")
        print(f"  Total:  {format_time(total):>8}\n")

if __name__ == "__main__":
    print("\n" + "~" * 50)
    print("  Built by Jonathan Tsang | BU Swimming '27")
    print("~" * 50 + "\n")
    generate_splits(target_time=105.0, num_laps=4)
    print("Tip: Negative splits = trust the back half!")
    print("=" * 50 + "\n")
