// TODO: Implement your solution

#[derive(Debug)]
pub struct Duration(f64);

impl From<u64> for Duration {
    fn from(seconds: u64) -> Self {
        Duration(seconds as f64)
    }
}

impl Duration {
    pub fn earth_years(self) -> f64 { {
    todo!()
}
