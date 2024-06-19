use std::env;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: {} <input_file>", args[0]);
        std::process::exit(1);
    }

    let input_file = &args[1];
    let path = Path::new(input_file);
    let file = File::open(&path)?;

    let reader = io::BufReader::new(file);
    let mut case_number = 1;

    for line in reader.lines() {
        let line = line?;
        let mut parts = line.split_whitespace();
        
        if let Some(n_str) = parts.next() {
            if let Ok(n) = n_str.parse::<usize>() {
                let samples: Vec<i32> = parts.map(|s| s.parse::<i32>().unwrap()).collect();
                
                if samples.len() != n {
                    eprintln!("Error: Number of samples does not match the specified count");
                    std::process::exit(1);
                }
                
                let mut peaks = 0;
                for i in 1..(n - 1) {
                    if samples[i] > samples[i - 1] && samples[i] > samples[i + 1] {
                        peaks += 1;
                    }
                }

                println!("Case #{}: {}", case_number, peaks);
                case_number += 1;
            }
        }
    }

    Ok(())
}
