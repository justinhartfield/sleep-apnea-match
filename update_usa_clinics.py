#!/usr/bin/env python3
"""
Script to update all USA clinic detail pages to use the Mexico clinic template format.
Features:
- Hero section with city background and price range in header
- Sticky CTA lead capture form on right
- Treatment tags (colored pills instead of bullet lists)
- "Why Choose [City] for Stem Cell Therapy?" section
- "Other Clinics in [City]" section with navigation links
"""

import os
import re
import json
from pathlib import Path
from html.parser import HTMLParser

# State display names
STATE_NAMES = {
    'alabama': 'Alabama', 'alaska': 'Alaska', 'arizona': 'Arizona', 'arkansas': 'Arkansas',
    'california': 'California', 'colorado': 'Colorado', 'connecticut': 'Connecticut', 'delaware': 'Delaware',
    'florida': 'Florida', 'georgia': 'Georgia', 'hawaii': 'Hawaii', 'idaho': 'Idaho',
    'illinois': 'Illinois', 'indiana': 'Indiana', 'iowa': 'Iowa', 'kansas': 'Kansas',
    'kentucky': 'Kentucky', 'louisiana': 'Louisiana', 'maine': 'Maine', 'maryland': 'Maryland',
    'massachusetts': 'Massachusetts', 'michigan': 'Michigan', 'minnesota': 'Minnesota', 'mississippi': 'Mississippi',
    'missouri': 'Missouri', 'montana': 'Montana', 'nebraska': 'Nebraska', 'nevada': 'Nevada',
    'new-hampshire': 'New Hampshire', 'new-jersey': 'New Jersey', 'new-mexico': 'New Mexico', 'new-york': 'New York',
    'north-carolina': 'North Carolina', 'north-dakota': 'North Dakota', 'ohio': 'Ohio', 'oklahoma': 'Oklahoma',
    'oregon': 'Oregon', 'pennsylvania': 'Pennsylvania', 'rhode-island': 'Rhode Island', 'south-carolina': 'South Carolina',
    'south-dakota': 'South Dakota', 'tennessee': 'Tennessee', 'texas': 'Texas', 'utah': 'Utah',
    'vermont': 'Vermont', 'virginia': 'Virginia', 'washington': 'Washington', 'west-virginia': 'West Virginia',
    'wisconsin': 'Wisconsin', 'wyoming': 'Wyoming'
}

def slug_to_display(slug):
    """Convert slug to display name"""
    return STATE_NAMES.get(slug, slug.replace('-', ' ').title())

def extract_clinic_data(filepath):
    """Extract clinic data from existing HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    data = {}

    # Extract clinic name from title
    title_match = re.search(r'<title>([^<]+)', content)
    if title_match:
        title = title_match.group(1)
        # Extract clinic name (before " - Stem Cell" or " | ")
        name_match = re.match(r'([^-|]+)', title)
        if name_match:
            data['name'] = name_match.group(1).strip()

    # Extract from JSON-LD if available
    jsonld_match = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', content, re.DOTALL)
    if jsonld_match:
        try:
            jsonld = json.loads(jsonld_match.group(1))
            if '@graph' in jsonld:
                for item in jsonld['@graph']:
                    if item.get('@type') and ('MedicalBusiness' in str(item.get('@type')) or 'LocalBusiness' in str(item.get('@type'))):
                        if 'name' in item:
                            data['name'] = item['name']
                        if 'telephone' in item:
                            data['phone'] = item['telephone']
                        if 'address' in item and isinstance(item['address'], dict):
                            addr = item['address']
                            data['street'] = addr.get('streetAddress', '')
                            data['city_name'] = addr.get('addressLocality', '')
                            data['state_name'] = addr.get('addressRegion', '')
                        if 'priceRange' in item:
                            data['price_range'] = item['priceRange'].replace('$', '').replace(',', '')
        except:
            pass

    # Extract description from meta tag
    desc_match = re.search(r'<meta name="description" content="([^"]+)"', content)
    if desc_match:
        data['meta_description'] = desc_match.group(1)

    # Extract specialty from content
    specialty_match = re.search(r'<h3[^>]*>Specialty</h3>\s*<p[^>]*>([^<]+)</p>', content, re.IGNORECASE)
    if specialty_match:
        data['specialty'] = specialty_match.group(1).strip()
    else:
        # Try to get from meta description
        if 'meta_description' in data:
            spec_match = re.search(r'offers? ([^.]+?) in', data['meta_description'])
            if spec_match:
                data['specialty'] = spec_match.group(1).strip()

    # Extract about/description text
    about_match = re.search(r'<h2[^>]*>About[^<]*</h2>\s*<p[^>]*>([^<]+)</p>', content, re.IGNORECASE)
    if about_match:
        data['about'] = about_match.group(1).strip()

    # Extract treatments offered
    treatments = []
    treatments_section = re.search(r'<h3[^>]*>Treatments Offered</h3>\s*<ul[^>]*>(.*?)</ul>', content, re.DOTALL | re.IGNORECASE)
    if treatments_section:
        items = re.findall(r'<li>([^<]+)</li>', treatments_section.group(1))
        treatments = [t.strip() for t in items]
    data['treatments'] = treatments if treatments else ['Stem Cell Therapy', 'PRP Therapy', 'Regenerative Medicine']

    # Extract conditions treated
    conditions = []
    conditions_section = re.search(r'<h3[^>]*>Conditions Treated</h3>\s*<ul[^>]*>(.*?)</ul>', content, re.DOTALL | re.IGNORECASE)
    if conditions_section:
        items = re.findall(r'<li>([^<]+)</li>', conditions_section.group(1))
        conditions = [c.strip() for c in items]
    data['conditions'] = conditions if conditions else ['Knee Osteoarthritis', 'Back Pain', 'Shoulder Injuries', 'Hip Pain']

    # Extract price range if not from JSON-LD
    if 'price_range' not in data:
        price_match = re.search(r'Price [Rr]ange[^$]*\$([0-9,]+)\s*[-–]\s*\$([0-9,]+)', content)
        if price_match:
            data['price_range'] = f"{price_match.group(1)} - {price_match.group(2)}"

    # Extract phone if not from JSON-LD
    if 'phone' not in data:
        phone_match = re.search(r'(?:Phone|telephone)[^(]*(\([0-9]{3}\)\s*[0-9]{3}[-.]?[0-9]{4}|\+?[0-9]{1,3}[-.\s]?[0-9]{3}[-.\s]?[0-9]{3}[-.\s]?[0-9]{4})', content, re.IGNORECASE)
        if phone_match:
            data['phone'] = phone_match.group(1)

    # Extract address if not from JSON-LD
    if 'street' not in data:
        addr_match = re.search(r'<p[^>]*class="[^"]*text-slate-900[^"]*"[^>]*>([^<]+(?:St|Ave|Blvd|Dr|Rd|Way|Lane|Ct|Suite|#)[^<]*)</p>', content)
        if addr_match:
            data['street'] = addr_match.group(1).strip()

    # Get slug from filename
    data['slug'] = filepath.stem

    # Extract other clinics in city
    other_clinics = []
    other_section = re.search(r'Other Clinics in.*?<div class="grid[^>]*>(.*?)</div>\s*</div>\s*</div>', content, re.DOTALL | re.IGNORECASE)
    if other_section:
        clinic_links = re.findall(r'<a href="([^"]+)"[^>]*>.*?<h3[^>]*>([^<]+)</h3>.*?<p[^>]*>([^<]+)</p>.*?<p[^>]*text-blue[^>]*>([^<]+)</p>', other_section.group(1), re.DOTALL)
        for link, name, specialty, price in clinic_links:
            other_clinics.append({
                'href': link,
                'name': name.strip(),
                'specialty': specialty.strip(),
                'price': price.strip()
            })
    data['other_clinics'] = other_clinics

    return data

def get_state_features(state_slug):
    """Get Why Choose features for a state"""
    features = {
        'california': [
            ('Leading Medical Innovation', 'California is home to world-renowned research institutions and pioneering stem cell clinics'),
            ('Highly Experienced Physicians', 'Access to board-certified specialists with extensive regenerative medicine training'),
            ('Advanced Treatment Options', 'Latest stem cell protocols and cutting-edge regenerative technologies'),
            ('Comprehensive Care', 'Full-service clinics offering personalized treatment plans and follow-up care'),
        ],
        'texas': [
            ('Competitive Pricing', 'Texas offers stem cell treatments at prices 15-25% below coastal states'),
            ('Top Medical Centers', 'Houston and Dallas are home to world-class orthopedic facilities'),
            ('No State Income Tax', 'Patients save on overall costs with Texas tax advantages'),
            ('Growing Expertise', 'Rapidly expanding network of regenerative medicine specialists'),
        ],
        'florida': [
            ('Medical Tourism Hub', 'Florida attracts patients nationwide with its concentration of regenerative clinics'),
            ('Experienced Specialists', 'Many physicians with decades of stem cell therapy experience'),
            ('Year-Round Accessibility', 'Convenient location with major airports and pleasant recovery weather'),
            ('Competitive Pricing', 'Multiple clinics competing keeps prices reasonable'),
        ],
        'arizona': [
            ('Lower Cost of Living', 'Arizona clinics often offer more competitive pricing than coastal states'),
            ('Renowned Institutions', 'Home to Mayo Clinic Arizona and other prestigious medical centers'),
            ('Recovery-Friendly Climate', 'Dry, warm weather ideal for post-treatment recovery'),
            ('Growing Medical Hub', 'Phoenix and Scottsdale attract top regenerative medicine talent'),
        ],
        'new-york': [
            ('World-Class Specialists', 'NYC is home to Hospital for Special Surgery and leading orthopedic experts'),
            ('Cutting-Edge Research', 'Access to the latest clinical trials and innovative treatments'),
            ('Comprehensive Care Teams', 'Multi-disciplinary approach to regenerative medicine'),
            ('Convenient Access', 'Major international hub with extensive transportation options'),
        ],
        'colorado': [
            ('Sports Medicine Excellence', 'Home to Steadman Clinic and top sports orthopedics specialists'),
            ('Active Lifestyle Focus', 'Clinics specialized in treating athletic injuries and active patients'),
            ('Altitude Training Benefits', 'Some research suggests altitude may enhance recovery'),
            ('Growing Regenerative Hub', 'Denver is becoming a center for regenerative medicine'),
        ],
    }

    # Default features for states not specifically defined
    default_features = [
        ('Qualified Specialists', 'Board-certified physicians with regenerative medicine expertise'),
        ('Modern Facilities', 'State-of-the-art clinics with advanced treatment technologies'),
        ('Personalized Care', 'Customized treatment plans tailored to your specific condition'),
        ('Competitive Pricing', 'Transparent pricing and multiple financing options available'),
    ]

    return features.get(state_slug, default_features)

def generate_clinic_page(data, state_slug, city_slug, filepath):
    """Generate new clinic page HTML using Mexico template format"""

    state_name = slug_to_display(state_slug)
    city_name = data.get('city_name', slug_to_display(city_slug))
    clinic_name = data.get('name', 'Stem Cell Clinic')
    clinic_slug = data.get('slug', filepath.stem)
    specialty = data.get('specialty', 'Regenerative Medicine')
    phone = data.get('phone', '')
    street = data.get('street', city_name)
    price_range = data.get('price_range', '4,000 - 10,000')
    about = data.get('about', f'{clinic_name} offers stem cell therapy and regenerative medicine treatments in {city_name}, {state_name}.')
    treatments = data.get('treatments', [])
    conditions = data.get('conditions', [])
    other_clinics = data.get('other_clinics', [])

    # Format price range with $ signs if not already present
    if '$' not in price_range:
        price_parts = price_range.replace(',', '').split('-')
        if len(price_parts) == 2:
            try:
                low = int(price_parts[0].strip())
                high = int(price_parts[1].strip())
                price_range = f"${low:,} - ${high:,}"
            except:
                price_range = f"${price_range}"

    # Generate treatments HTML (colored tags)
    treatments_html = ''
    all_items = treatments + conditions
    for item in all_items[:8]:  # Limit to 8 items
        treatments_html += f'<div class="bg-blue-50 text-blue-700 px-4 py-2 rounded-lg text-sm font-medium">{item}</div>'

    # Generate features HTML
    features_html = ''
    feature_items = [
        'Board-certified physicians',
        'Modern treatment facilities',
        'Personalized care plans',
        'Follow-up support'
    ]
    for feature in feature_items:
        features_html += f'''<div class="flex items-center gap-2"><svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg><span class="text-gray-700">{feature}</span></div>'''

    # Generate Why Choose section
    state_features = get_state_features(state_slug)
    why_choose_html = ''
    for title, desc in state_features:
        why_choose_html += f'''<li class="flex items-start gap-2">
                            <span class="text-blue-500 mt-1">&#10003;</span>
                            <span><strong>{title}</strong> - {desc}</span>
                        </li>'''

    # Generate other clinics HTML
    other_clinics_html = f'''<a href="/locations/{state_slug}/{city_slug}/" class="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition">
                    <div class="text-blue-600 font-semibold">&larr; View All {city_name} Clinics</div>
                    <p class="text-gray-500 text-sm mt-1">Compare verified clinics</p>
                </a>
                <a href="/conditions/" class="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition">
                    <div class="text-blue-600 font-semibold">Treatment Guides</div>
                    <p class="text-gray-500 text-sm mt-1">Knee, hip, shoulder, spine</p>
                </a>
                <a href="/locations/{state_slug}/" class="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition">
                    <div class="text-blue-600 font-semibold">All {state_name} Locations</div>
                    <p class="text-gray-500 text-sm mt-1">Browse clinics statewide</p>
                </a>'''

    # Try to use city-specific background image, fallback to state or generic
    city_bg = f'/assets/images/cities/{city_slug}-large.webp'

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{clinic_name} - Stem Cell Clinic in {city_name}, {state_name} | StemCellPrices.com</title>
    <meta name="description" content="{clinic_name} offers stem cell therapy in {city_name}, {state_name}. {specialty}. Prices from {price_range}. Get a free consultation today.">
    <meta name="keywords" content="{clinic_name}, stem cell therapy {city_name}, stem cell clinic {state_name}, regenerative medicine, {specialty.lower()} {city_name}">
    <link rel="canonical" href="https://stemcellprices.com/locations/{state_slug}/{city_slug}/{clinic_slug}.html">

    <!-- Open Graph -->
    <meta property="og:title" content="{clinic_name} - Stem Cell Clinic in {city_name}, {state_name}">
    <meta property="og:description" content="{specialty}. Prices from {price_range}. Get a free quote.">
    <meta property="og:url" content="https://stemcellprices.com/locations/{state_slug}/{city_slug}/{clinic_slug}.html">
    <meta property="og:type" content="business.business">

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
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <script src="/assets/js/tracking.js"></script>

    <!-- Schema.org Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@graph": [
            {{
                "@type": "MedicalBusiness",
                "name": "{clinic_name}",
                "description": "{about}",
                "address": {{
                    "@type": "PostalAddress",
                    "streetAddress": "{street}",
                    "addressLocality": "{city_name}",
                    "addressRegion": "{state_name}",
                    "addressCountry": "US"
                }},
                "telephone": "{phone}",
                "priceRange": "{price_range}",
                "medicalSpecialty": "{specialty}",
                "url": "https://stemcellprices.com/locations/{state_slug}/{city_slug}/{clinic_slug}.html"
            }},
            {{
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://stemcellprices.com/"}},
                    {{"@type": "ListItem", "position": 2, "name": "Locations", "item": "https://stemcellprices.com/locations/"}},
                    {{"@type": "ListItem", "position": 3, "name": "{state_name}", "item": "https://stemcellprices.com/locations/{state_slug}/"}},
                    {{"@type": "ListItem", "position": 4, "name": "{city_name}", "item": "https://stemcellprices.com/locations/{state_slug}/{city_slug}/"}},
                    {{"@type": "ListItem", "position": 5, "name": "{clinic_name}"}}
                ]
            }}
        ]
    }}
    </script>
    <script src="/assets/js/clinic-gallery.js"></script>
    <style>
        [x-cloak] {{ display: none !important; }}
        .hero-gradient {{ background: linear-gradient(135deg, rgba(15, 23, 42, 0.7) 0%, rgba(30, 58, 138, 0.5) 100%); }}
    </style>
</head>
<body class="bg-gray-50">
    <!-- Header -->
    <nav class="sticky top-0 z-50 bg-white/80 backdrop-blur-md border-b border-slate-200" x-data="{{ mobileMenu: false, locationsOpen: false }}">
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
    </nav>

    <!-- Hero Section -->
    <section class="relative bg-cover bg-center text-white py-16" style="background-image: url('{city_bg}');">
        <div class="absolute inset-0 hero-gradient"></div>
        <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Breadcrumb -->
            <nav class="mb-6">
                <ol class="flex items-center space-x-2 text-sm text-blue-200">
                    <li><a href="/" class="hover:text-white">Home</a></li>
                    <li>/</li>
                    <li><a href="/locations/" class="hover:text-white">Locations</a></li>
                    <li>/</li>
                    <li><a href="/locations/{state_slug}/" class="hover:text-white">{state_name}</a></li>
                    <li>/</li>
                    <li><a href="/locations/{state_slug}/{city_slug}/" class="hover:text-white">{city_name}</a></li>
                    <li>/</li>
                    <li class="text-white font-medium">{clinic_name}</li>
                </ol>
            </nav>

            <div class="flex flex-col md:flex-row md:items-center md:justify-between">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        <span class='bg-green-400 text-green-900 px-3 py-1 rounded-full text-sm font-semibold'>&#10003; Verified</span>
                        <span class="bg-white/20 px-3 py-1 rounded-full text-sm">{state_name}</span>
                    </div>
                    <h1 class="text-4xl font-bold mb-2">{clinic_name}</h1>
                    <p class="text-xl text-blue-100 mb-4">{specialty}</p>
                    <p class="text-blue-200">
                        <svg class="w-5 h-5 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                        </svg>
                        {street}, {city_name}
                    </p>
                </div>
                <div class="mt-6 md:mt-0 text-right">
                    <div class="text-blue-200 text-sm mb-1">Price Range</div>
                    <div class="text-3xl font-bold">{price_range}</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <!-- Left Column - Clinic Details -->
            <div class="lg:col-span-2 space-y-8">
                <!-- About -->
                <div class="bg-white rounded-xl shadow-sm p-6">
                    <!-- Clinic Image Gallery -->
                    <div x-data="clinicGallery('{clinic_slug}')" x-init="init()" @keydown.window="handleKeydown($event)" class="mb-6">
                        <!-- Loading state -->
                        <template x-if="loading">
                            <div class="w-full h-64 bg-slate-100 rounded-xl animate-pulse flex items-center justify-center">
                                <svg class="w-8 h-8 text-slate-300 animate-spin" fill="none" viewBox="0 0 24 24">
                                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                                </svg>
                            </div>
                        </template>

                        <!-- Gallery content -->
                        <template x-if="!loading && images.length > 0">
                            <div>
                                <!-- Main Image -->
                                <div class="relative rounded-xl overflow-hidden cursor-pointer group" @click="openLightbox(0)">
                                    <img :src="images[0]?.url" :alt="images[0]?.alt" class="w-full h-64 object-cover transition-transform duration-300 group-hover:scale-105">
                                    <div class="absolute inset-0 bg-black/0 group-hover:bg-black/10 transition-colors flex items-center justify-center">
                                        <span class="opacity-0 group-hover:opacity-100 transition-opacity bg-white/90 px-4 py-2 rounded-full text-sm font-medium text-slate-700">
                                            <svg class="w-4 h-4 inline mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0zM10 7v3m0 0v3m0-3h3m-3 0H7"></path></svg>
                                            View Photos
                                        </span>
                                    </div>
                                    <!-- Image count badge -->
                                    <template x-if="hasMultipleImages">
                                        <div class="absolute bottom-3 right-3 bg-black/70 text-white px-3 py-1 rounded-full text-sm font-medium">
                                            <svg class="w-4 h-4 inline mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                                            <span x-text="images.length"></span> Photos
                                        </div>
                                    </template>
                                </div>

                                <!-- Thumbnail strip (only show if multiple images) -->
                                <template x-if="hasMultipleImages">
                                    <div class="flex gap-2 mt-3 overflow-x-auto pb-2">
                                        <template x-for="(image, index) in images" :key="index">
                                            <button @click="openLightbox(index)" class="flex-shrink-0 w-20 h-16 rounded-lg overflow-hidden border-2 transition-all" :class="index === 0 ? 'border-blue-500' : 'border-transparent hover:border-slate-300'">
                                                <img :src="image.url" :alt="image.alt" class="w-full h-full object-cover">
                                            </button>
                                        </template>
                                    </div>
                                </template>
                            </div>
                        </template>

                        <!-- No images fallback -->
                        <template x-if="!loading && images.length === 0">
                            <div class="w-full h-64 bg-gradient-to-br from-blue-50 to-slate-100 rounded-xl flex items-center justify-center">
                                <div class="text-center text-slate-400">
                                    <svg class="w-12 h-12 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                                    <p class="text-sm">No photos available</p>
                                </div>
                            </div>
                        </template>

                        <!-- Lightbox Modal -->
                        <template x-if="lightboxOpen">
                            <div class="fixed inset-0 z-50 flex items-center justify-center" @click.self="closeLightbox()">
                                <div class="absolute inset-0 bg-black/90"></div>

                                <!-- Close button -->
                                <button @click="closeLightbox()" class="absolute top-4 right-4 z-10 text-white/80 hover:text-white p-2">
                                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                                </button>

                                <!-- Navigation arrows -->
                                <template x-if="hasMultipleImages">
                                    <button @click="prevImage()" class="absolute left-4 z-10 text-white/80 hover:text-white p-2 bg-black/30 rounded-full">
                                        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
                                    </button>
                                </template>
                                <template x-if="hasMultipleImages">
                                    <button @click="nextImage()" class="absolute right-4 z-10 text-white/80 hover:text-white p-2 bg-black/30 rounded-full">
                                        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                                    </button>
                                </template>

                                <!-- Main image -->
                                <div class="relative z-0 max-w-5xl max-h-[80vh] px-4">
                                    <img :src="currentImage?.url" :alt="currentImage?.alt" class="max-w-full max-h-[80vh] object-contain rounded-lg">
                                </div>

                                <!-- Image counter -->
                                <template x-if="hasMultipleImages">
                                    <div class="absolute bottom-4 left-1/2 -translate-x-1/2 bg-black/50 text-white px-4 py-2 rounded-full text-sm">
                                        <span x-text="currentIndex + 1"></span> / <span x-text="images.length"></span>
                                    </div>
                                </template>
                            </div>
                        </template>
                    </div>
                    <h2 class="text-2xl font-bold text-gray-900 mb-4">About {clinic_name}</h2>
                    <p class="text-gray-600 leading-relaxed">{about}</p>
                </div>

                <!-- Treatments -->
                <div class="bg-white rounded-xl shadow-sm p-6">
                    <h2 class="text-2xl font-bold text-gray-900 mb-4">Treatments Offered</h2>
                    <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
                        {treatments_html}
                    </div>
                </div>

                <!-- Features -->
                <div class="bg-white rounded-xl shadow-sm p-6">
                    <h2 class="text-2xl font-bold text-gray-900 mb-4">Clinic Features</h2>
                    <div class="grid grid-cols-2 gap-4">
                        {features_html}
                    </div>
                </div>

                <!-- Why Choose This City -->
                <div class="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl p-6">
                    <h2 class="text-2xl font-bold text-gray-900 mb-4">Why Choose {city_name} for Stem Cell Therapy?</h2>
                    <ul class="space-y-3 text-gray-700">
                        {why_choose_html}
                    </ul>
                </div>
            </div>

            <!-- Right Column - Contact Form -->
            <div class="lg:col-span-1">
                <div class="bg-white rounded-xl shadow-sm p-6 sticky top-24">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Get a Free Quote</h3>
                    <form id="leadForm" class="space-y-4">
                        <input type="hidden" id="clinicName" value="{clinic_name}">
                        <input type="hidden" id="clinicCity" value="{city_name}">
                        <input type="hidden" id="clinicState" value="{state_name}">

                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Full Name *</label>
                            <input type="text" id="fullName" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Email *</label>
                            <input type="email" id="email" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Phone *</label>
                            <input type="tel" id="phone" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Condition</label>
                            <select id="condition" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent">
                                <option value="">Select condition...</option>
                                <option value="knee">Knee Pain / Osteoarthritis</option>
                                <option value="back">Back / Spine Pain</option>
                                <option value="shoulder">Shoulder / Rotator Cuff</option>
                                <option value="hip">Hip Pain</option>
                                <option value="anti-aging">Anti-Aging / Wellness</option>
                                <option value="other">Other</option>
                            </select>
                        </div>

                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Message</label>
                            <textarea id="message" rows="3" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent" placeholder="Tell us about your condition..."></textarea>
                        </div>

                        <button type="submit" class="w-full bg-blue-600 text-white py-3 px-4 rounded-lg font-semibold hover:bg-blue-700 transition">
                            Request Free Consultation
                        </button>
                    </form>

                    <div class="mt-6 pt-6 border-t border-gray-200">
                        <p class="text-sm text-gray-500 mb-3">Or contact directly:</p>
                        <a href="tel:{phone}" class="flex items-center justify-center gap-2 bg-gray-100 text-gray-700 py-3 px-4 rounded-lg font-semibold hover:bg-gray-200 transition">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                            </svg>
                            {phone if phone else 'Call Clinic'}
                        </a>
                    </div>

                    <p class="mt-4 text-xs text-gray-400 text-center">
                        By submitting, you agree to our privacy policy. Your information will be shared with this clinic.
                    </p>
                </div>
            </div>
        </div>

        <!-- Other Clinics in City -->
        <div class="mt-12">
            <h2 class="text-2xl font-bold text-gray-900 mb-6">Other Clinics in {city_name}</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                {other_clinics_html}
            </div>
        </div>
    </main>

    <!-- Footer -->
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
    </footer>

    <script>
        // Lead form submission
        document.getElementById('leadForm').addEventListener('submit', function(e) {{
            e.preventDefault();

            const lead = {{
                clinic: document.getElementById('clinicName').value,
                city: document.getElementById('clinicCity').value,
                state: document.getElementById('clinicState').value,
                name: document.getElementById('fullName').value,
                email: document.getElementById('email').value,
                phone: document.getElementById('phone').value,
                condition: document.getElementById('condition').value,
                message: document.getElementById('message').value,
                timestamp: new Date().toISOString(),
                source: window.location.href
            }};

            // Store lead
            const leads = JSON.parse(localStorage.getItem('stemcell_leads') || '[]');
            leads.push(lead);
            localStorage.setItem('stemcell_leads', JSON.stringify(leads));

            // Track conversion
            if (typeof gtag !== 'undefined') {{
                gtag('event', 'generate_lead', {{
                    'event_category': 'Lead',
                    'event_label': lead.clinic,
                    'value': 1
                }});
            }}

            alert('Thank you! Your request has been submitted. The clinic will contact you within 24-48 hours.');
            this.reset();
        }});
    </script>
</body>
</html>'''

    return html

def main():
    root = Path('.')
    updated = 0
    skipped = 0
    errors = []

    # Find all USA clinic HTML files (exclude Mexico and index files)
    for state_dir in (root / 'locations').iterdir():
        if not state_dir.is_dir():
            continue

        state_slug = state_dir.name

        # Skip Mexico (already has the template)
        if state_slug == 'mexico':
            print(f"Skipping: {state_slug} (Mexico already has template)")
            continue

        # Skip index.html files
        if state_slug == 'index.html':
            continue

        # Process each city in the state
        for city_dir in state_dir.iterdir():
            if not city_dir.is_dir():
                continue

            city_slug = city_dir.name

            # Process each clinic file in the city
            for clinic_file in city_dir.glob('*.html'):
                # Skip index files
                if clinic_file.name == 'index.html':
                    continue

                try:
                    # Extract data from existing file
                    data = extract_clinic_data(clinic_file)

                    # Generate new HTML
                    new_html = generate_clinic_page(data, state_slug, city_slug, clinic_file)

                    # Write updated file
                    with open(clinic_file, 'w', encoding='utf-8') as f:
                        f.write(new_html)

                    print(f"Updated: {clinic_file}")
                    updated += 1

                except Exception as e:
                    errors.append((clinic_file, str(e)))
                    print(f"Error: {clinic_file} - {e}")

    print(f"\n{'='*50}")
    print(f"Summary: Updated {updated}, Skipped {skipped}, Errors {len(errors)}")

    if errors:
        print("\nErrors:")
        for filepath, error in errors[:10]:
            print(f"  {filepath}: {error}")

if __name__ == '__main__':
    main()
