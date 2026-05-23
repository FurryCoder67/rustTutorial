# Rust Tutorial Workspace

This workspace is a structured Rust tutorial that teaches core Rust concepts through small example files grouped by topic. Every folder contains focused examples and a `README.md` explaining how the examples in that folder work and how the Rust concepts relate.

## Structure

- `cargo/`: cargo workflows, dependency management, testing conventions, and build script behavior.
- `conversion/`: Rust conversion traits and how to convert between custom types and strings.
- `crates/`: how to create a library crate and how to use it from another crate.
- `custom_types/`: constants, structures, and enumerations.
- `flow_of_control/`: conditional execution, loops, pattern matching, and destructuring.
- `functions/`: functions, methods, closures, and advanced closure examples.
- `helloworld/`: introductory output, comments, formatting, debugging, and display implementations.
- `modules/`: Rust module system, visibility, `use`, `self`, and `super`.
- `primitives/`: primitive compound types like arrays, slices, tuples, and literals.
- `types/`: type aliasing, casting, inference, and literal types.
- `variable_bindings/`: variable declaration patterns, mutability, freezing, and shadowing.

## How to use this workspace

Read the `README.md` inside each folder to understand the purpose of that topic and the mechanism behind every example file. This root README gives a bird's-eye view; each subfolder README goes into depth for that chapter.

## Notes

- Each `README.md` is written to help a Rust learner understand why each file exists and how it demonstrates important Rust behavior.
- The workspace is arranged by concept rather than by program entry points. Many files are small examples focused on one idea.
