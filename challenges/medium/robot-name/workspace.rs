// TODO: Implement your solution

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
    pub fn new() -> Self { {
    todo!()
}
