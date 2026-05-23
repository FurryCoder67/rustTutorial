# Robot Name

Implement a robot name generator that produces unique names and allows robots to reset their names.

## Challenge

- Each robot has a name containing two uppercase letters followed by three digits, e.g. `RX837`.
- `Robot::new` creates a robot with a unique name.
- `Reset` assigns a new unique name to an existing robot.
- Names should not repeat indefinitely.

## Files

- `workspace.rs` — implement the `Robot` struct and its methods.
- `solution.rs` — complete implementation.

## How it works

The solution uses a static counter to generate deterministic unique names, then formats the counter into the required `AA000` style.

## Learning outcomes

- How to use a struct with methods.
- How to keep global state safely with atomics.
- How to format and reset values.
