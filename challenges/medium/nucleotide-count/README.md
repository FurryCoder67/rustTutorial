# Nucleotide Count

Count the occurrences of each DNA nucleotide in a DNA strand.

## Challenge

- The valid nucleotides are `A`, `C`, `G`, and `T`.
- `count` should return how often a single nucleotide appears.
- `nucleotide_counts` should return counts for all four nucleotides.
- Invalid characters should produce an error.

## Files

- `workspace.rs` — implement `count` and `nucleotide_counts`.
- `solution.rs` — complete implementation.

## How it works

The solution validates the input and returns counts for each nucleotide in a fixed order.

## Learning outcomes

- How to validate string input.
- How to use `Result` for fallible operations.
- How to keep a fixed-order count of multiple categories.
