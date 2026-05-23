# Hello World Folder

This folder contains the very first Rust examples: comments, printing, formatting, and debugging. It is designed to teach the foundations of Rust syntax and output.

## Files

- `helloworld.rs`
  - Contains the canonical simple Rust program with `fn main()` and `println!`.
- `comments.rs`
  - Demonstrates Rust comment syntax, including single-line `//` and block comments `/* ... */`.
- `formatted_print/`
  - Contains examples of formatted printing, including `format!`, `println!`, debug formatting, and custom display.

## How it works

This folder is the introduction to Rust syntax. It shows how macros like `println!` and `format!` are built into Rust for output formatting, and how Rust uses braces and format traits to control how values are printed.

Key ideas:

- `println!` is a macro that expands to code that writes to standard output.
- Formatting traits like `Display` and `Debug` control how values are rendered.
- Comments are ignored by the compiler and are used for human-readable documentation.

## Learning outcomes

After studying this folder, you should understand:

- The structure of a minimal Rust program.
- How to write comments and why they matter.
- How Rust formatting macros work and why the formatting system is powerful.
- The difference between regular display formatting and debug formatting.
