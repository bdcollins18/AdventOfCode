use std::{
    io::{
        Result,
        BufReader,
        BufRead
    },
    fs::{
        File
    },
    ops::{
        RangeInclusive
    },
    cmp::{
        min,
        max
    }
};

fn range_str_to_range(range_string: &str) -> RangeInclusive<usize> {
    let parts = range_string.split('-').collect::<Vec<_>>();
    let (lower_string, upper_string) = (parts[0], parts[1]);
    lower_string.parse::<usize>().unwrap()..=upper_string.parse::<usize>().unwrap()
}

fn range_intersect(range1: RangeInclusive<usize>, range2: RangeInclusive<usize>) -> RangeInclusive<usize> {
    let (range1_lower, range1_upper) = range1.into_inner();
    let (range2_lower, range2_upper) = range2.into_inner();
    max::<usize>(range1_lower, range2_lower)..=min::<usize>(range1_upper, range2_upper)
}

fn range_len(range: RangeInclusive<usize>) -> usize {
    let (start, end) = (*range.start(), *range.end());
    if start > end {
        0
    } else {
        end - start + 1
    }
}

fn main() -> Result<()>{
    let file = File::open("./src/bin/day_4/input.txt")?;
    let reader = BufReader::new(file);
    let lines_iterator = reader.lines();

    let range_pairs = lines_iterator.map(|line| {
        let line_string = line.unwrap();
        let parts = line_string.split(',').collect::<Vec<_>>();
        let (range_1_string, range_2_string) = (parts[0], parts[1]);
        (range_str_to_range(range_1_string), range_str_to_range(range_2_string))
    });

    let mut contained_range_count: usize = 0;
    let mut overlapping_range_count: usize = 0;
    for (range_1, range_2) in range_pairs {
        let intersection = range_intersect(range_1.clone(), range_2.clone());
        if (intersection == range_1) || (intersection == range_2) {
            contained_range_count += 1;
        }
        if range_len(intersection) > 0 {
            overlapping_range_count += 1;
        }
    }

    print!("Contained Ranges Count: {:?}\n", contained_range_count);
    print!("Overlappig Ranges Count: {:?}\n", overlapping_range_count);
    Ok(())
}
