pub fn to_rna(dna: &str) -> Result<String, String> {
    dna.chars()
        .map(|c| match c {
            'G' => Ok('C'),
            'C' => Ok('G'),
            'T' => Ok('A'),
            'A' => Ok('U'),
            _ => Err(format!("invalid dna nucleotide: {}", c)),
        })
        .collect()
}
