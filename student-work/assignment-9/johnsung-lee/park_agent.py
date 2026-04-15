import requests

def ask_llm(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "smollm2:1.7b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    data = response.json()

    if "response" not in data:
        raise Exception(f"Ollama error: {data}")

    return data["response"]


PARK_INFO = {
    "yellowstone": "Famous for geysers, wildlife, and geothermal features.",
    "yosemite": "Known for granite cliffs, waterfalls, and scenic valleys.",
    "grand canyon": "Massive canyon with hiking and breathtaking views.",
    "zion": "Great for hiking and red rock landscapes.",
    "rocky mountain": "Mountain scenery and alpine lakes."
}


def plan_trip(park):
    info = PARK_INFO.get(park.lower(), "No info available.")

    print("\n--- Step 1: Itinerary ---")
    itinerary = ask_llm(
        f"Give a very short 2-day itinerary for {park}. "
        f"Park info: {info}. "
        f"Use only 4 bullet points total."
    )
    print(itinerary)

    print("\n--- Step 2: Packing List ---")
    packing = ask_llm(
        f"Based on this itinerary:\n{itinerary}\n"
        f"Give a very short packing list with only 6 bullet points."
    )
    print(packing)

    print("\n--- Step 3: Travel Logistics ---")
    travel = ask_llm(
        f"Give only 4 short travel tips for visiting {park}."
    )
    print(travel)

    print("\n--- Step 4: Summary ---")
    summary = ask_llm(
        f"Summarize this trip plan in 5 short bullet points:\n"
        f"{itinerary}\n{packing}\n{travel}"
    )
    print(summary)

    with open("trip_plan.txt", "w", encoding="utf-8") as f:
        f.write(summary)


if __name__ == "__main__":
    park = input("Which park do you want to visit? ")
    plan_trip(park)