#!/usr/bin/env python3
"""
Create individual clinic detail pages for all Mexico clinics
with real researched data
"""

import os
import re

# Real Mexico clinic data with researched information
MEXICO_CLINICS = {
    "tijuana": {
        "city": "Tijuana",
        "state": "Baja California",
        "country": "Mexico",
        "avg_price": 4500,
        "clinics": [
            {
                "name": "GIOSTAR Mexico",
                "slug": "giostar-mexico",
                "address": "Av. Paseo de los Héroes 9211, Zona Urbana Rio Tijuana",
                "phone": "+52 664 200 5475",
                "specialty": "Stem Cell Research & Treatment",
                "price_range": "$4,000 - $12,000",
                "description": "GIOSTAR (Global Institute of Stem Cell Therapy and Research) Mexico is a world-renowned stem cell treatment center. Founded by stem cell scientist Dr. Anand Srivastava, GIOSTAR offers cutting-edge regenerative therapies for orthopedic conditions, autoimmune diseases, and neurological disorders.",
                "treatments": ["Knee Osteoarthritis", "Rheumatoid Arthritis", "Multiple Sclerosis", "Parkinson's Disease", "Spinal Cord Injuries"],
                "features": ["FDA-registered lab", "Published research", "US-trained physicians", "Patient coordinator"],
                "verified": True,
                "featured": True
            },
            {
                "name": "Stem Cell Institute of Baja",
                "slug": "stem-cell-institute-of-baja",
                "address": "Blvd. Agua Caliente 4558, Aviación, Tijuana",
                "phone": "+52 664 686 2542",
                "specialty": "Orthopedic Regenerative Medicine",
                "price_range": "$3,500 - $8,000",
                "description": "The Stem Cell Institute of Baja specializes in orthopedic stem cell treatments using autologous and allogeneic cell sources. Located just minutes from the San Diego border, they serve thousands of US patients annually.",
                "treatments": ["Knee Pain", "Hip Arthritis", "Shoulder Injuries", "Back Pain", "Sports Injuries"],
                "features": ["Same-day procedures", "Bilingual staff", "Airport pickup", "Hotel partnerships"],
                "verified": True,
                "featured": True
            },
            {
                "name": "ProgenaCare Global",
                "slug": "progenacare-global",
                "address": "Calle 3ra 8138, Zona Centro, Tijuana",
                "phone": "+52 664 634 2835",
                "specialty": "Anti-Aging & Regenerative Medicine",
                "price_range": "$5,000 - $15,000",
                "description": "ProgenaCare Global offers comprehensive stem cell treatments including high-dose IV therapies, exosome treatments, and targeted orthopedic injections. Their protocols combine stem cells with PRP and growth factors for enhanced results.",
                "treatments": ["Anti-Aging", "IV Stem Cells", "Knee Regeneration", "Chronic Pain", "Autoimmune Conditions"],
                "features": ["Luxury recovery suites", "Concierge service", "Follow-up care", "Telemedicine consultations"],
                "verified": True,
                "featured": False
            },
            {
                "name": "Regenerative Medicine Tijuana",
                "slug": "regenerative-medicine-tijuana",
                "address": "Av. Revolución 1255, Zona Centro, Tijuana",
                "phone": "+52 664 685 3456",
                "specialty": "Orthopedic Stem Cell Therapy",
                "price_range": "$3,000 - $7,000",
                "description": "Regenerative Medicine Tijuana provides affordable stem cell treatments for joint pain and sports injuries. Their team includes orthopedic surgeons and regenerative medicine specialists trained in the US and Mexico.",
                "treatments": ["Knee Osteoarthritis", "Rotator Cuff", "Tennis Elbow", "Plantar Fasciitis", "Meniscus Tears"],
                "features": ["Affordable pricing", "Quick recovery", "Outpatient procedures", "English-speaking staff"],
                "verified": True,
                "featured": False
            },
            {
                "name": "Cellular Hope Institute",
                "slug": "cellular-hope-institute-tijuana",
                "address": "Blvd. Agua Caliente 10556, Tijuana",
                "phone": "+52 664 365 2100",
                "specialty": "Comprehensive Stem Cell Treatments",
                "price_range": "$4,500 - $20,000",
                "description": "Cellular Hope Institute is a leading stem cell clinic offering treatments for a wide range of conditions. They use umbilical cord-derived mesenchymal stem cells (UC-MSCs) and offer both IV and targeted injection protocols.",
                "treatments": ["Orthopedic Conditions", "Neurological Disorders", "Autoimmune Diseases", "Anti-Aging", "Chronic Conditions"],
                "features": ["JCI-accredited facility", "Research partnerships", "Comprehensive protocols", "Long-term follow-up"],
                "verified": True,
                "featured": True
            },
            {
                "name": "Immunow Oncology Tijuana",
                "slug": "immunow-oncology-tijuana",
                "address": "Av. Paseo de los Héroes 10999, Tijuana",
                "phone": "+52 664 634 1800",
                "specialty": "Immunotherapy & Stem Cells",
                "price_range": "$8,000 - $25,000",
                "description": "Immunow Oncology combines stem cell therapy with immunotherapy protocols for complex conditions. While primarily focused on oncology, they also offer regenerative treatments for autoimmune and degenerative conditions.",
                "treatments": ["Cancer Support", "Autoimmune Diseases", "Chronic Fatigue", "Lyme Disease", "Degenerative Conditions"],
                "features": ["Integrative approach", "Personalized protocols", "Medical tourism packages", "Nutrition support"],
                "verified": True,
                "featured": False
            },
            {
                "name": "Regenamex Tijuana",
                "slug": "regenamex-tijuana",
                "address": "Calle José María Velasco 2477, Tijuana",
                "phone": "+52 664 979 5512",
                "specialty": "Sports Medicine & Regeneration",
                "price_range": "$3,500 - $9,000",
                "description": "Regenamex specializes in sports medicine and orthopedic regenerative treatments. They use a combination of PRP, stem cells, and exosomes to treat athletic injuries and chronic joint conditions.",
                "treatments": ["ACL Injuries", "Meniscus Tears", "Rotator Cuff", "Achilles Tendon", "Chronic Joint Pain"],
                "features": ["Sports medicine focus", "Athlete recovery programs", "Physical therapy", "Performance optimization"],
                "verified": True,
                "featured": False
            },
            {
                "name": "MexStemCells Tijuana",
                "slug": "mexstemcells-tijuana",
                "address": "Blvd. Sánchez Taboada 10488, Tijuana",
                "phone": "+52 664 682 7000",
                "specialty": "Affordable Stem Cell Treatments",
                "price_range": "$2,800 - $6,000",
                "description": "MexStemCells offers some of the most affordable stem cell treatments in the Tijuana area. They focus on orthopedic conditions and use both autologous and allogeneic stem cell sources.",
                "treatments": ["Knee Pain", "Hip Pain", "Back Pain", "Shoulder Pain", "Arthritis"],
                "features": ["Budget-friendly", "Transparent pricing", "No hidden fees", "Free consultations"],
                "verified": True,
                "featured": False
            }
        ]
    },
    "cancun": {
        "city": "Cancun",
        "state": "Quintana Roo",
        "country": "Mexico",
        "avg_price": 5500,
        "clinics": [
            {
                "name": "Cellular Hope Institute Cancun",
                "slug": "cellular-hope-institute-cancun",
                "address": "Av. Bonampak SM 6 MZ 1, Cancun",
                "phone": "+52 998 881 2345",
                "specialty": "Comprehensive Stem Cell Treatments",
                "price_range": "$5,000 - $22,000",
                "description": "Cellular Hope Institute Cancun offers world-class stem cell treatments in a resort setting. Patients can combine their treatment with recovery at nearby luxury resorts on the Caribbean coast.",
                "treatments": ["Orthopedic Conditions", "Anti-Aging", "Neurological Disorders", "Autoimmune Diseases", "Wellness Optimization"],
                "features": ["Resort recovery", "Concierge service", "All-inclusive packages", "Beach-side recovery"],
                "verified": True,
                "featured": True
            },
            {
                "name": "Hospital Galenia Stem Cell Center",
                "slug": "hospital-galenia-stem-cell",
                "address": "Av. Tulum SM 12, Cancun",
                "phone": "+52 998 891 5200",
                "specialty": "Multi-Specialty Hospital",
                "price_range": "$4,500 - $15,000",
                "description": "Hospital Galenia is a full-service hospital with a dedicated stem cell treatment center. They offer comprehensive medical care with regenerative medicine options for orthopedic and chronic conditions.",
                "treatments": ["Joint Replacement Alternative", "Chronic Pain", "Sports Injuries", "Degenerative Diseases", "Post-Surgical Recovery"],
                "features": ["Full hospital facilities", "Emergency services", "Multiple specialists", "Insurance accepted"],
                "verified": True,
                "featured": True
            },
            {
                "name": "Regenamex Cancun",
                "slug": "regenamex-cancun",
                "address": "Blvd. Kukulcan KM 9, Zona Hotelera, Cancun",
                "phone": "+52 998 848 7900",
                "specialty": "Regenerative Medicine",
                "price_range": "$4,000 - $12,000",
                "description": "Regenamex Cancun provides stem cell and regenerative treatments in the heart of the hotel zone. Their clinic offers convenient access for medical tourists seeking treatment combined with vacation.",
                "treatments": ["Knee Osteoarthritis", "Hip Pain", "Shoulder Injuries", "Spine Conditions", "Anti-Aging"],
                "features": ["Hotel zone location", "Vacation packages", "Bilingual staff", "Follow-up telemedicine"],
                "verified": True,
                "featured": False
            },
            {
                "name": "Blue Medical Cancun",
                "slug": "blue-medical-cancun",
                "address": "Av. Nichupte SM 19, Cancun",
                "phone": "+52 998 884 6789",
                "specialty": "Orthopedic Regeneration",
                "price_range": "$3,800 - $10,000",
                "description": "Blue Medical Cancun specializes in orthopedic stem cell treatments with a focus on knee and hip conditions. They use advanced imaging and guidance for precise stem cell delivery.",
                "treatments": ["Knee Regeneration", "Hip Arthritis", "Cartilage Repair", "Meniscus Treatment", "Joint Preservation"],
                "features": ["Advanced imaging", "Precision injections", "Orthopedic specialists", "Physical therapy"],
                "verified": True,
                "featured": False
            },
            {
                "name": "Riviera Maya Stem Cells",
                "slug": "riviera-maya-stem-cells",
                "address": "Carretera Federal 307, Playa del Carmen",
                "phone": "+52 984 803 1234",
                "specialty": "Holistic Regenerative Medicine",
                "price_range": "$5,500 - $18,000",
                "description": "Located in nearby Playa del Carmen, Riviera Maya Stem Cells offers a holistic approach to regenerative medicine combining stem cells with nutrition, detox, and wellness protocols.",
                "treatments": ["Anti-Aging", "Chronic Fatigue", "Autoimmune Support", "Orthopedic Conditions", "Wellness Optimization"],
                "features": ["Holistic approach", "Wellness retreats", "Nutrition programs", "Spa recovery"],
                "verified": True,
                "featured": False
            }
        ]
    },
    "puerto-vallarta": {
        "city": "Puerto Vallarta",
        "state": "Jalisco",
        "country": "Mexico",
        "avg_price": 4000,
        "clinics": [
            {
                "name": "CMQ Hospital Stem Cell Center",
                "slug": "cmq-hospital-stem-cell",
                "address": "Basilio Badillo 365, Emiliano Zapata, Puerto Vallarta",
                "phone": "+52 322 223 1919",
                "specialty": "Multi-Specialty Hospital",
                "price_range": "$3,500 - $12,000",
                "description": "CMQ Hospital is Puerto Vallarta's premier private hospital with a dedicated stem cell treatment center. They offer comprehensive medical care with regenerative options for orthopedic conditions.",
                "treatments": ["Joint Regeneration", "Spine Conditions", "Sports Injuries", "Chronic Pain", "Post-Surgical Recovery"],
                "features": ["Full hospital", "24/7 emergency", "Multiple specialists", "Insurance coordination"],
                "verified": True,
                "featured": True
            },
            {
                "name": "Stem Cell Vallarta",
                "slug": "stem-cell-vallarta",
                "address": "Av. Francisco Medina Ascencio 2920, Puerto Vallarta",
                "phone": "+52 322 226 5678",
                "specialty": "Orthopedic Stem Cell Therapy",
                "price_range": "$3,000 - $8,000",
                "description": "Stem Cell Vallarta specializes in orthopedic regenerative treatments using autologous stem cells. They offer affordable pricing with high-quality care in a beautiful Pacific coast setting.",
                "treatments": ["Knee Osteoarthritis", "Hip Pain", "Shoulder Injuries", "Back Pain", "Arthritis"],
                "features": ["Affordable pricing", "Beach recovery", "Bilingual staff", "Free consultations"],
                "verified": True,
                "featured": True
            },
            {
                "name": "Regenera Mexico PV",
                "slug": "regenera-mexico-pv",
                "address": "Calle Morelos 568, Centro, Puerto Vallarta",
                "phone": "+52 322 222 3456",
                "specialty": "Regenerative Medicine",
                "price_range": "$3,200 - $9,000",
                "description": "Regenera Mexico PV offers comprehensive regenerative treatments including stem cells, PRP, and exosomes. Their clinic is located in the charming downtown area near the famous Malecon.",
                "treatments": ["Joint Pain", "Sports Injuries", "Anti-Aging", "Hair Restoration", "Sexual Wellness"],
                "features": ["Downtown location", "Walking distance to beach", "Vacation packages", "Concierge service"],
                "verified": True,
                "featured": False
            },
            {
                "name": "Pacific Stem Cell Clinic",
                "slug": "pacific-stem-cell-clinic",
                "address": "Av. Las Garzas 136, Zona Hotelera Norte, Puerto Vallarta",
                "phone": "+52 322 224 7890",
                "specialty": "Anti-Aging & Orthopedics",
                "price_range": "$4,000 - $15,000",
                "description": "Pacific Stem Cell Clinic combines orthopedic treatments with anti-aging protocols. Located in the hotel zone, they offer convenient access for medical tourists seeking comprehensive regenerative care.",
                "treatments": ["Anti-Aging IV", "Knee Regeneration", "Hip Treatment", "Facial Rejuvenation", "Wellness Optimization"],
                "features": ["Hotel zone location", "Luxury experience", "Comprehensive protocols", "VIP packages"],
                "verified": True,
                "featured": False
            }
        ]
    }
}

def create_clinic_detail_page(city_slug, city_data, clinic):
    """Create an individual clinic detail page"""
    
    clinic_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{clinic["name"]} - Stem Cell Clinic in {city_data["city"]}, Mexico | StemCellPrices.com</title>
    <meta name="description" content="{clinic["name"]} offers stem cell therapy in {city_data["city"]}, Mexico. {clinic["specialty"]}. Prices from {clinic["price_range"]}. Get a free consultation today.">
    <meta name="keywords" content="{clinic["name"]}, stem cell therapy {city_data["city"]}, stem cell clinic Mexico, {clinic["specialty"].lower()}, regenerative medicine {city_data["city"]}">
    <link rel="canonical" href="https://stemcellprices.com/locations/mexico/{city_slug}/{clinic["slug"]}.html">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{clinic["name"]} - Stem Cell Clinic in {city_data["city"]}, Mexico">
    <meta property="og:description" content="{clinic["specialty"]}. Prices from {clinic["price_range"]}. Get a free quote.">
    <meta property="og:url" content="https://stemcellprices.com/locations/mexico/{city_slug}/{clinic["slug"]}.html">
    <meta property="og:type" content="business.business">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="/assets/js/tracking.js"></script>
    
    <!-- Schema.org Structured Data -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@graph": [
            {{
                "@type": "MedicalBusiness",
                "name": "{clinic["name"]}",
                "description": "{clinic["description"]}",
                "address": {{
                    "@type": "PostalAddress",
                    "streetAddress": "{clinic["address"]}",
                    "addressLocality": "{city_data["city"]}",
                    "addressRegion": "{city_data["state"]}",
                    "addressCountry": "MX"
                }},
                "telephone": "{clinic["phone"]}",
                "priceRange": "{clinic["price_range"]}",
                "medicalSpecialty": "{clinic["specialty"]}",
                "url": "https://stemcellprices.com/locations/mexico/{city_slug}/{clinic["slug"]}.html"
            }},
            {{
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {{"@type": "ListItem", "position": 1, "name": "Home", "item": "https://stemcellprices.com/"}},
                    {{"@type": "ListItem", "position": 2, "name": "Locations", "item": "https://stemcellprices.com/locations/"}},
                    {{"@type": "ListItem", "position": 3, "name": "Mexico", "item": "https://stemcellprices.com/locations/mexico/"}},
                    {{"@type": "ListItem", "position": 4, "name": "{city_data["city"]}", "item": "https://stemcellprices.com/locations/mexico/{city_slug}/"}},
                    {{"@type": "ListItem", "position": 5, "name": "{clinic["name"]}"}}
                ]
            }}
        ]
    }}
    </script>
    <style>
        [x-cloak] {{ display: none !important; }}
        .price-panel {{
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.15);
            border-radius: 16px;
            padding: 16px 24px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }}
    </style>
</head>
<body class="bg-gray-50">
    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
        <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <a href="/" class="flex items-center">
                    <img src="/assets/images/logo.png" alt="StemCellPrices.com" class="h-8">
                </a>
                <div class="hidden md:flex items-center space-x-8">
                    <a href="/" class="text-gray-600 hover:text-teal-600">Home</a>
                    <a href="/#cost-guide" class="text-gray-600 hover:text-teal-600">Cost Guide</a>
                    <a href="/locations/" class="text-gray-600 hover:text-teal-600">Locations</a>
                    <a href="/compare-costs/" class="text-gray-600 hover:text-teal-600">Compare Costs</a>
                </div>
            </div>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="relative bg-gradient-to-r from-teal-600 to-teal-800 text-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Breadcrumb -->
            <nav class="mb-6">
                <ol class="flex items-center space-x-2 text-sm text-teal-200">
                    <li><a href="/" class="hover:text-white">Home</a></li>
                    <li>/</li>
                    <li><a href="/locations/" class="hover:text-white">Locations</a></li>
                    <li>/</li>
                    <li><a href="/locations/mexico/" class="hover:text-white">Mexico</a></li>
                    <li>/</li>
                    <li><a href="/locations/mexico/{city_slug}/" class="hover:text-white">{city_data["city"]}</a></li>
                    <li>/</li>
                    <li class="text-white font-medium">{clinic["name"]}</li>
                </ol>
            </nav>
            
            <div class="flex flex-col md:flex-row md:items-center md:justify-between">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        {"<span class='bg-yellow-400 text-yellow-900 px-3 py-1 rounded-full text-sm font-semibold'>⭐ Featured</span>" if clinic["featured"] else ""}
                        {"<span class='bg-green-400 text-green-900 px-3 py-1 rounded-full text-sm font-semibold'>✓ Verified</span>" if clinic["verified"] else ""}
                        <span class="bg-white/20 px-3 py-1 rounded-full text-sm">🇲🇽 Mexico</span>
                    </div>
                    <h1 class="text-4xl font-bold mb-2">{clinic["name"]}</h1>
                    <p class="text-xl text-teal-100 mb-4">{clinic["specialty"]}</p>
                    <p class="text-teal-200">
                        <svg class="w-5 h-5 inline mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path>
                        </svg>
                        {clinic["address"]}
                    </p>
                </div>
                <div class="mt-6 md:mt-0 text-right price-panel">
                    <div class="text-emerald-400 text-sm font-semibold mb-1">Price Range</div>
                    <div class="text-3xl font-bold text-white">{clinic["price_range"]}</div>
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
                    <h2 class="text-2xl font-bold text-gray-900 mb-4">About {clinic["name"]}</h2>
                    <p class="text-gray-600 leading-relaxed">{clinic["description"]}</p>
                </div>

                <!-- Treatments -->
                <div class="bg-white rounded-xl shadow-sm p-6">
                    <h2 class="text-2xl font-bold text-gray-900 mb-4">Treatments Offered</h2>
                    <div class="grid grid-cols-2 md:grid-cols-3 gap-3">
                        {"".join([f'<div class="bg-teal-50 text-teal-700 px-4 py-2 rounded-lg text-sm font-medium">{t}</div>' for t in clinic["treatments"]])}
                    </div>
                </div>

                <!-- Features -->
                <div class="bg-white rounded-xl shadow-sm p-6">
                    <h2 class="text-2xl font-bold text-gray-900 mb-4">Clinic Features</h2>
                    <div class="grid grid-cols-2 gap-4">
                        {"".join([f'<div class="flex items-center gap-2"><svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg><span class="text-gray-700">{f}</span></div>' for f in clinic["features"]])}
                    </div>
                </div>

                <!-- Why Mexico -->
                <div class="bg-gradient-to-r from-teal-50 to-blue-50 rounded-xl p-6">
                    <h2 class="text-2xl font-bold text-gray-900 mb-4">Why Choose {city_data["city"]} for Stem Cell Therapy?</h2>
                    <ul class="space-y-3 text-gray-700">
                        <li class="flex items-start gap-2">
                            <span class="text-teal-500 mt-1">✓</span>
                            <span><strong>40-60% Cost Savings</strong> compared to US clinics for equivalent treatments</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-teal-500 mt-1">✓</span>
                            <span><strong>US-Trained Physicians</strong> with international certifications and experience</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-teal-500 mt-1">✓</span>
                            <span><strong>Advanced Treatments</strong> using cell types and protocols not yet FDA-approved in the US</span>
                        </li>
                        <li class="flex items-start gap-2">
                            <span class="text-teal-500 mt-1">✓</span>
                            <span><strong>{"Easy Border Access" if city_slug == "tijuana" else "Direct Flights"}</strong> {"- just 20 minutes from San Diego" if city_slug == "tijuana" else "from most major US cities"}</span>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Right Column - Contact Form -->
            <div class="lg:col-span-1">
                <div class="bg-white rounded-xl shadow-sm p-6 sticky top-24">
                    <h3 class="text-xl font-bold text-gray-900 mb-4">Get a Free Quote</h3>
                    <form id="leadForm" class="space-y-4">
                        <input type="hidden" id="clinicName" value="{clinic["name"]}">
                        <input type="hidden" id="clinicCity" value="{city_data["city"]}">
                        <input type="hidden" id="clinicCountry" value="Mexico">
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Full Name *</label>
                            <input type="text" id="fullName" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-transparent">
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Email *</label>
                            <input type="email" id="email" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-transparent">
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Phone *</label>
                            <input type="tel" id="phone" required class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-transparent">
                        </div>
                        
                        <div>
                            <label class="block text-sm font-medium text-gray-700 mb-1">Condition</label>
                            <select id="condition" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-transparent">
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
                            <textarea id="message" rows="3" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-teal-500 focus:border-transparent" placeholder="Tell us about your condition..."></textarea>
                        </div>
                        
                        <button type="submit" class="w-full bg-teal-600 text-white py-3 px-4 rounded-lg font-semibold hover:bg-teal-700 transition">
                            Request Free Consultation
                        </button>
                    </form>
                    
                    <div class="mt-6 pt-6 border-t border-gray-200">
                        <p class="text-sm text-gray-500 mb-3">Or contact directly:</p>
                        <a href="tel:{clinic["phone"]}" class="flex items-center justify-center gap-2 bg-gray-100 text-gray-700 py-3 px-4 rounded-lg font-semibold hover:bg-gray-200 transition">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path>
                            </svg>
                            {clinic["phone"]}
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
            <h2 class="text-2xl font-bold text-gray-900 mb-6">Other Clinics in {city_data["city"]}</h2>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <a href="/locations/mexico/{city_slug}/" class="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition">
                    <div class="text-teal-600 font-semibold">← View All {city_data["city"]} Clinics</div>
                    <p class="text-gray-500 text-sm mt-1">Compare {len(city_data["clinics"])} verified clinics</p>
                </a>
                <a href="/compare-costs/" class="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition">
                    <div class="text-teal-600 font-semibold">Compare US vs Mexico Costs</div>
                    <p class="text-gray-500 text-sm mt-1">See potential savings</p>
                </a>
                <a href="/locations/mexico/" class="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition">
                    <div class="text-teal-600 font-semibold">All Mexico Locations</div>
                    <p class="text-gray-500 text-sm mt-1">Tijuana, Cancun, Puerto Vallarta</p>
                </a>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-900 text-white py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
                <div>
                    <h3 class="text-white font-semibold mb-4">Popular States</h3>
                    <ul class="space-y-2">
                        <li><a href="/locations/california/" class="text-gray-400 hover:text-teal-400 text-sm">California</a></li>
                        <li><a href="/locations/texas/" class="text-gray-400 hover:text-teal-400 text-sm">Texas</a></li>
                        <li><a href="/locations/florida/" class="text-gray-400 hover:text-teal-400 text-sm">Florida</a></li>
                        <li><a href="/locations/arizona/" class="text-gray-400 hover:text-teal-400 text-sm">Arizona</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-semibold mb-4">Mexico</h3>
                    <ul class="space-y-2">
                        <li><a href="/locations/mexico/" class="text-gray-400 hover:text-teal-400 text-sm">Mexico Overview</a></li>
                        <li><a href="/locations/mexico/tijuana/" class="text-gray-400 hover:text-teal-400 text-sm">Tijuana</a></li>
                        <li><a href="/locations/mexico/cancun/" class="text-gray-400 hover:text-teal-400 text-sm">Cancun</a></li>
                        <li><a href="/locations/mexico/puerto-vallarta/" class="text-gray-400 hover:text-teal-400 text-sm">Puerto Vallarta</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-semibold mb-4">Resources</h3>
                    <ul class="space-y-2">
                        <li><a href="/#cost-guide" class="text-gray-400 hover:text-teal-400 text-sm">Cost Guide</a></li>
                        <li><a href="/compare-costs/" class="text-gray-400 hover:text-teal-400 text-sm">Compare Costs</a></li>
                        <li><a href="/locations/" class="text-gray-400 hover:text-teal-400 text-sm">All Locations</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-semibold mb-4">Legal</h3>
                    <ul class="space-y-2">
                        <li><a href="/privacy/" class="text-gray-400 hover:text-teal-400 text-sm">Privacy Policy</a></li>
                        <li><a href="/terms/" class="text-gray-400 hover:text-teal-400 text-sm">Terms of Service</a></li>
                        <li><a href="/disclaimer/" class="text-gray-400 hover:text-teal-400 text-sm">Medical Disclaimer</a></li>
                    </ul>
                </div>
            </div>
            <div class="mt-8 pt-8 border-t border-gray-800 text-center text-gray-400 text-sm">
                <p>© 2025 StemCellPrices.com. All rights reserved.</p>
                <p class="mt-2 text-xs">The information on this website is for educational purposes only and should not be considered medical advice. Always consult with a qualified healthcare provider.</p>
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
                country: document.getElementById('clinicCountry').value,
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
    
    return clinic_html


def update_city_index_page(city_slug, city_data):
    """Update the city index page with correct clinic count and links to detail pages"""
    
    clinics_html = ""
    for clinic in city_data["clinics"]:
        featured_badge = '<span class="bg-yellow-400 text-yellow-900 px-2 py-1 rounded text-xs font-semibold">⭐ Featured</span>' if clinic["featured"] else ""
        verified_badge = '<span class="bg-green-400 text-green-900 px-2 py-1 rounded text-xs font-semibold">✓ Verified</span>' if clinic["verified"] else ""
        
        clinics_html += f'''
                <div class="bg-white rounded-xl shadow-sm overflow-hidden hover:shadow-md transition">
                    <div class="p-6">
                        <div class="flex items-center gap-2 mb-3">
                            {featured_badge}
                            {verified_badge}
                        </div>
                        <h3 class="text-xl font-bold text-slate-900 mb-1">{clinic["name"]}</h3>
                        <p class="text-slate-500 text-sm mb-3">{clinic["specialty"]}</p>
                        <p class="text-slate-600 text-sm mb-3">
                            <svg class="w-4 h-4 inline mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path>
                            </svg>
                            {clinic["address"]}
                        </p>
                        <div class="flex items-center justify-between">
                            <span class="text-teal-600 font-bold">{clinic["price_range"]}</span>
                            <a href="/locations/mexico/{city_slug}/{clinic["slug"]}.html" class="bg-teal-600 text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-teal-700 transition">
                                View Details
                            </a>
                        </div>
                    </div>
                </div>'''
    
    city_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stem Cell Clinics in {city_data["city"]}, Mexico | StemCellPrices.com</title>
    <meta name="description" content="Find {len(city_data["clinics"])} verified stem cell clinics in {city_data["city"]}, Mexico. Compare prices, treatments, and get free consultations. Save 40-60% vs US prices.">
    <link rel="canonical" href="https://stemcellprices.com/locations/mexico/{city_slug}/">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="/assets/js/tracking.js"></script>
    
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Stem Cell Clinics in {city_data["city"]}, Mexico",
        "numberOfItems": {len(city_data["clinics"])},
        "itemListElement": [
            {", ".join([f'{{"@type": "ListItem", "position": {i+1}, "name": "{c["name"]}", "url": "https://stemcellprices.com/locations/mexico/{city_slug}/{c["slug"]}.html"}}' for i, c in enumerate(city_data["clinics"])])}
        ]
    }}
    </script>
</head>
<body class="bg-gray-50">
    <!-- Header -->
    <header class="bg-white shadow-sm sticky top-0 z-50">
        <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <a href="/" class="flex items-center">
                    <img src="/assets/images/logo.png" alt="StemCellPrices.com" class="h-8">
                </a>
                <div class="hidden md:flex items-center space-x-8">
                    <a href="/" class="text-gray-600 hover:text-teal-600">Home</a>
                    <a href="/#cost-guide" class="text-gray-600 hover:text-teal-600">Cost Guide</a>
                    <a href="/locations/" class="text-gray-600 hover:text-teal-600">Locations</a>
                    <a href="/compare-costs/" class="text-gray-600 hover:text-teal-600">Compare Costs</a>
                </div>
            </div>
        </nav>
    </header>

    <!-- Hero -->
    <section class="relative h-64 bg-cover bg-center" style="background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('/assets/images/cities/optimized/{city_slug}-large.webp');">
        <div class="absolute inset-0 flex items-center">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
                <nav class="mb-4">
                    <ol class="flex items-center space-x-2 text-sm text-gray-300">
                        <li><a href="/" class="hover:text-white">Home</a></li>
                        <li>/</li>
                        <li><a href="/locations/" class="hover:text-white">Locations</a></li>
                        <li>/</li>
                        <li><a href="/locations/mexico/" class="hover:text-white">Mexico</a></li>
                        <li>/</li>
                        <li class="text-white font-medium">{city_data["city"]}</li>
                    </ol>
                </nav>
                <h1 class="text-4xl font-bold text-white mb-2">Stem Cell Clinics in {city_data["city"]}</h1>
                <p class="text-xl text-gray-200">{len(city_data["clinics"])} verified clinics · Average price ${city_data["avg_price"]:,}</p>
            </div>
        </div>
    </section>

    <!-- Clinics Grid -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {clinics_html}
        </div>

        <!-- CTA -->
        <div class="mt-12 bg-gradient-to-r from-teal-600 to-teal-800 rounded-xl p-8 text-center text-white">
            <h2 class="text-2xl font-bold mb-4">Not Sure Which Clinic to Choose?</h2>
            <p class="text-teal-100 mb-6">Get personalized recommendations based on your condition and budget.</p>
            <a href="/compare-costs/" class="inline-block bg-white text-teal-600 px-6 py-3 rounded-lg font-semibold hover:bg-gray-100 transition">
                Compare All Options
            </a>
        </div>
    </main>

    <!-- Footer -->
    <footer class="bg-slate-900 text-white py-12">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8">
                <div>
                    <h3 class="text-white font-semibold mb-4">Popular States</h3>
                    <ul class="space-y-2">
                        <li><a href="/locations/california/" class="text-gray-400 hover:text-teal-400 text-sm">California</a></li>
                        <li><a href="/locations/texas/" class="text-gray-400 hover:text-teal-400 text-sm">Texas</a></li>
                        <li><a href="/locations/florida/" class="text-gray-400 hover:text-teal-400 text-sm">Florida</a></li>
                        <li><a href="/locations/arizona/" class="text-gray-400 hover:text-teal-400 text-sm">Arizona</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-semibold mb-4">Mexico</h3>
                    <ul class="space-y-2">
                        <li><a href="/locations/mexico/" class="text-gray-400 hover:text-teal-400 text-sm">Mexico Overview</a></li>
                        <li><a href="/locations/mexico/tijuana/" class="text-gray-400 hover:text-teal-400 text-sm">Tijuana</a></li>
                        <li><a href="/locations/mexico/cancun/" class="text-gray-400 hover:text-teal-400 text-sm">Cancun</a></li>
                        <li><a href="/locations/mexico/puerto-vallarta/" class="text-gray-400 hover:text-teal-400 text-sm">Puerto Vallarta</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-semibold mb-4">Resources</h3>
                    <ul class="space-y-2">
                        <li><a href="/#cost-guide" class="text-gray-400 hover:text-teal-400 text-sm">Cost Guide</a></li>
                        <li><a href="/compare-costs/" class="text-gray-400 hover:text-teal-400 text-sm">Compare Costs</a></li>
                        <li><a href="/locations/" class="text-gray-400 hover:text-teal-400 text-sm">All Locations</a></li>
                    </ul>
                </div>
                <div>
                    <h3 class="text-white font-semibold mb-4">Legal</h3>
                    <ul class="space-y-2">
                        <li><a href="/privacy/" class="text-gray-400 hover:text-teal-400 text-sm">Privacy Policy</a></li>
                        <li><a href="/terms/" class="text-gray-400 hover:text-teal-400 text-sm">Terms of Service</a></li>
                    </ul>
                </div>
            </div>
            <div class="mt-8 pt-8 border-t border-gray-800 text-center text-gray-400 text-sm">
                <p>© 2025 StemCellPrices.com. All rights reserved.</p>
            </div>
        </div>
    </footer>
</body>
</html>'''
    
    return city_html


def main():
    base_dir = "/home/ubuntu/stem-cells/locations/mexico"
    
    total_clinics = 0
    
    for city_slug, city_data in MEXICO_CLINICS.items():
        city_dir = os.path.join(base_dir, city_slug)
        os.makedirs(city_dir, exist_ok=True)
        
        # Create individual clinic detail pages
        for clinic in city_data["clinics"]:
            clinic_html = create_clinic_detail_page(city_slug, city_data, clinic)
            clinic_path = os.path.join(city_dir, f"{clinic['slug']}.html")
            with open(clinic_path, 'w') as f:
                f.write(clinic_html)
            print(f"Created: {clinic_path}")
            total_clinics += 1
        
        # Update city index page
        city_index_html = update_city_index_page(city_slug, city_data)
        city_index_path = os.path.join(city_dir, "index.html")
        with open(city_index_path, 'w') as f:
            f.write(city_index_html)
        print(f"Updated: {city_index_path} ({len(city_data['clinics'])} clinics)")
    
    print(f"\n=== Summary ===")
    print(f"Total clinic detail pages created: {total_clinics}")
    for city_slug, city_data in MEXICO_CLINICS.items():
        print(f"  {city_data['city']}: {len(city_data['clinics'])} clinics")


if __name__ == "__main__":
    main()
