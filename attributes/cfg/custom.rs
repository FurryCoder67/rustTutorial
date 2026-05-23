#[cfg(some_condition)]
fn conditional_function() {
    println!("condition met!");
}

fn main() {
    conditional_function();
}
$ rustc --cfg some_condition custom.rs && ./custom
condition met!
