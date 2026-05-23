# Functions Folder

This folder covers how to define and call functions and methods in Rust, as well as the basics of closures.

## Files

- `functions.rs`
  - Shows how to define standalone functions, specify parameters and return types, and use function calls.
- `methods.rs`
  - Demonstrates struct methods, the `impl` block, and how `self`, `&self`, and `&mut self` differ.
- `diverging_functions.rs`
  - Explains diverging functions that never return, using the `!` return type, and when such functions are useful.
- `higher_order_functions.rs`
  - Covers functions that take other functions or closures as parameters, return functions, and demonstrate function-pointer semantics.
- `closures/`
  - Contains detailed coverage of closures, capturing environment, and type behavior.

## How it works

The key idea in this folder is that Rust functions are first-class constructs that can also be used as methods on types. The same folder introduces closures as anonymous functions that capture their surrounding environment.

Important concepts:

- Functions are declared with `fn` and can take typed arguments.
- Methods are declared inside `impl` and can read or modify the instance through `self` references.
- Diverging functions never return and are useful for panic paths and infinite loops.
- Higher-order functions unlock abstraction by accepting behavior as arguments.

## Learning outcomes

You will learn:

- How to design function interfaces in Rust.
- How methods encapsulate behavior on custom types.
- How closures differ from functions in syntax, capture, and type inference.
- How to write more reusable code with higher-order functions.
