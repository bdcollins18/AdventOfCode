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

struct Game {
    opponent_shape: Shape,
    your_shape: Shape
}

impl Game {
    pub fn new(input: &str) -> Self {
        Self {
            opponent_shape: match input.chars().nth(0).unwrap() {
                'A' => Shape::Rock,
                'B' => Shape::Paper,
                'C' => Shape::Scissors,
                c => panic!("Found {:?}", c)
            },
            your_shape: match input.chars().nth(2).unwrap() {
                'X' => Shape::Rock,
                'Y' => Shape::Paper,
                'Z' => Shape::Scissors,
                c => panic!("Found {:?}", c)
            }
        }
    }

    pub fn get_outcome(&self) -> Outcome {
        match self {
            Game{opponent_shape:Shape::Rock, your_shape:Shape::Scissors} |
            Game{opponent_shape:Shape::Paper, your_shape:Shape::Rock} |
            Game{opponent_shape:Shape::Scissors, your_shape:Shape::Paper} => Outcome::Loss,

            Game{opponent_shape:Shape::Rock, your_shape:Shape::Rock} |
            Game{opponent_shape:Shape::Paper, your_shape:Shape::Paper} |
            Game{opponent_shape:Shape::Scissors, your_shape:Shape::Scissors}  => Outcome::Draw,

            Game{opponent_shape:Shape::Rock, your_shape:Shape::Paper} |
            Game{opponent_shape:Shape::Paper, your_shape:Shape::Scissors} |
            Game{opponent_shape:Shape::Scissors, your_shape:Shape::Rock} => Outcome::Win,
        }
    }

    pub fn score(&self) -> u8 {
        self.your_shape.score() + self.get_outcome().score()
    }
}

fn main() -> Result<()> {
    let file = File::open("./src/bin/day_2/input.txt")?;
    let reader = BufReader::new(file);
    let lines_iterator = reader.lines();

    let games = lines_iterator.map(|line| Game::new(&line.unwrap())).collect::<Vec<Game>>();

    let score = games.iter().map(|game| game.score() as u64).sum::<u64>();

    print!("Total Score: {:?}\n", score);

    Ok(())
}