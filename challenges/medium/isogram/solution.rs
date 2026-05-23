pub fn check(phrase: &str) -> bool {
    let mut seen = std::collections::HashSet::new();
    phrase
        .to_lowercase()
        .chars()
        .filter(|c| c.is_alphabetic())
        .all(|c| seen.insert(c))
}
