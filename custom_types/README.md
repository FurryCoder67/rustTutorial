# Custom Types Folder

This folder explores Rust's custom type system, covering constants, user-defined structures, and enumerations.

## Files

- `constants.rs`
  - Explains Rust constants and `static` values, how they differ from variables, and when to use compile-time constant values.
- `structures.rs`
  - Demonstrates how to define structs, instantiate them, use field syntax, and perform destructuring of struct values.
  - Explains tuple structs, named-field structs, and the value semantics of structs.
- `enums/`
  - Contains examples of Rust enums, including C-like enums, algebraic data types, and enum usage patterns.

## How it works

Custom types in Rust are the foundation of expressive, type-safe programs. It demonstrates:

- How `struct` creates a named composite type with fields.
- How `enum` can represent a value that is one of several variants, possibly with associated data.
- Why constants are useful for fixed compile-time values and how `const` differs from `let`.

Enums are powerful because they combine variant shape, pattern matching, and strong typing, which is why the `enums/` subfolder is grouped separately.

## Learning outcomes


- How to define and use structs and constants.
- How Rust enforces memory safety through value ownership in structs.
- How enums express variant-based data and how they integrate with pattern matching.
