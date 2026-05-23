# Flow of Control Folder

Focuses on Rust control flow constructs: conditional execution, loops, and pattern matching. It is one of the most important chapters for understanding how Rust programs make decisions.

## Files

- `if-else.rs`
  - Shows standard `if` and `else` branching and explains how Rust conditions must evaluate to `bool`.
- `if_let.rs`
  - Demonstrates `if let` for selectively matching a pattern and extracting data from enums or option-like values.
- `let-else.rs`
  - Covers the `let ... else` construct for early exits when pattern matching fails while destructuring values.
- `while_loop.rs`
  - Introduces `while` loops and explains when Rust repeats computation until a condition becomes false.
- `while-let.rs`
  - Combines `while` loops with pattern matching, allowing loops to continue while a value matches a pattern.
- `for_and_range_loops.rs`
  - Explains `for` loops, iterators, and range expressions.
- `loop/`
  - Contains deeper loop examples including labeled loops and returning values from loops.
- `match/`
  - Contains pattern matching examples including guards, binding, and destructuring nested data.

## How it works

Rust control flow is unified around the idea of expressions that produce values and patterns that match data. It shows both the simplest style of branching and the more powerful `match` expression.

Key points:

- `if` in Rust is an expression, so it can return values.
- `match` is exhaustive, forcing you to handle every possible shape of data.
- Loop labels and `break` with values let you write complex loops in a structured way.
- Pattern-based constructs like `if let`, `while let`, and `let else` make the flow both safe and concise.

## Learning outcomes

## Learning outcomes

- The difference between `if`, `match`, and loop constructs.
- How to apply pattern matching to control flow.
- How loop labels and values work in Rust.
- How to structure code to handle optional or error cases cleanly.
