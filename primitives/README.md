# Primitives Folder

Introduces Rust primitive compound types: arrays, slices, tuples, and literal values.

## Files

- `arrays_and_slices.rs`
  - Explains fixed-size arrays, slice references, and how Rust treats arrays and slices differently.
- `tuples.rs`
  - Demonstrates tuples as fixed-size heterogeneous collections and how to destructure them.
- `literals_and_operators.rs`
  - Covers numeric, boolean, and string literals, plus Rust operator behavior for arithmetic, comparisons, and logic.

## How it works

Covers the simplest data structures Rust provides out of the box and how they behave with ownership and borrowing.

Important ideas:

- Arrays have a fixed length known at compile time and may live on the stack.
- Slices are views into collections; they do not own the data and can be borrowed from arrays or vectors.
- Tuples group values of different types together, and pattern matching can extract tuple elements.
- Literal syntax defines values directly in code; operators perform expression-based transformations.

## Learning outcomes

## Learning outcomes

- The difference between owned arrays and borrowed slices.
- How tuples provide lightweight grouping of values.
- How literals and operators form the basis of Rust expressions.
