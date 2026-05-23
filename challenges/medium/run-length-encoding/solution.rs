pub fn encode(source: &str) -> String {
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
}
