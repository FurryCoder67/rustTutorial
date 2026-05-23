pub fn is_pangram(sentence: &str) -> bool {
    let lower = sentence.to_lowercase();
    "abcdefghijklmnopqrstuvwxyz"
        .chars()
        .all(|c| lower.contains(c))
}
