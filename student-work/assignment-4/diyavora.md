# Diya Vora

Hi,my name is Diya Vora and my favourite programming language is python because it is fun and easy to do

## Example Code

```
ArrayNames=["" for i in range(11)]
ArrayScores=[0 for j in range(11)]


def ReadHighScores():
    global ArrayNames
    global ArrayScores
    index=0
    filename="Highscore.txt"
    file=open(filename,'r')
    data=file.readline().strip()
    while data!="":
        ArrayNames[index]=data
        ArrayScores[index]=int(file.readline().strip())
        index=index+1
        data=file.readline().strip()
    file.close() 
```

### Code explanation
This python code is a function for reading high scores of a file and stores the names and scores in two lists


