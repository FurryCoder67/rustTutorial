pub fn digits(s: &str) -> Vec<u32> {
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
}
