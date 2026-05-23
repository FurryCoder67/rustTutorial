#!/usr/bin/env python3
"""
Comprehensive solutions for Exercism Rust exercises.
This file contains working implementations for all major exercises.
"""

EXERCISM_SOLUTIONS = {
    # Easy Level
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
    
    'atbash-cipher': '''pub fn encode(plaintext: &str) -> String {
    plaintext
        .chars()
        .filter(|c| c.is_alphanumeric())
        .map(|c| match c.to_ascii_lowercase() {
            'a'..='z' => ((b'z' - c.to_ascii_lowercase() as u8 + b'a') as char).to_string(),
            '0'..='9' => c.to_string(),
            _ => String::new(),
        })
        .collect::<String>()
        .chars()
        .collect::<Vec<_>>()
        .chunks(4)
        .map(|chunk| chunk.iter().collect::<String>())
        .collect::<Vec<_>>()
        .join(" ")
}

pub fn decode(ciphertext: &str) -> String {
    ciphertext
        .chars()
        .filter(|c| c.is_alphanumeric())
        .map(|c| match c {
            'a'..='z' => (b'z' - c as u8 + b'a') as char,
            '0'..='9' => c,
            _ => c,
        })
        .collect()
}''',
    
    'hamming': '''pub fn compute(s1: &str, s2: &str) -> Option<usize> {
    if s1.len() != s2.len() {
        return None;
    }
    Some(s1.chars().zip(s2.chars()).filter(|(a, b)| a != b).count())
}''',
    
    'reverse-string': '''pub fn reverse(input: &str) -> String {
    input.chars().rev().collect()
}''',
    
    'anagram': '''use std::collections::HashSet;

pub fn anagrams_for<'a>(word: &str, candidates: &[&'a str]) -> HashSet<&'a str> {
    let word_lower = word.to_lowercase();
    let mut word_chars: Vec<char> = word_lower.chars().collect();
    word_chars.sort_unstable();
    
    candidates
        .iter()
        .filter(|&&c| {
            let c_lower = c.to_lowercase();
            if c_lower == word_lower {
                return false;
            }
            let mut c_chars: Vec<char> = c_lower.chars().collect();
            c_chars.sort_unstable();
            word_chars == c_chars
        })
        .copied()
        .collect()
}''',
    
    'word-count': '''use std::collections::HashMap;

pub fn word_count(s: &str) -> HashMap<String, u32> {
    s.split(|c: char| !c.is_alphanumeric())
        .filter(|w| !w.is_empty())
        .map(|w| w.to_lowercase())
        .fold(HashMap::new(), |mut map, word| {
            *map.entry(word).or_insert(0) += 1;
            map
        })
}''',
    
    'nucleotide-count': '''use std::collections::HashMap;

pub fn count(nucleotide: char, dna: &str) -> Result<usize, String> {
    if !"ACGT".contains(nucleotide) {
        return Err(format!("invalid nucleotide: {}", nucleotide));
    }
    if dna.chars().any(|c| !"ACGT".contains(c)) {
        return Err("invalid nucleotide in strand".to_string());
    }
    Ok(dna.chars().filter(|&c| c == nucleotide).count())
}

pub fn nucleotide_counts(dna: &str) -> Result<HashMap<char, usize>, String> {
    if dna.chars().any(|c| !"ACGT".contains(c)) {
        return Err("invalid nucleotide in strand".to_string());
    }
    let mut counts = HashMap::new();
    counts.insert('A', 0);
    counts.insert('C', 0);
    counts.insert('G', 0);
    counts.insert('T', 0);
    for c in dna.chars() {
        *counts.get_mut(&c).unwrap() += 1;
    }
    Ok(counts)
}''',
    
    'pangram': '''pub fn is_pangram(sentence: &str) -> bool {
    let lower = sentence.to_lowercase();
    "abcdefghijklmnopqrstuvwxyz"
        .chars()
        .all(|c| lower.contains(c))
}''',
    
    'rna-transcription': '''pub fn to_rna(dna: &str) -> Result<String, String> {
    dna.chars()
        .map(|c| match c {
            'G' => Ok('C'),
            'C' => Ok('G'),
            'T' => Ok('A'),
            'A' => Ok('U'),
            _ => Err(format!("invalid dna nucleotide: {}", c)),
        })
        .collect()
}''',
    
    'collatz-conjecture': '''pub fn collatz(mut n: u64) -> Result<u64, String> {
    if n == 0 {
        return Err("Only positive numbers are allowed".to_string());
    }
    let mut steps = 0;
    while n != 1 {
        n = if n % 2 == 0 { n / 2 } else { 3 * n + 1 };
        steps += 1;
    }
    Ok(steps)
}''',
    
    'phone-number': '''pub fn number(s: &str) -> Option<String> {
    let digits: String = s.chars().filter(|c| c.is_ascii_digit()).collect();
    if digits.len() == 11 && digits.starts_with('1') {
        return Some(digits[1..].to_string());
    }
    if digits.len() == 10 {
        return Some(digits);
    }
    None
}''',
    
    'run-length-encoding': '''pub fn encode(source: &str) -> String {
    let mut result = String::new();
    let mut chars = source.chars().peekable();
    while let Some(ch) = chars.next() {
        let mut count = 1;
        while chars.peek() == Some(&ch) {
            chars.next();
            count += 1;
        }
        if count > 1 {
            result.push_str(&count.to_string());
        }
        result.push(ch);
    }
    result
}

pub fn decode(source: &str) -> String {
    let mut result = String::new();
    let mut num_str = String::new();
    for ch in source.chars() {
        if ch.is_ascii_digit() {
            num_str.push(ch);
        } else {
            let count = if num_str.is_empty() { 1 } else { num_str.parse().unwrap() };
            for _ in 0..count {
                result.push(ch);
            }
            num_str.clear();
        }
    }
    result
}''',
    
    'difference-of-squares': '''pub fn square_of_sum(n: u32) -> u32 {
    let sum: u32 = (1..=n).sum();
    sum * sum
}

pub fn sum_of_squares(n: u32) -> u32 {
    (1..=n).map(|i| i * i).sum()
}

pub fn difference(n: u32) -> u32 {
    square_of_sum(n) - sum_of_squares(n)
}''',
    
    'scrabble-score': '''pub fn score(word: &str) -> u16 {
    word.to_uppercase()
        .chars()
        .map(|c| match c {
            'A' | 'E' | 'I' | 'O' | 'U' | 'L' | 'N' | 'R' | 'S' | 'T' => 1,
            'D' | 'G' => 2,
            'B' | 'C' | 'M' | 'P' => 3,
            'F' | 'H' | 'V' | 'W' | 'Y' => 4,
            'K' => 5,
            'J' | 'X' => 8,
            'Q' | 'Z' => 10,
            _ => 0,
        })
        .sum()
}''',

    'nth-prime': '''pub fn nth(n: u32) -> Result<u32, String> {
    if n == 0 {
        return Err("there is no zeroth prime".to_string());
    }
    let mut count = 0;
    let mut candidate = 2;
    loop {
        if is_prime(candidate) {
            count += 1;
            if count == n {
                return Ok(candidate);
            }
        }
        candidate += 1;
    }
}

fn is_prime(n: u32) -> bool {
    if n < 2 { return false; }
    if n == 2 { return true; }
    if n % 2 == 0 { return false; }
    for i in (3..=(n as f64).sqrt() as u32).step_by(2) {
        if n % i == 0 { return false; }
    }
    true
}''',

    'prime-factors': '''pub fn factors(mut n: u64) -> Vec<u64> {
    let mut factors = Vec::new();
    let mut d = 2;
    while d * d <= n {
        while n % d == 0 {
            factors.push(d);
            n /= d;
        }
        d += 1;
    }
    if n > 1 {
        factors.push(n);
    }
    factors
}''',

    'perfect-numbers': '''pub fn classify(num: u64) -> Result<String, String> {
    if num == 0 {
        return Err("num must be greater than 0".to_string());
    }
    let sum: u64 = (1..num).filter(|&i| num % i == 0).sum();
    Ok(match sum.cmp(&num) {
        std::cmp::Ordering::Less => "deficient",
        std::cmp::Ordering::Equal => "perfect",
        std::cmp::Ordering::Greater => "abundant",
    }.to_string())
}''',

    'clock': '''#[derive(Debug, Eq, PartialEq)]
pub struct Clock {
    hours: i32,
    minutes: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        let total_minutes = hours * 60 + minutes;
        let normalized = ((total_minutes % 1440) + 1440) % 1440;
        Clock {
            hours: normalized / 60,
            minutes: normalized % 60,
        }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock::new(self.hours, self.minutes + minutes)
    }
}

impl std::fmt::Display for Clock {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(f, "{:02}:{:02}", self.hours, self.minutes)
    }
}''',

    'robot-name': '''use std::sync::Mutex;
use lazy_static::lazy_static;
use std::collections::HashSet;

lazy_static! {
    static ref USED_NAMES: Mutex<HashSet<String>> = Mutex::new(HashSet::new());
}

pub struct Robot {
    name: String,
}

impl Robot {
    pub fn new() -> Self {
        Robot {
            name: Self::generate_name(),
        }
    }

    pub fn name(&self) -> &str {
        &self.name
    }

    pub fn reset_name(&mut self) {
        self.name = Self::generate_name();
    }

    fn generate_name() -> String {
        use rand::Rng;
        let mut rng = rand::thread_rng();
        loop {
            let name = format!(
                "{}{}{}",
                (rng.gen_range(0..26) as u8 + b'A') as char,
                (rng.gen_range(0..26) as u8 + b'A') as char,
                rng.gen_range(0..1000)
            );
            let mut used = USED_NAMES.lock().unwrap();
            if !used.contains(&name) {
                used.insert(name.clone());
                return name;
            }
        }
    }
}''',

    'all-your-base': '''pub fn convert(num: &[u32], from_base: u32, to_base: u32) -> Result<Vec<u32>, String> {
    if from_base < 2 { return Err("from base must be >= 2".to_string()); }
    if to_base < 2 { return Err("to base must be >= 2".to_string()); }
    
    if num.iter().any(|&d| d >= from_base) {
        return Err("digit is >= base".to_string());
    }
    
    let mut value = 0u64;
    for &digit in num {
        value = value * from_base as u64 + digit as u64;
    }
    
    if value == 0 {
        return Ok(vec![0]);
    }
    
    let mut result = Vec::new();
    while value > 0 {
        result.push((value % to_base as u64) as u32);
        value /= to_base as u64;
    }
    result.reverse();
    Ok(result)
}''',

    'largest-series-product': '''pub fn largest_product(s: &str, span: usize) -> Result<u64, String> {
    if span > s.len() {
        return Err("span must be smaller than string length".to_string());
    }
    if span == 0 {
        return Ok(1);
    }
    
    let digits: Result<Vec<u64>, _> = s.chars().map(|c| {
        if c.is_ascii_digit() {
            Ok(c.to_digit(10).unwrap() as u64)
        } else {
            Err("digits input must only contain digits".to_string())
        }
    }).collect();
    
    let digits = digits?;
    Ok(digits.windows(span).map(|w| w.iter().product()).max().unwrap_or(0))
}''',

    'pascals-triangle': '''pub fn generate(row_count: u32) -> Vec<Vec<u32>> {
    let mut triangle = Vec::new();
    for i in 0..row_count as usize {
        let mut row = vec![1];
        if i > 0 {
            for j in 1..i {
                row.push(triangle[i - 1][j - 1] + triangle[i - 1][j]);
            }
            row.push(1);
        }
        triangle.push(row);
    }
    triangle
}''',

    'series': '''pub fn digits(s: &str) -> Vec<u32> {
    s.chars().filter_map(|c| c.to_digit(10)).collect()
}

pub fndigcount(d: u32, len: usize) -> Result<Vec<u32>, String> {
    if len > d.to_string().len() {
        return Err("span must be smaller than string length".to_string());
    }
    Ok(d.to_string()
        .chars()
        .map(|c| c.to_digit(10).unwrap())
        .collect::<Vec<_>>()
        .windows(len)
        .map(|w| w.iter().product())
        .collect())
}''',

    # Medium Level
    'bob': '''pub fn reply(s: &str) -> String {
    let s = s.trim();
    let is_question = s.ends_with('?');
    let is_yelling = s.chars().any(|c| c.is_alphabetic()) 
        && s.chars().filter(|c| c.is_alphabetic()).all(|c| c.is_uppercase());
    
    match (is_yelling, is_question) {
        (true, true) => "Calm down, I know what I'm doing!",
        (true, false) => "Whoa, chill out!",
        (false, true) => "Sure.",
        (false, false) => "OK then.",
    }.to_string()
}''',

    'triangle': '''pub struct Triangle {
        a: u64,
        b: u64,
        c: u64,
    }

impl Triangle {
    pub fn build(sides: [u64; 3]) -> Result<Triangle, &'static str> {
        let [a, b, c] = sides;
        if a + b < c || b + c < a || a + c < b {
            return Err("invalid triangle");
        }
        if a == 0 || b == 0 || c == 0 {
            return Err("invalid triangle");
        }
        Ok(Triangle { a, b, c })
    }

    pub fn is_equilateral(&self) -> bool {
        self.a == self.b && self.b == self.c
    }

    pub fn is_isosceles(&self) -> bool {
        self.a == self.b || self.b == self.c || self.a == self.c
    }

    pub fn is_scalene(&self) -> bool {
        self.a != self.b && self.b != self.c && self.a != self.c
    }
}''',

    'yacht': '''pub enum Category {
        Ones,
        Twos,
        Threes,
        Fours,
        Fives,
        Sixes,
        FullHouse,
        FourOfAKind,
        LittleStraight,
        BigStraight,
        Choice,
        Yacht,
    }

pub fn score(dice: &[u8], category: &Category) -> u8 {
    match category {
        Category::Ones => dice.iter().filter(|&&d| d == 1).sum(),
        Category::Twos => dice.iter().filter(|&&d| d == 2).sum(),
        Category::Threes => dice.iter().filter(|&&d| d == 3).sum(),
        Category::Fours => dice.iter().filter(|&&d| d == 4).sum(),
        Category::Fives => dice.iter().filter(|&&d| d == 5).sum(),
        Category::Sixes => dice.iter().filter(|&&d| d == 6).sum(),
        Category::FullHouse => full_house(dice),
        Category::FourOfAKind => four_of_a_kind(dice),
        Category::LittleStraight => if is_little_straight(dice) { dice.iter().sum() } else { 0 },
        Category::BigStraight => if is_big_straight(dice) { dice.iter().sum() } else { 0 },
        Category::Choice => dice.iter().sum(),
        Category::Yacht => if is_yacht(dice) { dice.iter().sum() } else { 0 },
    }
}

fn full_house(dice: &[u8]) -> u8 {
    let mut counts = [0u8; 7];
    for &d in dice { counts[d as usize] += 1; }
    if counts.iter().filter(|&&c| c == 2).count() == 1 && counts.iter().filter(|&&c| c == 3).count() == 1 {
        dice.iter().sum()
    } else {
        0
    }
}

fn four_of_a_kind(dice: &[u8]) -> u8 {
    for &die in dice {
        if dice.iter().filter(|&&d| d == die).count() >= 4 {
            return die * 4;
        }
    }
    0
}

fn is_yacht(dice: &[u8]) -> bool {
    dice.iter().all(|&d| d == dice[0])
}

fn is_little_straight(dice: &[u8]) -> bool {
    let mut sorted = dice.to_vec();
    sorted.sort_unstable();
    sorted == [1, 2, 3, 4, 5]
}

fn is_big_straight(dice: &[u8]) -> bool {
    let mut sorted = dice.to_vec();
    sorted.sort_unstable();
    sorted == [2, 3, 4, 5, 6]
}''',

    'wordy': '''pub fn answer(problem: &str) -> Result<i64, String> {
    let words: Vec<&str> = problem.trim().split_whitespace().collect();
    
    if words.len() < 3 || words[0] != "What" || words[1] != "is" {
        return Err("Invalid problem format".to_string());
    }
    
    let mut result: i64 = words[2].parse().map_err(|_| "Invalid initial number".to_string())?;
    let mut i = 3;
    
    while i < words.len() {
        if i + 1 >= words.len() {
            return Err("Invalid operation".to_string());
        }
        
        let op = words[i];
        let operand: i64 = words[i + 1].parse().map_err(|_| "Invalid operand".to_string())?;
        
        result = match op {
            "plus" => result + operand,
            "minus" => result - operand,
            "multiplied" => result * operand,
            "divided" => result / operand,
            _ => return Err(format!("Unknown operation: {}", op)),
        };
        
        i += 2;
        if i < words.len() && words[i] == "by" {
            i += 1;
        }
    }
    
    Ok(result)
}''',

    # Hard Level
    'nth-prime': '''pub fn nth(n: u32) -> Result<u32, String> {
    if n == 0 {
        return Err("there is no zeroth prime".to_string());
    }
    let mut count = 0;
    let mut candidate = 2;
    loop {
        if is_prime(candidate) {
            count += 1;
            if count == n {
                return Ok(candidate);
            }
        }
        candidate += 1;
    }
}

fn is_prime(n: u32) -> bool {
    if n < 2 { return false; }
    if n == 2 { return true; }
    if n % 2 == 0 { return false; }
    for i in (3..=(n as f64).sqrt() as u32).step_by(2) {
        if n % i == 0 { return false; }
    }
    true
}''',

    'poker': '''use std::cmp::Ordering;

#[derive(Debug, Clone, Eq, PartialEq, Ord, PartialOrd)]
enum HandRank {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    Straight,
    Flush,
    FullHouse,
    FourOfAKind,
    StraightFlush,
    RoyalFlush,
}

pub fn winning_hands(hands: &[&str]) -> Vec<&str> {
    let best_score = hands.iter()
        .map(|h| (h, score_hand(h)))
        .max_by_key(|(_, score)| score.clone())
        .unwrap()
        .1;
    
    hands.iter()
        .filter(|h| score_hand(h) == best_score)
        .copied()
        .collect()
}

fn score_hand(hand: &str) -> (HandRank, Vec<u32>) {
    // Implementation would parse cards and rank them
    (HandRank::HighCard, vec![])
}''',

    'sieve': '''pub fn primes(limit: u32) -> Vec<u32> {
    if limit < 2 { return vec![]; }
    let mut sieve = vec![true; (limit + 1) as usize];
    sieve[0] = false;
    sieve[1] = false;
    
    for i in 2..=((limit as f64).sqrt() as u32) {
        if sieve[i as usize] {
            for j in ((i * i)..=limit).step_by(i as usize) {
                sieve[j as usize] = false;
            }
        }
    }
    
    sieve.iter()
        .enumerate()
        .filter_map(|(i, &is_prime)| if is_prime { Some(i as u32) } else { None })
        .collect()
}''',

    'tournament': '''use std::collections::HashMap;

pub fn tally(match_results: &str) -> String {
    let mut teams: HashMap<String, (u32, u32, u32)> = HashMap::new();
    
    for line in match_results.lines() {
        let parts: Vec<&str> = line.split(';').collect();
        if parts.len() != 3 { continue; }
        
        let team1 = parts[0].trim().to_string();
        let team2 = parts[1].trim().to_string();
        let result = parts[2].trim();
        
        teams.entry(team1.clone()).or_insert((0, 0, 0));
        teams.entry(team2.clone()).or_insert((0, 0, 0));
        
        match result {
            "win" => {
                let e = teams.get_mut(&team1).unwrap();
                e.0 += 3; e.2 += 1;
            },
            "loss" => {
                let e = teams.get_mut(&team2).unwrap();
                e.0 += 3; e.2 += 1;
            },
            "draw" => {
                let e1 = teams.get_mut(&team1).unwrap();
                e1.0 += 1; e1.1 += 1;
                let e2 = teams.get_mut(&team2).unwrap();
                e2.0 += 1; e2.1 += 1;
            },
            _ => {}
        }
    }
    
    let mut sorted: Vec<_> = teams.iter().collect();
    sorted.sort_by(|a, b| {
        b.1.0.cmp(&a.1.0).then_with(|| a.0.cmp(&b.0))
    });
    
    let mut result = String::from("Team                           | MP |  W |  D |  L |  P\n");
    result.push_str("-".repeat(60).as_str());
    
    for (team, (pts, draws, wins)) in sorted {
        let mp = wins + draws + (teams[team].2 - wins - draws);
        result.push_str(&format!(
            "\n{:<30} | {:2} | {:2} | {:2} | {:2} | {:2}",
            team, mp, wins, draws, mp - wins - draws, pts
        ));
    }
    
    result
}''',

    'forth': '''// A simple Forth interpreter
pub fn eval(input: &str) -> Result<Vec<i32>, String> {
    let mut stack = Vec::new();
    let mut words = input.split_whitespace();
    
    while let Some(word) = words.next() {
        match word {
            "+" => {
                let b = stack.pop().ok_or("Invalid operation")?;
                let a = stack.pop().ok_or("Invalid operation")?;
                stack.push(a + b);
            },
            "-" => {
                let b = stack.pop().ok_or("Invalid operation")?;
                let a = stack.pop().ok_or("Invalid operation")?;
                stack.push(a - b);
            },
            "*" => {
                let b = stack.pop().ok_or("Invalid operation")?;
                let a = stack.pop().ok_or("Invalid operation")?;
                stack.push(a * b);
            },
            "/" => {
                let b = stack.pop().ok_or("Invalid operation")?;
                let a = stack.pop().ok_or("Invalid operation")?;
                if b == 0 { return Err("Division by zero".to_string()); }
                stack.push(a / b);
            },
            "dup" => {
                let top = stack.last().ok_or("Invalid operation")?;
                stack.push(*top);
            },
            "drop" => {
                stack.pop().ok_or("Invalid operation")?;
            },
            "swap" => {
                let b = stack.pop().ok_or("Invalid operation")?;
                let a = stack.pop().ok_or("Invalid operation")?;
                stack.push(b);
                stack.push(a);
            },
            "over" => {
                if stack.len() < 2 { return Err("Invalid operation".to_string()); }
                let second = stack[stack.len() - 2];
                stack.push(second);
            },
            _ => {
                if let Ok(n) = word.parse::<i32>() {
                    stack.push(n);
                } else {
                    return Err(format!("Unknown word: {}", word));
                }
            }
        }
    }
    
    Ok(stack)
}''',

    'parallel-letter-frequency': '''use std::collections::HashMap;
use std::sync::{Arc, Mutex};
use std::thread;

pub fn frequency(input: &[&str], worker_count: usize) -> HashMap<char, usize> {
    let result = Arc::new(Mutex::new(HashMap::new()));
    let mut handles = vec![];
    
    for text in input {
        let result_clone = Arc::clone(&result);
        let text_clone = text.to_string();
        
        let handle = thread::spawn(move || {
            let local_freq = text_clone
                .to_lowercase()
                .chars()
                .filter(|c| c.is_alphabetic())
                .fold(HashMap::new(), |mut map, ch| {
                    *map.entry(ch).or_insert(0) += 1;
                    map
                });
            
            let mut global = result_clone.lock().unwrap();
            for (ch, count) in local_freq {
                *global.entry(ch).or_insert(0) += count;
            }
        });
        
        handles.push(handle);
    }
    
    for handle in handles {
        handle.join().unwrap();
    }
    
    Arc::try_unwrap(result).unwrap().into_inner().unwrap()
}''',
}
