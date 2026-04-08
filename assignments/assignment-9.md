# Assignment 9: Build a National Park Trip Planner Agent

## Overview

In this assignment, you will build a simple AI **agent** — a program that takes a goal, breaks it into
steps, and executes each step using a language model. Your agent will plan a trip to a U.S. National Park.

You'll run a small language model **locally on your laptop** using Ollama — no API keys, no cloud accounts, no cost.

This builds on what we covered with local LLMs. The difference here is that instead of asking a model
a single question (like a chatbot), your program will **orchestrate multiple calls** to the model, feeding
the output of one step into the next. That's what makes it an agent.

## Setup

### Install Ollama

1. Go to [https://ollama.com/download](https://ollama.com/download)
2. Download and install for your operating system
3. Open a terminal and verify:

```bash
ollama --version
```

### Pull a Small Model

We'll use **smollm2**, a small model (~1GB) that runs on almost any laptop:

```bash
ollama pull smollm2:1.7b
```

> If your laptop has 8GB+ RAM, you can try `qwen2.5:3b` for better quality responses.
> If resources are tight, `smollm2:360m` is even smaller.

### Make Sure Ollama is Running

On Mac, Ollama usually starts automatically. If not, open a **separate terminal** and run:

```bash
ollama serve
```

Leave that terminal open. You'll use a different terminal for the rest of the assignment.

### Test It

```bash
ollama run smollm2:1.7b "What is Yellowstone National Park known for?"
```

You should see a response about geysers, wildlife, etc. If this works, you're good to go.

### Set Up Python

You'll need Python 3.8+ and the `requests` library.

```bash
python3 --version
```

Create a virtual environment (this avoids permission errors when installing packages):

```bash
python3 -m venv park-env
```

Activate it:

```bash
# Mac/Linux:
source park-env/bin/activate

# Windows:
park-env\Scripts\activate
```

You should see `(park-env)` at the start of your terminal prompt. Now install the library we need:

```bash
pip install requests
```

> **Important:** Every time you open a new terminal to work on this assignment, you'll need to
> activate the environment again with the `source` (or Windows) command above.

## Part 1: Talk to Your Local Model from Code

Create a file called `park_agent.py`. This starter code sends a prompt to the model running on your machine
and prints the response. Read through the comments — they explain what each part does.

```python
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

# Quick test
answer = ask_llm("Name 3 national parks in Utah.")
print(answer)
```

Run it:

```bash
python3 park_agent.py
```

You should see parks like Zion, Bryce Canyon, Arches, etc. Everything is running locally on your machine —
no internet connection to an AI service needed.

## Part 2: Build the Agent

Now replace the test code at the bottom of your file with the full agent below. This is the core of the
assignment — **read through the code carefully** and understand what each step does before running it.

```python
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


# --- RUN THE AGENT ---
print("Welcome to the National Park Trip Planner!")
print(f"Available parks: {', '.join(name.title() for name in PARK_INFO.keys())}")
print()
park_choice = input("Which park do you want to visit? ")
plan_trip(park_choice)
```

Run it and pick a park:

```bash
python3 park_agent.py
```

Watch the agent work through its 4 steps. Notice how each step builds on the previous one — the packing list
is based on the itinerary, not generated in isolation. That chaining is the key idea.

## Part 3: Make It Your Own

Pick **at least two** of the following enhancements:

### Option A: Add More Parks
Add 2 more national parks to the `PARK_INFO` dictionary with real information.

### Option B: Add a New Planning Step
Add a **Step 5** to the agent. Ideas:
- Wildlife you might see
- Budget estimate for the trip
- Photography spots
- Food and dining options near the park

Follow the same pattern: build a prompt with context from previous steps, call `ask_llm()`, print the result.

### Option C: Follow-up Questions
After the plan is generated, let the user ask follow-up questions about their trip. Add this after
`plan_trip()` finishes:

```python
print("\nAsk follow-up questions about your trip! (type 'quit' to exit)\n")
while True:
    question = input("You: ")
    if question.lower() in ["quit", "exit", "q"]:
        break
    followup_prompt = f"""You are a national park travel expert.
The user is planning a trip to {park_choice.title()} National Park.
Answer their question in 2-3 sentences.

Question: {question}"""
    answer = ask_llm(followup_prompt)
    print(f"Agent: {answer}\n")
```

### Option D: Save the Plan
Write the full trip plan to a text file so the user can keep it. You can use Python's built-in
file writing — no extra libraries needed.

## Deliverables

You need to submit **three things** for this assignment:

| # | What | Where |
|---|---|---|
| 1 | `park_agent.py` — your completed agent with at least 2 enhancements | Pull request on GitHub |
| 2 | Demo video — 1.5 minutes or less showing your agent running | Link in the Google Form |
| 3 | Reflection answers — responses to the questions in the form | Google Form |

That's it — one file in your PR, everything else goes in the form.

## Submission Instructions

### Step 1: Record a Short Demo

Record a **1.5 minute or less** video showing your agent running and producing a trip plan.
Use a screen recorder — no need for audio, but feel free to add it. Use an editor to cut out
any long wait times while the model generates responses. We don't want to watch the model think!

Upload your video somewhere accessible (Google Drive, YouTube unlisted, etc.) and have the link ready.

### Step 2: Sync and Branch

Make sure your local repo is up to date and create a new branch:

```bash
cd spark-seprep
git fetch upstream
git checkout -b assignment-9 upstream/main
```

### Step 3: Add Your File

Place **only** your `park_agent.py` in the correct directory:

```
spark-seprep/student-work/assignment-9/<firstname-lastname>/
└── park_agent.py
```

For example:

```bash
mkdir -p student-work/assignment-9/jane-doe
cp /path/to/your/park_agent.py student-work/assignment-9/jane-doe/
```

### Step 4: Commit and Push

Write a clear, descriptive commit message. Your PR should contain **only 1 commit**.

```bash
git add student-work/assignment-9/<firstname-lastname>/park_agent.py
git commit -m "Add national park agent - <brief description of your enhancements>"
git push origin assignment-9
```

If you need to make corrections after committing, use `git commit --amend` and `git push -f`
rather than creating additional commits.

### Step 5: Open a Pull Request

Open a PR against `DS219/spark-seprep` from your fork's `assignment-9` branch.
Your PR should contain **only one file** (`park_agent.py`) — no extra files, no changes to other parts of the repo.

### Step 6: Submit the Form

Fill out the submission form with your PR link, video link, and reflection answers:
[Form to submit assignment](https://forms.gle/559PR37hSzXChM87A)

> **Your assignment is not complete until both the PR and the form are submitted.**

## Grading

| Component | Points |
|---|---|
| Agent runs successfully and produces a trip plan | 5 |
| At least 2 enhancements from Part 3 implemented | 5 |
| Demo video shows agent working (1.5 min or less) | 3 |
| Reflection answers in form are thoughtful | 3 |
| Clear, descriptive commit message | 1 |
| Single commit in PR, only `park_agent.py`, no extraneous files | 2 |
| Correct branch and directory structure | 1 |
| **Total** | **20** |

## Troubleshooting

| Problem | Fix |
|---|---|
| "Connection refused" error | Make sure Ollama is running — open a terminal and run `ollama serve` |
| Model is very slow | Try a smaller model: change `smollm2:1.7b` to `smollm2:360m` in your code |
| Response quality is poor | Small models aren't perfect — try more specific prompts, or use `qwen2.5:3b` if your machine handles it |
| Python not found | Try `python` instead of `python3`, or `py` on Windows |
| `requests` not found | Run `pip3 install requests` (or `pip install requests`) |
