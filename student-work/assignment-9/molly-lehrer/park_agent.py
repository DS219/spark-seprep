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
    "yellowstone": {
        "state": "Wyoming, Montana, Idaho",
        "best_season": "Summer (June-August)",
        "top_activities": ["Watch Old Faithful geyser", "Hike Grand Prismatic Spring",
                           "Wildlife watching in Lamar Valley"],
        "things_to_pack": ["Bear spray", "Layers for cold mornings", "Binoculars", "Sunscreen"],
        "nearby_airports": ["Bozeman, MT (BZN)", "Jackson Hole, WY (JAC)"],
        "campgrounds": ["Madison", "Bridge Bay", "Canyon Village"],
        "fun_fact": "Yellowstone was the world's first national park, established in 1872.",
        "wildlife": ["Bison", "Grizzly bears", "Gray wolves", "Elk", "Bald eagles"]
    },
    "yosemite": {
        "state": "California",
        "best_season": "Spring (April-June) for waterfalls, Summer for hiking",
        "top_activities": ["Hike Half Dome", "See Yosemite Falls", "Drive Glacier Point Road"],
        "things_to_pack": ["Hiking boots", "Water filter", "Camera", "Warm jacket"],
        "nearby_airports": ["Fresno, CA (FAT)", "Merced, CA"],
        "campgrounds": ["Upper Pines", "North Pines", "Camp 4"],
        "fun_fact": "Yosemite Falls is the tallest waterfall in North America at 2,425 feet.",
        "wildlife": ["Black bears", "Mule deer", "Coyotes", "Peregrine falcons", "Mountain lions"]
    },
    "grand canyon": {
        "state": "Arizona",
        "best_season": "Spring (March-May) or Fall (September-November)",
        "top_activities": ["Hike Bright Angel Trail", "Watch sunrise at Mather Point",
                           "Raft the Colorado River"],
        "things_to_pack": ["Plenty of water", "Sun hat", "Sturdy hiking shoes", "Salty snacks"],
        "nearby_airports": ["Flagstaff, AZ (FLG)", "Phoenix, AZ (PHX)"],
        "campgrounds": ["Mather", "Desert View", "Bright Angel (inner canyon)"],
        "fun_fact": "The Grand Canyon is over 6 million years old and 277 miles long.",
        "wildlife": ["California condors", "Mule deer", "Desert bighorn sheep", "Rattlesnakes", "Ravens"]
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
        "fun_fact": "Zion Canyon is 15 miles long and up to 2,640 feet deep.",
        "wildlife": ["Mule deer", "California condors", "Desert tortoises", "Peregrine falcons", "Ringtail cats"]
    },
    "great smoky mountains": {
        "state": "Tennessee, North Carolina",
        "best_season": "Fall (October) for foliage, Spring for wildflowers",
        "top_activities": ["Drive Cades Cove Loop", "Hike to Clingmans Dome",
                           "Visit Elkmont ghost town"],
        "things_to_pack": ["Rain jacket", "Bug spray", "Camera for fall colors", "Light layers"],
        "nearby_airports": ["Knoxville, TN (TYS)", "Asheville, NC (AVL)"],
        "campgrounds": ["Cades Cove", "Elkmont", "Smokemont"],
        "fun_fact": "Great Smoky Mountains is the most visited national park in the US.",
        "wildlife": ["Black bears", "White-tailed deer", "Wild turkeys", "River otters", "Salamanders"]
    },
    "acadia": {
        "state": "Maine",        "best_season": "Summer (July-August) for hiking, Fall (September-October) for foliage",
        "top_activities": ["Watch sunrise from Cadillac Mountain", "Hike the Beehive Trail",
                           "Bike the carriage roads"],
        "things_to_pack": ["Windproof jacket", "Hiking boots", "Sunscreen", "Rain gear"],
        "nearby_airports": ["Bangor, ME (BGR)", "Portland, ME (PWM)"],
        "campgrounds": ["Blackwoods", "Seawall", "Schoodic Woods"],
        "fun_fact": "Cadillac Mountain in Acadia is the first place in the US to see sunrise from October to March.",
        "wildlife": ["Harbor seals", "Peregrine falcons", "White-tailed deer", "Moose", "Bald eagles"]
    },
    "olympic": {
        "state": "Washington",
        "best_season": "Summer (July-September) for dry weather and full trail access",
        "top_activities": ["Explore the Hoh Rain Forest", "Hike Hurricane Ridge",
                           "Tide-pooling at Ruby Beach"],
        "things_to_pack": ["Waterproof jacket", "Waterproof boots", "Layers", "Bear canister"],
        "nearby_airports": ["Seattle, WA (SEA)", "Port Angeles, WA (CLM)"],
        "campgrounds": ["Hoh", "Kalaloch", "Sol Duc"],
        "fun_fact": "Olympic National Park contains one of the few temperate rain forests in the world, receiving up to 14 feet of rain per year.",
        "wildlife": ["Roosevelt elk", "Black bears", "Mountain goats", "Orca whales", "Banana slugs"]
    }
}


def get_park_info(park_name):
    """Look up a park from our knowledge base."""
    park_name = park_name.lower().strip()
    if park_name in PARK_INFO:
        return PARK_INFO[park_name]
    return None


def plan_trip(park_name):
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

    # STEP 4: Final summary
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

    # STEP 5: Wildlife guide
    print("\n[Agent] Step 5: Wildlife you might see...\n")
    wildlife_prompt = f"""A traveler is visiting {park_name.title()} National Park.

Known wildlife in the park: {', '.join(park['wildlife'])}

Write 3-4 sentences about the wildlife they might encounter, including one safety tip
if any dangerous animals are present. Keep it fun and informative."""
    wildlife_info = ask_llm(wildlife_prompt)
    print("--- Wildlife Guide ---")
    print(wildlife_info)

    print(f"\n{'='*60}")
    print("  Agent complete! 5 steps executed.")
    print(f"{'='*60}\n")

    # Save the full plan to a text file (Option D)
    filename = f"{park_name.replace(' ', '_')}_trip_plan.txt"
    with open(filename, "w") as f:
        f.write(f"TRIP PLAN: {park_name.title()} National Park\n")
        f.write("="*60 + "\n\n")
        f.write("ITINERARY\n" + "-"*40 + "\n")
        f.write(itinerary + "\n\n")
        f.write("PACKING LIST\n" + "-"*40 + "\n")
        f.write(packing_list + "\n\n")
        f.write("TRAVEL TIPS\n" + "-"*40 + "\n")
        f.write(logistics + "\n\n")
        f.write("TRIP SUMMARY\n" + "-"*40 + "\n")
        f.write(summary + "\n\n")
        f.write("WILDLIFE GUIDE\n" + "-"*40 + "\n")
        f.write(wildlife_info + "\n")
    print(f"Trip plan saved to: {filename}\n")


# --- RUN THE AGENT ---
print("Welcome to the National Park Trip Planner!")
print(f"Available parks: {', '.join(name.title() for name in PARK_INFO.keys())}")
print()
park_choice = input("Which park do you want to visit? ")
plan_trip(park_choice)
