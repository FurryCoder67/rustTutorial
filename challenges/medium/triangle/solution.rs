pub struct Triangle {
        a: u64,
        b: u64,
        c: u64,
    }

impl Triangle {
    pub fn build(sides: [u64; 3]) -> Result<Triangle, &'static str> {
        let [a, b, c] = sides;
        if a + b < c || b + c < a || a + c < b {
            return Err("invalid triangle");
        }
        if a == 0 || b == 0 || c == 0 {
            return Err("invalid triangle");
        }
        Ok(Triangle { a, b, c })
    }

    pub fn is_equilateral(&self) -> bool {
        self.a == self.b && self.b == self.c
    }

    pub fn is_isosceles(&self) -> bool {
        self.a == self.b || self.b == self.c || self.a == self.c
    }

    pub fn is_scalene(&self) -> bool {
        self.a != self.b && self.b != self.c && self.a != self.c
    }
}
