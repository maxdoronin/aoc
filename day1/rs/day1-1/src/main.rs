use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    if let Ok(lines) = read_lines("../../input.txt") {
        // Consumes the iterator, returns an (Optional) String

        let mut counter = 0;
        let mut index = 0;
        let mut depth0 = 0;

        for line in lines {
            if let Ok(depth_string) = line {
                let depth = depth_string.parse::<i32>().unwrap(); //we'll crash on non-numbers
                if index == 0 {
                    depth0 = depth;
                    index += 1;
                    continue;
                }
                if depth > depth0 {
                    counter += 1;
                }
                depth0 = depth;
                index += 1;
            }
        }
        println!("{}", counter);
    } else {
        panic!("Can't open file");
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}