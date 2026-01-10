#!/usr/bin/env python3
"""
Generate Cost Guide Static Pages for StemCellPrices.com
Creates ~250 pages across 6 conditions and 30 cities

URL Structure: /{condition-slug}/{state-slug}/{city-slug}/index.html

Usage: python3 generate_cost_guides.py
"""

import os
import re
import json
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# All condition data
CONDITIONS = {
    'knee': {
        'name': 'Knee Osteoarthritis',
        'shortName': 'Knee',
        'slug': 'knee-cost-guide',
        'description': 'Comprehensive pricing and outcomes data for stem cell treatment of knee osteoarthritis, based on Cochrane Review 2025, Mayo Clinic research, and data from 250+ US clinics.',
        'priceRange': {'low': 3500, 'median': 5800, 'high': 9000},
        'outcomes': {
            'successRate': '68-77%',
            'painReduction': '1.2 pts',
            'painScale': '0-10 scale',
            'functionImprovement': '14.2 pts',
            'functionScale': '0-100 scale',
            'duration': '12-24+',
            'durationUnit': 'months',
            'source': 'Cochrane Review 2025, Mayo Clinic'
        }
    },
    'spine': {
        'name': 'Lumbar Spine / Disc',
        'shortName': 'Back & Spine',
        'slug': 'spine-cost-guide',
        'description': 'Comprehensive pricing and outcomes data for stem cell treatment of lumbar disc degeneration and lower back pain, based on clinical studies and data from 200+ US spine centers.',
        'priceRange': {'low': 4000, 'median': 7500, 'high': 15000},
        'outcomes': {
            'successRate': '55-70%',
            'painReduction': '2.1 pts',
            'painScale': '0-10 scale',
            'functionImprovement': '18.5 pts',
            'functionScale': 'ODI scale',
            'duration': '12-18',
            'durationUnit': 'months',
            'source': 'NIH Regenerative Medicine Database, Clinical Pain Studies 2024'
        }
    },
    'shoulder': {
        'name': 'Shoulder (Rotator Cuff)',
        'shortName': 'Shoulder',
        'slug': 'shoulder-cost-guide',
        'description': 'Comprehensive pricing and outcomes data for stem cell treatment of rotator cuff injuries and shoulder conditions, based on orthopedic research and data from 180+ US sports medicine clinics.',
        'priceRange': {'low': 3000, 'median': 5500, 'high': 12000},
        'outcomes': {
            'successRate': '65-78%',
            'painReduction': '2.8 pts',
            'painScale': '0-10 scale',
            'functionImprovement': '22.4 pts',
            'functionScale': 'ASES score',
            'duration': '12-24',
            'durationUnit': 'months',
            'source': 'Journal of Shoulder and Elbow Surgery 2024, Sports Medicine Research'
        }
    },
    'hip': {
        'name': 'Hip Osteoarthritis',
        'shortName': 'Hip',
        'slug': 'hip-cost-guide',
        'description': 'Comprehensive pricing and outcomes data for stem cell treatment of hip osteoarthritis, based on orthopedic research and data from 150+ US regenerative medicine clinics.',
        'priceRange': {'low': 4000, 'median': 6500, 'high': 14000},
        'outcomes': {
            'successRate': '60-72%',
            'painReduction': '1.8 pts',
            'painScale': '0-10 scale',
            'functionImprovement': '16.8 pts',
            'functionScale': 'HOOS score',
            'duration': '12-18',
            'durationUnit': 'months',
            'source': 'Arthritis Care & Research 2024, Hip Preservation Society'
        }
    },
    'neck': {
        'name': 'Cervical Spine (Neck)',
        'shortName': 'Neck',
        'slug': 'neck-cost-guide',
        'description': 'Comprehensive pricing and outcomes data for stem cell treatment of cervical disc degeneration and neck pain, based on spine research and data from 120+ US pain management centers.',
        'priceRange': {'low': 4500, 'median': 8000, 'high': 18000},
        'outcomes': {
            'successRate': '58-68%',
            'painReduction': '2.3 pts',
            'painScale': '0-10 scale',
            'functionImprovement': '15.2 pts',
            'functionScale': 'NDI score',
            'duration': '10-16',
            'durationUnit': 'months',
            'source': 'Spine Journal 2024, Cervical Spine Research Society'
        }
    },
    'si-joint': {
        'name': 'Sacroiliac (SI) Joint',
        'shortName': 'SI Joint',
        'slug': 'si-joint-cost-guide',
        'description': 'Comprehensive pricing and outcomes data for stem cell treatment of sacroiliac joint dysfunction, based on pain medicine research and data from 100+ US interventional pain clinics.',
        'priceRange': {'low': 3500, 'median': 6000, 'high': 12000},
        'outcomes': {
            'successRate': '62-75%',
            'painReduction': '2.5 pts',
            'painScale': '0-10 scale',
            'functionImprovement': '19.3 pts',
            'functionScale': 'ODI score',
            'duration': '12-20',
            'durationUnit': 'months',
            'source': 'Pain Medicine Journal 2024, SI Joint Research Consortium'
        }
    }
}

# City data with price modifiers
CITY_PRICES = {
    'los-angeles': {'name': 'Los Angeles', 'state': 'California', 'stateSlug': 'california', 'priceModifier': 1.15},
    'san-diego': {'name': 'San Diego', 'state': 'California', 'stateSlug': 'california', 'priceModifier': 1.10},
    'san-francisco': {'name': 'San Francisco', 'state': 'California', 'stateSlug': 'california', 'priceModifier': 1.20},
    'houston': {'name': 'Houston', 'state': 'Texas', 'stateSlug': 'texas', 'priceModifier': 0.95},
    'dallas': {'name': 'Dallas', 'state': 'Texas', 'stateSlug': 'texas', 'priceModifier': 0.98},
    'austin': {'name': 'Austin', 'state': 'Texas', 'stateSlug': 'texas', 'priceModifier': 1.02},
    'san-antonio': {'name': 'San Antonio', 'state': 'Texas', 'stateSlug': 'texas', 'priceModifier': 0.90},
    'miami': {'name': 'Miami', 'state': 'Florida', 'stateSlug': 'florida', 'priceModifier': 1.12},
    'tampa': {'name': 'Tampa', 'state': 'Florida', 'stateSlug': 'florida', 'priceModifier': 1.00},
    'orlando': {'name': 'Orlando', 'state': 'Florida', 'stateSlug': 'florida', 'priceModifier': 0.98},
    'jacksonville': {'name': 'Jacksonville', 'state': 'Florida', 'stateSlug': 'florida', 'priceModifier': 0.94},
    'phoenix': {'name': 'Phoenix', 'state': 'Arizona', 'stateSlug': 'arizona', 'priceModifier': 0.92},
    'scottsdale': {'name': 'Scottsdale', 'state': 'Arizona', 'stateSlug': 'arizona', 'priceModifier': 1.05},
    'denver': {'name': 'Denver', 'state': 'Colorado', 'stateSlug': 'colorado', 'priceModifier': 1.00},
    'chicago': {'name': 'Chicago', 'state': 'Illinois', 'stateSlug': 'illinois', 'priceModifier': 1.05},
    'new-york-city': {'name': 'New York City', 'state': 'New York', 'stateSlug': 'new-york', 'priceModifier': 1.25},
    'atlanta': {'name': 'Atlanta', 'state': 'Georgia', 'stateSlug': 'georgia', 'priceModifier': 0.98},
    'seattle': {'name': 'Seattle', 'state': 'Washington', 'stateSlug': 'washington', 'priceModifier': 1.08},
    'boston': {'name': 'Boston', 'state': 'Massachusetts', 'stateSlug': 'massachusetts', 'priceModifier': 1.18},
    'las-vegas': {'name': 'Las Vegas', 'state': 'Nevada', 'stateSlug': 'nevada', 'priceModifier': 0.95},
    'philadelphia': {'name': 'Philadelphia', 'state': 'Pennsylvania', 'stateSlug': 'pennsylvania', 'priceModifier': 1.08},
    'nashville': {'name': 'Nashville', 'state': 'Tennessee', 'stateSlug': 'tennessee', 'priceModifier': 0.95},
    'charlotte': {'name': 'Charlotte', 'state': 'North Carolina', 'stateSlug': 'north-carolina', 'priceModifier': 0.96},
    'raleigh': {'name': 'Raleigh', 'state': 'North Carolina', 'stateSlug': 'north-carolina', 'priceModifier': 0.98},
    'minneapolis': {'name': 'Minneapolis', 'state': 'Minnesota', 'stateSlug': 'minnesota', 'priceModifier': 1.02},
    'detroit': {'name': 'Detroit', 'state': 'Michigan', 'stateSlug': 'michigan', 'priceModifier': 0.92},
    'portland': {'name': 'Portland', 'state': 'Oregon', 'stateSlug': 'oregon', 'priceModifier': 1.05},
    'sacramento': {'name': 'Sacramento', 'state': 'California', 'stateSlug': 'california', 'priceModifier': 1.08},
    'san-jose': {'name': 'San Jose', 'state': 'California', 'stateSlug': 'california', 'priceModifier': 1.18},
    'kansas-city': {'name': 'Kansas City', 'state': 'Missouri', 'stateSlug': 'missouri', 'priceModifier': 0.90}
}


def format_price(amount):
    """Format number as currency string"""
    return f"${amount:,}"


def get_adjusted_prices(condition_key, city_slug):
    """Get prices adjusted for city market"""
    condition = CONDITIONS[condition_key]
    city = CITY_PRICES.get(city_slug)

    if city:
        modifier = city['priceModifier']
        return {
            'low': round(condition['priceRange']['low'] * modifier / 100) * 100,
            'median': round(condition['priceRange']['median'] * modifier / 100) * 100,
            'high': round(condition['priceRange']['high'] * modifier / 100) * 100
        }
    else:
        return condition['priceRange'].copy()


def get_state_code(state_name):
    """Get two-letter state code"""
    state_codes = {
        'California': 'CA', 'Texas': 'TX', 'Florida': 'FL', 'Arizona': 'AZ',
        'Colorado': 'CO', 'Illinois': 'IL', 'New York': 'NY', 'Georgia': 'GA',
        'Washington': 'WA', 'Massachusetts': 'MA', 'Nevada': 'NV',
        'Pennsylvania': 'PA', 'Tennessee': 'TN', 'North Carolina': 'NC',
        'Minnesota': 'MN', 'Michigan': 'MI', 'Oregon': 'OR', 'Missouri': 'MO'
    }
    return state_codes.get(state_name, state_name[:2].upper())


def generate_page_content(condition_key, city_slug=None):
    """Generate HTML content for a cost guide page"""
    condition = CONDITIONS[condition_key]

    # Determine if this is a location-specific page
    if city_slug and city_slug in CITY_PRICES:
        city = CITY_PRICES[city_slug]
        prices = get_adjusted_prices(condition_key, city_slug)
        location_title = f" in {city['name']}, {city['state']}"
        location_path = f"{city['stateSlug']}/{city_slug}/"
        city_name = city['name']
        state_name = city['state']
        state_slug = city['stateSlug']
        state_code = get_state_code(state_name)
        meta_description = f"{condition['name']} stem cell therapy costs ${format_price(prices['low'])} to ${format_price(prices['high'])} in {city['name']}, {state_name}. Compare prices from verified clinics."
    else:
        prices = condition['priceRange'].copy()
        location_title = ""
        location_path = ""
        city_name = ""
        state_name = ""
        state_slug = ""
        state_code = ""
        city_slug = ""
        meta_description = condition['description']

    # Read template
    template_path = BASE_DIR / 'cost-guide-template.html'
    with open(template_path, 'r') as f:
        template = f.read()

    # Replace all placeholders
    replacements = {
        '{{CONDITION_NAME}}': condition['name'],
        '{{CONDITION_SHORT}}': condition['shortName'],
        '{{CONDITION_SLUG}}': condition['slug'],
        '{{CONDITION_KEY}}': condition_key,
        '{{LOCATION_TITLE}}': location_title,
        '{{LOCATION_PATH}}': location_path,
        '{{LOCATION_CTA}}': f"in {city_name}" if city_name else "",
        '{{META_DESCRIPTION}}': meta_description,
        '{{CITY}}': city_name,
        '{{CITY_SLUG}}': city_slug,
        '{{STATE}}': state_name,
        '{{STATE_SLUG}}': state_slug,
        '{{STATE_CODE}}': state_code,
        '{{PRICE_LOW}}': format_price(prices['low']),
        '{{PRICE_MEDIAN}}': format_price(prices['median']),
        '{{PRICE_HIGH}}': format_price(prices['high']),
        '{{SUCCESS_RATE}}': condition['outcomes']['successRate'],
        '{{PAIN_REDUCTION}}': condition['outcomes']['painReduction'],
        '{{PAIN_SCALE}}': f"({condition['outcomes']['painScale']})",
        '{{FUNCTION_IMPROVEMENT}}': condition['outcomes']['functionImprovement'],
        '{{FUNCTION_SCALE}}': f"({condition['outcomes']['functionScale']})",
        '{{DURATION}}': condition['outcomes']['duration'],
        '{{DURATION_UNIT}}': condition['outcomes']['durationUnit'],
        '{{OUTCOMES_SOURCE}}': condition['outcomes']['source']
    }

    content = template
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, str(value))

    return content


def create_cost_guide_directories():
    """Create all necessary directories for cost guide pages"""
    created = 0

    for condition_key, condition in CONDITIONS.items():
        slug = condition['slug']
        condition_dir = BASE_DIR / slug
        condition_dir.mkdir(exist_ok=True)
        created += 1

        # Create state directories
        states_created = set()
        for city_slug, city in CITY_PRICES.items():
            state_slug = city['stateSlug']
            if state_slug not in states_created:
                state_dir = condition_dir / state_slug
                state_dir.mkdir(exist_ok=True)
                states_created.add(state_slug)
                created += 1

            # Create city directory
            city_dir = condition_dir / state_slug / city_slug
            city_dir.mkdir(exist_ok=True)
            created += 1

    print(f"Created {created} directories")
    return created


def generate_all_pages():
    """Generate all cost guide pages"""
    # First create directories
    create_cost_guide_directories()

    pages_created = 0

    for condition_key, condition in CONDITIONS.items():
        slug = condition['slug']
        condition_dir = BASE_DIR / slug

        # Generate default page (with geo-detection)
        default_content = generate_page_content(condition_key, None)
        default_path = condition_dir / 'index.html'
        with open(default_path, 'w') as f:
            f.write(default_content)
        pages_created += 1
        print(f"  Created: /{slug}/index.html")

        # Generate city-specific pages
        for city_slug, city in CITY_PRICES.items():
            city_content = generate_page_content(condition_key, city_slug)
            city_path = condition_dir / city['stateSlug'] / city_slug / 'index.html'

            with open(city_path, 'w') as f:
                f.write(city_content)
            pages_created += 1

        print(f"  Created {len(CITY_PRICES)} city pages for {condition['name']}")

    print(f"\nTotal pages created: {pages_created}")
    return pages_created


def generate_sitemap_entries():
    """Generate sitemap XML entries for all cost guide pages"""
    entries = []
    base_url = "https://stemcellprices.com"

    for condition_key, condition in CONDITIONS.items():
        slug = condition['slug']

        # Default page (high priority)
        entries.append({
            'url': f"{base_url}/{slug}/",
            'priority': '0.9',
            'changefreq': 'weekly'
        })

        # City-specific pages (medium priority)
        for city_slug, city in CITY_PRICES.items():
            entries.append({
                'url': f"{base_url}/{slug}/{city['stateSlug']}/{city_slug}/",
                'priority': '0.7',
                'changefreq': 'monthly'
            })

    return entries


def print_summary():
    """Print summary of what will be generated"""
    total_pages = len(CONDITIONS) * (1 + len(CITY_PRICES))  # 1 default + all cities per condition

    print("=" * 60)
    print("Cost Guide Page Generator")
    print("=" * 60)
    print(f"\nConditions: {len(CONDITIONS)}")
    for key, cond in CONDITIONS.items():
        print(f"  - {cond['name']} -> /{cond['slug']}/")

    print(f"\nCities: {len(CITY_PRICES)}")

    print(f"\nTotal pages to generate: {total_pages}")
    print(f"  - {len(CONDITIONS)} default pages (geo-detected)")
    print(f"  - {len(CONDITIONS) * len(CITY_PRICES)} location-specific pages")
    print("=" * 60)


if __name__ == '__main__':
    print_summary()

    response = input("\nGenerate all pages? (y/n): ").strip().lower()
    if response == 'y':
        generate_all_pages()

        # Generate sitemap entries
        sitemap_entries = generate_sitemap_entries()
        print(f"\nSitemap entries: {len(sitemap_entries)}")

        # Save sitemap entries to JSON for reference
        with open(BASE_DIR / 'cost-guide-sitemap.json', 'w') as f:
            json.dump(sitemap_entries, f, indent=2)
        print("Saved cost-guide-sitemap.json")
    else:
        print("Cancelled.")
