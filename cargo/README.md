# Cargo Folder

Explains how Rust projects are built, tested, and organized using Cargo, Rust's package manager and build tool.

## Files

- `conventions.rs`
  - Explains common Cargo and Rust style conventions for project structure, module names, file layout, and how examples are arranged.
- `dependencies.rs`
  - Demonstrates how to declare external dependencies in `Cargo.toml`, how Cargo resolves crates, and how dependency versions affect compilation.
- `testing.rs`
  - Shows Rust's built-in test framework, how to write unit tests, and how `cargo test` executes those tests.
- `build_scripts.txt`
  - Documents the purpose of Cargo build scripts (`build.rs`), how they run before compilation, and how they can generate code or configure compilation environment variables.

## How it works

Cargo manages three main phases:

1. Dependency resolution: Cargo reads `Cargo.toml` and downloads crates from crates.io or local paths.
2. Build orchestration: Cargo compiles crates in dependency order, collects metadata, and links binaries.
3. Testing and packaging: Cargo runs tests, examples, benchmarks, and packages crates for distribution.

Each Rust source file here is a compact guide to the different phases of that workflow. The examples are not necessarily runnable programs by themselves; they are designed to teach Cargo concepts through code structure and annotations.

## Learning outcomes

## Learning outcomes

- How to keep Cargo project conventions clean and idiomatic.
- How to manage and reason about dependency graphs.
- How to write and run tests with `cargo test`.
- How build scripts extend Cargo behavior for generated code or conditional compilation.
