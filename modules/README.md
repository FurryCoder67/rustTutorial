# Modules Folder

Explains Rust's module system, hierarchical file structure, and visibility controls.

## Files

- `file_hierarchy.rs`
  - Shows how Rust maps files and directories into module namespaces.
- `visibility.rs`
  - Explains `pub`, private items, and the default privacy rules for functions, structs, and modules.
- `use_declaration.rs`
  - Demonstrates the `use` keyword for bringing items into scope and making code easier to read.
- `super_and_self.rs`
  - Covers `self`, `super`, and absolute paths for accessing items relative to the current module.
- `struct_visibility.rs`
  - Focuses on visibility rules for `struct` fields and how to expose only the intended API.

## How it works

Rust modules provide namespacing and encapsulation. Explains how to organize code into nested modules, how file paths correspond to module paths, and how visibility controls access from other modules.

Important concepts:

- Modules are declared with `mod` and can be defined across files and directories.
- Item visibility is private by default; `pub` makes items accessible outside the current module.
- `use` imports names into the current scope, reducing repetition.
- `self` and `super` help express relative module paths.

## Learning outcomes

You'll learn:

- How to structure Rust code across multiple files.
- How module privacy works and why it matters.
- How to design public APIs with selective visibility.
- How to use `use` to simplify references to items in nested modules.
