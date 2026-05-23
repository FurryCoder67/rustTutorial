#!/usr/bin/env python3
"""
Populate all solution.rs and workspace.rs files with proper implementations.
"""

import os
from solutions_dict import EXERCISM_SOLUTIONS

def populate_solutions():
    """Populate all exercise files with solutions from the dictionary."""
    root = "."
    updated_count = 0
    
    for difficulty in ['easy', 'medium', 'hard']:
        diff_dir = os.path.join(root, difficulty)
        if not os.path.isdir(diff_dir):
            continue
            
        for exercise_name in os.listdir(diff_dir):
            exercise_dir = os.path.join(diff_dir, exercise_name)
            if not os.path.isdir(exercise_dir):
                continue
            
            solution_path = os.path.join(exercise_dir, "solution.rs")
            workspace_path = os.path.join(exercise_dir, "workspace.rs")
            
            # Get solution code
            solution_code = EXERCISM_SOLUTIONS.get(exercise_name)
            
            if solution_code:
                # Write solution
                with open(solution_path, 'w', encoding='utf-8') as f:
                    f.write(solution_code + "\n")
                
                # Write workspace stub
                with open(workspace_path, 'w', encoding='utf-8') as f:
                    # Extract function signatures from solution for the stub
                    lines = solution_code.split('\n')
                    stub_lines = []
                    for line in lines:
                        if line.startswith('pub fn') or line.startswith('pub struct') or line.startswith('pub enum'):
                            # For functions, add the signature and todo!()
                            if 'pub fn' in line and '{' in line:
                                # Single-line function
                                fn_sig = line[:line.index('{')].strip()
                                stub_lines.append(fn_sig + " {\n    todo!()\n}")
                            else:
                                # Multi-line, find the opening brace
                                stub_lines.append(line)
                                if '{' not in line:
                                    # Need to keep reading for the brace
                                    continue
                                else:
                                    stub_lines.append("    todo!()\n}")
                        elif '// ' in line:
                            stub_lines.append(line)
                    
                    # Simpler approach: add todo!() to the first function
                    if 'pub fn' in solution_code:
                        stub = "// TODO: Implement your solution\n\n"
                        for line in lines:
                            if line.strip().startswith('pub fn'):
                                # Add todo!() implementation
                                stub += line + " {\n    todo!()\n}\n"
                                break
                            else:
                                stub += line + "\n" if line.strip() else "\n"
                        f.write(stub)
                    else:
                        f.write("// TODO: Implement your solution\npub fn solution() {}\n")
                
                updated_count += 1
                print(f"✓ {difficulty}/{exercise_name}")
            else:
                print(f"- {difficulty}/{exercise_name} (no solution found)")
    
    print(f"\nUpdated {updated_count} exercises")

if __name__ == '__main__':
    populate_solutions()
