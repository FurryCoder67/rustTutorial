pub fn answer(problem: &str) -> Result<i64, String> {
    let words: Vec<&str> = problem.trim().split_whitespace().collect();
    
    if words.len() < 3 || words[0] != "What" || words[1] != "is" {
        return Err("Invalid problem format".to_string());
    }
    
    let mut result: i64 = words[2].parse().map_err(|_| "Invalid initial number".to_string())?;
    let mut i = 3;
    
    while i < words.len() {
        if i + 1 >= words.len() {
            return Err("Invalid operation".to_string());
        }
        
        let op = words[i];
        let operand: i64 = words[i + 1].parse().map_err(|_| "Invalid operand".to_string())?;
        
        result = match op {
            "plus" => result + operand,
            "minus" => result - operand,
            "multiplied" => result * operand,
            "divided" => result / operand,
            _ => return Err(format!("Unknown operation: {}", op)),
        };
        
        i += 2;
        if i < words.len() && words[i] == "by" {
            i += 1;
        }
    }
    
    Ok(result)
}
