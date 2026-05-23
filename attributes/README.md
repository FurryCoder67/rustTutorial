# Attributes Folder

Explains Rust attributes, which are metadata annotations that alter compiler behavior, enable conditional compilation, and configure code generation.

## Files

- `crates.rs`
  - Demonstrates crate-level attributes and how attributes can affect crate behavior and features.
- `dead_code.rs`
  - Shows the `#[allow(dead_code)]` attribute and explains how Rust attributes can suppress warnings or control lints.
- `cfg/`
  - Contains examples of conditional compilation using `cfg` attributes.

## How it works

Attributes in Rust are written with `#[]` and are attached to items like functions, modules, structs, and crates. They can be used for:

- enabling or disabling warnings and lints
- enabling features or conditional compilation
- deriving trait implementations
- supplying metadata for tools and the compiler

Rust parses attributes before normal compilation, so they can shape how the compiler interprets the item they annotate.

## Learning outcomes

Teaches:

- How to use attributes to configure compiler behavior.
- How to apply lint-related attributes such as `allow`, `warn`, and `deny`.
- How attributes differ from normal code syntax.
- Why attributes are essential for conditional and feature-specific code.
