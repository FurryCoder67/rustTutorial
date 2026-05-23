# Display Folder

Contains examples of Rust's `Display` formatting trait and how to implement custom output for user-defined types.

## Files

- `testcase_list.rs`
  - Demonstrates implementing `fmt::Display` for a custom type and how `println!` uses that trait.

## How it works

`Display` is the trait for user-facing text representations. It is used whenever a value is printed with `{}` inside a format string.

Important concepts:

- `Display` requires implementing `fmt(&self, f: &mut Formatter) -> fmt::Result`.
- Custom types use `Display` to control exactly how they render.
- `Display` output should be readable and user-friendly, unlike `Debug` which is developer-oriented.

## Learning outcomes


- How to implement `Display` for a type.
- What makes `Display` output appropriate for end users.
- How `Display` and `Debug` differ in purpose and usage.
