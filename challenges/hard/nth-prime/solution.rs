fn is_prime(n: u32) -> bool {
    if n <= 1 {
        return false;
    }
    if n == 2 {
        return true;
    }
    if n % 2 == 0 {
        return false;
    }

    let limit = (n as f64).sqrt() as u32;
    (3..=limit).step_by(2).all(|i| n % i != 0)
}

pub fn nth(n: u32) -> u32 {
    assert!(n > 0, "n must be greater than zero");

    let mut count = 0;
    let mut candidate = 1;

    while count < n {
        candidate += 1;
        if is_prime(candidate) {
            count += 1;
        }
    }

    candidate
}
