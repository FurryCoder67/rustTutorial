use std::sync::Mutex;
use lazy_static::lazy_static;
use std::collections::HashSet;

lazy_static! {
    static ref USED_NAMES: Mutex<HashSet<String>> = Mutex::new(HashSet::new());
}

pub struct Robot {
    name: String,
}

impl Robot {
    pub fn new() -> Self {
        Robot {
            name: Self::generate_name(),
        }
    }

    pub fn name(&self) -> &str {
        &self.name
    }

    pub fn reset_name(&mut self) {
        self.name = Self::generate_name();
    }

    fn generate_name() -> String {
        use rand::Rng;
        let mut rng = rand::thread_rng();
        loop {
            let name = format!(
                "{}{}{}",
                (rng.gen_range(0..26) as u8 + b'A') as char,
                (rng.gen_range(0..26) as u8 + b'A') as char,
                rng.gen_range(0..1000)
            );
            let mut used = USED_NAMES.lock().unwrap();
            if !used.contains(&name) {
                used.insert(name.clone());
                return name;
            }
        }
    }
}
