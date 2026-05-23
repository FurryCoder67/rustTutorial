use std::collections::HashMap;
use std::sync::{Arc, Mutex};
use std::thread;

pub fn frequency(input: &[&str], worker_count: usize) -> HashMap<char, usize> {
    let result = Arc::new(Mutex::new(HashMap::new()));
    let mut handles = vec![];
    
    for text in input {
        let result_clone = Arc::clone(&result);
        let text_clone = text.to_string();
        
        let handle = thread::spawn(move || {
            let local_freq = text_clone
                .to_lowercase()
                .chars()
                .filter(|c| c.is_alphabetic())
                .fold(HashMap::new(), |mut map, ch| {
                    *map.entry(ch).or_insert(0) += 1;
                    map
                });
            
            let mut global = result_clone.lock().unwrap();
            for (ch, count) in local_freq {
                *global.entry(ch).or_insert(0) += count;
            }
        });
        
        handles.push(handle);
    }
    
    for handle in handles {
        handle.join().unwrap();
    }
    
    Arc::try_unwrap(result).unwrap().into_inner().unwrap()
}
