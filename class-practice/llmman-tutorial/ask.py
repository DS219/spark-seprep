"""Ask a question of a model served by `llmman serve`.

Uses only the Python standard library, so there is nothing to pip install.

    python3 ask.py "What is a model server?"
"""

import json
import sys
import urllib.request

ENDPOINT = "http://127.0.0.1:17434/v1/chat/completions"
MODEL = "gemma3:4b"

question = " ".join(sys.argv[1:]) or "In two sentences, what is a model server?"

request_body = {
    "model": MODEL,
    "messages": [
        # Try changing the system message and asking the same question again.
        {"role": "system", "content": "You are a friendly tutor. Answer briefly."},
        {"role": "user", "content": question},
    ],
}

request = urllib.request.Request(
    ENDPOINT,
    data=json.dumps(request_body).encode("utf-8"),
    headers={"Content-Type": "application/json"},
)

with urllib.request.urlopen(request) as response:
    reply = json.load(response)

print(reply["choices"][0]["message"]["content"])
