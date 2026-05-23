pub fn classify(num: u64) -> Result<String, String> {
    if num == 0 {
        return Err("num must be greater than 0".to_string());
    }
    let sum: u64 = (1..num).filter(|&i| num % i == 0).sum();
    Ok(match sum.cmp(&num) {
        std::cmp::Ordering::Less => "deficient",
        std::cmp::Ordering::Equal => "perfect",
        std::cmp::Ordering::Greater => "abundant",
    }.to_string())
}
