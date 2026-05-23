fn atbash_char(ch: char) -> Option<char> {
    if ch.is_ascii_alphabetic() {
        let offset = ch.to_ascii_lowercase() as u8 - b'a';
        Some((b'z' - offset) as char)
    } else {
        None
    }
}

pub fn encode(plain: &str) -> String {
    plain
        .chars()
        .filter_map(|ch| {
            if ch.is_ascii_alphabetic() {
                atbash_char(ch)
            } else if ch.is_ascii_digit() {
                Some(ch)
            } else {
                None
            }
        })
        .collect::<String>()
        .chars()
        .collect::<Vec<_>>()
        .chunks(5)
        .map(|chunk| chunk.iter().collect::<String>())
        .collect::<Vec<_>>()
        .join(" ")
}

pub fn decode(cipher: &str) -> String {
    cipher
        .chars()
        .filter(|ch| ch.is_ascii_alphanumeric())
        .map(|ch| {
            if ch.is_ascii_digit() {
                ch
            } else {
                atbash_char(ch).unwrap_or(ch)
            }
        })
        .collect()
}
