import requests
import json

def ask_llm(prompt):
    """Send a prompt to the local Ollama model and return the response."""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "smollm2:1.7b",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


# --- PARK DATA ---
PARK_INFO = {
    "acadia": {
        "state": "Maine",
        "best_season": "Fall (September-October)",
        "top_activities": ["Drive Park Loop Road", "Hike Cadillac Mountain for sunrise",
                           "Explore tide pools along the coast"],
        "things_to_pack": ["Windbreaker jacket", "Hiking shoes", "Camera", "Snacks"],
        "nearby_airports": ["Bangor, ME (BGR)", "Portland, ME (PWM)"],
        "campgrounds": ["Blackwoods Campground", "Seawall Campground"],
        "fun_fact": "Acadia National Park is one of the first places in the U.S. to see the sunrise."
    },

    "rocky mountain": {
        "state": "Colorado",
        "best_season": "Summer (June-September)",
        "top_activities": ["Drive Trail Ridge Road", "Hike Bear Lake Trail",
                           "Wildlife spotting like elk and moose"],
        "things_to_pack": ["Warm layers", "Water bottle", "Hiking boots", "Sunscreen"],
        "nearby_airports": ["Denver International Airport (DEN)"],
        "campgrounds": ["Moraine Park Campground", "Glacier Basin Campground"],
        "fun_fact": "Trail Ridge Road is the highest continuous paved road in North America."
    },

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
    }
}


def get_park_info(park_name):
    """Look up a park from our knowledge base."""
    park_name = park_name.lower().strip()
    return PARK_INFO.get(park_name)


def plan_trip(park_name):

    park = get_park_info(park_name)

    if park is None:
        print(f"Sorry, I don't have info about '{park_name}'.")
        print(f"Available parks: {', '.join(PARK_INFO.keys())}")
        return

    print(f"\n{'='*60}")
    print("  National Park Trip Planner Agent")
    print(f"  Planning your trip to: {park_name.title()}")
    print(f"{'='*60}\n")

    # STEP 1
    print("[Agent] Step 1: Creating a trip itinerary...\n")

    planning_prompt = f"""You are a trip planning assistant.
A user wants to visit {park_name.title()} National Park.

Location: {park['state']}
Best time: {park['best_season']}
Top activities: {', '.join(park['top_activities'])}

Create a 2-day itinerary."""

    itinerary = ask_llm(planning_prompt)
    print(itinerary)

    # STEP 2
    print("\n[Agent] Step 2: Building packing list...\n")

    packing_prompt = f"""Itinerary:
{itinerary}

Pack list ideas:
{', '.join(park['things_to_pack'])}

Make a checklist (max 10 items)."""

    packing_list = ask_llm(packing_prompt)
    print(packing_list)

    # STEP 3
    print("\n[Agent] Step 3: Travel logistics...\n")

    logistics_prompt = f"""Airports: {', '.join(park['nearby_airports'])}
Campgrounds: {', '.join(park['campgrounds'])}
Fun fact: {park['fun_fact']}"""

    logistics = ask_llm(logistics_prompt)
    print(logistics)

    # STEP 4
    print("\n[Agent] Step 4: Final summary...\n")

    summary_prompt = f"""Combine into a 3-4 sentence exciting trip summary.

Itinerary: {itinerary[:300]}
Packing: {packing_list[:200]}
Logistics: {logistics[:200]}"""

    summary = ask_llm(summary_prompt)
    print(summary)

    # STEP 5
    print("\n[Agent] Step 5: Budget estimate...\n")

    budget_prompt = f"""Estimate a 2-day trip budget for {park_name.title()}.

Include:
- Transportation
- Food
- Lodging/camping
- Extras

Itinerary: {itinerary}"""

    budget = ask_llm(budget_prompt)
    print(budget)

    print(f"\n{'='*60}")
    print("Agent complete!")
    print(f"{'='*60}\n")


# --- RUN ---
print("Welcome to the National Park Trip Planner!")
print(f"Available parks: {', '.join(PARK_INFO.keys())}")

park_choice = input("Which park do you want to visit? ")
plan_trip(park_choice)