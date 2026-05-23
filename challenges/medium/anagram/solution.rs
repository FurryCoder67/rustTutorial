use std::collections::HashSet;

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
}
