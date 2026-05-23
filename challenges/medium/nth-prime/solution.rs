pub fn nth(n: u32) -> Result<u32, String> {
    if n == 0 {
        return Err("there is no zeroth prime".to_string());
    }
    let mut count = 0;
    let mut candidate = 2;
    loop {
        if is_prime(candidate) {
            count += 1;
            if count == n {
                return Ok(candidate);
            }
        }
        candidate += 1;
    }
}

fn is_prime(n: u32) -> bool {
    if n < 2 { return false; }
    if n == 2 { return true; }
    if n % 2 == 0 { return false; }
    for i in (3..=(n as f64).sqrt() as u32).step_by(2) {
        if n % i == 0 { return false; }
    }
    true
}
