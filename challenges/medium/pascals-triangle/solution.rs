pub fn generate(row_count: u32) -> Vec<Vec<u32>> {
    let mut triangle = Vec::new();
    for i in 0..row_count as usize {
        let mut row = vec![1];
        if i > 0 {
            for j in 1..i {
                row.push(triangle[i - 1][j - 1] + triangle[i - 1][j]);
            }
            row.push(1);
        }
        triangle.push(row);
    }
    triangle
}
