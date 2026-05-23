# Variable Bindings Folder

Explains how Rust handles variable declarations, mutability, shadowing, and scope.

## Files

- `variable_bindings.rs`
  - Introduces Rust’s basic variable binding syntax with `let`.
- `declare_first.rs`
  - Shows how variables can be declared without initialization and assigned later.
- `mutability.rs`
  - Explains `mut`, how mutable bindings work, and why immutability is the default.
- `freezing.rs`
  - Demonstrates how immutable bindings can be borrowed as mutable references temporarily.
- `scope_and_shadowing.rs`
  - Covers lexical scope, nested scopes, and how shadowing creates a new binding with the same name.

## How it works

Rust variable bindings are central to its ownership model. Explains how values are bound to names, how mutability is controlled, and how scope determines when values are valid.

Key ideas:

- `let` creates a binding, and the value is immutable unless `mut` is used.
- Shadowing allows reusing an identifier for a new value while keeping the old value out of scope.
- Borrowing rules require careful handling of mutable and immutable references.
- Scope boundaries determine when values are dropped and when references become invalid.

## Learning outcomes


- The default immutability philosophy of Rust.
- How to declare variables, including deferred initialization.
- How shadowing can simplify transformations while preserving safety.
- How scope affects lifetime and resource cleanup.
