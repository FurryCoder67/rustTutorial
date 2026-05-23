# CFG Folder

It shows how Rust uses `cfg` attributes for conditional compilation based on target configuration, features, and other compile-time settings.

## Files

- `cfg.rs`
  - Demonstrates the core `#[cfg(...)]` attribute and how it enables or disables code depending on build conditions.
- `custom.rs`
  - Shows how custom configuration flags can be defined and used with Cargo features or compiler-defined values.

## How it works

The `cfg` system allows Rust code to compile differently on different platforms or when different features are enabled.

Key points:

- `#[cfg(...)]` is evaluated at compile time and code inside false branches is excluded from the compilation unit.
- `#[cfg_attr(...)]` can apply attributes conditionally.
- Conditional compilation supports platform-specific code, optional features, and feature-gated APIs.

## Learning outcomes

From this folder, you should understand:

- How `cfg` attributes control what code is compiled.
- How to write platform- or feature-specific Rust code safely.
- How conditional compilation helps maintain cross-platform libraries.
