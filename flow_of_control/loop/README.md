# Loop Folder

This folder dives into Rust loop constructs, including plain loops, labels, nesting, and returning values from loops.

## Files

- `loop.rs`
  - Introduces the basic `loop` construct, which repeats until explicitly broken out of.
- `nesting_and_labels.rs`
  - Demonstrates nested loops and loop labels to specify which loop `break` or `continue` should affect.
- `returning_from_loops.rs`
  - Shows how loops can produce values via `break`, treating the loop itself as an expression.

## How it works

Rust loops are expressions too, meaning they can yield values. This folder explains the mechanics of infinite loops, labeled control flow, and how to use `break` with data.

Key concepts:

- `loop` runs indefinitely until `break` or `return` exits it.
- Labels like `'outer:` allow fine-grained control in nested loops.
- `break value` makes the loop expression evaluate to that value.
- `continue` restarts the current loop iteration while preserving labels.

## Learning outcomes

You will learn:

- How plain loops differ from `for` and `while`.
- How to control nested loops safely.
- How to use loops as expressions to return results.
- How labels make multi-level loop control readable and deterministic.
