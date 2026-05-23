# Types Folder

Covers Rust's type-related fundamentals, including aliasing, casting, inference, and literal types.

## Files

- `aliasing.rs`
  - Explains `type` aliases and how they help document code and simplify long type names.
- `casting.rs`
  - Shows numeric casting with the `as` keyword and explains when explicit conversions are required.
- `inference.rs`
  - Demonstrates Rust's type inference rules and how the compiler determines types from usage.
- `literals.rs`
  - Covers numeric, boolean, character, and string literals, including literal suffixes and default types.

## How it works

Rust is a statically typed language, and Explains how type information is both explicit and inferable. It also shows how the compiler enforces type correctness and why explicit casts are necessary when converting between incompatible primitive types.

Important points:

- `type` aliases do not create new types; they create a new name for an existing type.
- Rust requires explicit casting for many primitive conversions to avoid silent data loss.
- Type inference reduces verbosity, but the compiler still ensures every expression has a concrete type.
- Literal suffixes like `42u8` or `3.14f64` set exact types for constants.

## Learning outcomes

Teaches:

- How to use aliasing for readable APIs.
- When and how to cast primitive values safely.
- How Rust infers types from context.
- How literals are typed and how to control literal type selection.
