#!/usr/bin/env python3
"""
Script to add Alpine.js to Mexico clinic pages that are missing it.
"""

import os
from pathlib import Path

ALPINE_SCRIPT = '    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>\n'

def fix_mexico_clinic(filepath):
    """Add Alpine.js to a Mexico clinic file if missing"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if Alpine.js is already included
    if 'alpinejs' in content:
        return False, "Already has Alpine.js"

    # Add Alpine.js after Tailwind CSS
    if '<script src="https://cdn.tailwindcss.com"></script>' in content:
        content = content.replace(
            '<script src="https://cdn.tailwindcss.com"></script>',
            '<script src="https://cdn.tailwindcss.com"></script>\n' + ALPINE_SCRIPT.rstrip()
        )
    else:
        return False, "Tailwind not found"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, "Added Alpine.js"

def main():
    mexico_dir = Path('locations/mexico')
    updated = 0
    skipped = 0

    for city_dir in mexico_dir.iterdir():
        if not city_dir.is_dir():
            continue

        for html_file in city_dir.glob('*.html'):
            if html_file.name == 'index.html':
                continue

            success, result = fix_mexico_clinic(html_file)
            if success:
                print(f"Updated: {html_file}")
                updated += 1
            else:
                print(f"Skipped: {html_file} - {result}")
                skipped += 1

    print(f"\n{'='*50}")
    print(f"Summary: Updated {updated}, Skipped {skipped}")

if __name__ == '__main__':
    main()
