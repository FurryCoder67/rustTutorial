# Crates Folder

Teaches the Rust crate system, with one side demonstrating how to use an existing crate and the other showing how to create a library crate.

## Files

- `using_a_library.rs`
  - Shows how to depend on an external crate or a local library crate, how to add the dependency to `Cargo.toml`, and how to import items with `use`.
  - Demonstrates the separation between crate root and public API surface.
- `creating_a_library/`
  - Contains an example library crate implementation. This folder demonstrates how to design a crate's public API using `pub`, how to keep implementation details private, and how to structure module exports.

## How it works

In Rust, a crate is the primary compilation unit. There are two major crate types:

- Binary crates: produce executable programs.
- Library crates: produce reusable libraries consumed by other crates.

A crate can be made available through `Cargo.toml` and imported with `use`. The `creating_a_library` folder is designed to make the library semantics concrete by showing how exports and visibility work from inside a library crate.

## Learning outcomes

Explains:

- The difference between a crate and a module.
- How to create and publish a library crate structure.
- How to use a crate from another crate with `extern crate` semantics handled by Cargo.
- How visibility controls the API surface of a library.
