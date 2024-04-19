use std::io::{self, Read};

// 주어진 두 숫자와 부등호 연산자에 대해 조건을 검사하는 함수
fn get_num(x: char, y: char, oper: char) -> bool {
    match oper {
        '<' => x < y,
        '>' => x > y,
        _ => true,
    }
}

// 깊이 우선 탐색(DFS)를 사용하여 가능한 모든 숫자 조합을 생성하는 함수
fn dfs(idx: usize, num: &str, oper: &[char], check: &mut [bool], results: &mut Vec<String>) {
    // 모든 부등호 조건을 충족하는 숫자 조합이 완성된 경우 결과 벡터에 추가
    if idx == oper.len() + 1 {
        results.push(num.to_string()); 
        return;
    }

    // 가능한 모든 숫자 (0-9)를 반복
    for i in 0..10 {
        let ic = (i as u8 + b'0') as char; 
        // 해당 숫자가 아직 사용되지 않았고, 첫 숫자이거나 부등호 조건을 만족하는 경우
        if !check[i] {
            if idx == 0 || get_num(num.chars().last().unwrap(), ic, oper[idx - 1]) {
                // 해당 숫자를 사용했다고 표시
                check[i] = true; 
                dfs(idx + 1, &(num.to_owned() + &ic.to_string()), oper, check, results); // 다음 숫자로 DFS 수행
                // 사용했던 숫자를 다시 사용 가능하게 함
                check[i] = false; 
            }
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // 입력을 줄 단위로 나눔
    let mut lines = input.lines();
    // 부등호 개수
    let k: usize = lines.next().unwrap().trim().parse().unwrap(); 
    let oper: Vec<char> = lines.next().unwrap().trim().split_whitespace().map(|x| x.chars().next().unwrap()).collect(); // 부등호 배열 읽기
    // 각 숫자의 사용 여부를 추적하는 배열
    let mut check = vec![false; 10]; 
    // 가능한 모든 숫자 조합을 저장할 벡터
    let mut results = Vec::new(); 

    dfs(0, "", &oper, &mut check, &mut results); 
    results.sort();
    
    println!("{}", results.last().unwrap());
    println!("{}", results.first().unwrap());
}
