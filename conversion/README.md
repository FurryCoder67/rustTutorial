# Conversion Folder

Covers Rust type conversion traits and idioms for converting values between different types, especially custom types and strings.

## Files

- `from_and_into.rs`
  - Explains the `From` and `Into` traits. `From<T> for U` defines a direct conversion, and `Into<U>` is automatically available for types implementing `From<U>`.
  - Shows how Rust prefers `From` implementations and how `Into` is useful in generic code.
- `to_and_from_strings.rs`
  - Covers `ToString` and `FromStr` traits, which are the canonical Rust traits for converting values to and from text.
  - Demonstrates how `to_string()` is a convenience method provided by `ToString` and how `FromStr` is used with `str::parse()`.
- `tryfrom_and_tryinto.rs`
  - Introduces fallible conversions using `TryFrom` and `TryInto`. These traits return a `Result` when the conversion may fail.
  - Explains when to use fallible vs infallible conversions, and how `try_into()` behaves in generic contexts.

## How it works

Rust conversion traits are organized around two classes of conversion:

- Infallible conversion: `From`, `Into`, `ToString`.
- Fallible conversion: `TryFrom`, `TryInto`, `FromStr`.

The guide in this folder shows how to implement these traits for user-defined types so conversions become ergonomic and idiomatic. It also explains how the standard library relies on these traits to support generic conversion patterns.

## Learning outcomes

After reading this folder, you should understand:

- The distinction between `From`/`Into` and `TryFrom`/`TryInto`.
- How to implement conversion traits for custom types.
- Why `ToString` and `FromStr` are the text-conversion traits in Rust.
- How generic code can use `Into` or `TryInto` to accept a wide range of convertible inputs.
