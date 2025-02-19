# Charo Payares 

My favorite programming language is probably java because I like that it is a strongly typed language. I feel it makes me more aware
of how the methods I write are actually being structured/working every step of the way.

## Example Code
```
public MyArray(int[] arr){
        //makes a new array obj of the array inputs size
        newArray = new int[arr.length];
        
        //iterates over each element of the array
        for(int i = 0; i < arr.length; i++){

            //checks if the array element is valid with the given bounds
            if (arr[i] >= LOWER && arr[i] <= UPPER){
                
                //changes the array to hold the value of the input array if it is a valid value
                newArray[i] = arr[i];

                //adds 1 to numElements as one number has been entered to the array
                numElements += 1;
            }
        }
    }
``` 
### Code Explanation, this is a constructor for a class MyArray that constructs a new instance of the class when given the input of an integer array. It will return the new MyArray object of the same length of the array but without the array elements that are invalid due to given Upper and lower bounds.

