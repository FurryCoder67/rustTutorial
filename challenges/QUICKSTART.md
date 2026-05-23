# Challenge System Quick Start

## 5-Minute Setup

### 1. See What's Available
```bash
python challenges/test_runner.py --list
```

This shows all 99 exercises organized by difficulty.

### 2. Pick a Challenge
Start with an Easy exercise. Example: `raindrops`

### 3. Edit Your Solution
Open: `challenges/easy/raindrops/workspace.rs`

Replace the `todo!()` with your implementation.

### 4. Test It
```bash
python challenges/test_runner.py raindrops
```

If it compiles ✅, move to the next challenge.  
If it fails ❌, check the error message and fix it.

### 5. Compare (Optional)
Look at `challenges/easy/raindrops/solution.rs` to see a reference implementation.

## Understanding the Test Output

### ✅ Passed
Your code compiles! You can move on to the next challenge.

### ⚠️ Incomplete
Still has `todo!()` - finish your implementation.

### ❌ Compile Error
Your code has syntax/type errors. Read the error message and fix it.

## Workflow Examples

### Easy Path (Beginner)
1. raindrops
2. sum-of-multiples
3. gigasecond
4. leap
5. hamming

### Medium Path (Intermediate)
1. bob
2. triangle
3. word-count
4. anagram
5. wordy

### Hard Path (Advanced)
1. poker
2. tournament
3. forth
4. sieve
5. parallel-letter-frequency

## Tips

1. **Read the problem first** - Open the README.md in each folder
2. **Start small** - Easy exercises build confidence
3. **Test often** - Run tests after each small change
4. **Learn from solutions** - Compare your approach to solution.rs
5. **Refactor** - Try different approaches to solve the same problem

## Files in Each Challenge

- `workspace.rs` - Your solution goes here
- `solution.rs` - Reference implementation (read after solving)
- `README.md` - Problem description

## Resetting a Challenge

Want to retry a challenge? Just replace your `workspace.rs` with the `solution.rs` and modify it.

Or copy the `workspace.rs` from another challenge folder if needed.

## Next Steps

1. Solve 5 Easy challenges
2. Try 5 Medium challenges
3. Attempt the Hard ones
4. Look at multiple solutions for the same problem
5. Refactor your solutions to be more idiomatic

## Need Help?

- Check the error message first
- Look at the function signature - it tells you the types
- Read the README.md for hints
- Compare with solution.rs for a different approach
- Check the Rust book: https://doc.rust-lang.org/book/

Good luck! 🦀
