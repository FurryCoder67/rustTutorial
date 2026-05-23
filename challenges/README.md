# Exercism Rust Challenges

This directory contains 99 Exercism Rust track exercises organized by difficulty level. Each exercise includes a starter template (`workspace.rs`), a reference solution (`solution.rs`), and documentation.

## Quick Start

### Run a Challenge Test

Test your solution against the reference:

```bash
# Using the test wrapper (Windows)
test.bat raindrops

# Using the test wrapper (macOS/Linux)
./test.sh raindrops

# Using Python directly
python challenges/test_runner.py raindrops
```

The test runner will:
1. Check if you've implemented the solution (no `todo!()` calls)
2. Verify that your code compiles with rustc
3. Report any compilation errors with helpful messages

### List Available Challenges

```bash
python challenges/test_runner.py --list
```

This shows all 99 exercises organized by difficulty.

## Difficulty Levels

- **Easy** (41 exercises): Great for beginners, focusing on fundamentals
- **Medium** (53 exercises): Intermediate concepts, more complex logic
- **Hard** (5 exercises): Advanced challenges, specialized topics

## How to Use Each Challenge

### Step 1: Choose a Challenge

```bash
python challenges/test_runner.py --list
```

Find a challenge that interests you.

### Step 2: Open workspace.rs

Navigate to `challenges/easy/raindrops/` (or your chosen difficulty/challenge).

Open `workspace.rs` - this is where you write your solution.

### Step 3: Read the Problem

1. Check `README.md` in the challenge folder for the problem description
2. Look at the function signature in `workspace.rs`
3. Implement your solution

### Step 4: Test Your Solution

```bash
python challenges/test_runner.py raindrops
```

The test runner will compile your code and report any errors.

### Step 5: Compare with Reference

If you get stuck, check `solution.rs` for a reference implementation. You can also use this to:
- Learn different approaches to solve the problem
- Understand idiomatic Rust patterns
- See alternative algorithms

## File Structure

Each challenge contains:

```
challenges/
├── easy/
│   ├── raindrops/
│   │   ├── README.md         # Problem description
│   │   ├── workspace.rs      # Your solution goes here (has todo!())
│   │   └── solution.rs       # Reference implementation
│   └── ... (40 more exercises)
├── medium/
│   ├── word-count/
│   │   ├── README.md
│   │   ├── workspace.rs
│   │   └── solution.rs
│   └── ... (52 more exercises)
├── hard/
│   ├── poker/
│   │   ├── README.md
│   │   ├── workspace.rs
│   │   └── solution.rs
│   └── ... (4 more exercises)
├── test_runner.py           # Test execution engine
├── fetch_exercism_solutions.py  # Syncs with Exercism API
└── README.md                # This file
```

## Workflow Tips

### For Learning

1. Start with **Easy** exercises to build confidence
2. Move to **Medium** for more complex patterns
3. Tackle **Hard** exercises for advanced Rust concepts
4. Compare your solution to `solution.rs` even if you pass

### For Practice

1. Try to solve without looking at the reference
2. Run tests frequently (`test raindrops`)
3. Refactor your solution to be more idiomatic
4. Study alternative approaches in `solution.rs`

### For Benchmarking

Track your progress:

```bash
# After solving each challenge, note the difficulty and date
# This helps you identify learning patterns
```

## Updating Exercises

The exercises are synced with the official Exercism Rust track. To get the latest:

```bash
python challenges/fetch_exercism_solutions.py
```

This script:
1. Fetches the latest 99 exercises from Exercism
2. Updates problem descriptions
3. Reorganizes by difficulty if changes occur
4. Preserves any custom notes you've added

## Test Runner Output Examples

### ✅ Success
```
📋 Testing: raindrops (easy)
   Directory: challenges\easy\raindrops

✅ SUCCESS: Compilation successful! Your solution compiles.

Your solution compiles correctly!
```

### ⚠️ Incomplete
```
📋 Testing: word-count (medium)
   Directory: challenges\medium\word-count

⚠️  INCOMPLETE: workspace.rs still contains todo!() - Please implement the solution
```

### ❌ Compile Error
```
📋 Testing: atbash-cipher (easy)
   Directory: challenges\easy\atbash-cipher

❌ COMPILE ERROR:
   Your code has compilation errors:
   
   error[E0308]: mismatched types
     |
   8 |     fn encode(input: &str) -> String {
     |                                ^^^^^^
   ...
```

## Tips for Success

1. **Read the problem carefully** - Each README explains what to implement
2. **Start with the function signature** - It tells you what types you're working with
3. **Use Rust's type system** - Let the compiler guide you with error messages
4. **Test frequently** - Run tests after each small change
5. **Read the reference solution** - Even if you solve it, see how the pros do it

## For More Information

- [Exercism Rust Track](https://exercism.org/tracks/rust)
- [Rust Book](https://doc.rust-lang.org/book/)
- [Rust Standard Library](https://doc.rust-lang.org/std/)

## Common Issues

### rustc not found
**Solution**: Make sure Rust is installed. Download from [rust-lang.org](https://www.rust-lang.org/tools/install)

### Challenge not found
Run `python challenges/test_runner.py --list` to see all available challenges

### Tests always show "todo!()"
Make sure you've replaced the `todo!()` call in your `workspace.rs` with actual code

### Compilation hangs
Add a timeout to the test runner. Most exercises should compile in seconds
