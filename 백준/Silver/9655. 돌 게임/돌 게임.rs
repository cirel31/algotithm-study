use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();

    if n % 2 == 0 {
        println!("CY");
    } else {
        println!("SK");
    }
}
