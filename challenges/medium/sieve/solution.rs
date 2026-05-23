pub fn primes(limit: u32) -> Vec<u32> {
    if limit < 2 { return vec![]; }
    let mut sieve = vec![true; (limit + 1) as usize];
    sieve[0] = false;
    sieve[1] = false;
    
    for i in 2..=((limit as f64).sqrt() as u32) {
        if sieve[i as usize] {
            for j in ((i * i)..=limit).step_by(i as usize) {
                sieve[j as usize] = false;
            }
        }
    }
    
    sieve.iter()
        .enumerate()
        .filter_map(|(i, &is_prime)| if is_prime { Some(i as u32) } else { None })
        .collect()
}
