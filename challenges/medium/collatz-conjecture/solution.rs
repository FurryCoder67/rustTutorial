pub fn collatz(mut n: u64) -> Result<u64, String> {
    if n == 0 {
        return Err("Only positive numbers are allowed".to_string());
    }
    let mut steps = 0;
    while n != 1 {
        n = if n % 2 == 0 { n / 2 } else { 3 * n + 1 };
        steps += 1;
    }
    Ok(steps)
}
