# Error Handling Folder

## Files

- `error.rs`
  - Contains examples of handling recoverable and unrecoverable errors in Rust.

## How it works

Rust separates recoverable errors from unrecoverable errors. Recoverable errors use `Result<T, E>`, while unrecoverable errors use panic.

Key concepts:

- `Result` is the standard type for recoverable errors.
- `Option` is often used when a value may be absent.
- Error propagation uses `?` to return early on failure.
- `panic!` aborts the current thread for unrecoverable failures.

## Learning outcomes

From this folder, you should learn:

- How to use `Result` and `Option` for error handling.
- How to propagate errors with `?`.
- When to use `panic!` versus returning a `Result`.
- Why Rust’s error model is explicit and type-safe.
