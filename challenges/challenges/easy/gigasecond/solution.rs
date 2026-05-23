use std::time::Duration;

pub fn after(start: Duration) -> Duration {
    start + Duration::from_secs(1_000_000_000)
}
