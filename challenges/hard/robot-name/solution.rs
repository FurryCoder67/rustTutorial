use std::sync::atomic::{AtomicUsize, Ordering};

static ROBOT_COUNTER: AtomicUsize = AtomicUsize::new(0);
const MAX_ROBOTS: usize = 26 * 26 * 1000;

fn next_name() -> String {
    let count = ROBOT_COUNTER.fetch_add(1, Ordering::SeqCst) % MAX_ROBOTS;
    let letters = count / 1000;
    let digits = count % 1000;
    let first = (letters / 26) as u8 + b'A';
    let second = (letters % 26) as u8 + b'A';
    format!("{}{}{:03}", first as char, second as char, digits)
}

pub struct Robot {
    name: String,
}

impl Robot {
    pub fn new() -> Self {
        Robot {
            name: next_name(),
        }
    }

    pub fn name(&self) -> &str {
        &self.name
    }

    pub fn reset_name(&mut self) {
        self.name = next_name();
    }
}
