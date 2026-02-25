#Given two strings needle and haystack, return the index of the first occurrence of needle in 
# haystack, or -1 if needle is not part of haystack.

def strStr(haystack, needle):
    if needle == "":
        return 0

    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):
        if haystack[i:i+m] == needle:
            return i
    return -1


print(strStr("sadness", "sad"))