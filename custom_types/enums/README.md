# Enums Folder

Explains Rust enums and several different ways to use them.

## Files

- `c-like-enums.rs`
  - Demonstrates C-like enums that behave like integer constants with named variants.
- `enums.rs`
  - Shows richer enums with associated data and how they encode variant-specific payloads.
- `use.rs`
  - Covers importing enum variants with `use` to simplify pattern matching and construction.
- `testcase_linked_lists.rs`
  - Uses enums to build a linked list structure, demonstrating how recursive enums represent recursive data.

## How it works

Enums in Rust are algebraic data types. They let a single type represent multiple variants, each of which may carry different data.

Important concepts:

- C-like enums are simple tagged integer values.
- Rich enums can store different data for each variant.
- Pattern matching on enums is exhaustive, which ensures all cases are handled.
- Recursive enums are a common way to represent linked data structures like lists and trees.

## Learning outcomes

Teaches:

- How to define both simple and complex enums.
- How to use enums as a safer alternative to tagged unions or discriminated unions.
- How to import and match enum variants cleanly.
- How recursive enums model data types such as linked lists.
