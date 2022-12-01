use std::{
    vec::{
        Vec
    },
    io::{
        Result,
        BufReader,
        BufRead
    },
    fs::{
        File
    }
};

fn main() -> Result<()> {
    let file = File::open("./src/day_1/input.txt")?;
    let reader = BufReader::new(file);
    let lines_iterator = reader.lines();

    let mut elf_calories: Vec<u64> = Vec::new();
    let mut calories_accumulator: u64 = 0;
    for line_result in lines_iterator {
        let line = line_result.expect("Failed to read line");

        if line.is_empty() {
            elf_calories.push(calories_accumulator);
            calories_accumulator = 0;
            continue;
        }

        calories_accumulator += line.parse::<u64>().expect("Failed to parse line");
    }
    elf_calories.push(calories_accumulator);

    elf_calories.sort();

    let max_3_calories = &elf_calories[elf_calories.len() - 3 .. elf_calories.len()];

    print!("Max 3 elf calories: {:?}, Sum: {:?}\n", max_3_calories, max_3_calories.iter().sum::<u64>());

    Ok(())
}