def isAnagram(s, t):
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for i in range(len(s)):
        count_s[s[i]] = count_s.get(s[i], 0) + 1
        count_t[t[i]] = count_t.get(t[i], 0) + 1
        
    return count_s == count_t


# Test case 1 (True case)
s = "anagram"
t = "nagaram"
result = isAnagram(s, t)
print(f"Is '{s}' an anagram of '{t}'? {result}")

# Test case 2 (False case)
s = "rat"
t = "car"
result = isAnagram(s, t)
print(f"Is '{s}' an anagram of '{t}'? {result}")


	
