# Urvashi Mohnani

Hi, my name is Urvashi Mohnani and my favorite programing language is Go because I love developing container related technology!

## Example code

```
package main
import("fmt";"math/rand";"time")
func main(){
    rand.Seed(time.Now().UnixNano())
    jokes := []string{"There are 10 types of people in the world: those who understand binary and those who don't.","Why did the programmer quit his job? Because he didn't get arrays.","I'm not lazy, I'm just in energy-saving mode.","Debugging: Removing the needles from the haystack."}
    fmt.Println(jokes[rand.Intn(len(jokes))])
}
```

### Code explanation

This script will display one random joke each time you run it. To run from the terminal, copy the above to a `jokes.go` and run it with `go run jokes.go`.
You need to have Golang installed. See [Golang install documentation](https://go.dev/doc/install). 

