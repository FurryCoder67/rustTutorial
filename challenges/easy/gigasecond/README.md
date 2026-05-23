# Gigasecond

Calculate the moment when someone has lived for one gigasecond (1,000,000,000 seconds) after a given starting time.

## Challenge

- Implement `add_gigasecond` to return the moment exactly one gigasecond after the input.
- Use the standard library `SystemTime` type.

## Files

- `workspace.rs` — implement `add_gigasecond`.
- `solution.rs` — complete implementation.

## How it works

A gigasecond is a fixed duration of 1,000,000,000 seconds. The function adds that duration to the input time and returns the resulting timestamp.

## Learning outcomes

- How to use `std::time::SystemTime` and `Duration`.
- How to perform time arithmetic in Rust.
- How to return a new timestamp without mutating the original.
