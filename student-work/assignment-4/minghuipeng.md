# Minghui Peng

Hi! I'm Minghui, and my favorite programming language is Rust. I love Rust because of its memory safety, performance, and strong type system. It empowers developers to write efficient and reliable code without worrying about common issues like null pointer dereferencing or data races.

## Code Example

Here’s a fun Rust program that prints a countdown before launching a "spaceship" 🚀:

```rust
fn main() {
    for i in (1..=5).rev() {
        println!("T-minus {}...", i);
    }
    println!("🚀 Liftoff!");
}
```
### Code Explanation

	•	The for i in (1..=5).rev() loop counts down from 5 to 1.
	•	println!() is used to print each countdown step.
	•	After the countdown, it prints "🚀 Liftoff!" to simulate a rocket launch.

To run this code, save it as main.rs and execute:
rustc main.rs
./main

You’ll see:
T-minus 5...
T-minus 4...
T-minus 3...
T-minus 2...
T-minus 1...
🚀 Liftoff!
Enjoy the countdown!
