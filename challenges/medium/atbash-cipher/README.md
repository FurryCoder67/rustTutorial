# Atbash Cipher

Encode and decode text using the Atbash substitution cipher.

## Challenge

- `encode` should transform plaintext to cipher text using the reversed alphabet.
- `decode` should convert cipher text back into plaintext.
- Encoding groups output into blocks of 5 characters separated by spaces.
- The cipher ignores punctuation and case.

## Files

- `workspace.rs` — implement `encode` and `decode`.
- `solution.rs` — complete implementation.

## How it works

Atbash maps `a` to `z`, `b` to `y`, and so on. The implementation normalizes characters, applies the substitution, and formats output in chunks.

## Learning outcomes

- How to implement a simple substitution cipher.
- How to normalize and transform strings.
- How to format encoded output into fixed-size groups.
