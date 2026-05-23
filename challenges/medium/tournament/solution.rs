use std::collections::HashMap;

pub fn tally(match_results: &str) -> String {
    let mut teams: HashMap<String, (u32, u32, u32)> = HashMap::new();
    
    for line in match_results.lines() {
        let parts: Vec<&str> = line.split(';').collect();
        if parts.len() != 3 { continue; }
        
        let team1 = parts[0].trim().to_string();
        let team2 = parts[1].trim().to_string();
        let result = parts[2].trim();
        
        teams.entry(team1.clone()).or_insert((0, 0, 0));
        teams.entry(team2.clone()).or_insert((0, 0, 0));
        
        match result {
            "win" => {
                let e = teams.get_mut(&team1).unwrap();
                e.0 += 3; e.2 += 1;
            },
            "loss" => {
                let e = teams.get_mut(&team2).unwrap();
                e.0 += 3; e.2 += 1;
            },
            "draw" => {
                let e1 = teams.get_mut(&team1).unwrap();
                e1.0 += 1; e1.1 += 1;
                let e2 = teams.get_mut(&team2).unwrap();
                e2.0 += 1; e2.1 += 1;
            },
            _ => {}
        }
    }
    
    let mut sorted: Vec<_> = teams.iter().collect();
    sorted.sort_by(|a, b| {
        b.1.0.cmp(&a.1.0).then_with(|| a.0.cmp(&b.0))
    });
    
    let mut result = String::from("Team                           | MP |  W |  D |  L |  P
");
    result.push_str("-".repeat(60).as_str());
    
    for (team, (pts, draws, wins)) in sorted {
        let mp = wins + draws + (teams[team].2 - wins - draws);
        result.push_str(&format!(
            "
{:<30} | {:2} | {:2} | {:2} | {:2} | {:2}",
            team, mp, wins, draws, mp - wins - draws, pts
        ));
    }
    
    result
}
