import random

def simulate_stock(ticker, days=7):
    print(f"\n📈 Stock Summary: {ticker}")
    print("-" * 30)
    price = round(random.uniform(100, 500), 2)
    for day in range(1, days + 1):
        change = round(random.uniform(-5, 5), 2)
        price = round(price + change, 2)
        direction = "▲" if change >= 0 else "▼"
        print(f"Day {day}: ${price:.2f}  {direction} {abs(change):.2f}")
    print(f"\nFinal price: ${price:.2f}")

simulate_stock("AAPL")
simulate_stock("NVDA")
