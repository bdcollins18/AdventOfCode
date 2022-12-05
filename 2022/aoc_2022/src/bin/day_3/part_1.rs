use std::{
    io::{
        Result,
        BufReader,
        BufRead
    },
    fs::{
        File
    },
    collections::{
        HashSet
    },
};

fn ascii_index_to_score(x: i32) -> i32 {
    const UPPER_A_INDEX:i32 = 65;
    const UPPER_Z_INDEX:i32 = 90;
    const LOWER_A_INDEX:i32 = 97;
    const LOWER_Z_INDEX:i32 = 122;
    match x {
        (UPPER_A_INDEX..=UPPER_Z_INDEX) => (x - UPPER_A_INDEX) + 27,
        (LOWER_A_INDEX..=LOWER_Z_INDEX) => (x - LOWER_A_INDEX) + 1,
        _ => panic!()
    }
}

#[derive(Debug)]
struct Rucksack {
    first_compartment: Vec<i32>,
    second_compartment: Vec<i32>
}

impl Rucksack {
    pub fn new(rucksack_str: String) -> Self {
        let rucksack_size = rucksack_str.bytes().count();
        let half_rucksack_size = rucksack_size / 2;
        Rucksack{
            first_compartment: rucksack_str.bytes().take(half_rucksack_size)
                .map(|x| ascii_index_to_score(x as i32)).collect::<Vec<_>>(),
            second_compartment: rucksack_str.bytes().skip(half_rucksack_size)
                .map(|x| ascii_index_to_score(x as i32)).collect::<Vec<_>>()
        }
    }

    pub fn comaprtment_single_intersection(&self) -> i32 {
        let first_compartment_set: HashSet<i32> = HashSet::from_iter(self.first_compartment.clone());
        let second_compartment_set: HashSet<i32> = HashSet::from_iter(self.second_compartment.clone());
        let mut intersection = first_compartment_set.intersection(&second_compartment_set);
        *(intersection.nth(0).unwrap())
    }
}

fn main() -> Result<()> {
    let file = File::open("./src/bin/day_3/input.txt")?;
    let reader = BufReader::new(file);
    let lines_iterator = reader.lines();

    let rucksacks = lines_iterator.map(|line| {
        let rucksack_str = line.unwrap();
        Rucksack::new(rucksack_str)
    }).collect::<Vec<_>>();
    let intersection_sum = rucksacks.iter().map(|rucksack| rucksack.comaprtment_single_intersection()).sum::<i32>();

    print!("Intersection Sum: {:?}\n", intersection_sum);
    Ok(())
}