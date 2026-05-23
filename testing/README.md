# Testing Folder

## Files

- `testing.rs`
  - Contains examples of writing unit tests, integration tests, and using the built-in Rust test framework.

## How it works

Rust has a built-in test harness that works with `cargo test`. Tests are typically written in `#[cfg(test)]` modules and use the `#[test]` attribute.

Key concepts:

- `#[test]` marks a function as a test.
- `assert!`, `assert_eq!`, and `assert_ne!` verify expected behavior.
- The test harness discovers and runs tests automatically.
- Integration tests and benchmarks can be organized separately from library code.

## Learning outcomes


- How to write and run Rust tests.
- How to use assertions for test validation.
- How Rust’s test framework is integrated with Cargo.
- Why testing is important for safe, reliable Rust code.
