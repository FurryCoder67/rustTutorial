# All Your Base

Convert numbers between different bases using a generalized base conversion algorithm.

## Challenge

- Implement `decode` to convert a string representation from a given base to a decimal number.
- Implement `encode` to convert a decimal number into a string representation in a target base.
- Implement `reencode` to convert from one base to another.
- Reject invalid bases and invalid digits for the given base.

## Files

- `workspace.rs` — implement `decode`, `encode`, and `reencode`.
- `solution.rs` — complete implementation.

## How it works

The solution validates base ranges and digit characters, then performs positional arithmetic to decode and encode numbers between bases.

## Learning outcomes

- How to validate input for base conversion.
- How to implement number encoding and decoding.
- How to handle radixes greater than 10.
