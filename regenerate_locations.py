#!/usr/bin/env python3
"""
Regenerate location pages with correct sleep apnea provider data
"""

import os
import json
import re
from collections import defaultdict

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'[\s_]+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

def load_clinics():
    """Load clinic data from JSON"""
    with open('api/clinics.json', 'r') as f:
        data = json.load(f)
    return data['medical_centers']

def group_by_location(clinics):
    """Group clinics by state and city"""
    locations = defaultdict(lambda: defaultdict(list))
    for clinic in clinics:
        state = clinic.get('state', 'Unknown')
        city = clinic.get('city', 'Unknown')
        locations[state][city].append(clinic)
    return locations

def generate_city_page(state, city, clinics, state_slug, city_slug):
    """Generate a city index page with clinic listings"""

    clinic_cards = ""
    schema_items = []

    for i, clinic in enumerate(clinics):
        procedures = clinic.get('procedures_offered', 'Sleep apnea surgery')
        if len(procedures) > 100:
            procedures = procedures[:100] + '...'

        inspire_badge = ""
        if clinic.get('inspire_certified'):
            inspire_badge = '<span class="inline-block bg-green-100 text-green-800 text-xs px-2 py-1 rounded-full ml-2">Inspire Certified</span>'

        clinic_cards += f'''
            <div class="bg-white rounded-xl shadow-md overflow-hidden card-hover">
                <div class="p-6">
                    <div class="flex justify-between items-start mb-3">
                        <h3 class="text-xl font-bold text-slate-900">{clinic['name']}</h3>
                        {inspire_badge}
                    </div>
                    <p class="text-slate-600 text-sm mb-2">{clinic.get('address', '')}</p>
                    <p class="text-slate-500 text-sm mb-3">{clinic.get('specializations', 'Sleep Surgery')}</p>
                    <p class="text-sm text-slate-600 mb-4">{procedures}</p>
                    <div class="flex justify-between items-center">
                        <span class="text-brand-600 font-semibold">{clinic.get('phone', '')}</span>
                        <a href="/locations/{state_slug}/{city_slug}/{clinic['slug']}.html" class="bg-brand-600 text-white px-4 py-2 rounded-lg text-sm hover:bg-brand-700 transition">View Details</a>
                    </div>
                </div>
            </div>
        '''

        schema_items.append({
            "@type": "ListItem",
            "position": i + 1,
            "item": {
                "@type": "MedicalBusiness",
                "name": clinic['name'],
                "address": {
                    "@type": "PostalAddress",
                    "addressLocality": city,
                    "addressRegion": state
                }
            }
        })

    schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": f"Sleep Surgery Clinics in {city}, {state}",
        "numberOfItems": len(clinics),
        "itemListElement": schema_items
    }, indent=2)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sleep Apnea Surgery Clinics in {city}, {state} | SleepApneaMatch.com</title>
    <meta name="description" content="Find {len(clinics)} verified sleep apnea surgery clinics in {city}, {state}. Compare providers, view procedures offered, and connect with sleep surgery specialists.">
    <link rel="canonical" href="https://sleepapneamatch.com/locations/{state_slug}/{city_slug}/">
    <meta property="og:title" content="Sleep Apnea Surgery Clinics in {city}, {state}">
    <meta property="og:description" content="Find {len(clinics)} verified sleep apnea surgery clinics in {city}, {state}.">
    <meta property="og:type" content="website">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            50: '#f0f7ff',
                            100: '#e0effe',
                            600: '#2563eb',
                            700: '#1d4ed8',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .card-hover {{ transition: all 0.3s ease; }}
        .card-hover:hover {{ transform: translateY(-4px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); }}
    </style>
    <script type="application/ld+json">
    {schema_json}
    </script>
</head>
<body class="bg-slate-50">
    <nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <a href="/" class="flex items-center gap-2">
                    <span class="text-xl font-bold tracking-tight text-slate-900">SleepApneaMatch<span class="text-brand-600">.</span></span>
                </a>
                <div class="hidden md:flex space-x-8 text-sm font-semibold text-slate-600">
                    <a href="/" class="hover:text-brand-600 transition">Home</a>
                    <a href="/locations/" class="hover:text-brand-600 transition">Locations</a>
                    <a href="/blog/" class="hover:text-brand-600 transition">Blog</a>
                    <a href="/faq/" class="hover:text-brand-600 transition">FAQ</a>
                </div>
            </div>
        </div>
    </nav>

    <div class="relative h-48 bg-gradient-to-r from-blue-900 to-blue-700">
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex flex-col justify-center">
            <nav class="text-sm text-blue-200 mb-4">
                <a href="/" class="hover:text-white">Home</a>
                <span class="mx-2">/</span>
                <a href="/locations/" class="hover:text-white">Locations</a>
                <span class="mx-2">/</span>
                <a href="/locations/{state_slug}/" class="hover:text-white">{state}</a>
                <span class="mx-2">/</span>
                <span class="text-white">{city}</span>
            </nav>
            <h1 class="text-3xl md:text-4xl font-bold text-white mb-2">Sleep Apnea Surgery in {city}</h1>
            <p class="text-blue-100">{len(clinics)} verified sleep surgery providers</p>
        </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            {clinic_cards}
        </div>
    </div>

    <footer class="bg-slate-900 text-slate-400 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p>&copy; 2026 SleepApneaMatch.com. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>'''
    return html


def generate_state_page(state, cities, state_slug):
    """Generate a state index page"""
    total_clinics = sum(len(clinics) for clinics in cities.values())

    city_cards = ""
    for city, clinics in sorted(cities.items()):
        city_slug = slugify(city)
        city_cards += f'''
            <a href="/locations/{state_slug}/{city_slug}/" class="card-hover bg-white rounded-xl overflow-hidden shadow-md">
                <div class="p-6">
                    <h3 class="text-lg font-bold text-slate-900">{city}</h3>
                    <p class="text-sm text-slate-600">{len(clinics)} Sleep Surgery Provider{"s" if len(clinics) > 1 else ""}</p>
                </div>
            </a>
        '''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sleep Apnea Surgery Clinics in {state} | SleepApneaMatch.com</title>
    <meta name="description" content="Find {total_clinics} verified sleep apnea surgery clinics across {len(cities)} cities in {state}. Compare providers and connect with sleep surgery specialists.">
    <link rel="canonical" href="https://sleepapneamatch.com/locations/{state_slug}/">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            50: '#f0f7ff',
                            100: '#e0effe',
                            600: '#2563eb',
                            700: '#1d4ed8',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .card-hover {{ transition: all 0.3s ease; }}
        .card-hover:hover {{ transform: translateY(-4px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); }}
    </style>
</head>
<body class="bg-slate-50">
    <nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <a href="/" class="flex items-center gap-2">
                    <span class="text-xl font-bold tracking-tight text-slate-900">SleepApneaMatch<span class="text-brand-600">.</span></span>
                </a>
                <div class="hidden md:flex space-x-8 text-sm font-semibold text-slate-600">
                    <a href="/" class="hover:text-brand-600 transition">Home</a>
                    <a href="/locations/" class="hover:text-brand-600 transition">Locations</a>
                    <a href="/blog/" class="hover:text-brand-600 transition">Blog</a>
                    <a href="/faq/" class="hover:text-brand-600 transition">FAQ</a>
                </div>
            </div>
        </div>
    </nav>

    <div class="relative h-48 bg-gradient-to-r from-blue-900 to-blue-700">
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex flex-col justify-center">
            <nav class="text-sm text-blue-200 mb-4">
                <a href="/" class="hover:text-white">Home</a>
                <span class="mx-2">/</span>
                <a href="/locations/" class="hover:text-white">Locations</a>
                <span class="mx-2">/</span>
                <span class="text-white">{state}</span>
            </nav>
            <h1 class="text-3xl md:text-4xl font-bold text-white mb-2">Sleep Apnea Surgery in {state}</h1>
            <p class="text-blue-100">{total_clinics} providers across {len(cities)} cities</p>
        </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <h2 class="text-2xl font-bold text-slate-900 mb-6">Cities in {state}</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {city_cards}
        </div>
    </div>

    <footer class="bg-slate-900 text-slate-400 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p>&copy; 2026 SleepApneaMatch.com. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>'''
    return html


def generate_locations_index(locations):
    """Generate the main locations index page"""
    total_clinics = sum(
        sum(len(clinics) for clinics in cities.values())
        for cities in locations.values()
    )

    state_cards = ""
    for state, cities in sorted(locations.items()):
        state_slug = slugify(state)
        clinic_count = sum(len(clinics) for clinics in cities.values())
        state_cards += f'''
            <a href="/locations/{state_slug}/" class="card-hover bg-white rounded-xl overflow-hidden shadow-md">
                <div class="p-6">
                    <h3 class="text-lg font-bold text-slate-900">{state}</h3>
                    <p class="text-sm text-slate-600">{clinic_count} Providers · {len(cities)} Cities</p>
                </div>
            </a>
        '''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sleep Apnea Surgery Clinics by State | SleepApneaMatch.com</title>
    <meta name="description" content="Find {total_clinics} verified sleep apnea surgery clinics across the United States. Browse by state and connect with sleep surgery specialists.">
    <link rel="canonical" href="https://sleepapneamatch.com/locations/">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        brand: {{
                            50: '#f0f7ff',
                            100: '#e0effe',
                            600: '#2563eb',
                            700: '#1d4ed8',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        .card-hover {{ transition: all 0.3s ease; }}
        .card-hover:hover {{ transform: translateY(-4px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); }}
    </style>
</head>
<body class="bg-slate-50">
    <nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <a href="/" class="flex items-center gap-2">
                    <span class="text-xl font-bold tracking-tight text-slate-900">SleepApneaMatch<span class="text-brand-600">.</span></span>
                </a>
                <div class="hidden md:flex space-x-8 text-sm font-semibold text-slate-600">
                    <a href="/" class="hover:text-brand-600 transition">Home</a>
                    <a href="/locations/" class="text-brand-600 transition">Locations</a>
                    <a href="/blog/" class="hover:text-brand-600 transition">Blog</a>
                    <a href="/faq/" class="hover:text-brand-600 transition">FAQ</a>
                </div>
            </div>
        </div>
    </nav>

    <div class="relative h-48 bg-gradient-to-r from-blue-900 to-blue-700">
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-full flex flex-col justify-center">
            <nav class="text-sm text-blue-200 mb-4">
                <a href="/" class="hover:text-white">Home</a>
                <span class="mx-2">/</span>
                <span class="text-white">Locations</span>
            </nav>
            <h1 class="text-3xl md:text-4xl font-bold text-white mb-2">Sleep Apnea Surgery Directory</h1>
            <p class="text-blue-100">{total_clinics} verified providers across {len(locations)} states</p>
        </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <h2 class="text-2xl font-bold text-slate-900 mb-6">Browse by State</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {state_cards}
        </div>
    </div>

    <footer class="bg-slate-900 text-slate-400 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <p>&copy; 2026 SleepApneaMatch.com. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>'''
    return html


def main():
    print("Loading clinic data...")
    clinics = load_clinics()
    print(f"Loaded {len(clinics)} clinics")

    print("Grouping by location...")
    locations = group_by_location(clinics)
    print(f"Found {len(locations)} states")

    # Delete old location pages
    print("Cleaning up old location pages...")
    os.system("rm -rf locations/*/")

    # Generate locations index
    print("Generating locations index...")
    os.makedirs("locations", exist_ok=True)
    with open("locations/index.html", "w") as f:
        f.write(generate_locations_index(locations))

    # Generate state and city pages
    for state, cities in locations.items():
        state_slug = slugify(state)
        state_dir = f"locations/{state_slug}"
        os.makedirs(state_dir, exist_ok=True)

        print(f"  Generating {state}...")
        with open(f"{state_dir}/index.html", "w") as f:
            f.write(generate_state_page(state, cities, state_slug))

        for city, city_clinics in cities.items():
            city_slug = slugify(city)
            city_dir = f"{state_dir}/{city_slug}"
            os.makedirs(city_dir, exist_ok=True)

            with open(f"{city_dir}/index.html", "w") as f:
                f.write(generate_city_page(state, city, city_clinics, state_slug, city_slug))

    print("Done!")
    print(f"Generated pages for {len(locations)} states")

if __name__ == "__main__":
    main()
