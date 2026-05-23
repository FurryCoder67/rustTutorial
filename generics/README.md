# Generics Folder

## Files

- `generics.rs`
  - Contains examples of generic functions, generic types, and how generics enable code reuse.

## How it works

Generics let Rust code operate on multiple types while still being statically checked. They are a core part of Rust's type system for writing abstract and reusable APIs.

Important concepts:

- Generic parameters appear in angle brackets, e.g. `fn foo<T>(x: T) {}`.
- Traits are often used with generics to constrain what operations a type supports.
- Generic types enable containers like `Option<T>` and `Result<T, E>`.
- Monomorphization specializes generic definitions at compile time.

## Learning outcomes

From this folder, you should learn:

- How to define generic functions and types.
- How to use trait bounds to restrict generic parameters.
- Why generics are safe and efficient in Rust.
