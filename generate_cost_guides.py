#!/usr/bin/env python3
"""
Generate Procedure Cost Guide Pages for SleepApneaMatch.com
Creates comprehensive cost guide pages for each major sleep apnea procedure
"""

import json
import os
from pathlib import Path

# Procedure data with comprehensive information
PROCEDURES = {
    'uppp': {
        'id': 'uppp',
        'name': 'UPPP (Uvulopalatopharyngoplasty)',
        'short_name': 'UPPP',
        'slug': 'uppp-cost-guide',
        'description': 'Surgical removal and repositioning of excess tissue in the throat including the uvula, soft palate, and tonsils to widen the airway.',
        'long_description': 'Uvulopalatopharyngoplasty (UPPP) is one of the most commonly performed surgeries for obstructive sleep apnea. The procedure removes and repositions excess tissue in the throat—including the uvula, soft palate, and often the tonsils—to widen the airway and reduce obstruction during sleep. UPPP has been performed since the 1980s and remains a primary surgical option for patients with palate-level obstruction who have failed or cannot tolerate CPAP therapy.',
        'price_range': {'low': 5000, 'median': 10000, 'high': 15000},
        'success_rate': {'min': 40, 'max': 60},
        'cure_rate': {'min': 15, 'max': 25},
        'ahi_reduction': {'min': 30, 'max': 50},
        'recovery_time': '2-4 weeks',
        'hospital_stay': '1 day or outpatient',
        'work_return': '1-2 weeks',
        'anesthesia': 'General',
        'insurance_covered': True,
        'cpt_codes': ['42145'],
        'best_for': 'Patients with palate-level obstruction who have failed CPAP therapy',
        'considerations': [
            'One of the most common sleep apnea surgeries performed worldwide',
            'Success rates vary significantly based on patient anatomy and severity',
            'May be combined with other procedures for multi-level surgery',
            'Pain and difficulty swallowing common for 1-2 weeks after surgery',
            'Some patients experience voice changes or regurgitation'
        ],
        'meta_description': 'UPPP surgery costs $5,000-$15,000. Compare 45 verified sleep surgery providers, success rates (40-60%), and insurance coverage options.'
    },
    'inspire': {
        'id': 'inspire',
        'name': 'Inspire Therapy (Hypoglossal Nerve Stimulation)',
        'short_name': 'Inspire',
        'slug': 'inspire-cost-guide',
        'description': 'FDA-approved implantable device that stimulates the hypoglossal nerve to keep the airway open during sleep.',
        'long_description': 'Inspire therapy is an FDA-approved, implantable device that treats moderate to severe obstructive sleep apnea by stimulating the hypoglossal nerve. A small generator is implanted under the skin in the upper chest, with a sensing lead detecting breathing patterns and a stimulation lead moving the tongue forward to keep the airway open. Patients use a small remote to turn the device on before sleep. Inspire is approved for patients 18+ with moderate to severe OSA (AHI 15-65) who have failed CPAP therapy and have a BMI under 35.',
        'price_range': {'low': 30000, 'median': 45000, 'high': 65000},
        'success_rate': {'min': 66, 'max': 75},
        'cure_rate': {'min': 20, 'max': 30},
        'ahi_reduction': {'min': 60, 'max': 70},
        'recovery_time': '1-2 weeks',
        'hospital_stay': 'Outpatient or 1 day',
        'work_return': '1 week',
        'anesthesia': 'General',
        'insurance_covered': True,
        'cpt_codes': ['64568'],
        'best_for': 'Moderate to severe OSA, BMI < 35, CPAP intolerant, age 18+',
        'considerations': [
            'Requires drug-induced sleep endoscopy (DISE) evaluation before surgery',
            'Device requires periodic battery replacement (typically 10-11 years)',
            'Most major insurance companies now cover Inspire therapy',
            'Activation occurs 1 month after implantation',
            'Highest satisfaction rates among sleep apnea surgeries'
        ],
        'meta_description': 'Inspire implant costs $30,000-$65,000. Compare 45 certified Inspire surgeons, success rates (66-75%), and insurance coverage details.'
    },
    'mma': {
        'id': 'mma',
        'name': 'MMA (Maxillomandibular Advancement)',
        'short_name': 'MMA Surgery',
        'slug': 'mma-cost-guide',
        'description': 'Major surgical procedure that advances both the upper jaw (maxilla) and lower jaw (mandible) to enlarge the airway.',
        'long_description': 'Maxillomandibular advancement (MMA) is considered the most effective surgical treatment for obstructive sleep apnea, with success rates of 85-95%. The procedure involves surgically cutting and repositioning both the upper jaw (maxilla) and lower jaw (mandible), advancing them forward typically 10-12mm. This dramatically enlarges the airway space behind the tongue and soft palate. MMA is often reserved for severe OSA cases, patients who have failed other surgeries, or those with skeletal deficiency contributing to their airway obstruction.',
        'price_range': {'low': 40000, 'median': 65000, 'high': 100000},
        'success_rate': {'min': 85, 'max': 95},
        'cure_rate': {'min': 40, 'max': 50},
        'ahi_reduction': {'min': 80, 'max': 90},
        'recovery_time': '4-6 weeks',
        'hospital_stay': '1-2 days',
        'work_return': '2-4 weeks',
        'anesthesia': 'General',
        'insurance_covered': True,
        'cpt_codes': ['21141', '21196'],
        'best_for': 'Severe OSA, patients with skeletal deficiency, failed other surgeries',
        'considerations': [
            'Most effective surgical option with highest success rates',
            'Most invasive procedure with longest recovery time',
            'May alter facial appearance (usually considered improvement)',
            'Requires oral and maxillofacial surgeon experienced in sleep surgery',
            'Often combined with genioglossus advancement'
        ],
        'meta_description': 'MMA surgery costs $40,000-$100,000. The most effective sleep apnea surgery (85-95% success). Compare 45 maxillofacial surgeons.'
    },
    'septoplasty': {
        'id': 'septoplasty',
        'name': 'Septoplasty',
        'short_name': 'Septoplasty',
        'slug': 'septoplasty-cost-guide',
        'description': 'Surgical correction of a deviated nasal septum to improve nasal airflow and reduce obstruction.',
        'long_description': 'Septoplasty is a surgical procedure to correct a deviated nasal septum—the wall of bone and cartilage that divides the nasal cavity. When the septum is significantly off-center, it can obstruct airflow and worsen sleep apnea symptoms. While septoplasty alone rarely cures sleep apnea, it can significantly improve nasal breathing, enhance CPAP tolerance, and is often performed as part of multi-level sleep surgery. The procedure is performed through the nostrils with no external incisions.',
        'price_range': {'low': 3000, 'median': 6000, 'high': 10000},
        'success_rate': {'min': 70, 'max': 90},
        'cure_rate': {'min': 5, 'max': 15},
        'ahi_reduction': {'min': 10, 'max': 25},
        'recovery_time': '1-2 weeks',
        'hospital_stay': 'Outpatient',
        'work_return': '1 week',
        'anesthesia': 'General or local',
        'insurance_covered': True,
        'cpt_codes': ['30520'],
        'best_for': 'Patients with nasal obstruction due to deviated septum',
        'considerations': [
            'Often combined with turbinate reduction for maximum benefit',
            'May significantly improve CPAP tolerance and compliance',
            'Rarely cures sleep apnea alone but important adjunct procedure',
            'Quick recovery compared to other sleep surgeries',
            'May also help with snoring even if AHI unchanged'
        ],
        'meta_description': 'Septoplasty surgery costs $3,000-$10,000. Improve CPAP tolerance and nasal breathing. Compare 45 ENT surgeons and insurance options.'
    },
    'turbinate-reduction': {
        'id': 'turbinate-reduction',
        'name': 'Turbinate Reduction',
        'short_name': 'Turbinate Reduction',
        'slug': 'turbinate-reduction-cost-guide',
        'description': 'Surgical reduction of the inferior turbinates to improve nasal airflow.',
        'long_description': 'Turbinate reduction is a minimally invasive procedure to reduce the size of the inferior turbinates—curved bone and tissue structures inside the nose that can become enlarged and obstruct airflow. The procedure can be performed using various techniques including radiofrequency ablation, submucosal resection, or outfracture. Like septoplasty, turbinate reduction is often performed alongside other sleep surgery procedures and can significantly improve nasal breathing and CPAP compliance.',
        'price_range': {'low': 2000, 'median': 3500, 'high': 5000},
        'success_rate': {'min': 70, 'max': 85},
        'cure_rate': {'min': 5, 'max': 10},
        'ahi_reduction': {'min': 5, 'max': 15},
        'recovery_time': '1 week',
        'hospital_stay': 'Outpatient',
        'work_return': '2-3 days',
        'anesthesia': 'Local or general',
        'insurance_covered': True,
        'cpt_codes': ['30140'],
        'best_for': 'Chronic nasal congestion, turbinate hypertrophy',
        'considerations': [
            'Minimally invasive with quick recovery',
            'Often performed with septoplasty for comprehensive nasal surgery',
            'Multiple techniques available (radiofrequency most common)',
            'May improve CPAP compliance significantly',
            'Low risk procedure with high patient satisfaction'
        ],
        'meta_description': 'Turbinate reduction costs $2,000-$5,000. Minimally invasive nasal surgery to improve breathing. Compare 45 ENT surgeons.'
    },
    'tonsillectomy': {
        'id': 'tonsillectomy',
        'name': 'Tonsillectomy',
        'short_name': 'Tonsillectomy',
        'slug': 'tonsillectomy-cost-guide',
        'description': 'Surgical removal of the tonsils, often combined with adenoidectomy for sleep apnea treatment.',
        'long_description': 'Tonsillectomy—often combined with adenoidectomy (T&A)—is the first-line surgical treatment for pediatric obstructive sleep apnea and can also benefit adults with enlarged tonsils. The procedure removes the palatine tonsils (and adenoids if included), which can obstruct the airway during sleep. In children, T&A has cure rates of 50-70%, making it one of the most effective sleep apnea treatments. Adults with visibly enlarged tonsils may also benefit significantly, though success rates are lower than in children.',
        'price_range': {'low': 3000, 'median': 5000, 'high': 8000},
        'success_rate': {'min': 75, 'max': 82},
        'cure_rate': {'min': 50, 'max': 70},
        'ahi_reduction': {'min': 50, 'max': 75},
        'recovery_time': '1-2 weeks',
        'hospital_stay': 'Outpatient or 1 day',
        'work_return': '1-2 weeks',
        'anesthesia': 'General',
        'insurance_covered': True,
        'cpt_codes': ['42826'],
        'best_for': 'Children with OSA, adults with enlarged tonsils',
        'considerations': [
            'First-line treatment for pediatric sleep apnea',
            'Higher success rate in children than adults',
            'Often combined with adenoidectomy (T&A)',
            'Painful recovery lasting 1-2 weeks',
            'Post-operative bleeding risk requires monitoring'
        ],
        'meta_description': 'Tonsillectomy costs $3,000-$8,000. First-line surgery for pediatric sleep apnea (50-70% cure rate). Compare 45 ENT surgeons.'
    },
    'genioglossus-advancement': {
        'id': 'genioglossus-advancement',
        'name': 'Genioglossus Advancement (GA)',
        'short_name': 'GA',
        'slug': 'genioglossus-advancement-cost-guide',
        'description': 'Surgical procedure to advance the genioglossus muscle attachment, pulling the tongue forward to prevent airway collapse.',
        'long_description': 'Genioglossus advancement (GA) is a surgical procedure that repositions the main tongue muscle to prevent it from collapsing backward during sleep. The surgery involves cutting a small window in the chin bone (mandible) where the genioglossus muscle attaches, advancing it forward, and securing it in its new position. This pulls the tongue base forward and helps keep the airway open. GA is typically performed as part of multi-level surgery for sleep apnea, often combined with UPPP or other procedures targeting different levels of obstruction.',
        'price_range': {'low': 8000, 'median': 12000, 'high': 20000},
        'success_rate': {'min': 39, 'max': 65},
        'cure_rate': {'min': 15, 'max': 25},
        'ahi_reduction': {'min': 30, 'max': 50},
        'recovery_time': '2-3 weeks',
        'hospital_stay': '1 day',
        'work_return': '1-2 weeks',
        'anesthesia': 'General',
        'insurance_covered': True,
        'cpt_codes': ['21199'],
        'best_for': 'Tongue base obstruction, often combined with other procedures',
        'considerations': [
            'Usually performed as part of multi-level surgery',
            'Specifically addresses tongue-base collapse',
            'Less invasive than MMA for tongue repositioning',
            'May cause temporary numbness in lower teeth',
            'Often combined with UPPP or hyoid suspension'
        ],
        'meta_description': 'Genioglossus advancement costs $8,000-$20,000. Tongue surgery for sleep apnea (39-65% success). Compare 45 sleep surgeons.'
    },
    'tors': {
        'id': 'tors',
        'name': 'TORS (Transoral Robotic Surgery)',
        'short_name': 'TORS',
        'slug': 'tors-cost-guide',
        'description': 'Minimally invasive robotic surgery to remove tissue at the base of the tongue causing airway obstruction.',
        'long_description': 'Transoral Robotic Surgery (TORS) uses the da Vinci surgical robot to perform precise tissue removal at the base of the tongue and in the throat. The robotic arms provide enhanced visualization and dexterity, allowing surgeons to access difficult-to-reach areas through the mouth without external incisions. For sleep apnea, TORS is primarily used to reduce enlarged lingual tonsils or excess tissue at the tongue base that causes obstruction. The procedure offers advantages over traditional open surgery including less pain, faster recovery, and reduced risk of complications.',
        'price_range': {'low': 15000, 'median': 25000, 'high': 40000},
        'success_rate': {'min': 60, 'max': 68},
        'cure_rate': {'min': 20, 'max': 30},
        'ahi_reduction': {'min': 50, 'max': 60},
        'recovery_time': '2-3 weeks',
        'hospital_stay': '1-2 days',
        'work_return': '2 weeks',
        'anesthesia': 'General',
        'insurance_covered': True,
        'cpt_codes': ['41530'],
        'best_for': 'Tongue base obstruction, lingual tonsil hypertrophy',
        'considerations': [
            'Requires specialized robotic equipment and trained surgeon',
            'Less invasive than traditional tongue surgery',
            'Excellent visualization of tongue base',
            'Often combined with other procedures for multi-level treatment',
            'Not available at all medical centers'
        ],
        'meta_description': 'TORS surgery costs $15,000-$40,000. Robotic tongue base surgery for sleep apnea (60-68% success). Compare 45 TORS surgeons.'
    }
}

def generate_cost_guide_page(procedure):
    """Generate the main cost guide page for a procedure"""
    p = PROCEDURES[procedure]

    considerations_html = ""
    for consideration in p['considerations']:
        considerations_html += f'''<li class="flex items-start gap-3">
                            <svg class="w-5 h-5 text-primary mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                            </svg>
                            <span class="text-slate-600">{consideration}</span>
                        </li>'''

    compare_procedures_html = ""
    for proc_id, proc in PROCEDURES.items():
        active_class = 'bg-primary/10' if proc['id'] == procedure else ''
        compare_procedures_html += f'''<a href="/{proc['slug']}/" class="block p-3 rounded-lg hover:bg-slate-50 transition-colors {active_class}">
                                    <div class="font-medium text-slate-800">{proc['short_name']}</div>
                                    <div class="text-sm text-slate-500">${proc['price_range']['low']:,} - ${proc['price_range']['high']:,}</div>
                                </a>'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{p['short_name']} Cost Guide 2026 | {p['name']} Prices | SleepApneaMatch.com</title>
    <meta name="description" content="{p['meta_description']}">
    <meta name="keywords" content="{p['short_name']} cost, {p['short_name']} price, {p['short_name']} surgery cost, sleep apnea surgery cost, {p['short_name']} insurance">

    <!-- Open Graph -->
    <meta property="og:title" content="{p['short_name']} Surgery Cost Guide 2026 | SleepApneaMatch.com">
    <meta property="og:description" content="{p['meta_description']}">
    <meta property="og:image" content="https://sleepapneamatch.com/assets/images/og-{procedure}.jpg">
    <meta property="og:url" content="https://sleepapneamatch.com/{p['slug']}/">
    <meta property="og:type" content="article">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{p['short_name']} Surgery Cost Guide 2026">
    <meta name="twitter:description" content="{p['meta_description']}">

    <!-- Canonical -->
    <link rel="canonical" href="https://sleepapneamatch.com/{p['slug']}/">

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        primary: '#2563eb',
                        secondary: '#1e40af'
                    }}
                }}
            }}
        }}
    </script>

    <!-- Schema.org -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "name": "{p['name']} Cost Guide",
        "description": "{p['meta_description']}",
        "url": "https://sleepapneamatch.com/{p['slug']}/",
        "datePublished": "2026-01-10",
        "dateModified": "2026-01-10",
        "author": {{
            "@type": "Organization",
            "name": "SleepApneaMatch.com"
        }},
        "reviewedBy": {{
            "@type": "Person",
            "name": "Dr. Igor I. Bussel, MD",
            "jobTitle": "Board-Certified Physician",
            "affiliation": {{
                "@type": "Organization",
                "name": "University of California, Irvine"
            }}
        }},
        "about": {{
            "@type": "MedicalProcedure",
            "name": "{p['name']}",
            "procedureType": "Surgical",
            "description": "{p['description']}"
        }}
    }}
    </script>

    <style>
        .glass-panel {{
            background: rgba(255, 255, 255, 0.85);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
        }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800">
    <!-- Navigation -->
    <nav class="bg-white shadow-sm sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <a href="/" class="flex items-center gap-2">
                    <div class="w-8 h-8 bg-primary rounded-lg flex items-center justify-center">
                        <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>
                        </svg>
                    </div>
                    <span class="font-bold text-xl text-slate-800">SleepApneaMatch</span>
                </a>
                <div class="hidden md:flex items-center gap-6">
                    <a href="/locations/" class="text-slate-600 hover:text-primary">Find Providers</a>
                    <div class="relative group">
                        <button class="text-slate-600 hover:text-primary flex items-center gap-1">
                            Cost Guides
                            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                            </svg>
                        </button>
                        <div class="absolute top-full left-0 mt-2 w-64 bg-white rounded-xl shadow-lg opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 p-2">
                            <a href="/inspire-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">Inspire Therapy</a>
                            <a href="/mma-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">MMA Surgery</a>
                            <a href="/uppp-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">UPPP Surgery</a>
                            <a href="/tors-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">TORS (Robotic Surgery)</a>
                            <a href="/tonsillectomy-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">Tonsillectomy</a>
                            <a href="/genioglossus-advancement-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">Genioglossus Adv.</a>
                            <a href="/septoplasty-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">Septoplasty</a>
                            <a href="/turbinate-reduction-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">Turbinate Reduction</a>
                        </div>
                    </div>
                    <a href="/blog/" class="text-slate-600 hover:text-primary">Blog</a>
                    <a href="/faq/" class="text-slate-600 hover:text-primary">FAQ</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Breadcrumbs -->
    <div class="bg-slate-100 border-b">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
            <nav class="flex text-sm">
                <a href="/" class="text-slate-500 hover:text-primary">Home</a>
                <span class="mx-2 text-slate-400">/</span>
                <span class="text-slate-700">{p['short_name']} Cost Guide</span>
            </nav>
        </div>
    </div>

    <!-- Hero Section -->
    <section class="bg-gradient-to-br from-primary to-secondary text-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid lg:grid-cols-2 gap-12 items-center">
                <div>
                    <div class="inline-flex items-center gap-2 bg-white/20 px-3 py-1 rounded-full text-sm mb-4">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                        </svg>
                        Updated January 2026
                    </div>
                    <h1 class="text-4xl md:text-5xl font-bold mb-4">{p['name']} Cost Guide</h1>
                    <p class="text-xl text-blue-100 mb-6">{p['description']}</p>
                    <div class="flex flex-wrap gap-4">
                        <a href="#providers" class="bg-white text-primary px-6 py-3 rounded-lg font-semibold hover:bg-blue-50 transition-colors">
                            Find Providers
                        </a>
                        <a href="#costs" class="border border-white/50 px-6 py-3 rounded-lg font-semibold hover:bg-white/10 transition-colors">
                            View Costs
                        </a>
                    </div>
                </div>

                <!-- Price Panel -->
                <div class="glass-panel rounded-2xl p-8 text-slate-800">
                    <h2 class="text-lg font-semibold mb-4">2026 {p['short_name']} Cost Summary</h2>
                    <div class="space-y-4">
                        <div class="flex justify-between items-center pb-4 border-b">
                            <span class="text-slate-600">Price Range</span>
                            <span class="text-2xl font-bold text-primary">${p['price_range']['low']:,} - ${p['price_range']['high']:,}</span>
                        </div>
                        <div class="flex justify-between items-center pb-4 border-b">
                            <span class="text-slate-600">Average Cost</span>
                            <span class="text-xl font-semibold">${p['price_range']['median']:,}</span>
                        </div>
                        <div class="flex justify-between items-center pb-4 border-b">
                            <span class="text-slate-600">Success Rate</span>
                            <span class="text-xl font-semibold text-green-600">{p['success_rate']['min']}-{p['success_rate']['max']}%</span>
                        </div>
                        <div class="flex justify-between items-center pb-4 border-b">
                            <span class="text-slate-600">Insurance</span>
                            <span class="inline-flex items-center gap-1 text-green-600 font-medium">
                                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                                </svg>
                                {'Typically Covered' if p['insurance_covered'] else 'Varies'}
                            </span>
                        </div>
                        <div class="flex justify-between items-center">
                            <span class="text-slate-600">Recovery Time</span>
                            <span class="font-medium">{p['recovery_time']}</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Medical Review Badge -->
    <section class="bg-white border-b">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <div class="flex items-center gap-4">
                <img src="/assets/images/dr_igor.jpg" alt="Dr. Igor I. Bussel, MD" class="w-12 h-12 rounded-full object-cover">
                <div>
                    <div class="flex items-center gap-2">
                        <span class="text-sm font-semibold text-slate-700">Medically Reviewed by Dr. Igor I. Bussel, MD</span>
                        <svg class="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                            <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                        </svg>
                    </div>
                    <p class="text-xs text-slate-500">Board-Certified Physician | UCI Gavin Herbert Eye Institute | Last Updated: January 2026</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <section class="py-16" id="costs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid lg:grid-cols-3 gap-12">
                <!-- Main Content -->
                <div class="lg:col-span-2">
                    <h2 class="text-3xl font-bold mb-6">What is {p['name']}?</h2>
                    <p class="text-lg text-slate-600 mb-8">{p['long_description']}</p>

                    <h3 class="text-2xl font-bold mb-4">How Much Does {p['short_name']} Cost in 2026?</h3>
                    <p class="text-slate-600 mb-6">
                        The cost of {p['short_name']} surgery ranges from <strong>${p['price_range']['low']:,} to ${p['price_range']['high']:,}</strong>,
                        with an average cost of approximately <strong>${p['price_range']['median']:,}</strong>. These costs can vary significantly based on:
                    </p>
                    <ul class="list-disc list-inside text-slate-600 mb-8 space-y-2">
                        <li>Geographic location and local cost of living</li>
                        <li>Hospital vs. outpatient surgical center</li>
                        <li>Surgeon's experience and expertise</li>
                        <li>Complexity of your specific case</li>
                        <li>Whether combined with other procedures</li>
                        <li>Your insurance coverage and deductible</li>
                    </ul>

                    <h3 class="text-2xl font-bold mb-4">{p['short_name']} Success Rates</h3>
                    <div class="bg-gradient-to-r from-green-50 to-emerald-50 rounded-xl p-6 mb-8">
                        <div class="grid md:grid-cols-3 gap-6">
                            <div class="text-center">
                                <div class="text-3xl font-bold text-green-600">{p['success_rate']['min']}-{p['success_rate']['max']}%</div>
                                <div class="text-sm text-slate-600 mt-1">Success Rate</div>
                            </div>
                            <div class="text-center">
                                <div class="text-3xl font-bold text-green-600">{p['cure_rate']['min']}-{p['cure_rate']['max']}%</div>
                                <div class="text-sm text-slate-600 mt-1">Cure Rate</div>
                            </div>
                            <div class="text-center">
                                <div class="text-3xl font-bold text-green-600">{p['ahi_reduction']['min']}-{p['ahi_reduction']['max']}%</div>
                                <div class="text-sm text-slate-600 mt-1">AHI Reduction</div>
                            </div>
                        </div>
                    </div>

                    <h3 class="text-2xl font-bold mb-4">Who is a Good Candidate?</h3>
                    <p class="text-slate-600 mb-6"><strong>Best for:</strong> {p['best_for']}</p>

                    <h3 class="text-2xl font-bold mb-4">Important Considerations</h3>
                    <ul class="space-y-3 mb-8">
                        {considerations_html}
                    </ul>

                    <h3 class="text-2xl font-bold mb-4">Recovery & Downtime</h3>
                    <div class="grid md:grid-cols-3 gap-4 mb-8">
                        <div class="bg-slate-100 rounded-xl p-4 text-center">
                            <div class="text-lg font-bold text-slate-800">{p['recovery_time']}</div>
                            <div class="text-sm text-slate-500">Full Recovery</div>
                        </div>
                        <div class="bg-slate-100 rounded-xl p-4 text-center">
                            <div class="text-lg font-bold text-slate-800">{p['hospital_stay']}</div>
                            <div class="text-sm text-slate-500">Hospital Stay</div>
                        </div>
                        <div class="bg-slate-100 rounded-xl p-4 text-center">
                            <div class="text-lg font-bold text-slate-800">{p['work_return']}</div>
                            <div class="text-sm text-slate-500">Return to Work</div>
                        </div>
                    </div>

                    <h3 class="text-2xl font-bold mb-4">Insurance Coverage</h3>
                    <p class="text-slate-600 mb-4">
                        {p['short_name']} is {'typically covered by insurance' if p['insurance_covered'] else 'coverage varies by insurance'}
                        when deemed medically necessary for obstructive sleep apnea treatment.
                        {'Most major insurance companies, including Medicare, cover this procedure when patients meet specific criteria.' if p['insurance_covered'] else ''}
                    </p>
                    <p class="text-slate-600 mb-8">
                        <strong>CPT Code(s):</strong> {', '.join(p['cpt_codes'])}
                    </p>
                </div>

                <!-- Sidebar -->
                <div class="lg:col-span-1">
                    <div class="sticky top-24 space-y-6">
                        <!-- Quick Stats -->
                        <div class="bg-white rounded-xl shadow-lg p-6">
                            <h3 class="font-bold text-lg mb-4">Quick Facts</h3>
                            <div class="space-y-3 text-sm">
                                <div class="flex justify-between">
                                    <span class="text-slate-500">Procedure Type</span>
                                    <span class="font-medium">Surgical</span>
                                </div>
                                <div class="flex justify-between">
                                    <span class="text-slate-500">Anesthesia</span>
                                    <span class="font-medium">{p['anesthesia']}</span>
                                </div>
                                <div class="flex justify-between">
                                    <span class="text-slate-500">Procedure Time</span>
                                    <span class="font-medium">1-3 hours</span>
                                </div>
                                <div class="flex justify-between">
                                    <span class="text-slate-500">CPT Code</span>
                                    <span class="font-medium">{p['cpt_codes'][0]}</span>
                                </div>
                            </div>
                        </div>

                        <!-- CTA -->
                        <div class="bg-gradient-to-br from-primary to-secondary rounded-xl p-6 text-white">
                            <h3 class="font-bold text-lg mb-2">Find {p['short_name']} Providers</h3>
                            <p class="text-blue-100 text-sm mb-4">Compare 45+ verified sleep surgery specialists in your area.</p>
                            <a href="/locations/" class="block w-full bg-white text-primary text-center py-3 rounded-lg font-semibold hover:bg-blue-50 transition-colors">
                                View Providers
                            </a>
                        </div>

                        <!-- Other Procedures -->
                        <div class="bg-white rounded-xl shadow-lg p-6">
                            <h3 class="font-bold text-lg mb-4">Compare Procedures</h3>
                            <div class="space-y-3">
                                {compare_procedures_html}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Providers Section -->
    <section class="bg-white py-16" id="providers">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold mb-8 text-center">Find {p['short_name']} Providers Near You</h2>
            <p class="text-center text-slate-600 mb-12 max-w-2xl mx-auto">
                Compare 45+ verified sleep surgery specialists across the United States.
                All providers are experienced in {p['short_name']} and other sleep apnea surgical treatments.
            </p>
            <div class="text-center">
                <a href="/locations/" class="inline-flex items-center gap-2 bg-primary text-white px-8 py-4 rounded-xl font-semibold hover:bg-secondary transition-colors">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                    </svg>
                    Browse All Providers
                </a>
            </div>
        </div>
    </section>

    <!-- FAQ Section -->
    <section class="py-16 bg-slate-50">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-3xl font-bold mb-8 text-center">Frequently Asked Questions</h2>
            <div class="space-y-4">
                <div class="bg-white rounded-xl p-6 shadow-sm">
                    <h3 class="font-bold text-lg mb-2">How much does {p['short_name']} cost without insurance?</h3>
                    <p class="text-slate-600">Without insurance, {p['short_name']} typically costs between ${p['price_range']['low']:,} and ${p['price_range']['high']:,}, depending on the provider, location, and complexity of the case. Many providers offer payment plans or financing options.</p>
                </div>
                <div class="bg-white rounded-xl p-6 shadow-sm">
                    <h3 class="font-bold text-lg mb-2">Is {p['short_name']} covered by insurance?</h3>
                    <p class="text-slate-600">{'Yes, ' + p['short_name'] + ' is typically covered by insurance when deemed medically necessary for obstructive sleep apnea. Most patients need to have tried CPAP therapy first. Check with your insurance provider for specific coverage details.' if p['insurance_covered'] else 'Coverage varies by insurance plan. Contact your provider for specific details.'}</p>
                </div>
                <div class="bg-white rounded-xl p-6 shadow-sm">
                    <h3 class="font-bold text-lg mb-2">What is the success rate of {p['short_name']}?</h3>
                    <p class="text-slate-600">{p['short_name']} has a success rate of {p['success_rate']['min']}-{p['success_rate']['max']}% in reducing sleep apnea severity. The procedure can reduce AHI (apnea-hypopnea index) by {p['ahi_reduction']['min']}-{p['ahi_reduction']['max']}% on average.</p>
                </div>
                <div class="bg-white rounded-xl p-6 shadow-sm">
                    <h3 class="font-bold text-lg mb-2">How long is recovery after {p['short_name']}?</h3>
                    <p class="text-slate-600">Full recovery from {p['short_name']} typically takes {p['recovery_time']}. Most patients can return to work in {p['work_return']}. Hospital stay is usually {p['hospital_stay'].lower()}.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="bg-slate-900 text-slate-400 py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-4 gap-8">
                <div>
                    <div class="flex items-center gap-2 mb-4">
                        <div class="w-8 h-8 bg-primary rounded-lg flex items-center justify-center">
                            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>
                            </svg>
                        </div>
                        <span class="font-bold text-white">SleepApneaMatch</span>
                    </div>
                    <p class="text-sm">Connecting patients with verified sleep apnea surgery specialists nationwide.</p>
                </div>
                <div>
                    <h4 class="font-semibold text-white mb-4">Cost Guides</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/inspire-cost-guide/" class="hover:text-white">Inspire Therapy</a></li>
                        <li><a href="/mma-cost-guide/" class="hover:text-white">MMA Surgery</a></li>
                        <li><a href="/uppp-cost-guide/" class="hover:text-white">UPPP Surgery</a></li>
                        <li><a href="/tors-cost-guide/" class="hover:text-white">TORS</a></li>
                        <li><a href="/tonsillectomy-cost-guide/" class="hover:text-white">Tonsillectomy</a></li>
                        <li><a href="/septoplasty-cost-guide/" class="hover:text-white">Septoplasty</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-semibold text-white mb-4">Resources</h4>
                    <ul class="space-y-2 text-sm">
                        <li><a href="/locations/" class="hover:text-white">Find Providers</a></li>
                        <li><a href="/blog/" class="hover:text-white">Blog</a></li>
                        <li><a href="/faq/" class="hover:text-white">FAQ</a></li>
                    </ul>
                </div>
                <div>
                    <h4 class="font-semibold text-white mb-4">Medical Review</h4>
                    <div class="flex items-center gap-3">
                        <img src="/assets/images/dr_igor.jpg" alt="Dr. Igor I. Bussel" class="w-10 h-10 rounded-full object-cover">
                        <div class="text-sm">
                            <div class="text-white font-medium">Dr. Igor I. Bussel, MD</div>
                            <div class="text-xs">Board-Certified Physician</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="border-t border-slate-800 mt-12 pt-8 text-center text-sm">
                <p>&copy; 2026 SleepApneaMatch.com. All rights reserved.</p>
                <p class="mt-2 text-xs">Information provided is for educational purposes only and should not replace medical advice.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''
    return html


def main():
    """Generate all cost guide pages"""
    print("Generating procedure cost guide pages...")

    for procedure_id, procedure in PROCEDURES.items():
        # Create directory
        dir_path = Path(procedure['slug'])
        dir_path.mkdir(parents=True, exist_ok=True)

        # Generate main page
        html = generate_cost_guide_page(procedure_id)

        # Write file
        file_path = dir_path / 'index.html'
        with open(file_path, 'w') as f:
            f.write(html)

        print(f"  Generated: {file_path}")

    print(f"\nTotal cost guide pages generated: {len(PROCEDURES)}")


if __name__ == "__main__":
    main()
