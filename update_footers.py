#!/usr/bin/env python3
"""
Script to apply a universal footer to all HTML pages.
"""

import os
import re
from pathlib import Path

# Universal footer HTML
UNIVERSAL_FOOTER = '''<!-- Footer -->
    <footer class="bg-slate-900">
        <div class="max-w-7xl mx-auto px-4 py-12">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
                <div>
                    <h3 class="text-white font-semibold mb-4">Conditions</h3>
                    <ul class="space-y-2">
                        <li><a href="/knee-cost-guide/" class="text-gray-400 hover:text-blue-400 text-sm">Knee</a></li>
                        <li><a href="/hip-cost-guide/" class="text-gray-400 hover:text-blue-400 text-sm">Hip</a></li>
                        <li><a href="/shoulder-cost-guide/" class="text-gray-400 hover:text-blue-400 text-sm">Shoulder</a></li>
                        <li><a href="/spine-cost-guide/" class="text-gray-400 hover:text-blue-400 text-sm">Spine</a></li>
                        <li><a href="/neck-cost-guide/" class="text-gray-400 hover:text-blue-400 text-sm">Neck</a></li>
                        <li><a href="/si-joint-cost-guide/" class="text-gray-400 hover:text-blue-400 text-sm">SI Joint</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-semibold mb-4">Top Locations</h3>
                    <ul class="space-y-2">
                        <li><a href="/locations/california/los-angeles/" class="text-gray-400 hover:text-blue-400 text-sm">Los Angeles</a></li>
                        <li><a href="/locations/new-york/new-york-city/" class="text-gray-400 hover:text-blue-400 text-sm">New York</a></li>
                        <li><a href="/locations/florida/miami/" class="text-gray-400 hover:text-blue-400 text-sm">Miami</a></li>
                        <li><a href="/locations/texas/houston/" class="text-gray-400 hover:text-blue-400 text-sm">Houston</a></li>
                        <li><a href="/locations/arizona/scottsdale/" class="text-gray-400 hover:text-blue-400 text-sm">Scottsdale</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-semibold mb-4">Mexico</h3>
                    <ul class="space-y-2">
                        <li><a href="/locations/mexico/" class="text-gray-400 hover:text-blue-400 text-sm">All Mexico Clinics</a></li>
                        <li><a href="/locations/mexico/tijuana/" class="text-gray-400 hover:text-blue-400 text-sm">Tijuana</a></li>
                        <li><a href="/locations/mexico/cancun/" class="text-gray-400 hover:text-blue-400 text-sm">Cancun</a></li>
                        <li><a href="/locations/mexico/puerto-vallarta/" class="text-gray-400 hover:text-blue-400 text-sm">Puerto Vallarta</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-semibold mb-4">Company</h3>
                    <ul class="space-y-2">
                        <li><a href="/#cost-guide" class="text-gray-400 hover:text-blue-400 text-sm">Cost Guide</a></li>
                        <li><a href="/locations/" class="text-gray-400 hover:text-blue-400 text-sm">All Locations</a></li>
                        <li><a href="/privacy-policy.html" class="text-gray-400 hover:text-blue-400 text-sm">Privacy Policy</a></li>
                        <li><a href="/terms-of-service.html" class="text-gray-400 hover:text-blue-400 text-sm">Terms of Service</a></li>
                    </ul>
                </div>
            </div>
            <div class="border-t border-gray-800 mt-8 pt-8">
                <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                    <p class="text-gray-400 text-sm">&copy; 2025 StemCellPrices.com. All rights reserved.</p>
                    <p class="text-gray-500 text-xs">The information on this website is for educational purposes only and should not be considered medical advice.</p>
                </div>
            </div>
        </div>
    </footer>'''

def update_footer(filepath):
    """Update footer in a single HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Pattern to match various footer structures
    # Match from <footer or <!-- Footer to </footer>
    footer_patterns = [
        r'<!-- Footer -->.*?</footer>',
        r'<footer[^>]*>.*?</footer>',
    ]

    replaced = False
    for pattern in footer_patterns:
        if re.search(pattern, content, re.DOTALL | re.IGNORECASE):
            content = re.sub(pattern, UNIVERSAL_FOOTER, content, flags=re.DOTALL | re.IGNORECASE)
            replaced = True
            break

    if not replaced:
        return False, "No footer found"

    if content == original_content:
        return False, "No changes needed"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, "Updated"

def main():
    root = Path('.')
    updated = 0
    skipped = 0
    errors = []

    # Find all HTML files
    html_files = list(root.glob('**/*.html'))

    for html_file in html_files:
        # Skip files in hidden directories
        if any(part.startswith('.') for part in html_file.parts):
            continue

        try:
            success, result = update_footer(html_file)
            if success:
                print(f"Updated: {html_file}")
                updated += 1
            else:
                print(f"Skipped: {html_file} - {result}")
                skipped += 1
        except Exception as e:
            errors.append((html_file, str(e)))
            print(f"Error: {html_file} - {e}")

    print(f"\n{'='*50}")
    print(f"Summary: Updated {updated}, Skipped {skipped}, Errors {len(errors)}")

    if errors:
        print("\nErrors:")
        for filepath, error in errors[:10]:
            print(f"  {filepath}: {error}")

if __name__ == '__main__':
    main()
