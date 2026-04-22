import requests
import json

def ask_llm(prompt):
    """Send a prompt to the local Ollama model and return the response."""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:3b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

# test
# --- PARK DATA ---
# This is our "knowledge base." In a real system this could be a database or API.
PARK_INFO = {
    "yellowstone": {
        "state": "Wyoming, Montana, Idaho",
        "best_season": "Summer (June-August)",
        "top_activities": ["Watch Old Faithful geyser", "Hike Grand Prismatic Spring",
                           "Wildlife watching in Lamar Valley"],
        "things_to_pack": ["Bear spray", "Layers for cold mornings", "Binoculars", "Sunscreen"],
        "nearby_airports": ["Bozeman, MT (BZN)", "Jackson Hole, WY (JAC)"],
        "campgrounds": ["Madison", "Bridge Bay", "Canyon Village"],
        "fun_fact": "Yellowstone was the world's first national park, established in 1872."
    },
    "yosemite": {
        "state": "California",
        "best_season": "Spring (April-June) for waterfalls, Summer for hiking",
        "top_activities": ["Hike Half Dome", "See Yosemite Falls", "Drive Glacier Point Road"],
        "things_to_pack": ["Hiking boots", "Water filter", "Camera", "Warm jacket"],
        "nearby_airports": ["Fresno, CA (FAT)", "Merced, CA"],
        "campgrounds": ["Upper Pines", "North Pines", "Camp 4"],
        "fun_fact": "Yosemite Falls is the tallest waterfall in North America at 2,425 feet."
    },
    "grand canyon": {
        "state": "Arizona",
        "best_season": "Spring (March-May) or Fall (September-November)",
        "top_activities": ["Hike Bright Angel Trail", "Watch sunrise at Mather Point",
                           "Raft the Colorado River"],
        "things_to_pack": ["Plenty of water", "Sun hat", "Sturdy hiking shoes", "Salty snacks"],
        "nearby_airports": ["Flagstaff, AZ (FLG)", "Phoenix, AZ (PHX)"],
        "campgrounds": ["Mather", "Desert View", "Bright Angel (inner canyon)"],
        "fun_fact": "The Grand Canyon is over 6 million years old and 277 miles long."
    },
    "zion": {
        "state": "Utah",
        "best_season": "Spring (March-May) or Fall (September-November)",
        "top_activities": ["Hike Angels Landing", "The Narrows river hike",
                           "Scenic drive through the canyon"],
        "things_to_pack": ["Water shoes for The Narrows", "Trekking poles", "Sunscreen",
                           "Refillable water bottle"],
        "nearby_airports": ["Las Vegas, NV (LAS)", "St. George, UT (SGU)"],
        "campgrounds": ["Watchman", "South", "Lava Point"],
        "fun_fact": "Zion Canyon is 15 miles long and up to 2,640 feet deep."
    },
    "great smoky mountains": {
        "state": "Tennessee, North Carolina",
        "best_season": "Fall (October) for foliage, Spring for wildflowers",
        "top_activities": ["Drive Cades Cove Loop", "Hike to Clingmans Dome",
                           "Visit Elkmont ghost town"],
        "things_to_pack": ["Rain jacket", "Bug spray", "Camera for fall colors", "Light layers"],
        "nearby_airports": ["Knoxville, TN (TYS)", "Asheville, NC (AVL)"],
        "campgrounds": ["Cades Cove", "Elkmont", "Smokemont"],
        "fun_fact": "Great Smoky Mountains is the most visited national park in the US."
    },
    "olympic": {
        "state": "Washington",
        "best_season": "Summer (July-September) for dry weather and open trails",
        "top_activities": ["Explore Hoh Rain Forest", "Hike Hurricane Ridge",
                           "Tide-pooling at Ruby Beach"],
        "things_to_pack": ["Waterproof jacket", "Gaiters", "Layers", "Waterproof boots"],
        "nearby_airports": ["Seattle-Tacoma, WA (SEA)", "Port Angeles, WA (CLM)"],
        "campgrounds": ["Hoh", "Kalaloch", "Sol Duc"],
        "fun_fact": "Olympic National Park contains three distinct ecosystems: temperate rainforest, rugged coastline, and glacier-capped mountains."
    },
    "acadia": {
        "state": "Maine",
        "best_season": "Fall (September-October) for foliage, Summer for hiking",
        "top_activities": ["Hike Cadillac Mountain for sunrise", "Cycle the carriage roads",
                           "Sea kayaking around the coastline"],
        "things_to_pack": ["Wind-resistant jacket", "Bike helmet", "Sunscreen", "Sturdy hiking shoes"],
        "nearby_airports": ["Bangor, ME (BGR)", "Portland, ME (PWM)"],
        "campgrounds": ["Blackwoods", "Seawall", "Schoodic Woods"],
        "fun_fact": "Cadillac Mountain in Acadia is the first place in the US to see the sunrise from October through March."
    }
}


def get_park_info(park_name):
    """Look up a park from our knowledge base."""
    park_name = park_name.lower().strip()
    if park_name in PARK_INFO:
        return PARK_INFO[park_name]
    return None


def plan_trip(park_name):
    """
    THE AGENT LOOP

    Instead of one big question, we break the work into steps:
      1. Create an itinerary
      2. Build a packing list based on the itinerary
      3. Figure out travel logistics
      4. Combine everything into a final summary

    Each step uses output from previous steps — that's what makes this an agent.
    """

    park = get_park_info(park_name)
    if park is None:
        print(f"Sorry, I don't have info about '{park_name}'.")
        print(f"Available parks: {', '.join(PARK_INFO.keys())}")
        return

    print(f"\n{'='*60}")
    print(f"  National Park Trip Planner Agent")
    print(f"  Planning your trip to: {park_name.title()}")
    print(f"{'='*60}\n")

    # STEP 1: Create an itinerary
    print("[Agent] Step 1: Creating a trip itinerary...\n")

    planning_prompt = f"""You are a trip planning assistant. A user wants to visit {park_name.title()} National Park.

Here is what we know about the park:
- Location: {park['state']}
- Best time to visit: {park['best_season']}
- Top activities: {', '.join(park['top_activities'])}

Create a simple 2-day itinerary. For each day, list 2-3 activities with a one-sentence description.
Keep it short and practical."""

    itinerary = ask_llm(planning_prompt)
    print("--- Itinerary ---")
    print(itinerary)

    # STEP 2: Packing list based on the itinerary
    print("\n[Agent] Step 2: Building a packing list...\n")

    packing_prompt = f"""Based on this itinerary for {park_name.title()} National Park:

{itinerary}

And these recommended items: {', '.join(park['things_to_pack'])}

Create a short packing checklist organized into categories (Clothing, Gear, Safety).
Keep it to 10 items or fewer."""

    packing_list = ask_llm(packing_prompt)
    print("--- Packing List ---")
    print(packing_list)

    # STEP 3: Travel logistics
    print("\n[Agent] Step 3: Figuring out travel logistics...\n")

    logistics_prompt = f"""A traveler is visiting {park_name.title()} National Park in {park['state']}.

Nearby airports: {', '.join(park['nearby_airports'])}
Campground options: {', '.join(park['campgrounds'])}

Write 2-3 short travel tips about getting there and where to stay.
Include a fun fact: {park['fun_fact']}"""

    logistics = ask_llm(logistics_prompt)
    print("--- Travel Tips ---")
    print(logistics)

    # STEP 4: Final summary combining everything
    print("\n[Agent] Step 4: Creating final summary...\n")

    summary_prompt = f"""You are a friendly travel agent. Combine these into a brief, exciting
trip summary for {park_name.title()} National Park. Use 3-4 sentences that would make
someone excited to go.

Itinerary highlights: {itinerary[:300]}
Key items to bring: {packing_list[:200]}
Travel info: {logistics[:200]}"""

    summary = ask_llm(summary_prompt)
    print("--- Your Trip Summary ---")
    print(summary)

    print(f"\n{'='*60}")
    print("  Agent complete! 4 steps executed.")
    print(f"{'='*60}\n")

    print("\nAsk follow-up questions about your trip! (type 'quit' to exit)\n")
    while True:
        question = input("You: ")
        if question.lower() in ["quit", "exit", "q"]:
            break
        followup_prompt = f"""You are a national park travel expert.
The user is planning a trip to {park_name.title()} National Park.
Answer their question in 2-3 sentences.

Question: {question}"""
        answer = ask_llm(followup_prompt)
        print(f"Agent: {answer}\n")



# --- RUN THE AGENT ---
print("Welcome to the National Park Trip Planner!")
print(f"Available parks: {', '.join(name.title() for name in PARK_INFO.keys())}")
print()
park_choice = input("Which park do you want to visit? ")
plan_trip(park_choice)
