from datetime import datetime

def main():
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"Current time: {current_time}")

if __name__ == "__main__":
    main()

