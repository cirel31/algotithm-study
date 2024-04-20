use std::io;

fn stone_game(n: usize) -> &'static str {
    let mut dp = vec![false; n + 1];

    if n >= 1 {
        dp[1] = true;
    }
    if n >= 2 {
        dp[2] = false;
    }
    if n >= 3 {
        dp[3] = true;
    }

    for i in 4..=n {
        dp[i] = !dp[i - 1] || (i >= 3 && !dp[i - 3]);
    }

    if dp[n] {
        "SK"
    } else {
        "CY"
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap(); 
    println!("{}", stone_game(n));
}
