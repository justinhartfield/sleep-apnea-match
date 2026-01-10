#!/usr/bin/env python3
"""
Script to update all pages with a consistent navigation menu.
Uses the index.html nav as template but converts to static links.
"""

import os
import re
from pathlib import Path

# Universal navigation HTML (static version for non-SPA pages)
UNIVERSAL_NAV = '''<nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200" x-data="{ mobileMenu: false, locationsOpen: false }">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <a href="/" class="flex items-center gap-2">
                    <img src="/assets/images/logo-icon.png" alt="StemCellPrices.com" class="w-8 h-8 rounded-lg">
                    <span class="text-xl font-bold tracking-tight text-slate-900">StemCellPrices.com<span class="text-brand-600">.</span></span>
                </a>
                <div class="hidden md:flex space-x-8 text-sm font-semibold text-slate-600">
                    <a href="/" class="hover:text-brand-600 transition">Find Clinics</a>
                    <a href="/#cost-guide" class="hover:text-brand-600 transition">Cost Guide</a>
                    <a href="/conditions/" class="hover:text-brand-600 transition">Conditions</a>
                    <div class="relative" @mouseenter="locationsOpen = true" @mouseleave="locationsOpen = false">
                        <a href="/locations/" class="hover:text-brand-600 transition inline-flex items-center gap-1">Locations <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg></a>
                        <div x-show="locationsOpen" x-cloak class="absolute top-full left-0 pt-0 w-64 bg-white rounded-xl shadow-xl border border-slate-200 py-2 z-50 max-h-96 overflow-y-auto">
                            <a href="/locations/" class="block px-4 py-2 text-sm font-bold text-brand-600 hover:bg-brand-50">View All 30 States &rarr;</a>
                            <div class="border-t border-slate-100 my-2"></div>
                            <a href="/locations/california/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-brand-50 hover:text-brand-600">California</a>
                            <a href="/locations/texas/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-brand-50 hover:text-brand-600">Texas</a>
                            <a href="/locations/florida/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-brand-50 hover:text-brand-600">Florida</a>
                            <a href="/locations/new-york/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-brand-50 hover:text-brand-600">New York</a>
                            <a href="/locations/arizona/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-brand-50 hover:text-brand-600">Arizona</a>
                            <a href="/locations/colorado/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-brand-50 hover:text-brand-600">Colorado</a>
                            <a href="/locations/illinois/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-brand-50 hover:text-brand-600">Illinois</a>
                            <a href="/locations/georgia/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-brand-50 hover:text-brand-600">Georgia</a>
                            <a href="/locations/washington/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-brand-50 hover:text-brand-600">Washington</a>
                            <a href="/locations/massachusetts/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-brand-50 hover:text-brand-600">Massachusetts</a>
                            <div class="border-t border-slate-100 my-2"></div>
                            <p class="px-4 py-1 text-xs text-slate-400 uppercase tracking-wider">International</p>
                            <a href="/locations/mexico/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-brand-50 hover:text-brand-600">Mexico</a>
                        </div>
                    </div>
                </div>
                <div class="flex items-center gap-4">
                    <a href="/#clinic-login" class="hidden sm:block text-sm font-bold text-brand-700 bg-brand-50 px-4 py-2 rounded-full hover:bg-brand-100 transition">Clinic Login</a>
                    <button class="md:hidden p-2" @click="mobileMenu = !mobileMenu">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                    </button>
                </div>
            </div>
            <div x-show="mobileMenu" x-cloak class="md:hidden py-4 border-t border-slate-100">
                <div class="flex flex-col space-y-3">
                    <a href="/" class="px-4 py-2 text-sm font-semibold text-slate-600 hover:bg-brand-50 rounded-lg">Find Clinics</a>
                    <a href="/#cost-guide" class="px-4 py-2 text-sm font-semibold text-slate-600 hover:bg-brand-50 rounded-lg">Cost Guide</a>
                    <a href="/conditions/" class="px-4 py-2 text-sm font-semibold text-slate-600 hover:bg-brand-50 rounded-lg">Conditions</a>
                    <a href="/locations/" class="px-4 py-2 text-sm font-semibold text-slate-600 hover:bg-brand-50 rounded-lg">Locations</a>
                </div>
            </div>
        </div>
    </nav>'''

# Patterns to match various existing nav structures
NAV_PATTERNS = [
    # Pattern for pages with <nav...>...</nav> structure
    r'<nav\s+class="[^"]*(?:sticky|bg-white)[^"]*"[^>]*>.*?</nav>',
    # Pattern for header with nav inside
    r'<header[^>]*>.*?<nav[^>]*>.*?</nav>.*?</header>',
]

def needs_alpine(content):
    """Check if the page needs Alpine.js added"""
    return 'alpinejs' not in content.lower()

def needs_tailwind_config(content):
    """Check if page needs brand color config"""
    return 'brand-600' in UNIVERSAL_NAV and 'brand:' not in content

ALPINE_SCRIPT = '<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>'

TAILWIND_CONFIG = '''<script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            50: '#f0f7ff',
                            100: '#e0effe',
                            600: '#2563eb',
                            700: '#1d4ed8',
                        }
                    }
                }
            }
        }
    </script>'''

def update_page(filepath):
    """Update a single page with the universal nav"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip index.html - it has the SPA version
    if filepath.name == 'index.html' and filepath.parent.name == 'stem cells':
        return False, "Skipped (main index.html)"

    original_content = content

    # Try to find and replace existing nav
    # First try: look for <nav> that's a direct child of body or after header
    nav_match = re.search(r'(<body[^>]*>.*?)(<nav\s+class="[^"]*(?:bg-white|sticky|shadow)[^"]*".*?</nav>)', content, re.DOTALL)

    if nav_match:
        # Replace the nav
        before_nav = nav_match.group(1)
        content = content[:nav_match.start(2)] + UNIVERSAL_NAV + content[nav_match.end(2):]
    else:
        # Try header pattern
        header_match = re.search(r'<header[^>]*>.*?</header>', content, re.DOTALL)
        if header_match:
            content = content[:header_match.start()] + UNIVERSAL_NAV + content[header_match.end():]
        else:
            # Try simple nav pattern
            simple_nav = re.search(r'<nav[^>]*>.*?</nav>', content, re.DOTALL)
            if simple_nav:
                content = content[:simple_nav.start()] + UNIVERSAL_NAV + content[simple_nav.end():]
            else:
                return False, "No nav found"

    # Add Alpine.js if needed
    if needs_alpine(content):
        if '</head>' in content:
            content = content.replace('</head>', f'    {ALPINE_SCRIPT}\n</head>')

    # Add Tailwind brand colors if needed
    if needs_tailwind_config(content):
        if '<script src="https://cdn.tailwindcss.com"></script>' in content:
            content = content.replace(
                '<script src="https://cdn.tailwindcss.com"></script>',
                f'<script src="https://cdn.tailwindcss.com"></script>\n    {TAILWIND_CONFIG}'
            )

    # Add x-cloak style if not present
    if 'x-cloak' in content and '[x-cloak]' not in content:
        if '<style>' in content:
            content = content.replace('<style>', '<style>\n        [x-cloak] { display: none !important; }')
        elif '</head>' in content:
            content = content.replace('</head>', '    <style>[x-cloak] { display: none !important; }</style>\n</head>')

    if content == original_content:
        return False, "No changes made"

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

    # Exclude certain files
    exclude = ['index.html']  # Main index has SPA nav

    for html_file in html_files:
        # Skip the main index.html
        if html_file.name == 'index.html' and html_file.parent == root:
            print(f"Skipped: {html_file} (main SPA page)")
            skipped += 1
            continue

        try:
            success, result = update_page(html_file)
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

if __name__ == '__main__':
    main()
