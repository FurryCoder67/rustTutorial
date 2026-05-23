# Scoping Rules Folder

## Files

- `scope.rs`
  - Shows how Rust determines the scope and lifetime of variables, as well as when values are dropped.

## How it works

Scoping rules define where names are valid and when resources are released. In Rust, scope is closely tied to ownership and lifetime.

Key ideas:

- A binding is valid within the block where it is declared.
- Values are dropped when they go out of scope.
- Nested scopes can shadow outer bindings.
- Scoping rules are the foundation of safe memory management in Rust.

## Learning outcomes

Teaches:

- How scope affects variable lifetime.
- How nested blocks create new scopes.
- Why Rust drops values at the end of their scope.
