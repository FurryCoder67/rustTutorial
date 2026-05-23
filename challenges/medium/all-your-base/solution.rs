pub fn convert(num: &[u32], from_base: u32, to_base: u32) -> Result<Vec<u32>, String> {
    if from_base < 2 { return Err("from base must be >= 2".to_string()); }
    if to_base < 2 { return Err("to base must be >= 2".to_string()); }
    
    if num.iter().any(|&d| d >= from_base) {
        return Err("digit is >= base".to_string());
    }
    
    let mut value = 0u64;
    for &digit in num {
        value = value * from_base as u64 + digit as u64;
    }
    
    if value == 0 {
        return Ok(vec![0]);
    }
    
    let mut result = Vec::new();
    while value > 0 {
        result.push((value % to_base as u64) as u32);
        value /= to_base as u64;
    }
    result.reverse();
    Ok(result)
}
