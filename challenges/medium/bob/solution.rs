pub fn reply(s: &str) -> String {
    let s = s.trim();
    let is_question = s.ends_with('?');
    let is_yelling = s.chars().any(|c| c.is_alphabetic()) 
        && s.chars().filter(|c| c.is_alphabetic()).all(|c| c.is_uppercase());
    
    match (is_yelling, is_question) {
        (true, true) => "Calm down, I know what I'm doing!",
        (true, false) => "Whoa, chill out!",
        (false, true) => "Sure.",
        (false, false) => "OK then.",
    }.to_string()
}
