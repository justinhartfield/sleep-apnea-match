#!/usr/bin/env python3
"""
Script to update Mexico clinic pages to use city background images
instead of the teal gradient.
"""

import os
import re
from pathlib import Path

# Map city directories to their image files
CITY_IMAGES = {
    'cancun': '/assets/images/cities/cancun.jpg',
    'tijuana': '/assets/images/cities/tijuana.jpg',
    'puerto-vallarta': '/assets/images/cities/puerto-vallarta.jpg',
}

# Old pattern: green gradient hero section
OLD_HERO_PATTERN = r'<section class="relative bg-gradient-to-r from-teal-600 to-teal-800 text-white py-16">'

def get_new_hero_html(city_image):
    """Generate the new hero section with background image"""
    return f'''<section class="relative bg-cover bg-center text-white py-16" style="background-image: url('{city_image}');">
        <div class="absolute inset-0 bg-gradient-to-r from-teal-900/90 to-teal-700/80"></div>
        <div class="relative">'''

# We also need to close the extra div we added
OLD_CONTENT_START = r'(<section class="relative bg-cover bg-center text-white py-16"[^>]*>)\s*<div class="absolute inset-0[^>]*></div>\s*<div class="relative">\s*<div class="max-w-7xl'

def update_mexico_clinic(filepath):
    """Update a single Mexico clinic file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already updated
    if 'bg-cover bg-center' in content and 'cities/' in content:
        return False, "Already updated"

    # Check for old pattern
    if not re.search(OLD_HERO_PATTERN, content):
        return False, "No matching hero pattern"

    # Determine city from filepath
    city = filepath.parent.name
    if city not in CITY_IMAGES:
        return False, f"Unknown city: {city}"

    city_image = CITY_IMAGES[city]

    # Replace the hero section opening
    new_hero = f'''<section class="relative bg-cover bg-center text-white py-16" style="background-image: url('{city_image}');">
        <div class="absolute inset-0 bg-gradient-to-r from-teal-900/90 to-teal-700/80"></div>
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">'''

    # Replace opening section and the inner div
    content = re.sub(
        r'<section class="relative bg-gradient-to-r from-teal-600 to-teal-800 text-white py-16">\s*<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">',
        new_hero,
        content
    )

    # Find the closing </section> for the hero and add closing </div> before it
    # The hero section ends after the price/contact info
    # We need to close the extra "relative" div we added

    # Find pattern: </div>\s*</section>\s*<!-- Main Content -->
    content = re.sub(
        r'(</div>\s*)(</section>\s*<!-- Main Content -->)',
        r'\1        </div>\n    \2',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, city

def main():
    mexico_dir = Path('locations/mexico')
    updated = 0
    skipped = 0
    errors = []

    for city_dir in mexico_dir.iterdir():
        if not city_dir.is_dir():
            continue

        for html_file in city_dir.glob('*.html'):
            if html_file.name == 'index.html':
                continue

            try:
                success, result = update_mexico_clinic(html_file)
                if success:
                    print(f"Updated: {html_file} (city: {result})")
                    updated += 1
                else:
                    print(f"Skipped: {html_file} - {result}")
                    skipped += 1
            except Exception as e:
                errors.append((html_file, str(e)))
                print(f"Error: {html_file} - {e}")

    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Updated: {updated} files")
    print(f"  Skipped: {skipped} files")
    print(f"  Errors: {len(errors)} files")

if __name__ == '__main__':
    main()
