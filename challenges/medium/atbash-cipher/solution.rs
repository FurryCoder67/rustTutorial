pub fn encode(plaintext: &str) -> String {
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
}
