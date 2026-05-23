# Creating a Library Folder

This folder demonstrates how to structure and expose a Rust library crate.

## Files

- `rary.rs`
  - Contains the library implementation. It shows how to define public and private items, expose modules, and structure a crate's API.

## How it works

A library crate provides reusable code that other crates can depend on. This folder explains the difference between the crate root and internal modules, as well as how `pub` controls visibility.

Important concepts:

- Library crates expose their public API through `pub` items.
- Internal helper functions and implementation details remain private unless explicitly exposed.
- Cargo treats each library crate as a separate compilation target, which can be shared with other packages.
- The crate root file defines the API surface and may re-export items from submodules.

## Learning outcomes

From this folder you will understand:

- How to organize a library crate in Rust.
- How to make types and functions public while keeping internals hidden.
- How crate boundaries affect visibility and imports.
- Why modular design is important for reusable Rust libraries.
