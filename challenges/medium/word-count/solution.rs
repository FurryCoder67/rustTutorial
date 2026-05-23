use std::collections::HashMap;

pub fn word_count(phrase: &str) -> HashMap<String, u32> {
    phrase
        .to_lowercase()
        .chars()
        .map(|c| if c.is_alphanumeric() { c } else { ' ' })
        .collect::<String>()
        .split_whitespace()
        .fold(HashMap::new(), |mut counts, word| {
            *counts.entry(word.to_string()).or_insert(0) += 1;
            counts
        })
}
