import requests
import json
import os
from datetime import datetime
 
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
        "wildlife": ["Bison", "Grizzly bear", "Wolf", "Elk", "Bald eagle"],
        "photo_spots": ["Grand Prismatic Spring overlook", "Lamar Valley at dawn", "Old Faithful eruption"],
        "avg_daily_cost": 150
    },
    "yosemite": {
        "state": "California",
        "best_season": "Spring (April-June) for waterfalls, Summer for hiking",
        "top_activities": ["Hike Half Dome", "See Yosemite Falls", "Drive Glacier Point Road"],
        "things_to_pack": ["Hiking boots", "Water filter", "Camera", "Warm jacket"],
        "nearby_airports": ["Fresno, CA (FAT)", "Merced, CA"],
        "campgrounds": ["Upper Pines", "North Pines", "Camp 4"],
        "fun_fact": "Yosemite Falls is the tallest waterfall in North America at 2,425 feet.",
        "wildlife": ["Black bear", "Mule deer", "Coyote", "Peregrine falcon", "Bobcat"],
        "photo_spots": ["Tunnel View at sunrise", "Mirror Lake reflection", "Glacier Point panorama"],
        "avg_daily_cost": 130
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
        "wildlife": ["California condor", "Mule deer", "Bighorn sheep", "Mountain lion", "Rattlesnake"],
        "photo_spots": ["Mather Point at sunrise", "Desert View Watchtower", "Colorado River from South Rim"],
        "avg_daily_cost": 120
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
        "wildlife": ["Mule deer", "Desert tortoise", "Peregrine falcon", "Ringtail cat", "Canyon tree frog"],
        "photo_spots": ["Angels Landing summit", "The Narrows slot canyon", "Canyon Overlook Trail"],
        "avg_daily_cost": 110
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
        "wildlife": ["Black bear", "White-tailed deer", "Wild turkey", "Salamander", "Synchronous firefly"],
        "photo_spots": ["Clingmans Dome at sunrise", "Cades Cove open meadow", "Laurel Falls trail"],
        "avg_daily_cost": 100
    },
    # --- OPTION A: Two additional parks ---
    "acadia": {
        "state": "Maine",
        "best_season": "Summer (July-August) or Fall (September-October) for foliage",
        "top_activities": ["Drive the Park Loop Road", "Hike Cadillac Mountain for first sunrise in the US",
                           "Cycle the historic carriage roads"],
        "things_to_pack": ["Windproof jacket", "Hiking boots", "Sunscreen", "Tide chart for shore walks"],
        "nearby_airports": ["Bangor, ME (BGR)", "Portland, ME (PWM)"],
        "campgrounds": ["Blackwoods", "Seawall", "Schoodic Woods"],
        "fun_fact": "Cadillac Mountain in Acadia is the first place in the US to see the sunrise from October to March.",
        "wildlife": ["Harbor seal", "Peregrine falcon", "White-tailed deer", "Moose", "Bald eagle"],
        "photo_spots": ["Cadillac Mountain summit at sunrise", "Bass Harbor Head Lighthouse", "Jordan Pond with the Bubbles mountains"],
        "avg_daily_cost": 125
    },
    "olympic": {
        "state": "Washington",
        "best_season": "Summer (July-August) for dry weather and hiking",
        "top_activities": ["Explore Hoh Rain Forest", "Hike Hurricane Ridge for mountain views",
                           "Walk Ruby Beach on the Pacific coast"],
        "things_to_pack": ["Waterproof rain gear", "Gaiters", "Layers", "Waterproof boots"],
        "nearby_airports": ["Seattle, WA (SEA)", "Port Angeles, WA (CLM)"],
        "campgrounds": ["Kalaloch", "Hoh", "Sol Duc"],
        "fun_fact": "Olympic National Park contains three distinct ecosystems: temperate rainforest, alpine terrain, and over 70 miles of wild Pacific coastline.",
        "wildlife": ["Roosevelt elk", "Black bear", "River otter", "Bald eagle", "Banana slug"],
        "photo_spots": ["Hoh Rain Forest moss-covered trees", "Hurricane Ridge panoramic views", "Ruby Beach sea stacks at sunset"],
        "avg_daily_cost": 135
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
      4. Wildlife & photography guide          (OPTION B: new planning step)
      5. Budget estimate                       (OPTION B: new planning step)
      6. Combine everything into a final summary
    Each step uses output from previous steps — that's what makes this an agent.
    """
    park = get_park_info(park_name)
    if park is None:
        print(f"\nSorry, I don't have info about '{park_name}'.")
        print(f"Available parks: {', '.join(PARK_INFO.keys())}")
        return None, None  # return nothing so caller can handle gracefully
 
    # Collect all output so we can optionally save it later (OPTION D)
    full_plan_lines = []
 
    def log(text=""):
        """Print a line and also store it for saving."""
        print(text)
        full_plan_lines.append(text)
 
    log(f"\n{'='*60}")
    log(f"  National Park Trip Planner Agent")
    log(f"  Planning your trip to: {park_name.title()}")
    log(f"{'='*60}\n")
 
    # STEP 1: Create an itinerary
    log("[Agent] Step 1: Creating a trip itinerary...\n")
    planning_prompt = f"""You are a trip planning assistant. A user wants to visit {park_name.title()} National Park.
Here is what we know about the park:
- Location: {park['state']}
- Best time to visit: {park['best_season']}
- Top activities: {', '.join(park['top_activities'])}
Create a simple 2-day itinerary. For each day, list 2-3 activities with a one-sentence description.
Keep it short and practical."""
    itinerary = ask_llm(planning_prompt)
    log("--- Itinerary ---")
    log(itinerary)
 
    # STEP 2: Packing list based on the itinerary
    log("\n[Agent] Step 2: Building a packing list...\n")
    packing_prompt = f"""Based on this itinerary for {park_name.title()} National Park:
{itinerary}
And these recommended items: {', '.join(park['things_to_pack'])}
Create a short packing checklist organized into categories (Clothing, Gear, Safety).
Keep it to 10 items or fewer."""
    packing_list = ask_llm(packing_prompt)
    log("--- Packing List ---")
    log(packing_list)
 
    # STEP 3: Travel logistics
    log("\n[Agent] Step 3: Figuring out travel logistics...\n")
    logistics_prompt = f"""A traveler is visiting {park_name.title()} National Park in {park['state']}.
Nearby airports: {', '.join(park['nearby_airports'])}
Campground options: {', '.join(park['campgrounds'])}
Write 2-3 short travel tips about getting there and where to stay.
Include a fun fact: {park['fun_fact']}"""
    logistics = ask_llm(logistics_prompt)
    log("--- Travel Tips ---")
    log(logistics)
 
    # --- OPTION B: Step 4 — Wildlife & Photography Guide ---
    log("\n[Agent] Step 4: Wildlife & photography guide...\n")
    wildlife_prompt = f"""You are a nature guide for {park_name.title()} National Park.
Wildlife commonly spotted: {', '.join(park['wildlife'])}
Best photography spots: {', '.join(park['photo_spots'])}
Based on the trip itinerary below, suggest:
1. Two animals the visitor is most likely to encounter and when/where to look.
2. The single best photo opportunity for each day of the itinerary.
Keep your answer to 4-6 sentences.
Itinerary: {itinerary[:400]}"""
    wildlife_guide = ask_llm(wildlife_prompt)
    log("--- Wildlife & Photography Guide ---")
    log(wildlife_guide)
 
    # --- OPTION B: Step 5 — Budget Estimate ---
    log("\n[Agent] Step 5: Estimating trip budget...\n")
    budget_prompt = f"""You are a budget travel advisor. A visitor is planning a 2-day trip to {park_name.title()} National Park.
Estimated average daily cost for this park: ${park['avg_daily_cost']} (covers campsite, food, and fuel).
National Park entrance fee: $35 per vehicle.
Based on the itinerary and packing list below, give a simple 2-day budget breakdown:
- Park entrance
- Camping (2 nights)
- Food (2 days)
- Gear/supplies estimate
- Total estimate
Keep it concise, use real dollar amounts, and round to the nearest $5.
Itinerary: {itinerary[:300]}
Packing list highlights: {packing_list[:200]}"""
    budget = ask_llm(budget_prompt)
    log("--- Budget Estimate ---")
    log(budget)
 
    # STEP 6: Final summary combining everything
    log("\n[Agent] Step 6: Creating final summary...\n")
    summary_prompt = f"""You are a friendly travel agent. Combine these into a brief, exciting
trip summary for {park_name.title()} National Park. Use 3-4 sentences that would make
someone excited to go.
Itinerary highlights: {itinerary[:300]}
Key items to bring: {packing_list[:200]}
Travel info: {logistics[:200]}
Wildlife highlight: {wildlife_guide[:150]}
Budget: {budget[:150]}"""
    summary = ask_llm(summary_prompt)
    log("--- Your Trip Summary ---")
    log(summary)
 
    log(f"\n{'='*60}")
    log(f"  Agent complete! 6 steps executed.")
    log(f"{'='*60}\n")
 
    return "\n".join(full_plan_lines), park_name
 
# --- OPTION D: Save plan to a text file ---
def save_plan(plan_text, park_name):
    """Write the full trip plan to a timestamped text file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{park_name.replace(' ', '_')}_trip_plan_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(plan_text)
    print(f"[Agent] Trip plan saved to: {filename}")
    return filename
 
# --- RUN THE AGENT ---
print("Welcome to the National Park Trip Planner!")
print(f"Available parks: {', '.join(name.title() for name in PARK_INFO.keys())}")
print()
park_choice = input("Which park do you want to visit? ").strip().lower()
 
plan_text, chosen_park = plan_trip(park_choice)
 
# OPTION D: Offer to save the plan
if plan_text:
    save_answer = input("Would you like to save your trip plan to a text file? (yes/no): ").strip().lower()
    if save_answer in ["yes", "y"]:
        save_plan(plan_text, chosen_park)
 
# --- OPTION C: Follow-up questions ---
if plan_text:
    print("\nAsk follow-up questions about your trip! (type 'quit' to exit)\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in ["quit", "exit", "q", ""]:
            print("Happy travels! 🏕️")
            break
        followup_prompt = f"""You are a national park travel expert.
The user is planning a trip to {park_choice.title()} National Park.
Answer their question in 2-3 sentences.
Question: {question}"""
        answer = ask_llm(followup_prompt)
        print(f"Agent: {answer}\n")