scores = [85, 90, 95, 78, 92]

print("Chang Chi's Grade Summary")
print(f"Scores: {scores}")
print(f"Average: {sum(scores) / len(scores):.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest: {min(scores)}")
print(f"Passing scores: {sum(score >= 60 for score in scores)}/{len(scores)}")
