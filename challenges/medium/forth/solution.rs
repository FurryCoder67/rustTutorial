// A simple Forth interpreter
pub fn eval(input: &str) -> Result<Vec<i32>, String> {
    let mut stack = Vec::new();
    let mut words = input.split_whitespace();
    
    while let Some(word) = words.next() {
        match word {
            "+" => {
                let b = stack.pop().ok_or("Invalid operation")?;
                let a = stack.pop().ok_or("Invalid operation")?;
                stack.push(a + b);
            },
            "-" => {
                let b = stack.pop().ok_or("Invalid operation")?;
                let a = stack.pop().ok_or("Invalid operation")?;
                stack.push(a - b);
            },
            "*" => {
                let b = stack.pop().ok_or("Invalid operation")?;
                let a = stack.pop().ok_or("Invalid operation")?;
                stack.push(a * b);
            },
            "/" => {
                let b = stack.pop().ok_or("Invalid operation")?;
                let a = stack.pop().ok_or("Invalid operation")?;
                if b == 0 { return Err("Division by zero".to_string()); }
                stack.push(a / b);
            },
            "dup" => {
                let top = stack.last().ok_or("Invalid operation")?;
                stack.push(*top);
            },
            "drop" => {
                stack.pop().ok_or("Invalid operation")?;
            },
            "swap" => {
                let b = stack.pop().ok_or("Invalid operation")?;
                let a = stack.pop().ok_or("Invalid operation")?;
                stack.push(b);
                stack.push(a);
            },
            "over" => {
                if stack.len() < 2 { return Err("Invalid operation".to_string()); }
                let second = stack[stack.len() - 2];
                stack.push(second);
            },
            _ => {
                if let Ok(n) = word.parse::<i32>() {
                    stack.push(n);
                } else {
                    return Err(format!("Unknown word: {}", word));
                }
            }
        }
    }
    
    Ok(stack)
}
