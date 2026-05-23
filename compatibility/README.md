# Compatibility Folder

## Files

- `compatibility.rs`
  - Contains examples of maintaining compatibility across Rust versions and working with stable APIs.

## How it works

Compatibility guidance helps crate authors write code that works across editions and stable compiler versions. This includes using stable APIs and avoiding unstable or deprecated features.

Key ideas:

- Prefer stable, well-supported APIs.
- Be aware of edition-specific changes and compatibility shims.
- Use conditional compilation for platform-specific or version-specific code.
- Avoid relying on nightly-only features in libraries intended for wide use.

## Learning outcomes


- How to write code that is compatible across Rust versions.
- Why stability matters for library authors.
- How to use Cargo and Rust edition features to preserve compatibility.
