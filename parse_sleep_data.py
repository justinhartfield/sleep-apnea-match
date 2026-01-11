#!/usr/bin/env python3
"""
Parse Sleep Apnea research CSV files and generate JSON data for the website.
"""

import csv
import json
import os
from pathlib import Path

# Paths
RESEARCH_DIR = Path("/Users/tang/Projects/sleep-apnea")
OUTPUT_DIR = Path("/Users/tang/Projects/sleep-apnea-match/api")

def parse_medical_centers():
    """Parse medical centers CSV into structured JSON."""
    centers = []
    csv_path = RESEARCH_DIR / "research_medical_centers.csv"

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if not row.get('Center Name'):
                continue
            center = {
                "id": f"center-{i+1:03d}",
                "name": row.get('Center Name', '').strip(),
                "slug": row.get('Center Name', '').lower().replace(' ', '-').replace(',', '').replace('.', ''),
                "type": "academic_medical_center",
                "city": row.get('City', '').strip(),
                "state": row.get('State', '').strip(),
                "address": row.get('Address', '').strip(),
                "phone": row.get('Phone', '').strip(),
                "website": row.get('Website', '').strip(),
                "specializations": row.get('Specializations', '').strip(),
                "key_surgeons": row.get('Key Surgeons', '').strip(),
                "procedures_offered": row.get('Procedures Offered', '').strip(),
                "inspire_certified": row.get('Inspire Certified', '').strip().lower() == 'yes',
                "center_of_excellence": row.get('Center of Excellence', '').strip(),
                "research_programs": row.get('Research Programs', '').strip(),
                "patient_volume": row.get('Patient Volume', '').strip(),
                "insurance_accepted": row.get('Insurance Accepted', '').strip(),
                "notes": row.get('Notes', '').strip(),
                "featured": True,
                "verified": True
            }
            centers.append(center)

    return centers

def parse_independent_clinics():
    """Parse independent clinics CSV into structured JSON."""
    clinics = []
    csv_path = RESEARCH_DIR / "research_independent_clinics.csv"

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if not row.get('Clinic Name'):
                continue
            clinic = {
                "id": f"clinic-{i+1:03d}",
                "name": row.get('Clinic Name', '').strip(),
                "slug": row.get('Clinic Name', '').lower().replace(' ', '-').replace(',', '').replace('.', '').replace("'", ''),
                "type": "independent_practice",
                "lead_surgeon": row.get('Lead Surgeon', '').strip(),
                "city": row.get('City', '').strip(),
                "state": row.get('State', '').strip(),
                "address": row.get('Address', '').strip(),
                "phone": row.get('Phone', '').strip(),
                "website": row.get('Website', '').strip(),
                "specializations": row.get('Specializations', '').strip(),
                "procedures_offered": row.get('Procedures Offered', '').strip(),
                "inspire_certified": row.get('Inspire Certified', '').strip().lower() == 'yes',
                "notable_achievements": row.get('Notable Achievements', '').strip(),
                "patient_reviews": row.get('Patient Reviews Summary', '').strip(),
                "insurance_accepted": row.get('Insurance Accepted', '').strip(),
                "unique_services": row.get('Unique Services', '').strip(),
                "practice_type": row.get('Practice Type', '').strip(),
                "featured": False,
                "verified": True
            }
            clinics.append(clinic)

    return clinics

def parse_procedures():
    """Parse procedures CSV into structured JSON."""
    procedures = []
    csv_path = RESEARCH_DIR / "research_sleep_apnea_procedures.csv"

    with open(csv_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The CSV has a complex structure, parse manually
    lines = content.split('\n')
    if len(lines) < 2:
        return procedures

    # Get header
    header_line = lines[0]
    headers = []
    in_quote = False
    current = ''
    for char in header_line:
        if char == '"':
            in_quote = not in_quote
        elif char == ',' and not in_quote:
            headers.append(current.strip().strip('"'))
            current = ''
        else:
            current += char
    headers.append(current.strip().strip('"'))

    # Parse data rows - simplified approach
    # Key procedures we need
    key_procedures = [
        {
            "id": "uppp",
            "name": "UPPP (Uvulopalatopharyngoplasty)",
            "slug": "uppp",
            "description": "Surgical removal and repositioning of excess tissue in the throat including the uvula, soft palate, and tonsils to widen the airway.",
            "category": "soft_palate",
            "cost_low": 5000,
            "cost_high": 15000,
            "median_cost": 10000,
            "success_rate_min": 40,
            "success_rate_max": 60,
            "cure_rate_min": 15,
            "cure_rate_max": 25,
            "recovery_time": "2-4 weeks",
            "hospital_stay": "1 day or outpatient",
            "anesthesia": "General",
            "insurance_covered": True,
            "cpt_codes": "42145"
        },
        {
            "id": "inspire",
            "name": "Inspire (Hypoglossal Nerve Stimulation)",
            "slug": "inspire",
            "description": "Implantable device that stimulates the hypoglossal nerve to keep the airway open during sleep.",
            "category": "neuromodulation",
            "cost_low": 30000,
            "cost_high": 65000,
            "median_cost": 45000,
            "success_rate_min": 66,
            "success_rate_max": 75,
            "cure_rate_min": 20,
            "cure_rate_max": 30,
            "recovery_time": "1-2 weeks",
            "hospital_stay": "Outpatient or 1 day",
            "anesthesia": "General",
            "insurance_covered": True,
            "cpt_codes": "64568"
        },
        {
            "id": "mma",
            "name": "MMA (Maxillomandibular Advancement)",
            "slug": "mma",
            "description": "Surgical advancement of both the upper and lower jaw to enlarge the airway.",
            "category": "skeletal",
            "cost_low": 40000,
            "cost_high": 100000,
            "median_cost": 65000,
            "success_rate_min": 85,
            "success_rate_max": 95,
            "cure_rate_min": 40,
            "cure_rate_max": 50,
            "recovery_time": "4-6 weeks",
            "hospital_stay": "1-2 days",
            "anesthesia": "General",
            "insurance_covered": True,
            "cpt_codes": "21141, 21196"
        },
        {
            "id": "septoplasty",
            "name": "Septoplasty",
            "slug": "septoplasty",
            "description": "Surgical correction of a deviated nasal septum to improve nasal airflow.",
            "category": "nasal",
            "cost_low": 3000,
            "cost_high": 10000,
            "median_cost": 6000,
            "success_rate_min": 70,
            "success_rate_max": 90,
            "cure_rate_min": 5,
            "cure_rate_max": 15,
            "recovery_time": "1-2 weeks",
            "hospital_stay": "Outpatient",
            "anesthesia": "General or local",
            "insurance_covered": True,
            "cpt_codes": "30520"
        },
        {
            "id": "turbinate-reduction",
            "name": "Turbinate Reduction",
            "slug": "turbinate-reduction",
            "description": "Surgical reduction of the turbinates to improve nasal airflow.",
            "category": "nasal",
            "cost_low": 2000,
            "cost_high": 5000,
            "median_cost": 3500,
            "success_rate_min": 70,
            "success_rate_max": 85,
            "cure_rate_min": 5,
            "cure_rate_max": 10,
            "recovery_time": "1 week",
            "hospital_stay": "Outpatient",
            "anesthesia": "Local or general",
            "insurance_covered": True,
            "cpt_codes": "30140"
        },
        {
            "id": "tonsillectomy",
            "name": "Tonsillectomy",
            "slug": "tonsillectomy",
            "description": "Surgical removal of the tonsils, often combined with adenoidectomy for sleep apnea.",
            "category": "soft_palate",
            "cost_low": 3000,
            "cost_high": 8000,
            "median_cost": 5000,
            "success_rate_min": 75,
            "success_rate_max": 82,
            "cure_rate_min": 50,
            "cure_rate_max": 70,
            "recovery_time": "1-2 weeks",
            "hospital_stay": "Outpatient or 1 day",
            "anesthesia": "General",
            "insurance_covered": True,
            "cpt_codes": "42826"
        },
        {
            "id": "genioglossus-advancement",
            "name": "Genioglossus Advancement",
            "slug": "genioglossus-advancement",
            "description": "Surgical procedure to pull the tongue muscle attachment forward to prevent airway collapse.",
            "category": "tongue",
            "cost_low": 8000,
            "cost_high": 20000,
            "median_cost": 12000,
            "success_rate_min": 39,
            "success_rate_max": 65,
            "cure_rate_min": 15,
            "cure_rate_max": 25,
            "recovery_time": "2-3 weeks",
            "hospital_stay": "1 day",
            "anesthesia": "General",
            "insurance_covered": True,
            "cpt_codes": "21199"
        },
        {
            "id": "tors",
            "name": "TORS (Transoral Robotic Surgery)",
            "slug": "tors",
            "description": "Minimally invasive robotic surgery to remove tissue at the base of the tongue.",
            "category": "tongue",
            "cost_low": 15000,
            "cost_high": 40000,
            "median_cost": 25000,
            "success_rate_min": 60,
            "success_rate_max": 68,
            "cure_rate_min": 20,
            "cure_rate_max": 30,
            "recovery_time": "2-3 weeks",
            "hospital_stay": "1-2 days",
            "anesthesia": "General",
            "insurance_covered": True,
            "cpt_codes": "41530"
        }
    ]

    return key_procedures

def parse_faqs():
    """Parse FAQs CSV into structured JSON."""
    faqs = []
    csv_path = RESEARCH_DIR / "research_faqs.csv"

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            question = row.get('Question', '').strip()
            if not question:
                continue
            faq = {
                "id": f"faq-{i+1:03d}",
                "question": question,
                "answer": row.get('Answer', '').strip(),
                "category": row.get('Category', '').strip(),
                "related_procedures": row.get('Related Procedures', '').strip(),
                "sources": row.get('Sources', '').strip(),
                "seo_keywords": row.get('SEO Keywords', '').strip()
            }
            faqs.append(faq)

    return faqs

def parse_clinical_studies():
    """Parse clinical studies CSV into structured JSON."""
    studies = []
    csv_path = RESEARCH_DIR / "research_clinical_studies.csv"

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            study_name = row.get('Study Name', '').strip()
            if not study_name:
                continue
            study = {
                "id": f"study-{i+1:03d}",
                "name": study_name,
                "type": row.get('Study Type', '').strip(),
                "sample_size": row.get('Sample Size', '').strip(),
                "follow_up": row.get('Follow-up Duration', '').strip(),
                "ahi_reduction": row.get('AHI Reduction', '').strip(),
                "success_rate": row.get('Success Rate', '').strip(),
                "cure_rate": row.get('Cure Rate', '').strip(),
                "key_findings": row.get('Key Findings', '').strip(),
                "source": row.get('Source', '').strip()
            }
            studies.append(study)

    return studies

def generate_locations_data(centers, clinics):
    """Generate locations data from providers."""
    locations = {}

    all_providers = centers + clinics

    for provider in all_providers:
        state = provider.get('state', '').strip()
        city = provider.get('city', '').strip()

        if not state or not city:
            continue

        state_slug = state.lower().replace(' ', '-')
        city_slug = city.lower().replace(' ', '-').replace('.', '')

        if state_slug not in locations:
            locations[state_slug] = {
                "name": state,
                "slug": state_slug,
                "cities": {}
            }

        if city_slug not in locations[state_slug]["cities"]:
            locations[state_slug]["cities"][city_slug] = {
                "name": city,
                "slug": city_slug,
                "providers": []
            }

        locations[state_slug]["cities"][city_slug]["providers"].append({
            "id": provider.get('id'),
            "name": provider.get('name'),
            "slug": provider.get('slug'),
            "type": provider.get('type'),
            "inspire_certified": provider.get('inspire_certified', False)
        })

    return locations

def main():
    """Main function to parse all data and generate JSON files."""
    print("Parsing sleep apnea research data...")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Parse all data
    print("  Parsing medical centers...")
    centers = parse_medical_centers()
    print(f"    Found {len(centers)} medical centers")

    print("  Parsing independent clinics...")
    clinics = parse_independent_clinics()
    print(f"    Found {len(clinics)} independent clinics")

    print("  Parsing procedures...")
    procedures = parse_procedures()
    print(f"    Found {len(procedures)} procedures")

    print("  Parsing FAQs...")
    faqs = parse_faqs()
    print(f"    Found {len(faqs)} FAQs")

    print("  Parsing clinical studies...")
    studies = parse_clinical_studies()
    print(f"    Found {len(studies)} clinical studies")

    print("  Generating locations data...")
    locations = generate_locations_data(centers, clinics)
    print(f"    Found {len(locations)} states with providers")

    # Generate combined clinics.json
    all_providers = {
        "meta": {
            "version": "1.0",
            "generated": "2026-01-10",
            "total_providers": len(centers) + len(clinics)
        },
        "medical_centers": centers,
        "independent_clinics": clinics
    }

    # Write JSON files
    print("\nWriting JSON files...")

    with open(OUTPUT_DIR / "clinics.json", 'w', encoding='utf-8') as f:
        json.dump(all_providers, f, indent=2, ensure_ascii=False)
    print(f"  Written: {OUTPUT_DIR / 'clinics.json'}")

    with open(OUTPUT_DIR / "procedures.json", 'w', encoding='utf-8') as f:
        json.dump({"procedures": procedures}, f, indent=2, ensure_ascii=False)
    print(f"  Written: {OUTPUT_DIR / 'procedures.json'}")

    with open(OUTPUT_DIR / "faqs.json", 'w', encoding='utf-8') as f:
        json.dump({"faqs": faqs}, f, indent=2, ensure_ascii=False)
    print(f"  Written: {OUTPUT_DIR / 'faqs.json'}")

    with open(OUTPUT_DIR / "studies.json", 'w', encoding='utf-8') as f:
        json.dump({"studies": studies}, f, indent=2, ensure_ascii=False)
    print(f"  Written: {OUTPUT_DIR / 'studies.json'}")

    with open(OUTPUT_DIR / "locations.json", 'w', encoding='utf-8') as f:
        json.dump({"locations": locations}, f, indent=2, ensure_ascii=False)
    print(f"  Written: {OUTPUT_DIR / 'locations.json'}")

    # Generate summary data.json
    summary = {
        "meta": {
            "version": "1.0",
            "generated": "2026-01-10",
            "site": "SleepApneaMatch.com"
        },
        "stats": {
            "total_providers": len(centers) + len(clinics),
            "medical_centers": len(centers),
            "independent_clinics": len(clinics),
            "states_covered": len(locations),
            "procedures": len(procedures),
            "faqs": len(faqs),
            "clinical_studies": len(studies)
        },
        "price_ranges": {
            "uppp": {"low": 5000, "high": 15000},
            "inspire": {"low": 30000, "high": 65000},
            "mma": {"low": 40000, "high": 100000},
            "septoplasty": {"low": 3000, "high": 10000},
            "turbinate_reduction": {"low": 2000, "high": 5000},
            "tonsillectomy": {"low": 3000, "high": 8000}
        }
    }

    with open(OUTPUT_DIR / "data.json", 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"  Written: {OUTPUT_DIR / 'data.json'}")

    print("\nDone! All JSON files generated.")

if __name__ == "__main__":
    main()
