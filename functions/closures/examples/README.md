# Closure Examples Folder

Contains practical closure examples that show how closures are used with iterators, searching, and common collection operations.

## Files

- `iterator-any.rs`
  - Demonstrates using a closure with the `Iterator::any` method to check whether any element satisfies a condition.
- `searching-through.rs`
  - Shows how closures can be used in iterator adapters and search patterns to traverse collections cleanly.

## How it works

Closures here are used to define small, reusable predicates and transformation logic inline. That keeps the code concise while still leveraging Rust’s strong typing and safety.

Key ideas:

- Iterator adapters like `any`, `map`, `filter`, and `find` take closures as arguments.
- Closures can capture loop variables and compare them against collection elements.
- Using closures with iterators reduces boilerplate and expresses intent declaratively.

## Learning outcomes

From this folder, you should learn:

- How to use closures as inline callbacks.
- How iterator methods improve code readability.
- How closure capture interacts with collection iteration.
- Why closures are a natural fit for search-style code.
