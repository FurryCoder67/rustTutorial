# Destructuring Folder

This folder contains detailed examples of destructuring in Rust, the process of breaking complex values into their component parts.

## Files

- `destructuring_arrays-slices.rs`
  - Shows how arrays and slices can be matched by pattern and how portions can be extracted.
- `destructuring_enums.rs`
  - Demonstrates matching enum variants and pulling out associated values.
- `destructuring_pointers-ref.rs`
  - Explains pattern matching on pointers and references, including `&` and `ref` bindings.
- `destructuring_structs.rs`
  - Shows how to destructure structs by field names and how to ignore unused fields.
- `destructuring_tuples.rs`
  - Demonstrates tuple destructuring and how tuple patterns align with tuple structure.

## How it works

Destructuring is a key Rust pattern feature. It lets you match the shape of a value and bind its pieces in a single expression. Pattern matching is used in `let`, `match`, `if let`, and function parameters.

Key ideas:

- The shape of the pattern must match the shape of the value.
- Destructuring can be shallow or nested.
- Patterns can include wildcards `_` and variable bindings.
- Borrowing patterns preserve ownership or allow shared access depending on the pattern form.

## Learning outcomes

You will learn:

- How to destructure arrays, slices, enums, structs, and tuples.
- When to use destructuring for concise code.
- How reference patterns help avoid moving values unnecessarily.
- How destructuring interacts with ownership and borrowing.
