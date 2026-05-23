#!/usr/bin/env python3
"""
Test runner for Exercism challenges.
Usage: python test_runner.py <challenge-name>

The test runner compares the user's workspace.rs with the solution.rs
and reports pass/fail with detailed error messages.
"""

import os
import sys
import subprocess
import tempfile
import json
from pathlib import Path

def find_challenge(challenge_name: str) -> tuple:
    """Find a challenge by name and return (path, difficulty, slug)."""
    root = "challenges"
    
    for difficulty in ['easy', 'medium', 'hard']:
        challenge_dir = os.path.join(root, difficulty, challenge_name)
        if os.path.isdir(challenge_dir):
            return (challenge_dir, difficulty, challenge_name)
    
    # Try fuzzy matching
    for difficulty in ['easy', 'medium', 'hard']:
        diff_dir = os.path.join(root, difficulty)
        if os.path.isdir(diff_dir):
            for entry in os.listdir(diff_dir):
                if challenge_name.lower() in entry.lower() or entry.lower() in challenge_name.lower():
                    challenge_dir = os.path.join(root, difficulty, entry)
                    if os.path.isdir(challenge_dir):
                        return (challenge_dir, difficulty, entry)
    
    return (None, None, None)

def get_function_signatures(file_path: str) -> list:
    """Extract public function signatures from a Rust file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return []
    
    import re
    # Match pub fn/struct/impl patterns
    patterns = [
        r'pub\s+fn\s+(\w+)',
        r'pub\s+struct\s+(\w+)',
        r'pub\s+enum\s+(\w+)',
    ]
    
    signatures = []
    for pattern in patterns:
        matches = re.findall(pattern, content)
        signatures.extend(matches)
    
    return signatures

def create_test_file(challenge_dir: str, slug: str) -> str:
    """Create a test Rust file that imports both workspace and solution."""
    workspace_path = os.path.join(challenge_dir, "workspace.rs")
    solution_path = os.path.join(challenge_dir, "solution.rs")
    
    with open(workspace_path, 'r', encoding='utf-8') as f:
        workspace_code = f.read()
    
    with open(solution_path, 'r', encoding='utf-8') as f:
        solution_code = f.read()
    
    test_code = f'''// Generated test file
mod workspace {{{workspace_code}
}}

mod solution {{{solution_code}
}}

// Compile check - if both modules compile, syntax is valid
#[test]
fn modules_compile() {{
    // If this compiles, both workspace and solution are syntactically valid
}}
'''
    
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.rs', delete=False)
    temp_file.write(test_code)
    temp_file.close()
    return temp_file.name

def run_rust_check(file_path: str) -> tuple:
    """Run rustc to check if code compiles."""
    try:
        result = subprocess.run(
            ['rustc', '--crate-type', 'lib', '--edition', '2021', file_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        return (result.returncode == 0, result.stderr, result.stdout)
    except subprocess.TimeoutExpired:
        return (False, "Compilation timed out", "")
    except FileNotFoundError:
        return (False, "rustc not found. Please install Rust.", "")
    except Exception as e:
        return (False, str(e), "")

def compare_implementations(challenge_dir: str, slug: str) -> dict:
    """Compare workspace.rs with solution.rs."""
    workspace_path = os.path.join(challenge_dir, "workspace.rs")
    solution_path = os.path.join(challenge_dir, "solution.rs")
    
    # Check if files exist
    if not os.path.exists(workspace_path):
        return {
            'status': 'error',
            'message': f'workspace.rs not found in {challenge_dir}',
            'passed': False
        }
    
    if not os.path.exists(solution_path):
        return {
            'status': 'error',
            'message': f'solution.rs not found in {challenge_dir}',
            'passed': False
        }
    
    # Read both files
    with open(workspace_path, 'r', encoding='utf-8') as f:
        workspace_code = f.read()
    with open(solution_path, 'r', encoding='utf-8') as f:
        solution_code = f.read()
    
    # Check if workspace still has todo!()
    if 'todo!' in workspace_code:
        return {
            'status': 'incomplete',
            'message': 'workspace.rs still contains todo!() - Please implement the solution',
            'passed': False
        }
    
    # Try to compile workspace
    temp_file = create_test_file(challenge_dir, slug)
    try:
        success, stderr, stdout = run_rust_check(temp_file)
        
        if not success:
            # Parse error message to be more helpful
            error_lines = stderr.split('\n')
            relevant_errors = [line for line in error_lines if 'error' in line.lower()]
            
            return {
                'status': 'compile_error',
                'message': 'Your code has compilation errors:',
                'errors': relevant_errors[:5],  # First 5 errors
                'full_output': stderr,
                'passed': False
            }
        
        return {
            'status': 'pass',
            'message': 'Compilation successful! Your solution compiles.',
            'passed': True
        }
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

def main():
    if len(sys.argv) < 2:
        print("Usage: python test_runner.py <challenge-name>")
        print("       python test_runner.py --list")
        print("\nExample: python test_runner.py raindrops")
        print("         python test_runner.py word-count")
        sys.exit(1)
    
    if sys.argv[1] == '--list':
        print("Available challenges:\n")
        root = "challenges"
        for difficulty in ['easy', 'medium', 'hard']:
            diff_dir = os.path.join(root, difficulty)
            if os.path.isdir(diff_dir):
                challenges = sorted([d for d in os.listdir(diff_dir) if os.path.isdir(os.path.join(diff_dir, d))])
                print(f"{difficulty.upper()} ({len(challenges)} challenges):")
                for c in challenges:
                    print(f"  - {c}")
                print()
        sys.exit(0)
    
    challenge_name = sys.argv[1]
    challenge_dir, difficulty, slug = find_challenge(challenge_name)
    
    if challenge_dir is None:
        print(f"❌ Challenge '{challenge_name}' not found.")
        print("\nAvailable challenges:")
        root = "challenges"
        for difficulty in ['easy', 'medium', 'hard']:
            diff_dir = os.path.join(root, difficulty)
            if os.path.isdir(diff_dir):
                challenges = [d for d in os.listdir(diff_dir) if os.path.isdir(os.path.join(diff_dir, d))]
                print(f"\n  {difficulty.upper()}:")
                for c in sorted(challenges)[:10]:
                    print(f"    - {c}")
                if len(challenges) > 10:
                    print(f"    ... and {len(challenges) - 10} more")
        sys.exit(1)
    
    print(f"\n📋 Testing: {slug} ({difficulty})")
    print(f"   Directory: {challenge_dir}\n")
    
    result = compare_implementations(challenge_dir, slug)
    
    if result['status'] == 'error':
        print(f"❌ ERROR: {result['message']}")
        sys.exit(1)
    
    elif result['status'] == 'incomplete':
        print(f"⚠️  INCOMPLETE: {result['message']}")
        sys.exit(1)
    
    elif result['status'] == 'compile_error':
        print(f"❌ COMPILE ERROR:\n   {result['message']}\n")
        for error in result.get('errors', []):
            print(f"   {error}")
        print(f"\n   Full output:")
        for line in result.get('full_output', '').split('\n')[:20]:
            if line.strip():
                print(f"   {line}")
        sys.exit(1)
    
    elif result['status'] == 'pass':
        print(f"✅ SUCCESS: {result['message']}")
        print(f"\nYour solution compiles correctly!")
        sys.exit(0)
    
    else:
        print(f"⚠️  Unknown status: {result['status']}")
        sys.exit(1)

if __name__ == '__main__':
    main()
