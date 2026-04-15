import requests
import json

def ask_llm(prompt):
    # send prompt to local model and get response
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "smollm2:1.7b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


# basic park info (like a small database)
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

    # added 2 more parks
    "rocky mountain": {
        "state": "Colorado",
        "best_season": "Summer (June-September)",
        "top_activities": ["Trail Ridge Road drive", "Hiking alpine lakes", "Wildlife spotting"],
        "things_to_pack": ["Warm layers", "Hiking boots", "Water bottle", "Sunscreen"],
        "nearby_airports": ["Denver, CO (DEN)"],
        "campgrounds": ["Moraine Park", "Glacier Basin"],
        "fun_fact": "Rocky Mountain National Park has elevations over 14,000 feet."
    },
    "acadia": {
        "state": "Maine",
        "best_season": "Fall (September-October)",
        "top_activities": ["Cadillac Mountain sunrise", "Ocean Path walk", "Biking carriage roads"],
        "things_to_pack": ["Windbreaker", "Hiking shoes", "Camera", "Snacks"],
        "nearby_airports": ["Bangor, ME (BGR)"],
        "campgrounds": ["Blackwoods", "Seawall"],
        "fun_fact": "Acadia is one of the first places to see sunrise in the US."
    }
}


def get_park_info(park_name):
    park_name = park_name.lower().strip()
    if park_name in PARK_INFO:
        return PARK_INFO[park_name]
    return None


def plan_trip(park_name):
    park = get_park_info(park_name)

    if park is None:
        print("park not found")
        print("options:", ", ".join(PARK_INFO.keys()))
        return

    print("\nplanning trip to", park_name.title(), "\n")

    # step 1: itinerary
    itinerary = ask_llm(f"""Create a 2-day itinerary for {park_name.title()} National Park.
Top activities: {', '.join(park['top_activities'])}""")
    print("\n--- itinerary ---\n", itinerary)

    # step 2: packing
    packing_list = ask_llm(f"""Based on this itinerary:
{itinerary}
Create a short packing list.""")
    print("\n--- packing ---\n", packing_list)

    # step 3: travel
    logistics = ask_llm(f"""Travel tips for visiting {park_name.title()}.
Airports: {', '.join(park['nearby_airports'])}
Campgrounds: {', '.join(park['campgrounds'])}""")
    print("\n--- travel tips ---\n", logistics)

    # step 4: summary
    summary = ask_llm(f"""Summarize this trip:
{itinerary}
{packing_list}
{logistics}""")
    print("\n--- summary ---\n", summary)


# run program
print("national park trip planner")
print("parks:", ", ".join(name.title() for name in PARK_INFO.keys()))
print()

park_choice = input("which park? ")
plan_trip(park_choice)


# follow up questions
print("\nask questions (type 'quit' to stop)\n")

while True:
    question = input("you: ")
    if question.lower() in ["quit", "exit", "q"]:
        break

    followup_prompt = f"""You are a national park travel expert.
The user is planning a trip to {park_choice.title()} National Park.
Answer in 2-3 sentences.

Question: {question}"""

    answer = ask_llm(followup_prompt)
    print("agent:", answer, "\n")
