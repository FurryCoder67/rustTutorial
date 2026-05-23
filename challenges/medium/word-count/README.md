# Word Count

Count how many times each word appears in a phrase.

## Challenge

- Parse a string and count every word frequency.
- Words are separated by whitespace or punctuation.
- The count should be case-insensitive.

## Files

- `workspace.rs` — implement `word_count`.
- `solution.rs` — complete implementation.

## How it works

The solution normalizes the text to lowercase, removes punctuation, splits on whitespace, and counts each word using a map.

## Learning outcomes

- How to normalize text for case-insensitive comparison.
- How to count occurrences with `HashMap`.
- How to split input text into words safely.
