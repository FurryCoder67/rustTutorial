pub fn largest_product(s: &str, span: usize) -> Result<u64, String> {
    if span > s.len() {
        return Err("span must be smaller than string length".to_string());
    }
    if span == 0 {
        return Ok(1);
    }
    
    let digits: Result<Vec<u64>, _> = s.chars().map(|c| {
        if c.is_ascii_digit() {
            Ok(c.to_digit(10).unwrap() as u64)
        } else {
            Err("digits input must only contain digits".to_string())
        }
    }).collect();
    
    let digits = digits?;
    Ok(digits.windows(span).map(|w| w.iter().product()).max().unwrap_or(0))
}
