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
    elf_1: Vec<i32>,
    elf_2: Vec<i32>,
    elf_3: Vec<i32>
}

impl Rucksack {
    pub fn new(elf_1_str: String, elf_2_str: String, elf_3_str: String) -> Self {
        Rucksack{
            elf_1: elf_1_str.bytes().map(|x| ascii_index_to_score(x as i32)).collect::<Vec<_>>(),
            elf_2: elf_2_str.bytes().map(|x| ascii_index_to_score(x as i32)).collect::<Vec<_>>(),
            elf_3: elf_3_str.bytes().map(|x| ascii_index_to_score(x as i32)).collect::<Vec<_>>(),
        }
    }

    pub fn elf_single_intersection(&self) -> i32 {
        let elf_1_set: HashSet<i32> = HashSet::from_iter(self.elf_1.clone());
        let elf_2_set: HashSet<i32> = HashSet::from_iter(self.elf_2.clone());
        let elf_3_set: HashSet<i32> = HashSet::from_iter(self.elf_3.clone());
        let intersection_1_2 = elf_1_set.intersection(&elf_2_set);
        let intersection_1_2_deref = intersection_1_2.cloned().collect::<HashSet<i32>>();
        let mut intersection_1_2_3 = intersection_1_2_deref.intersection(&elf_3_set);
        *(intersection_1_2_3.nth(0).unwrap())
    }
}

fn main() -> Result<()> {
    let file = File::open("./src/bin/day_3/input.txt")?;
    let reader = BufReader::new(file);
    let mut lines_iterator = reader.lines();

    let mut rucksacks: Vec<Rucksack> = Vec::new();
    loop {
        let line1 = match lines_iterator.next() {
            Some(line) => line.unwrap(),
            None => break,
        };
        let line2 = lines_iterator.next().unwrap().unwrap();
        let line3 = lines_iterator.next().unwrap().unwrap();
        rucksacks.push(Rucksack::new(line1, line2, line3))
    }

    let intersection_sum = rucksacks.iter().map(|rucksack| rucksack.elf_single_intersection()).sum::<i32>();

    print!("Intersection Sum: {:?}\n", intersection_sum);
    Ok(())
}