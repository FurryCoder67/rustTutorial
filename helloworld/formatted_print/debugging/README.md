# Debugging Folder

Contains examples of Rust's debugging formatting capabilities.

## Files

- `debug1.rs`
  - Introduces the `{:?}` formatter for printing debug representations of values.
- `debug2.rs`
  - Demonstrates how derived `Debug` can automatically format structs and enums.
- `debug3.rs`
  - Shows custom debug output and how debug formatting can help inspect complex data.

## How it works

Rust uses the `Debug` trait for developer-focused output. Most standard types implement `Debug`, and custom types can derive or implement it manually.

Key points:

- `{:?}` prints a debug representation, while `{:#?}` pretty-prints it.
- Deriving `Debug` is usually the fastest way to get debug output for custom types.
- Debug formatting is intended for debugging, not polished user-facing text.

## Learning outcomes

Teaches:

- How to use debug formatting for inspection.
- How to derive `Debug` on structs and enums.
- How debug output differs from custom display output.
- Why debug formatting is helpful during development.
