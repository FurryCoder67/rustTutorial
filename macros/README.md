# macro_rules! Folder

This folder corresponds to the Rust by Example `macro_rules!` chapter.

## Files

- `macros.rs`
  - Explains declarative macros and how `macro_rules!` can generate repeated or pattern-based code.

## How it works

Macros in Rust operate on syntax rather than values. Declarative macros are expanded at compile time, letting you reduce repetition and define custom syntax patterns.

Key ideas:

- `macro_rules!` defines a macro by matching patterns and producing code.
- Macros can accept token trees, identifiers, expressions, and more.
- Macros are expanded before type checking.
- Use macros judiciously: they are powerful but can reduce readability if overused.

## Learning outcomes

From this folder, you should learn:

- How to write simple `macro_rules!` macros.
- How macros match input patterns and expand into Rust code.
- Why macros are useful for repetitive or syntactic boilerplate.
