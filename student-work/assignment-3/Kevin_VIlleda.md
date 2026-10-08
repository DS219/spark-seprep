# Kevin Villeda De Leon 

My favorite programming language is python. I like python because it is easy to understand and very versatile. It is also very well documented as well as syntax friendly. 

## Example Code

```
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  #what we want to insert
        j = i - 1     # index of last element in sorted array
        
        # Move elements
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
    return arr

```

## Code Explanation

Insertion sort is an algorithm that sorts the elements in a list. The way the algorithm does this is by going through each element (other than the first) and "inserting" it into the correct position up to whatever index (i) we are on (it doesn't actually insert it just moves the positions of the elements greater than it to the right and then places the current element in that gap). So that means the start of the array up to i will always be sorted as we move through the array. Once we reach the end we should have a fully sorted list. 

To run this function you call upon the function and input an array. 