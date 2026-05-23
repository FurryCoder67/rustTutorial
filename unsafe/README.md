# Unsafe Operations Folder

This folder corresponds to the Rust by Example Unsafe Operations chapter.

## Files

- `unsafe.rs`
  - Contains examples of `unsafe` blocks, raw pointers, and other operations that bypass some of Rust’s safety checks.

## How it works

Unsafe Rust gives you access to low-level operations that are not checked by the borrow checker. It is still part of Rust, but it requires careful guarantees from the programmer.

Important concepts:

- `unsafe` blocks allow dereferencing raw pointers and calling unsafe functions.
- Unsafe code can still be used safely when its invariants are upheld.
- Raw pointers are `*const T` and `*mut T`.
- Unsafe code is typically isolated behind safe abstractions.

## Learning outcomes

From this folder, you should learn:

- When and how to use `unsafe` code.
- What raw pointers are and how they behave.
- Why unsafe operations should be minimized and encapsulated.
