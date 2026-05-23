# Closures Folder

This folder explains Rust closures in depth: how they capture environment, how they are typed, and how they are used as arguments and return values.

## Files

- `closures.rs`
  - Introduces closure syntax, including how closures differ from normal functions.
- `capturing.rs`
  - Demonstrates how closures capture variables from the surrounding scope by borrowing, mutably borrowing, or moving.
- `input_parameters.rs`
  - Shows how to declare closure parameters and use closures in places that expect functions.
- `output_parameters.rs`
  - Explains closures that return values and how their return types are inferred.
- `type_anonymity.rs`
  - Covers the anonymous type of closures and why closures often need generic function parameters or `impl Fn` traits.
- `examples/`
  - Contains more practical closure usage examples with iterators and search patterns.

## How it works

Closures are Rust’s lightweight anonymous functions. They can capture surrounding variables automatically, which makes them useful for short pieces of behavior.

Important details:

- Closures infer their parameter and return types from context when possible.
- The compiler chooses capture mode (`&T`, `&mut T`, or `T`) based on how the closure uses external variables.
- Closure types are unique and anonymous, so generic bounds like `Fn`, `FnMut`, and `FnOnce` are used for abstraction.

## Learning outcomes

After reading this folder, you should understand:

- The difference between `Fn`, `FnMut`, and `FnOnce`.
- How closures capture and use environment variables.
- Why closures are useful for iterator adapters and callback-style APIs.
- How to write closures that integrate with generic code.
