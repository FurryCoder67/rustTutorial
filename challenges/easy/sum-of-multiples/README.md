# Sum of Multiples

Compute the sum of all numbers less than a limit that are multiples of any of a set of factors.

## Challenge

- Given a limit and a list of factors, sum every positive number below the limit that is divisible by at least one factor.
- If a factor is zero, it should be ignored to avoid division by zero.
- Multiples should not be counted more than once.

## Files

- `workspace.rs` — implement `sum`.
- `solution.rs` — complete implementation.

## How it works

The solution iterates through numbers from `1` to `limit - 1` and adds those that are divisible by any valid factor.

## Learning outcomes

- How to iterate over a range.
- How to test divisibility using the modulo operator.
- How to avoid duplicate counting by using a single inclusion test.
