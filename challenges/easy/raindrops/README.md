# Raindrops

Convert a number to a string that contains raindrop sounds corresponding to certain factors.

## Challenge

- If the number has 3 as a factor, add `Pling` to the result.
- If the number has 5 as a factor, add `Plang` to the result.
- If the number has 7 as a factor, add `Plong` to the result.
- If the number does not have any of those factors, return the number as a string.

## Files

- `workspace.rs` — implement `convert`.
- `solution.rs` — complete implementation.

## How it works

The function checks divisibility by 3, 5, and 7, then constructs the resulting string in order.

## Learning outcomes

- How to test divisibility.
- How to build a string conditionally.
- How to return either text or a numeric string.
