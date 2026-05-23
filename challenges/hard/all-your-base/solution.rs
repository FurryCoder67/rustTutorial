fn digit_value(digit: char) -> Option<u32> {
    match digit {
        '0'..='9' => Some((digit as u32) - ('0' as u32)),
        'a'..='z' => Some((digit as u32) - ('a' as u32) + 10),
        'A'..='Z' => Some((digit as u32) - ('A' as u32) + 10),
        _ => None,
    }
}

fn digit_char(value: u32) -> Option<char> {
    match value {
        0..=9 => Some((b'0' + value as u8) as char),
        10..=35 => Some((b'a' + (value as u8 - 10)) as char),
        _ => None,
    }
}

pub fn decode(input: &str, base: u32) -> Option<u32> {
    if base < 2 || base > 36 {
        return None;
    }

    input.chars().try_fold(0u32, |acc, digit| {
        let value = digit_value(digit)?;
        if value >= base {
            return None;
        }
        acc.checked_mul(base)?.checked_add(value)
    })
}

pub fn encode(mut number: u32, base: u32) -> Option<String> {
    if base < 2 || base > 36 {
        return None;
    }

    if number == 0 {
        return Some("0".to_string());
    }

    let mut digits = Vec::new();
    while number > 0 {
        let value = number % base;
        digits.push(digit_char(value)?);
        number /= base;
    }
    digits.reverse();
    Some(digits.iter().collect())
}

pub fn reencode(input: &str, from_base: u32, to_base: u32) -> Option<String> {
    decode(input, from_base).and_then(|value| encode(value, to_base))
}
