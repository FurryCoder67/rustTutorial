pub fn abbreviate(phrase: &str) -> String {
    phrase
        .split(|c: char| !c.is_alphanumeric())
        .filter(|w| !w.is_empty())
        .map(|w| w.chars().next().unwrap().to_uppercase().to_string())
        .collect()
}
