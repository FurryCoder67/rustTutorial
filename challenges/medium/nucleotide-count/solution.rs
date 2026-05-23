use std::collections::HashMap;

pub fn count(nucleotide: char, dna: &str) -> Result<usize, String> {
    if !"ACGT".contains(nucleotide) {
        return Err(format!("invalid nucleotide: {}", nucleotide));
    }
    if dna.chars().any(|c| !"ACGT".contains(c)) {
        return Err("invalid nucleotide in strand".to_string());
    }
    Ok(dna.chars().filter(|&c| c == nucleotide).count())
}

pub fn nucleotide_counts(dna: &str) -> Result<HashMap<char, usize>, String> {
    if dna.chars().any(|c| !"ACGT".contains(c)) {
        return Err("invalid nucleotide in strand".to_string());
    }
    let mut counts = HashMap::new();
    counts.insert('A', 0);
    counts.insert('C', 0);
    counts.insert('G', 0);
    counts.insert('T', 0);
    for c in dna.chars() {
        *counts.get_mut(&c).unwrap() += 1;
    }
    Ok(counts)
}
