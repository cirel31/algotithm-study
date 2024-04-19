use std::io::{self, BufRead, BufWriter, Write};

fn solve(stack: &mut Vec<i32>, command: &str, handle: &mut BufWriter<std::io::StdoutLock>) {
    let args: Vec<&str> = command.split_whitespace().collect();

    match args[0] {
        "1" => {
            let num: i32 = args[1].parse().unwrap();
            stack.push(num);
        },
        "2" => {
            if let Some(num) = stack.pop() {
                writeln!(handle, "{}", num).expect("Failed to write to buffer");
            } else {
                writeln!(handle, "-1").expect("Failed to write to buffer");
            }
        },
        "3" => writeln!(handle, "{}", stack.len()).expect("Failed to write to buffer"),
        "4" => writeln!(handle, "{}", if stack.is_empty() { 1 } else { 0 }).expect("Failed to write to buffer"),
        "5" => {
            if let Some(&num) = stack.last() {
                writeln!(handle, "{}", num).expect("Failed to write to buffer");
            } else {
                writeln!(handle, "-1").expect("Failed to write to buffer");
            }
        },
        _ => (),
    }
}

fn main() {
    // 미리 할당된 메모리 사용
    let stdin = io::stdin();
    let handle = stdin.lock();
    let mut lines = handle.lines();
    let num_commands: usize = lines.next().unwrap().unwrap().trim().parse().expect("Expected a number");
    
    let mut stack: Vec<i32> = Vec::with_capacity(100_000);
    let mut output = BufWriter::new(io::stdout().lock());

    // 명령어 처리
    for line in lines.take(num_commands) {
        if let Ok(command) = line {
            solve(&mut stack, &command, &mut output);
        }
    }

    output.flush().expect("Failed to flush the buffer");
}
