pub fn square(s: u32) -> Result<u64, String> {
    match s {
        1..=64 => Ok(1u64 << (s - 1)),
        _ => Err("square must be between 1 and 64".to_string()),
    }
}

pub fn total() -> u64 {
    u64::MAX
}
