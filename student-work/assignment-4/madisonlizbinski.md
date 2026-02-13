# Madison Lizbinski

Hi, my name is Madison Lizbinski and my favorite programming language is rust because of its memory safety and performance!

## Example code

```rust
use rand::Rng;

fn main() {
    let fortunes = [
        "You will debug code and it will actually work the first time.",
        "A mysterious bug will disappear when you add a println! statement.",
        "Today is a good day to cargo build.",
        "Your borrow checker errors will guide you to enlightenment.",
        "You will discover a missing semicolon... after 30 minutes.",
    ];

    let mut rng = rand::thread_rng();
    let random_index = rng.gen_range(0..fortunes.len());

    println!("Rust Fortune:");
    println!("{}", fortunes[random_index]);
}
```

### Code Explanation
This Rust program prints a random tech fortune each time it runs. It stores several fortunes in an array, generates a random number, and prints the fortune at that index.To run this in the terminal create a new project with cargo new rust-fortune, add rand = "0.8" to Cargo.toml, paste the code into src/main.rs, then run it from the project folder using cargo run.
