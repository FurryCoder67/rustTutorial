use std::time::{Duration, SystemTime};

pub fn add_gigasecond(start: SystemTime) -> SystemTime {
    start
        .checked_add(Duration::from_secs(1_000_000_000))
        .expect("gigasecond addition overflowed")
}
