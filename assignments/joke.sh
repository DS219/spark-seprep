#!/usr/bin/env bash

fallback_joke="Why do programmers prefer dark mode? Because light attracts bugs."

if joke=$(curl -fsSL --max-time 10 -H "Accept: text/plain" https://icanhazdadjoke.com/); then
  printf '%s\n' "$joke"
else
  printf '%s\n' "$fallback_joke"
fi
