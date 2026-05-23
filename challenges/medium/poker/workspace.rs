// TODO: Implement your solution

use std::cmp::Ordering;

#[derive(Debug, Clone, Eq, PartialEq, Ord, PartialOrd)]
enum HandRank {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    Straight,
    Flush,
    FullHouse,
    FourOfAKind,
    StraightFlush,
    RoyalFlush,
}

pub fn winning_hands(hands: &[&str]) -> Vec<&str> { {
    todo!()
}
