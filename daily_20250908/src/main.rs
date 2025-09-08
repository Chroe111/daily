use std::io::stdin;

fn expr(input: &Vec<char>, i: &mut usize) -> i32 {
    let mut val: i32 = term(input, i);
    
    while *i < input.len() && (input[*i] == '+' || input[*i] == '-') {
        let op: char = input[*i];
        *i += 1;
        let val2: i32 = term(input, i);
        if op == '+' {
            val += val2;
        } else {
            val -= val2;
        }
    };
    
    val
}

fn term(input: &Vec<char>, i: &mut usize) -> i32 {
    let mut val: i32 = number(input, i);

    while *i < input.len() && (input[*i] == '*' || input[*i] == '/') {
        let op: char = input[*i];
        *i += 1;
        let val2: i32 = number(input, i);
        if op == '*' {
            val *= val2;
        } else {
            val /= val2;
        }
    };

    val
}

fn number(input: &Vec<char>, i: &mut usize) -> i32 {
    let mut num_string = String::new();

    while *i < input.len() && input[*i].is_ascii_digit() {
        num_string.push(input[*i]);
        *i += 1;
    };

    num_string.parse().unwrap()
}

fn main() {
    let mut input_text: String = String::new();
    stdin().read_line(&mut input_text).expect("error");
    input_text.retain(|c| c != ' ');
    let chars: Vec<char> = input_text.trim().chars().collect();

    let mut i: usize = 0;
    println!("{}", expr(&chars, &mut i));
}
