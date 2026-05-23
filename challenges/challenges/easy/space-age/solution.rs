#[derive(Debug)]
pub struct Duration(f64);

impl From<u64> for Duration {
    fn from(seconds: u64) -> Self {
        Duration(seconds as f64)
    }
}

impl Duration {
    pub fn earth_years(self) -> f64 {
        self.0 / 31_557_600.0
    }
    pub fn mercury_years(self) -> f64 { self.earth_years() / 0.2408467 }
    pub fn venus_years(self) -> f64 { self.earth_years() / 0.61519726 }
    pub fn mars_years(self) -> f64 { self.earth_years() / 1.88082869 }
    pub fn jupiter_years(self) -> f64 { self.earth_years() / 11.862615 }
    pub fn saturn_years(self) -> f64 { self.earth_years() / 29.4571 }
    pub fn uranus_years(self) -> f64 { self.earth_years() / 84.07 }
    pub fn neptune_years(self) -> f64 { self.earth_years() / 164.79 }
}
