fn nucleotide_index(nucleotide: char) -> Option<usize> {
    match nucleotide {
        'A' => Some(0),
        'C' => Some(1),
        'G' => Some(2),
        'T' => Some(3),
        _ => None,
    }
}

pub fn count(nucleotide: char, dna: &str) -> Result<u32, String> {
    let nucleotide = nucleotide.to_ascii_uppercase();

    if nucleotide_index(nucleotide).is_none() {
        return Err(format!("Invalid nucleotide: {}", nucleotide));
    }

    let mut counts = [0u32; 4];
    for ch in dna.chars() {
        let ch = ch.to_ascii_uppercase();
        match nucleotide_index(ch) {
            Some(index) => counts[index] += 1,
            None => return Err(format!("Invalid DNA nucleotide: {}", ch)),
        }
    }

    Ok(counts[nucleotide_index(nucleotide).unwrap()])
}

pub fn nucleotide_counts(dna: &str) -> Result<[u32; 4], String> {
    let mut counts = [0u32; 4];
    for ch in dna.chars() {
        let ch = ch.to_ascii_uppercase();
        if let Some(index) = nucleotide_index(ch) {
            counts[index] += 1;
        } else {
            return Err(format!("Invalid DNA nucleotide: {}", ch));
        }
    }
    Ok(counts)
}
