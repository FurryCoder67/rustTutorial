# Match Folder

This folder is focused on Rust's `match` expression and related pattern-matching constructs.

## Files

- `match.rs`
  - Introduces the basic `match` expression and explains exhaustive matching.
- `guards.rs`
  - Demonstrates match guards, which add boolean conditions to patterns.
- `binding.rs`
  - Shows the use of `@` bindings inside patterns to capture matched values while still testing them.
- `destructuring/`
  - Contains examples of destructuring arrays, enums, pointers/references, structs, and tuples.

## How it works

`match` is Rust's central tool for branching on the shape of values. Exhaustiveness ensures that every possible variant is handled, and pattern matching works with many compound types.

Important points:

- Patterns can test and bind values simultaneously.
- `match` arms can include guards for more precise logic.
- The compiler verifies that all cases are covered or uses a wildcard `_` branch.
- Pattern matching scales to nested data structures.

## Learning outcomes

After reading this folder, you should understand:

- The power of pattern matching in Rust.
- How `match` differs from `if`/`else`.
- How guards and bindings extend pattern expressiveness.
- How destructuring makes it easy to work with nested values.
