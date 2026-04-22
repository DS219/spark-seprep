import requests
import json
import os
from datetime import datetime

def ask_llm(prompt):
    """Send a prompt to the local Ollama model and return the response."""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]


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
        "fun_fact": "Yellowstone was the world's first national park, established in 1872.",
        "wildlife": ["Grizzly bears", "Gray wolves", "Bison herds", "Elk", "Bald eagles"]
    },
    "yosemite": {
        "state": "California",
        "best_season": "Spring (April-June) for waterfalls, Summer for hiking",
        "top_activities": ["Hike Half Dome", "See Yosemite Falls", "Drive Glacier Point Road"],
        "things_to_pack": ["Hiking boots", "Water filter", "Camera", "Warm jacket"],
        "nearby_airports": ["Fresno, CA (FAT)", "Merced, CA"],
        "campgrounds": ["Upper Pines", "North Pines", "Camp 4"],
        "fun_fact": "Yosemite Falls is the tallest waterfall in North America at 2,425 feet.",
        "wildlife": ["Black bears", "Mule deer", "Coyotes", "Peregrine falcons", "Stellar's jays"]
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
        "wildlife": ["California condors", "Mule deer", "Bighorn sheep", "Ringtail cats", "Ravens"]
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
        "wildlife": ["Mule deer", "California condors", "Peregrine falcons", "Desert tortoises",
                     "Ringtail cats"]
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
        "wildlife": ["Black bears", "White-tailed deer", "Wild turkeys", "River otters",
                     "Synchronous fireflies (June)"]
    },
    # --- Option A: Two additional parks ---
    "olympic": {
        "state": "Washington",
        "best_season": "Summer (July-September) for dry weather and full trail access",
        "top_activities": ["Explore the Hoh Rain Forest", "Hike Hurricane Ridge",
                           "Tide-pooling at Ruby Beach"],
        "things_to_pack": ["Waterproof rain jacket", "Waterproof boots", "Layers",
                           "Trekking poles"],
        "nearby_airports": ["Seattle, WA (SEA)", "Port Angeles (small regional)"],
        "campgrounds": ["Hoh", "Kalaloch", "Sol Duc"],
        "fun_fact": ("Olympic National Park contains one of the only temperate rain forests "
                     "in the continental United States, receiving up to 140 inches of rain per year."),
        "wildlife": ["Roosevelt elk", "Black bears", "Mountain lions", "Banana slugs",
                     "Bald eagles", "Sea otters (offshore)"]
    },
    "acadia": {
        "state": "Maine",
        "best_season": "Late Summer to Fall (August-October) for foliage and fewer crowds",
        "top_activities": ["Hike Cadillac Mountain for the first sunrise in the US",
                           "Bike the historic carriage roads",
                           "Sea kayaking in Frenchman Bay"],
        "things_to_pack": ["Windproof jacket", "Layers for chilly mornings", "Bike helmet",
                           "Sunscreen"],
        "nearby_airports": ["Bangor, ME (BGR)", "Portland, ME (PWM)"],
        "campgrounds": ["Blackwoods", "Seawall", "Schoodic Woods"],
        "fun_fact": ("Acadia was the first national park established east of the Mississippi "
                     "River, donated largely by philanthropist John D. Rockefeller Jr."),
        "wildlife": ["White-tailed deer", "Peregrine falcons", "Harbor seals", "Minke whales",
                     "Common loons"]
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
      4. Wildlife & photography guide  (Option B — new Step 4)
      5. Combine everything into a final summary

    Each step uses output from previous steps — that's what makes this an agent.
    The full plan is saved to a text file at the end (Option D).
    """

    park = get_park_info(park_name)
    if park is None:
        print(f"Sorry, I don't have info about '{park_name}'.")
        print(f"Available parks: {', '.join(PARK_INFO.keys())}")
        return None  # Signal that planning failed so follow-up loop can skip

    output_lines = []

    def emit(text=""):
        """Print to screen and buffer for file output."""
        print(text)
        output_lines.append(text)

    emit(f"\n{'='*60}")
    emit(f"  National Park Trip Planner Agent")
    emit(f"  Planning your trip to: {park_name.title()}")
    emit(f"{'='*60}\n")

    # STEP 1: Create an itinerary
    emit("[Agent] Step 1: Creating a trip itinerary...\n")

    planning_prompt = f"""You are a trip planning assistant. A user wants to visit {park_name.title()} National Park.

Here is what we know about the park:
- Location: {park['state']}
- Best time to visit: {park['best_season']}
- Top activities: {', '.join(park['top_activities'])}

Create a simple 2-day itinerary. For each day, list 2-3 activities with a one-sentence description.
Keep it short and practical."""

    itinerary = ask_llm(planning_prompt)
    emit("--- Itinerary ---")
    emit(itinerary)

    # STEP 2: Packing list based on the itinerary
    emit("\n[Agent] Step 2: Building a packing list...\n")

    packing_prompt = f"""Based on this itinerary for {park_name.title()} National Park:

{itinerary}

And these recommended items: {', '.join(park['things_to_pack'])}

Create a short packing checklist organized into categories (Clothing, Gear, Safety).
Keep it to 10 items or fewer."""

    packing_list = ask_llm(packing_prompt)
    emit("--- Packing List ---")
    emit(packing_list)

    # STEP 3: Travel logistics
    emit("\n[Agent] Step 3: Figuring out travel logistics...\n")

    logistics_prompt = f"""A traveler is visiting {park_name.title()} National Park in {park['state']}.

Nearby airports: {', '.join(park['nearby_airports'])}
Campground options: {', '.join(park['campgrounds'])}

Write 2-3 short travel tips about getting there and where to stay.
Include a fun fact: {park['fun_fact']}"""

    logistics = ask_llm(logistics_prompt)
    emit("--- Travel Tips ---")
    emit(logistics)

    # STEP 4 (Option B): Wildlife & photography guide
    emit("\n[Agent] Step 4: Scouting wildlife and photography spots...\n")

    wildlife_prompt = f"""You are a wildlife and nature photography guide for {park_name.title()} National Park.

Known wildlife in the park: {', '.join(park['wildlife'])}
Best season: {park['best_season']}
Top locations from the itinerary: {itinerary[:300]}

Write a short guide (3-5 bullet points) covering:
- Which animals visitors are most likely to spot and where
- The best time of day for wildlife sightings
- One standout photography tip specific to this park

Keep the tone enthusiastic and practical."""

    wildlife_guide = ask_llm(wildlife_prompt)
    emit("--- Wildlife & Photography Guide ---")
    emit(wildlife_guide)

    # STEP 5: Final summary combining everything
    emit("\n[Agent] Step 5: Creating final summary...\n")

    summary_prompt = f"""You are a friendly travel agent. Combine these into a brief, exciting
trip summary for {park_name.title()} National Park. Use 3-4 sentences that would make
someone excited to go.

Itinerary highlights: {itinerary[:300]}
Key items to bring: {packing_list[:200]}
Travel info: {logistics[:200]}
Wildlife highlights: {wildlife_guide[:200]}"""

    summary = ask_llm(summary_prompt)
    emit("--- Your Trip Summary ---")
    emit(summary)

    emit(f"\n{'='*60}")
    emit("  Agent complete! 5 steps executed.")
    emit(f"{'='*60}\n")

    # OPTION D: Save the full plan to a text file
    safe_name = park_name.replace(" ", "_")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"trip_plan_{safe_name}_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write("\n".join(output_lines))
    print(f"[Agent] Trip plan saved to: {filename}\n")

    return park_name  # Return park name for follow-up loop


# --- RUN THE AGENT ---
print("Welcome to the National Park Trip Planner!")
print(f"Available parks: {', '.join(name.title() for name in PARK_INFO.keys())}")
print()
park_choice = input("Which park do you want to visit? ").strip()
result = plan_trip(park_choice)

# OPTION C: Follow-up questions
if result is not None:
    print("\nAsk follow-up questions about your trip! (type 'quit' to exit)\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in ["quit", "exit", "q", ""]:
            break
        followup_prompt = f"""You are a national park travel expert.
The user is planning a trip to {park_choice.title()} National Park.
Answer their question in 2-3 sentences.

Question: {question}"""
        answer = ask_llm(followup_prompt)
        print(f"Agent: {answer}\n")
