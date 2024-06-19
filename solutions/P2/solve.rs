use std::env; // For handling command-line arguments
use std::fs::File; // For file operations
use std::io::{self, BufRead, BufReader}; // For buffered reading

fn main() -> io::Result<()> {
    // Collect the command-line arguments
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        // Check if the number of arguments is correct
        eprintln!("Usage: {} <input_file>", args[0]);
        std::process::exit(1);
    }

    let input_file = &args[1];
    let file = File::open(input_file)?; // Open the file
    let reader = BufReader::new(file); // Create a buffered reader for efficient reading

    let mut lines = reader.lines();
    let t: usize = lines.next().unwrap()?.trim().parse().unwrap(); // Read the number of test cases

    for c in 1..=t {
        let mut ret = 0;
        let (n, mut b): (usize, i32) = {
            let line = lines.next().unwrap()?;
            let mut iter = line.split_whitespace();
            let n = iter.next().unwrap().parse().unwrap();
            let b = iter.next().unwrap().parse().unwrap();
            (n, b)
        };

        let mut a: Vec<i32> = {
            let line = lines.next().unwrap()?;
            line.split_whitespace().map(|s| s.parse().unwrap()).collect()
        };

    a.sort(); // Sort the house prices in ascending order

    for price in a {
        if price <= b {
            b -= price; // Deduct the house price from the budget
            ret += 1; // Increment the count of houses bought
        } else {
            break; // If the current house price exceeds the budget, break the loop
        }
    }

        println!("Case #{}: {}", c, ret); // Print the result for the current test case
    }

    Ok(())
}
