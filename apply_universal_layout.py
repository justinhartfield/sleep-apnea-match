#!/usr/bin/env python3
"""
Apply universal header and footer to all HTML pages for consistent branding.
"""

import os
import re
from pathlib import Path

# Universal Navigation HTML
UNIVERSAL_NAV = '''    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200" x-data="{ mobileMenu: false }">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <a href="/" class="flex items-center gap-2">
                    <div class="w-8 h-8 rounded-lg bg-brand-600 flex items-center justify-center">
                        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>
                        </svg>
                    </div>
                    <span class="text-xl font-bold tracking-tight text-slate-900">SleepApneaMatch<span class="text-brand-600">.</span></span>
                </a>

                <div class="hidden md:flex space-x-8 text-sm font-semibold text-slate-600">
                    <a href="/" class="hover:text-brand-600 transition">Find Providers</a>
                    <a href="/guides/" class="hover:text-brand-600 transition">Guides</a>
                    <a href="/blog/" class="hover:text-brand-600 transition">Blog</a>
                    <a href="/patient-journey/" class="hover:text-brand-600 transition">Patient Journey</a>
                    <div class="nav-dropdown-container">
                        <a href="/locations/" class="hover:text-brand-600 transition inline-flex items-center gap-1">
                            Locations
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </a>
                        <div class="nav-dropdown-menu">
                            <a href="/locations/" class="font-bold text-brand-600">View All Locations &rarr;</a>
                            <div class="h-px bg-slate-100 my-2"></div>
                            <a href="/locations/california/">California</a>
                            <a href="/locations/new-york/">New York</a>
                            <a href="/locations/texas/">Texas</a>
                            <a href="/locations/pennsylvania/">Pennsylvania</a>
                            <a href="/locations/illinois/">Illinois</a>
                            <a href="/locations/massachusetts/">Massachusetts</a>
                        </div>
                    </div>
                    <a href="/faq/" class="hover:text-brand-600 transition">FAQ</a>
                </div>

                <div class="hidden md:flex items-center gap-4">
                    <a href="/#consultation" class="bg-brand-600 text-white px-4 py-2 rounded-lg font-semibold text-sm hover:bg-brand-700 transition">
                        Get Matched
                    </a>
                </div>

                <!-- Mobile menu button -->
                <button @click="mobileMenu = !mobileMenu" class="md:hidden p-2">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>

            <!-- Mobile menu -->
            <div x-show="mobileMenu" x-cloak class="md:hidden py-4 border-t border-slate-200">
                <a href="/" class="block py-2 text-slate-600 font-medium">Find Providers</a>
                <a href="/guides/" class="block py-2 text-slate-600 font-medium">Guides</a>
                <a href="/blog/" class="block py-2 text-slate-600 font-medium">Blog</a>
                <a href="/patient-journey/" class="block py-2 text-slate-600 font-medium">Patient Journey</a>
                <a href="/locations/" class="block py-2 text-slate-600 font-medium">Locations</a>
                <a href="/faq/" class="block py-2 text-slate-600 font-medium">FAQ</a>
                <a href="/#consultation" class="block mt-4 bg-brand-600 text-white text-center py-2 rounded-lg font-semibold">Get Matched</a>
            </div>
        </div>
    </nav>'''

# Universal Footer HTML
UNIVERSAL_FOOTER = '''    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-4 gap-8 mb-12">
                <div>
                    <div class="flex items-center gap-2 mb-4">
                        <div class="w-8 h-8 rounded-lg bg-brand-600 flex items-center justify-center">
                            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>
                            </svg>
                        </div>
                        <span class="text-xl font-bold text-white">SleepApneaMatch</span>
                    </div>
                    <p class="text-sm">
                        Compare sleep apnea surgery costs and find verified providers. Medically reviewed by Dr. Igor I. Bussel, MD.
                    </p>
                </div>

                <div>
                    <h4 class="text-white font-semibold mb-4">Procedures</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/uppp-cost-guide/" class="hover:text-white transition">UPPP</a></li>
                        <li><a href="/inspire-cost-guide/" class="hover:text-white transition">Inspire Therapy</a></li>
                        <li><a href="/mma-cost-guide/" class="hover:text-white transition">MMA Surgery</a></li>
                        <li><a href="/septoplasty-cost-guide/" class="hover:text-white transition">Septoplasty</a></li>
                        <li><a href="/turbinate-reduction-cost-guide/" class="hover:text-white transition">Turbinate Reduction</a></li>
                        <li><a href="/tonsillectomy-cost-guide/" class="hover:text-white transition">Tonsillectomy</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-white font-semibold mb-4">Top Locations</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/locations/california/" class="hover:text-white transition">California</a></li>
                        <li><a href="/locations/new-york/" class="hover:text-white transition">New York</a></li>
                        <li><a href="/locations/texas/" class="hover:text-white transition">Texas</a></li>
                        <li><a href="/locations/pennsylvania/" class="hover:text-white transition">Pennsylvania</a></li>
                        <li><a href="/locations/ohio/" class="hover:text-white transition">Ohio</a></li>
                        <li><a href="/locations/" class="hover:text-white transition">All Locations &rarr;</a></li>
                    </ul>
                </div>

                <div>
                    <h4 class="text-white font-semibold mb-4">Resources</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/guides/" class="hover:text-white transition">Guides</a></li>
                        <li><a href="/blog/" class="hover:text-white transition">Blog</a></li>
                        <li><a href="/patient-journey/" class="hover:text-white transition">Patient Journey</a></li>
                        <li><a href="/faq/" class="hover:text-white transition">FAQ</a></li>
                    </ul>
                </div>
            </div>

            <div class="border-t border-slate-800 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
                <p class="text-sm">
                    &copy; 2026 SleepApneaMatch.com. All rights reserved.
                </p>
                <p class="text-xs text-slate-500">
                    Medical information is reviewed by Dr. Igor I. Bussel, MD. This site does not provide medical advice.
                </p>
            </div>
        </div>
    </footer>'''

# Required CSS styles for nav dropdown (to be added if not present)
NAV_DROPDOWN_CSS = '''        /* Navigation Dropdown */
        .nav-dropdown-container { position: relative; }
        .nav-dropdown-container:hover .nav-dropdown-menu {
            display: block;
            opacity: 1;
            visibility: visible;
            transform: translateY(0);
        }
        .nav-dropdown-menu {
            display: none;
            position: absolute;
            top: 100%;
            left: 0;
            min-width: 220px;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.15);
            padding: 8px 0;
            z-index: 1000;
            opacity: 0;
            visibility: hidden;
            transform: translateY(-10px);
            transition: all 0.2s ease;
        }
        .nav-dropdown-menu::before {
            content: '';
            position: absolute;
            top: -10px;
            left: 0;
            right: 0;
            height: 10px;
        }
        .nav-dropdown-menu a {
            display: block;
            padding: 8px 16px;
            color: #475569;
            font-size: 14px;
            transition: background 0.2s;
        }
        .nav-dropdown-menu a:hover {
            background: #f1f5f9;
        }
        [x-cloak] { display: none !important; }'''

# Brand colors Tailwind config
BRAND_COLORS_CONFIG = '''        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'system-ui', 'sans-serif'],
                    },
                    colors: {
                        brand: {
                            50: '#f0f7ff',
                            100: '#e0effe',
                            200: '#bae0fd',
                            400: '#60a5fa',
                            600: '#2563eb',
                            700: '#1d4ed8',
                            800: '#1e40af',
                            900: '#1e3a8a',
                        }
                    }
                }
            }
        }'''


def find_html_files(root_dir):
    """Find all HTML files in the project."""
    html_files = []
    skip_dirs = {'node_modules', '.git', '.netlify', '.claude'}

    for root, dirs, files in os.walk(root_dir):
        # Skip certain directories
        dirs[:] = [d for d in dirs if d not in skip_dirs]

        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    return html_files


def update_html_file(filepath):
    """Update an HTML file with universal header and footer."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return False

    original_content = content

    # Skip index.html at root (it's the template source)
    if filepath.endswith('/index.html') and filepath.count('/') <= 6:
        # Check if it's the root index.html
        if 'sleep-apnea-match/index.html' in filepath and '/blog/' not in filepath and '/guides/' not in filepath and '/locations/' not in filepath and '/faq/' not in filepath and '/patient-journey/' not in filepath:
            print(f"Skipping root index.html: {filepath}")
            return False

    # Replace navigation
    # Pattern to match nav elements
    nav_patterns = [
        r'<!-- Navigation -->.*?</nav>',
        r'<nav[^>]*>.*?</nav>',
    ]

    for pattern in nav_patterns:
        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, UNIVERSAL_NAV, content, count=1, flags=re.DOTALL)
            break

    # Replace footer
    footer_pattern = r'<!-- Footer -->.*?</footer>|<footer[^>]*>.*?</footer>'
    if re.search(footer_pattern, content, re.DOTALL):
        content = re.sub(footer_pattern, UNIVERSAL_FOOTER, content, count=1, flags=re.DOTALL)

    # Ensure Alpine.js is included
    if 'alpinejs' not in content and 'alpine' not in content.lower():
        # Add Alpine.js before </head>
        alpine_script = '    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>\n'
        content = content.replace('</head>', alpine_script + '</head>')

    # Ensure nav dropdown CSS is present
    if 'nav-dropdown-container' not in content or '.nav-dropdown-menu' not in content:
        # Add CSS before </style> or before </head>
        if '</style>' in content:
            content = content.replace('</style>', NAV_DROPDOWN_CSS + '\n    </style>')
        elif '<style>' in content:
            # Find the last </style> and add before it
            pass
        else:
            # Add a style block before </head>
            style_block = f'    <style>\n{NAV_DROPDOWN_CSS}\n    </style>\n'
            content = content.replace('</head>', style_block + '</head>')

    # Ensure brand colors are configured in Tailwind
    if 'brand-600' in content and 'brand:' not in content:
        # Need to add brand colors to tailwind config
        if 'tailwind.config' in content:
            # Already has config, try to update it
            pass
        else:
            # Add config after tailwindcss script
            if 'tailwindcss' in content or 'cdn.tailwindcss.com' in content:
                config_script = f'\n    <script>\n{BRAND_COLORS_CONFIG}\n    </script>'
                # Add after tailwind script
                content = re.sub(
                    r'(<script src="https://cdn\.tailwindcss\.com"></script>)',
                    r'\1' + config_script,
                    content
                )

    # Only write if content changed
    if content != original_content:
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filepath}")
            return True
        except Exception as e:
            print(f"Error writing {filepath}: {e}")
            return False
    else:
        print(f"No changes: {filepath}")
        return False


def main():
    """Main function to apply universal layout to all pages."""
    root_dir = os.getcwd()

    print("Finding HTML files...")
    html_files = find_html_files(root_dir)
    print(f"Found {len(html_files)} HTML files")

    updated_count = 0
    for filepath in html_files:
        if update_html_file(filepath):
            updated_count += 1

    print(f"\nUpdated {updated_count} files")


if __name__ == '__main__':
    main()
