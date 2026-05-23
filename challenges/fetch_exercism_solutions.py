#!/usr/bin/env python3
"""
Fetches all Exercism Rust track exercises and generates workspace/solution stubs.
Uses the official Exercism API to get exercise metadata and specs.
"""

import os
import json
import urllib.request
import urllib.error
import html.parser
import re
from pathlib import Path
from typing import Dict, List, Tuple

# Exercism API endpoints
EXERCISM_API_BASE = "https://exercism.org/api/v2"
TRACK_SLUG = "rust"

# Difficulty mapping (heuristic based on naming/position)
DIFFICULTY_LEVELS = {
    'easy': [
        'hello-world', 'leap', 'raindrops', 'sum-of-multiples', 'gigasecond',
        'isogram', 'space-age', 'grains', 'acronym', 'protein-translation',
        'difference-of-squares', 'collatz-conjecture', 'luhn', 'scrabble-score',
        'phone-number', 'isbn-verifier', 'perfect-numbers', 'resistor-color',
        'resistor-color-duo', 'all-your-base', 'robot-name', 'say', 'flatten-array',
        'rna-transcription', 'hamming', 'clock', 'error-handling', 'series',
        'reverse-string', 'nth-prime', 'prime-factors', 'pascals-triangle',
        'largest-series-product', 'atbash-cipher', 'run-length-encoding',
        'simple-cipher', 'word-count', 'nucleotide-count', 'anagram',
        'pangram', 'matching-brackets', 'matrix', 'saddle-points',
        'spiraling-values', 'trinary', 'bowling', 'binary-search-tree',
        'variable-length-quantity'
    ],
    'medium': [
        'bob', 'two-bucket', 'custom-set', 'dust-bluster', 'triangle',
        'rational-numbers', 'rock-paper-scissors', 'bracket-push',
        'pythagorean-triplet', 'word-search', 'yacht', 'alphametics',
        'sublist', 'connect', 'roman-numerals', 'crypto-square',
        'linked-list', 'octal', 'hex', 'assembly-line', 'accumulate',
        'squares', 'change', 'simple-linked-list', 'beer-song',
        'scale-generator', 'ocr-numbers', 'secret-handshake',
        'diamond', 'wordy', 'pig-latin', 'grade-school'
    ],
    'hard': [
        'poker', 'tournament', 'forth', 'parallel-letter-frequency',
        'totient', 'sieve', 'prime-generator', 'clock-builder',
        'custom-parser', 'lexer', 'parser-combinator'
    ]
}

def create_solution_stub(slug: str) -> str:
    """Create a basic solution stub based on exercise slug."""
    solutions = {
        'hello-world': '''pub fn hello() -> &'static str {
    "Hello, World!"
}''',
        'leap': '''pub fn is_leap_year(year: u64) -> bool {
    (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)
}''',
        'raindrops': '''pub fn convert(n: u32) -> String {
    let mut result = String::new();
    if n % 3 == 0 { result.push_str("Pling"); }
    if n % 5 == 0 { result.push_str("Plang"); }
    if n % 7 == 0 { result.push_str("Plong"); }
    if result.is_empty() { n.to_string() } else { result }
}''',
        'sum-of-multiples': '''pub fn sum_of_multiples(limit: u32, factors: &[u32]) -> u32 {
    (1..limit)
        .filter(|&i| factors.iter().any(|&f| f != 0 && i % f == 0))
        .sum()
}''',
        'gigasecond': '''use std::time::Duration;

pub fn after(start: Duration) -> Duration {
    start + Duration::from_secs(1_000_000_000)
}''',
        'isogram': '''pub fn check(phrase: &str) -> bool {
    let mut seen = std::collections::HashSet::new();
    phrase
        .to_lowercase()
        .chars()
        .filter(|c| c.is_alphabetic())
        .all(|c| seen.insert(c))
}''',
        'space-age': '''#[derive(Debug)]
pub struct Duration(f64);

impl From<u64> for Duration {
    fn from(seconds: u64) -> Self {
        Duration(seconds as f64)
    }
}

impl Duration {
    pub fn earth_years(self) -> f64 {
        self.0 / 31_557_600.0
    }
    pub fn mercury_years(self) -> f64 { self.earth_years() / 0.2408467 }
    pub fn venus_years(self) -> f64 { self.earth_years() / 0.61519726 }
    pub fn mars_years(self) -> f64 { self.earth_years() / 1.88082869 }
    pub fn jupiter_years(self) -> f64 { self.earth_years() / 11.862615 }
    pub fn saturn_years(self) -> f64 { self.earth_years() / 29.4571 }
    pub fn uranus_years(self) -> f64 { self.earth_years() / 84.07 }
    pub fn neptune_years(self) -> f64 { self.earth_years() / 164.79 }
}''',
        'grains': '''pub fn square(s: u32) -> Result<u64, String> {
    match s {
        1..=64 => Ok(1u64 << (s - 1)),
        _ => Err("square must be between 1 and 64".to_string()),
    }
}

pub fn total() -> u64 {
    u64::MAX
}''',
        'acronym': '''pub fn abbreviate(phrase: &str) -> String {
    phrase
        .split(|c: char| !c.is_alphanumeric())
        .filter(|w| !w.is_empty())
        .map(|w| w.chars().next().unwrap().to_uppercase().to_string())
        .collect()
}''',
    }
    
    # Return solution or a generic stub
    if slug in solutions:
        return solutions[slug]
    else:
        return "// TODO: Implement solution\npub fn solution() {}\n"

def fetch_exercism_track_exercises() -> List[Dict]:
    """Fetch all exercises from Exercism Rust track."""
    try:
        url = f"{EXERCISM_API_BASE}/tracks/{TRACK_SLUG}/exercises"
        headers = {'User-Agent': 'Rust-Tutorial-Bot'}
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            return data.get('exercises', [])
    except Exception as e:
        print(f"Error fetching exercises: {e}")
        return []

def get_exercise_difficulty(slug: str) -> str:
    """Determine exercise difficulty."""
    for level, exercises in DIFFICULTY_LEVELS.items():
        if slug in exercises:
            return level
    # Default heuristic: check position in common Exercism ordering
    return 'medium'

def ensure_solution_files(slug: str, difficulty: str, root: str = "challenges"):
    """Ensure workspace.rs and solution.rs exist for an exercise."""
    exercise_dir = os.path.join(root, difficulty, slug)
    os.makedirs(exercise_dir, exist_ok=True)
    
    workspace_path = os.path.join(exercise_dir, "workspace.rs")
    solution_path = os.path.join(exercise_dir, "solution.rs")
    readme_path = os.path.join(exercise_dir, "README.md")
    
    # Create workspace stub if missing
    if not os.path.exists(workspace_path):
        with open(workspace_path, 'w', encoding='utf-8') as f:
            f.write("// TODO: Implement your solution here\n")
    
    # Create solution if missing
    if not os.path.exists(solution_path):
        solution_code = create_solution_stub(slug)
        with open(solution_path, 'w', encoding='utf-8') as f:
            f.write(solution_code + "\n")
    
    # Create README if missing
    if not os.path.exists(readme_path):
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(f"# {slug.replace('-', ' ').title()}\n\n")
            f.write(f"**Difficulty:** {difficulty}\n\n")
            f.write("## Task\n\n[Add description from Exercism]\n\n")
            f.write("## Files\n\n")
            f.write("- `workspace.rs` - Your solution goes here\n")
            f.write("- `solution.rs` - Reference solution\n")

def main():
    print("Fetching Exercism Rust exercises...")
    exercises = fetch_exercism_track_exercises()
    
    if not exercises:
        print("Warning: Could not fetch from API. Using cached exercise list.")
        # Fallback: create from known difficulties
        for difficulty, slugs in DIFFICULTY_LEVELS.items():
            for slug in slugs:
                ensure_solution_files(slug, difficulty)
                print(f"  Created: {difficulty}/{slug}")
    else:
        print(f"Found {len(exercises)} exercises.")
        for ex in exercises:
            slug = ex.get('slug', '')
            difficulty = get_exercise_difficulty(slug)
            ensure_solution_files(slug, difficulty)
            print(f"  Created: {difficulty}/{slug}")
    
    print("Done!")

if __name__ == '__main__':
    main()
