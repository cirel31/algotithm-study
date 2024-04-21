use std::io::{self, Read};
use std::collections::VecDeque;
use std::cmp;

pub fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();

    let t: usize = lines.next().unwrap().trim().parse().unwrap();
    for _ in 0..t {
        let nk = lines.next().unwrap().trim().split_whitespace().map(|x| x.parse::<usize>().unwrap()).collect::<Vec<_>>();
        let n = nk[0];
        let k = nk[1];

        let times: Vec<i32> = lines.next().unwrap().trim().split_whitespace()
                                   .map(|x| x.parse::<i32>().unwrap())
                                   .collect();

        let mut pre = vec![0; n];
        let mut suc = vec![Vec::new(); n];

        for _ in 0..k {
            let xy = lines.next().unwrap().trim().split_whitespace().map(|x| x.parse::<usize>().unwrap()).collect::<Vec<_>>();
            let x = xy[0] - 1;
            let y = xy[1] - 1;
            suc[x].push(y);
            pre[y] += 1;
        }

        let w: usize = lines.next().unwrap().trim().parse::<usize>().unwrap() - 1;

        let mut result = vec![0; n];
        let mut queue = VecDeque::new();

        for i in 0..n {
            if pre[i] == 0 {
                queue.push_back(i);
            }
        }

        while pre[w] > 0 {
            let u = queue.pop_front().unwrap();
            for &next in &suc[u] {
                result[next] = cmp::max(result[next], result[u] + times[u]);
                pre[next] -= 1;
                if pre[next] == 0 {
                    queue.push_back(next);
                }
            }
        }

        println!("{}", result[w] + times[w]);
    }
}

