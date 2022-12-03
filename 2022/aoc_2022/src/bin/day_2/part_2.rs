use std::{
    io::{
        Result,
        BufReader,
        BufRead
    },
    fs::{
        File
    }
};

enum Shape {
    Rock,
    Paper,
    Scissors
}

impl Shape {
    pub fn score(&self) -> u8 {
        match self {
            Shape::Rock => 1,
            Shape::Paper => 2,
            Shape::Scissors => 3
        }
    }
}

enum Outcome {
    Loss,
    Draw,
    Win
}

impl Outcome {
    pub fn score(&self) -> u8 {
        match self {
            Outcome::Loss => 0,
            Outcome::Draw => 3,
            Outcome::Win => 6,
        }
    }
}

struct Strategy {
    opponent_shape: Shape,
    outcome_strategy: Outcome
}

impl Strategy {
    pub fn new(input: &str) -> Self {
        Self {
            opponent_shape: match input.chars().nth(0).unwrap() {
                'A' => Shape::Rock,
                'B' => Shape::Paper,
                'C' => Shape::Scissors,
                c => panic!("Found {:?}", c)
            },
            outcome_strategy: match input.chars().nth(2).unwrap() {
                'X' => Outcome::Loss,
                'Y' => Outcome::Draw,
                'Z' => Outcome::Win,
                c => panic!("Found {:?}", c)
            }
        }
    }

    pub fn get_shape(&self) -> Shape {
        match self {
            Strategy{opponent_shape:Shape::Rock, outcome_strategy:Outcome::Draw} |
            Strategy{opponent_shape:Shape::Paper, outcome_strategy:Outcome::Loss} |
            Strategy{opponent_shape:Shape::Scissors, outcome_strategy:Outcome::Win} => Shape::Rock,

            Strategy{opponent_shape:Shape::Rock, outcome_strategy:Outcome::Win} |
            Strategy{opponent_shape:Shape::Paper, outcome_strategy:Outcome::Draw} |
            Strategy{opponent_shape:Shape::Scissors, outcome_strategy:Outcome::Loss} => Shape::Paper,

            Strategy{opponent_shape:Shape::Rock, outcome_strategy:Outcome::Loss} |
            Strategy{opponent_shape:Shape::Paper, outcome_strategy:Outcome::Win} |
            Strategy{opponent_shape:Shape::Scissors, outcome_strategy:Outcome::Draw} => Shape::Scissors
        }
    }

    pub fn score(&self) -> u8 {
        self.get_shape().score() + self.outcome_strategy.score()
    }
}

fn main() -> Result<()> {
    let file = File::open("./src/bin/day_2/input.txt")?;
    let reader = BufReader::new(file);
    let lines_iterator = reader.lines();

    let games = lines_iterator.map(|line| Strategy::new(&line.unwrap())).collect::<Vec<Strategy>>();

    let score = games.iter().map(|game| game.score() as u64).sum::<u64>();

    print!("Total Score: {:?}\n", score);

    Ok(())
}