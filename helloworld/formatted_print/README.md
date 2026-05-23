# Formatted Print Folder

Teaches Rust's formatting macros, debug output, and custom display behavior.

## Files

- `formatted_print1.rs`
  - Introduces formatted printing with `println!` and `format!`, showing how placeholders and format specifiers work.
- `formatting_print2.rs`
  - Demonstrates more advanced formatting options, including width, precision, and named arguments.
- `debugging/`
  - Contains examples that focus on `Debug` formatting and debugging output.
- `display/`
  - Demonstrates custom `Display` implementations for user-defined types.

## How it works

Rust separates formatting concerns into traits. `Display` is for user-facing output, while `Debug` is for developer-facing debug output. Macros like `println!` use those traits to format values.

Important concepts:

- Formatting placeholders like `{}` and `{:?}` select the formatting trait.
- `format!` produces a string without printing it.
- Custom `Display` implementations let user-defined types control their text representation.
- `Debug` is automatically available for many types and is useful for quick inspection.

## Learning outcomes

After studying this folder, you will know:

- How to use Rust's formatting macros.
- How to control formatted output with specifiers.
- When to use `Debug` versus `Display`.
- How to implement the formatting traits for your own types.
