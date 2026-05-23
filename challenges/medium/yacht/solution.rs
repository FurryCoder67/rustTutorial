pub enum Category {
        Ones,
        Twos,
        Threes,
        Fours,
        Fives,
        Sixes,
        FullHouse,
        FourOfAKind,
        LittleStraight,
        BigStraight,
        Choice,
        Yacht,
    }

pub fn score(dice: &[u8], category: &Category) -> u8 {
    match category {
        Category::Ones => dice.iter().filter(|&&d| d == 1).sum(),
        Category::Twos => dice.iter().filter(|&&d| d == 2).sum(),
        Category::Threes => dice.iter().filter(|&&d| d == 3).sum(),
        Category::Fours => dice.iter().filter(|&&d| d == 4).sum(),
        Category::Fives => dice.iter().filter(|&&d| d == 5).sum(),
        Category::Sixes => dice.iter().filter(|&&d| d == 6).sum(),
        Category::FullHouse => full_house(dice),
        Category::FourOfAKind => four_of_a_kind(dice),
        Category::LittleStraight => if is_little_straight(dice) { dice.iter().sum() } else { 0 },
        Category::BigStraight => if is_big_straight(dice) { dice.iter().sum() } else { 0 },
        Category::Choice => dice.iter().sum(),
        Category::Yacht => if is_yacht(dice) { dice.iter().sum() } else { 0 },
    }
}

fn full_house(dice: &[u8]) -> u8 {
    let mut counts = [0u8; 7];
    for &d in dice { counts[d as usize] += 1; }
    if counts.iter().filter(|&&c| c == 2).count() == 1 && counts.iter().filter(|&&c| c == 3).count() == 1 {
        dice.iter().sum()
    } else {
        0
    }
}

fn four_of_a_kind(dice: &[u8]) -> u8 {
    for &die in dice {
        if dice.iter().filter(|&&d| d == die).count() >= 4 {
            return die * 4;
        }
    }
    0
}

fn is_yacht(dice: &[u8]) -> bool {
    dice.iter().all(|&d| d == dice[0])
}

fn is_little_straight(dice: &[u8]) -> bool {
    let mut sorted = dice.to_vec();
    sorted.sort_unstable();
    sorted == [1, 2, 3, 4, 5]
}

fn is_big_straight(dice: &[u8]) -> bool {
    let mut sorted = dice.to_vec();
    sorted.sort_unstable();
    sorted == [2, 3, 4, 5, 6]
}
