class Solution:
    def sortByBits(self, arr):
        return sorted(arr, key=lambda x: (bin(x).count("1"), x))
