#!/usr/bin/env python3
"""
Auto-update script for LeetCode Daily README.md
Scans solution files and updates the README with current progress.
"""

import os
import re
from datetime import datetime
from pathlib import Path

# Problem number mapping for common LeetCode problems
PROBLEM_MAP = {
    'contains_duplicate': {'number': 217, 'name': 'Contains Duplicate', 'difficulty': 'Easy'},
    'valid_anagrams': {'number': 242, 'name': 'Valid Anagram', 'difficulty': 'Easy'},
    'two_sum': {'number': 1, 'name': 'Two Sum', 'difficulty': 'Easy'},
    'grooup_anagrams': {'number': 49, 'name': 'Group Anagrams', 'difficulty': 'Medium'},
    'group_anagrams': {'number': 49, 'name': 'Group Anagrams', 'difficulty': 'Medium'},
    'top_k_frequent_elements': {'number': 347, 'name': 'Top K Frequent Elements', 'difficulty': 'Medium'},
}

def get_category_folders():
    """Get all category folders in the repository."""
    base_path = Path(__file__).parent
    folders = []
    
    for item in base_path.iterdir():
        if item.is_dir() and not item.name.startswith('.') and not item.name.startswith('__'):
            # Check if folder contains Python files
            if any(item.glob('*.py')):
                folders.append(item.name)
    
    return sorted(folders)

def scan_solutions(category):
    """Scan all solution files in a category folder."""
    base_path = Path(__file__).parent / category
    solutions = []
    
    if not base_path.exists():
        return solutions
    
    for file in base_path.glob('*.py'):
        filename = file.stem
        
        # Get problem info from mapping or use defaults
        if filename in PROBLEM_MAP:
            problem_info = PROBLEM_MAP[filename].copy()
        else:
            # Try to extract problem number from filename if it starts with a number
            match = re.match(r'^(\d+)', filename)
            if match:
                problem_number = int(match.group(1))
                problem_name = filename.replace(match.group(1), '').strip('_- ').replace('_', ' ').title()
            else:
                problem_number = 0
                problem_name = filename.replace('_', ' ').title()
            
            problem_info = {
                'number': problem_number,
                'name': problem_name,
                'difficulty': 'Unknown'
            }
        
        problem_info['file'] = f"{category}/{file.name}"
        solutions.append(problem_info)
    
    # Sort by problem number
    solutions.sort(key=lambda x: (x['number'] == 0, x['number'], x['name']))
    
    return solutions

def generate_problem_table(category, solutions):
    """Generate markdown table for problems."""
    if not solutions:
        return "No problems yet.\n"
    
    table = "| # | Problem | Solution | Difficulty |\n"
    table += "|---|---------|----------|------------|\n"
    
    for sol in solutions:
        number = sol['number'] if sol['number'] != 0 else '-'
        table += f"| {number} | {sol['name']} | [Python]({sol['file']}) | {sol['difficulty']} |\n"
    
    return table

def update_readme():
    """Update the README.md file with current solutions."""
    readme_path = Path(__file__).parent / 'README.md'
    
    if not readme_path.exists():
        print("README.md not found!")
        return
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Scan all categories
    categories = get_category_folders()
    total_problems = 0
    category_stats = {}
    
    for category in categories:
        solutions = scan_solutions(category)
        category_stats[category] = len(solutions)
        total_problems += len(solutions)
        
        # Update category section
        category_key = category.replace(' ', '_')
        start_marker = f"<!-- PROBLEMS_START:{category_key} -->"
        end_marker = f"<!-- PROBLEMS_END:{category_key} -->"
        
        if start_marker in content and end_marker in content:
            table = generate_problem_table(category, solutions)
            pattern = f"{re.escape(start_marker)}.*?{re.escape(end_marker)}"
            replacement = f"{start_marker}\n{table}{end_marker}"
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Update stats section
    stats_start = "<!-- STATS_START -->"
    stats_end = "<!-- STATS_END -->"
    
    if stats_start in content and stats_end in content:
        stats_text = f"- **Total Problems Solved:** {total_problems}\n"
        for category, count in category_stats.items():
            category_display = category.replace('_and_', ' & ').replace('_', ' ')
            stats_text += f"- **{category_display}:** {count}\n"
        
        pattern = f"{re.escape(stats_start)}.*?{re.escape(stats_end)}"
        replacement = f"{stats_start}\n{stats_text}{stats_end}"
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Update badge
    badge_pattern = r'!\[Problems Solved\]\(https://img\.shields\.io/badge/Problems%20Solved-\d+-brightgreen\)'
    badge_replacement = f'![Problems Solved](https://img.shields.io/badge/Problems%20Solved-{total_problems}-brightgreen)'
    content = re.sub(badge_pattern, badge_replacement, content)
    
    # Update last updated date
    current_date = datetime.now().strftime("%B %d, %Y")
    date_badge_pattern = r'!\[Last Updated\]\(https://img\.shields\.io/badge/Last%20Updated-[^)]+\)'
    date_badge_replacement = f'![Last Updated](https://img.shields.io/badge/Last%20Updated-{current_date.replace(" ", "%20").replace(",", "%2C")}-blue)'
    content = re.sub(date_badge_pattern, date_badge_replacement, content)
    
    # Update footer date
    footer_pattern = r'\*Last auto-updated: .*?\*'
    footer_replacement = f'*Last auto-updated: {current_date}*'
    content = re.sub(footer_pattern, footer_replacement, content)
    
    # Write updated content
    with open(readme_path, 'w') as f:
        f.write(content)
    
    print(f"✅ README updated successfully!")
    print(f"📊 Total problems: {total_problems}")
    for category, count in category_stats.items():
        print(f"   - {category}: {count}")

if __name__ == '__main__':
    update_readme()
