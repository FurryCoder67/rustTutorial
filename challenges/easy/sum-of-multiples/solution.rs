pub fn sum(limit: u32, factors: &[u32]) -> u32 {
    (1..limit)
        .filter(|&n| {
            factors
                .iter()
                .copied()
                .filter(|&f| f != 0)
                .any(|f| n % f == 0)
        })
        .sum()
}
