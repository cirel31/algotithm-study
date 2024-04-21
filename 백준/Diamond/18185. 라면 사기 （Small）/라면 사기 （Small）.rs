use std::io;

fn buy_one(arr: &mut Vec<i32>, x: usize, cost: &mut Vec<i32>) {
    cost.push(3 * arr[x]);
}

fn buy_two(arr: &mut Vec<i32>, x: usize, cost: &mut Vec<i32>) {
    let product = arr[x..x+2].iter().min().unwrap().to_owned();
    if product > 0 {
        cost.push(5 * product);
        for p in arr.iter_mut().take(x+2).skip(x) {
            *p -= product;
        }
    }
}

fn buy_three(arr: &mut Vec<i32>, x: usize, cost: &mut Vec<i32>) {
    let product = arr[x..x+3].iter().min().unwrap().to_owned();
    if product > 0 {
        cost.push(7 * product);
        for p in arr.iter_mut().take(x+3).skip(x) {
            *p -= product;
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();

    input.clear();
    io::stdin().read_line(&mut input).unwrap();
    let mut li: Vec<i32> = input.trim().split_whitespace().map(|num| num.parse().unwrap()).collect();
    li.extend(vec![0, 0]); // Append two zeros to the vector

    let mut cost: Vec<i32> = Vec::new();
    for i in 0..n {
        if li[i+1] > li[i+2] {
            let m = li[i].min(li[i+1] - li[i+2]);
            cost.push(m * 5);
            li[i] -= m;
            li[i+1] -= m;
            buy_three(&mut li, i, &mut cost);
            buy_two(&mut li, i, &mut cost);
            buy_one(&mut li, i, &mut cost);
        } else {
            buy_three(&mut li, i, &mut cost);
            buy_two(&mut li, i, &mut cost);
            buy_one(&mut li, i, &mut cost);
        }
    }
    println!("{}", cost.iter().sum::<i32>());
}
