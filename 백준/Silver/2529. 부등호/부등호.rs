use std::io::{self, Read};

fn get_num(x: char, y: char, oper: char) -> bool {
    match oper {
        '<' => x < y,
        '>' => x > y,
        _ => true,
    }
}

fn dfs(idx: usize, num: &str, oper: &[char], check: &mut [bool], results: &mut Vec<String>) {
    if idx == oper.len() + 1 {
        results.push(num.to_string());
        return;
    }

    for i in 0..10 {
        let ic = (i as u8 + b'0') as char;
        if !check[i] {
            if idx == 0 || get_num(num.chars().last().unwrap(), ic, oper[idx - 1]) {
                check[i] = true;
                dfs(idx + 1, &(num.to_owned() + &ic.to_string()), oper, check, results);
                check[i] = false;
            }
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let k: usize = lines.next().unwrap().trim().parse().unwrap();
    let oper: Vec<char> = lines.next().unwrap().trim().split_whitespace().map(|x| x.chars().next().unwrap()).collect();

    let mut check = vec![false; 10];
    let mut results = Vec::new();

    dfs(0, "", &oper, &mut check, &mut results);

    results.sort();
    println!("{}", results.last().unwrap());
    println!("{}", results.first().unwrap());
}
