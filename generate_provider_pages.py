#!/usr/bin/env python3
"""
Generate provider pages for SleepApneaMatch.com from JSON data.
"""

import json
import os
from pathlib import Path

BASE_DIR = Path("/Users/tang/Projects/sleep-apnea-match")
API_DIR = BASE_DIR / "api"
LOCATIONS_DIR = BASE_DIR / "locations"

def slugify(text):
    """Convert text to URL-friendly slug."""
    return text.lower().replace(' ', '-').replace(',', '').replace('.', '').replace("'", '').replace('&', 'and').replace('(', '').replace(')', '')

def generate_provider_page(provider, provider_type):
    """Generate HTML for a single provider page."""
    name = provider.get('name', 'Unknown Provider')
    city = provider.get('city', '')
    state = provider.get('state', '')
    address = provider.get('address', '')
    phone = provider.get('phone', '')
    website = provider.get('website', '')

    specializations = provider.get('specializations', '')
    procedures = provider.get('procedures_offered', '')
    key_surgeons = provider.get('key_surgeons', '') if provider_type == 'medical_center' else provider.get('lead_surgeon', '')
    inspire_certified = provider.get('inspire_certified', False)
    notes = provider.get('notes', '') if provider_type == 'medical_center' else provider.get('notable_achievements', '')
    insurance = provider.get('insurance_accepted', '')

    inspire_badge = '''<span class="bg-green-50 text-green-700 px-3 py-1 rounded-full text-sm font-medium">Inspire Certified</span>''' if inspire_certified else ''

    type_badge = 'Academic Medical Center' if provider_type == 'medical_center' else 'Private Practice'

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} | Sleep Apnea Surgery | SleepApneaMatch.com</title>
    <meta name="description" content="{name} in {city}, {state} offers sleep apnea surgery including UPPP, Inspire therapy, and more. View procedures, surgeons, and contact information.">
    <link rel="canonical" href="https://sleepapneamatch.com/locations/{slugify(state)}/{slugify(city)}/{slugify(name)}.html">

    <meta property="og:title" content="{name} | Sleep Apnea Surgery">
    <meta property="og:description" content="Sleep apnea surgery provider in {city}, {state}. View procedures, surgeons, and contact information.">
    <meta property="og:type" content="website">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>

    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ sans: ['Manrope', 'sans-serif'] }},
                    colors: {{
                        brand: {{
                            50: '#f0f7ff', 100: '#e0effe', 600: '#2563eb', 700: '#1d4ed8',
                        }}
                    }}
                }}
            }}
        }}
    </script>

    <style>
        [x-cloak] {{ display: none !important; }}
        .glass-panel {{
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.4);
        }}
    </style>

    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "MedicalBusiness",
        "name": "{name}",
        "address": {{
            "@type": "PostalAddress",
            "streetAddress": "{address}",
            "addressLocality": "{city}",
            "addressRegion": "{state}",
            "addressCountry": "US"
        }},
        "telephone": "{phone}",
        "url": "{website}",
        "medicalSpecialty": "Sleep Medicine"
    }}
    </script>
</head>
<body class="font-sans antialiased text-slate-900 bg-slate-50 min-h-screen">
    <!-- Navigation -->
    <nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200">
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
                    <a href="/#procedures" class="hover:text-brand-600 transition">Procedures</a>
                    <a href="/blog/" class="hover:text-brand-600 transition">Blog</a>
                    <a href="/locations/" class="hover:text-brand-600 transition">Locations</a>
                    <a href="/faq/" class="hover:text-brand-600 transition">FAQ</a>
                </div>
                <a href="/#consultation" class="hidden md:block bg-brand-600 text-white px-4 py-2 rounded-lg font-semibold text-sm hover:bg-brand-700 transition">
                    Get Matched
                </a>
            </div>
        </div>
    </nav>

    <!-- Breadcrumb -->
    <div class="bg-white border-b border-slate-200">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
            <nav class="text-sm text-slate-500">
                <a href="/" class="hover:text-brand-600">Home</a>
                <span class="mx-2">/</span>
                <a href="/locations/" class="hover:text-brand-600">Locations</a>
                <span class="mx-2">/</span>
                <a href="/locations/{slugify(state)}/" class="hover:text-brand-600">{state}</a>
                <span class="mx-2">/</span>
                <span class="text-slate-900 font-medium">{name}</span>
            </nav>
        </div>
    </div>

    <!-- Provider Header -->
    <section class="bg-white py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row md:items-start md:justify-between gap-6">
                <div>
                    <div class="flex flex-wrap gap-2 mb-4">
                        <span class="bg-brand-50 text-brand-700 px-3 py-1 rounded-full text-sm font-medium">{type_badge}</span>
                        {inspire_badge}
                    </div>
                    <h1 class="text-3xl lg:text-4xl font-bold text-slate-900 mb-2">{name}</h1>
                    <p class="text-lg text-slate-600">{city}, {state}</p>
                </div>
                <div class="glass-panel rounded-2xl p-6 min-w-[300px]">
                    <h3 class="font-bold text-slate-900 mb-4">Contact Information</h3>
                    <div class="space-y-3 text-sm">
                        <div class="flex items-start gap-3">
                            <svg class="w-5 h-5 text-slate-400 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                            </svg>
                            <span class="text-slate-600">{address}</span>
                        </div>
                        <div class="flex items-center gap-3">
                            <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                            </svg>
                            <a href="tel:{phone}" class="text-brand-600 font-medium hover:text-brand-700">{phone}</a>
                        </div>
                        <div class="flex items-center gap-3">
                            <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path>
                            </svg>
                            <a href="{website}" target="_blank" rel="noopener" class="text-brand-600 font-medium hover:text-brand-700">Visit Website</a>
                        </div>
                    </div>
                    <a href="/#consultation" class="block mt-6 bg-brand-600 text-white text-center py-3 rounded-lg font-semibold hover:bg-brand-700 transition">
                        Request Consultation
                    </a>
                </div>
            </div>
        </div>
    </section>

    <!-- Provider Details -->
    <section class="py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid lg:grid-cols-3 gap-8">
                <div class="lg:col-span-2 space-y-8">
                    <!-- About -->
                    <div class="bg-white rounded-2xl p-6 shadow-sm">
                        <h2 class="text-xl font-bold text-slate-900 mb-4">About {name}</h2>
                        <p class="text-slate-600 leading-relaxed">{notes if notes else f'{name} is a leading sleep apnea surgery provider in {city}, {state}, offering comprehensive evaluation and surgical treatment options for obstructive sleep apnea.'}</p>
                    </div>

                    <!-- Procedures -->
                    <div class="bg-white rounded-2xl p-6 shadow-sm">
                        <h2 class="text-xl font-bold text-slate-900 mb-4">Procedures Offered</h2>
                        <p class="text-slate-600 leading-relaxed">{procedures if procedures else 'UPPP, Inspire Therapy, Nasal Surgery, Palate Surgery, Tongue Surgery'}</p>
                    </div>

                    <!-- Surgeons -->
                    <div class="bg-white rounded-2xl p-6 shadow-sm">
                        <h2 class="text-xl font-bold text-slate-900 mb-4">Key Surgeons</h2>
                        <p class="text-slate-600 leading-relaxed">{key_surgeons if key_surgeons else 'Contact provider for surgeon information'}</p>
                    </div>
                </div>

                <div class="space-y-6">
                    <!-- Specializations -->
                    <div class="bg-white rounded-2xl p-6 shadow-sm">
                        <h3 class="font-bold text-slate-900 mb-4">Specializations</h3>
                        <p class="text-sm text-slate-600">{specializations if specializations else 'Sleep Surgery, Obstructive Sleep Apnea'}</p>
                    </div>

                    <!-- Insurance -->
                    <div class="bg-white rounded-2xl p-6 shadow-sm">
                        <h3 class="font-bold text-slate-900 mb-4">Insurance Accepted</h3>
                        <p class="text-sm text-slate-600">{insurance if insurance else 'Most major insurance plans accepted. Contact provider to verify coverage.'}</p>
                    </div>

                    <!-- Dr. Igor Callout -->
                    <div class="bg-gradient-to-br from-slate-50 to-slate-100 rounded-2xl p-6 border border-slate-200">
                        <div class="flex items-center gap-3 mb-3">
                            <img src="/assets/images/dr_igor.jpg" alt="Dr. Igor I. Bussel" class="w-10 h-10 rounded-full object-cover ring-2 ring-white shadow">
                            <div>
                                <div class="font-bold text-slate-900 text-sm">Dr. Igor I. Bussel, MD</div>
                                <div class="text-xs text-slate-500">Medical Reviewer</div>
                            </div>
                        </div>
                        <div class="flex items-center gap-1 text-xs text-green-600">
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                            </svg>
                            <span class="font-medium">Verified Provider</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                <div class="flex items-center gap-2">
                    <div class="w-8 h-8 rounded-lg bg-brand-600 flex items-center justify-center">
                        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>
                        </svg>
                    </div>
                    <span class="text-white font-bold">SleepApneaMatch</span>
                </div>
                <p class="text-sm">&copy; 2026 SleepApneaMatch.com. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''
    return html

def main():
    """Generate all provider pages."""
    print("Generating provider pages...")

    # Load clinics data
    with open(API_DIR / "clinics.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

    medical_centers = data.get('medical_centers', [])
    independent_clinics = data.get('independent_clinics', [])

    total_generated = 0

    # Generate medical center pages
    for center in medical_centers:
        state = center.get('state', '').strip()
        city = center.get('city', '').strip()
        name = center.get('name', '').strip()

        if not state or not city or not name:
            continue

        state_slug = slugify(state)
        city_slug = slugify(city)
        name_slug = slugify(name)

        # Create directories
        dir_path = LOCATIONS_DIR / state_slug / city_slug
        dir_path.mkdir(parents=True, exist_ok=True)

        # Generate page
        html = generate_provider_page(center, 'medical_center')

        file_path = dir_path / f"{name_slug}.html"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)

        total_generated += 1
        print(f"  Generated: {file_path.relative_to(BASE_DIR)}")

    # Generate independent clinic pages
    for clinic in independent_clinics:
        state = clinic.get('state', '').strip()
        city = clinic.get('city', '').strip()
        name = clinic.get('name', '').strip()

        if not state or not city or not name:
            continue

        # Skip international (Singapore, N/A state)
        if state == 'N/A' or state == 'Singapore':
            continue

        state_slug = slugify(state)
        city_slug = slugify(city)
        name_slug = slugify(name)

        # Create directories
        dir_path = LOCATIONS_DIR / state_slug / city_slug
        dir_path.mkdir(parents=True, exist_ok=True)

        # Generate page
        html = generate_provider_page(clinic, 'independent_clinic')

        file_path = dir_path / f"{name_slug}.html"
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)

        total_generated += 1
        print(f"  Generated: {file_path.relative_to(BASE_DIR)}")

    print(f"\nTotal provider pages generated: {total_generated}")

if __name__ == "__main__":
    main()
