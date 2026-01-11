#!/usr/bin/env python3
"""
Generate Blog Pages for SleepApneaMatch.com
Creates blog posts from FAQ data with Dr. Igor medical review
"""

import json
import os
import re
from pathlib import Path

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')[:60]

# Blog post templates from FAQ data - map FAQ ids to blog topics
BLOG_POSTS = [
    {
        'faq_id': 'faq-001',
        'title': 'Is Sleep Apnea Surgery Covered by Insurance? Complete 2026 Guide',
        'slug': 'sleep-apnea-surgery-insurance-coverage',
        'excerpt': 'Learn about insurance requirements for sleep apnea surgery, including CPAP prerequisites, coverage details, and what to expect from your provider.'
    },
    {
        'faq_id': 'faq-002',
        'title': 'Sleep Apnea Surgery Success Rates: What to Expect in 2026',
        'slug': 'sleep-apnea-surgery-success-rates',
        'excerpt': 'Compare success rates for different sleep apnea procedures including MMA (85-95%), UPPP (40-60%), and Inspire therapy (66-75%).'
    },
    {
        'faq_id': 'faq-006',
        'title': 'UPPP vs Inspire: Comparing Sleep Apnea Surgical Treatments',
        'slug': 'uppp-vs-inspire-comparison',
        'excerpt': 'An in-depth comparison of traditional UPPP surgery versus Inspire therapy for treating obstructive sleep apnea.'
    },
    {
        'faq_id': 'faq-010',
        'title': 'How to Find the Best Sleep Apnea Surgeon: Credentials & Tips',
        'slug': 'how-to-find-sleep-apnea-surgeon',
        'excerpt': 'Expert advice on finding a qualified sleep apnea surgeon, including board certifications, credentials, and what questions to ask.'
    },
    {
        'faq_id': 'faq-003',
        'title': 'Sleep Apnea Surgery Recovery: A Complete Guide',
        'slug': 'sleep-apnea-surgery-recovery-guide',
        'excerpt': 'Everything you need to know about recovering from sleep apnea surgery, including timelines, pain management, and return to work.'
    },
    {
        'faq_id': 'faq-008',
        'title': 'Is Sleep Apnea Surgery Worth It? Pros, Cons & Success Rates',
        'slug': 'is-sleep-apnea-surgery-worth-it',
        'excerpt': 'A balanced look at the benefits and risks of sleep apnea surgery to help you make an informed decision about your treatment.'
    },
    {
        'faq_id': 'faq-019',
        'title': 'Pediatric Sleep Apnea Surgery: Treatment Options for Children',
        'slug': 'pediatric-sleep-apnea-surgery-children',
        'excerpt': 'Learn about sleep apnea surgery options for children, including adenotonsillectomy success rates and when surgery is recommended.'
    },
    {
        'faq_id': 'faq-018',
        'title': 'What is DISE? Understanding Drug-Induced Sleep Endoscopy',
        'slug': 'what-is-dise-sleep-endoscopy',
        'excerpt': 'A comprehensive guide to DISE (Drug-Induced Sleep Endoscopy) and why it may be required before sleep apnea surgery.'
    },
    {
        'faq_id': 'faq-016',
        'title': 'Sleep Apnea Surgery Costs Without Insurance: 2026 Price Guide',
        'slug': 'sleep-apnea-surgery-costs-without-insurance',
        'excerpt': 'Complete breakdown of sleep apnea surgery costs without insurance, from $3,000 nasal procedures to $100,000 jaw surgery.'
    },
    {
        'faq_id': 'faq-020',
        'title': '15 Questions to Ask Your Sleep Surgeon Before Surgery',
        'slug': 'questions-to-ask-sleep-surgeon',
        'excerpt': 'Essential questions to ask your sleep apnea surgeon before your procedure, covering experience, risks, and recovery expectations.'
    }
]


def load_faqs():
    """Load FAQ data from JSON file"""
    with open('api/faqs.json', 'r') as f:
        data = json.load(f)
    return {faq['id']: faq for faq in data['faqs']}


def generate_blog_post(post, faq):
    """Generate a single blog post HTML"""

    # Clean up the answer text for HTML
    answer = faq['answer'].replace('\n\n', '</p><p class="text-slate-600 mb-4 leading-relaxed">')
    answer = f'<p class="text-slate-600 mb-4 leading-relaxed">{answer}</p>'

    # Parse sources
    sources_html = ""
    if faq.get('sources'):
        sources = faq['sources'].split(', ') if ', ' in faq['sources'] else faq['sources'].split('\n')
        sources_html = '<ul class="list-disc list-inside space-y-1">'
        for source in sources:
            if 'http' in source:
                url = re.search(r'https?://[^\s\)]+', source)
                if url:
                    sources_html += f'<li><a href="{url.group()}" target="_blank" rel="noopener" class="text-primary hover:underline break-all">{url.group()}</a></li>'
        sources_html += '</ul>'

    # Related procedures
    procedures_html = ""
    if faq.get('related_procedures'):
        procs = [p.strip() for p in faq['related_procedures'].split(',')]
        procedures_html = '<div class="flex flex-wrap gap-2">'
        for proc in procs[:6]:  # Limit to 6
            procedures_html += f'<span class="bg-primary/10 text-primary px-3 py-1 rounded-full text-sm">{proc}</span>'
        procedures_html += '</div>'

    # Build related and sources sections
    related_section = ""
    if procedures_html:
        related_section = f'''<div class="mt-12 pt-8 border-t">
                <h3 class="font-bold text-lg mb-4">Related Procedures</h3>
                {procedures_html}
            </div>'''

    sources_section = ""
    if sources_html:
        sources_section = f'''<div class="mt-8 pt-8 border-t">
                <h3 class="font-bold text-lg mb-4">Sources & References</h3>
                <div class="text-sm text-slate-600">
                    {sources_html}
                </div>
            </div>'''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post['title']} | SleepApneaMatch.com</title>
    <meta name="description" content="{post['excerpt']}">
    <meta name="keywords" content="{faq.get('seo_keywords', 'sleep apnea surgery, sleep apnea treatment')}">

    <!-- Open Graph -->
    <meta property="og:title" content="{post['title']}">
    <meta property="og:description" content="{post['excerpt']}">
    <meta property="og:image" content="https://sleepapneamatch.com/assets/images/og-blog.jpg">
    <meta property="og:url" content="https://sleepapneamatch.com/blog/{post['slug']}/">
    <meta property="og:type" content="article">

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{post['title']}">
    <meta name="twitter:description" content="{post['excerpt']}">

    <!-- Canonical -->
    <link rel="canonical" href="https://sleepapneamatch.com/blog/{post['slug']}/">

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

    <!-- Schema.org Article -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "MedicalWebPage",
        "headline": "{post['title']}",
        "description": "{post['excerpt']}",
        "url": "https://sleepapneamatch.com/blog/{post['slug']}/",
        "datePublished": "2026-01-10",
        "dateModified": "2026-01-10",
        "author": {{
            "@type": "Organization",
            "name": "SleepApneaMatch.com"
        }},
        "publisher": {{
            "@type": "Organization",
            "name": "SleepApneaMatch.com",
            "logo": {{
                "@type": "ImageObject",
                "url": "https://sleepapneamatch.com/assets/images/logo.png"
            }}
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
            "@type": "MedicalCondition",
            "name": "Obstructive Sleep Apnea"
        }}
    }}
    </script>
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
                            <a href="/uppp-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">UPPP Surgery</a>
                            <a href="/inspire-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">Inspire Therapy</a>
                            <a href="/mma-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">MMA Surgery</a>
                            <a href="/septoplasty-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">Septoplasty</a>
                        </div>
                    </div>
                    <a href="/blog/" class="text-primary font-medium">Blog</a>
                    <a href="/faq/" class="text-slate-600 hover:text-primary">FAQ</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Breadcrumbs -->
    <div class="bg-slate-100 border-b">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
            <nav class="flex text-sm">
                <a href="/" class="text-slate-500 hover:text-primary">Home</a>
                <span class="mx-2 text-slate-400">/</span>
                <a href="/blog/" class="text-slate-500 hover:text-primary">Blog</a>
                <span class="mx-2 text-slate-400">/</span>
                <span class="text-slate-700 truncate">{post['title'][:40]}...</span>
            </nav>
        </div>
    </div>

    <!-- Article -->
    <article class="py-12">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <!-- Header -->
            <header class="mb-8">
                <div class="flex items-center gap-2 text-sm text-slate-500 mb-4">
                    <span class="bg-primary/10 text-primary px-2 py-1 rounded">{faq.get('category', 'General')}</span>
                    <span>January 10, 2026</span>
                    <span>10 min read</span>
                </div>
                <h1 class="text-3xl md:text-4xl font-bold text-slate-900 mb-4">{post['title']}</h1>
                <p class="text-xl text-slate-600">{post['excerpt']}</p>
            </header>

            <!-- Medical Review Badge -->
            <div class="bg-gradient-to-br from-slate-50 to-slate-100 rounded-2xl p-6 border mb-8">
                <div class="flex items-center gap-4">
                    <img src="/assets/images/dr_igor.jpg" alt="Dr. Igor I. Bussel, MD" class="w-16 h-16 rounded-full object-cover border-2 border-white shadow">
                    <div>
                        <div class="flex items-center gap-2">
                            <span class="font-bold text-slate-800">Medically Reviewed by Dr. Igor I. Bussel, MD</span>
                            <svg class="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                            </svg>
                        </div>
                        <p class="text-sm text-slate-500">Board-Certified Physician | UCI Gavin Herbert Eye Institute</p>
                        <p class="text-xs text-slate-400 mt-1">Last reviewed and updated: January 2026</p>
                    </div>
                </div>
            </div>

            <!-- Content -->
            <div class="prose prose-lg max-w-none">
                {answer}
            </div>

            <!-- Related Procedures -->
            {related_section}

            <!-- Sources -->
            {sources_section}

            <!-- CTA -->
            <div class="mt-12 bg-gradient-to-br from-primary to-secondary rounded-2xl p-8 text-white text-center">
                <h3 class="text-2xl font-bold mb-2">Find Sleep Apnea Specialists Near You</h3>
                <p class="text-blue-100 mb-6">Compare 45+ verified sleep surgery providers across the United States.</p>
                <a href="/locations/" class="inline-block bg-white text-primary px-8 py-3 rounded-xl font-semibold hover:bg-blue-50 transition-colors">
                    Browse Providers
                </a>
            </div>
        </div>
    </article>

    <!-- Related Posts -->
    <section class="bg-white py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <h2 class="text-2xl font-bold mb-8">More Articles</h2>
            <div class="grid md:grid-cols-2 gap-6">
                <a href="/blog/" class="block p-6 bg-slate-50 rounded-xl hover:bg-slate-100 transition-colors">
                    <span class="text-primary font-semibold">View All Articles &rarr;</span>
                    <p class="text-sm text-slate-500 mt-1">Browse our complete sleep apnea surgery resource library</p>
                </a>
                <a href="/faq/" class="block p-6 bg-slate-50 rounded-xl hover:bg-slate-100 transition-colors">
                    <span class="text-primary font-semibold">Frequently Asked Questions &rarr;</span>
                    <p class="text-sm text-slate-500 mt-1">Get quick answers to common sleep apnea surgery questions</p>
                </a>
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
                        <li><a href="/uppp-cost-guide/" class="hover:text-white">UPPP Surgery</a></li>
                        <li><a href="/inspire-cost-guide/" class="hover:text-white">Inspire Therapy</a></li>
                        <li><a href="/mma-cost-guide/" class="hover:text-white">MMA Surgery</a></li>
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


def generate_blog_index(posts, faqs):
    """Generate the blog index page"""

    posts_html = ""
    for post in posts:
        faq = faqs.get(post['faq_id'], {})
        posts_html += f'''
            <article class="bg-white rounded-xl shadow-sm overflow-hidden hover:shadow-lg transition-shadow">
                <a href="/blog/{post['slug']}/" class="block p-6">
                    <div class="flex items-center gap-2 text-sm text-slate-500 mb-2">
                        <span class="bg-primary/10 text-primary px-2 py-1 rounded text-xs">{faq.get('category', 'General')}</span>
                        <span>January 2026</span>
                    </div>
                    <h2 class="text-xl font-bold text-slate-900 mb-2 hover:text-primary transition-colors">{post['title']}</h2>
                    <p class="text-slate-600 mb-4">{post['excerpt']}</p>
                    <span class="text-primary font-medium">Read more &rarr;</span>
                </a>
            </article>
        '''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sleep Apnea Surgery Blog | Expert Insights & Research | SleepApneaMatch.com</title>
    <meta name="description" content="Expert articles on sleep apnea surgery, treatment options, success rates, and recovery. Medically reviewed by Dr. Igor I. Bussel, MD.">

    <!-- Open Graph -->
    <meta property="og:title" content="Sleep Apnea Surgery Blog | SleepApneaMatch.com">
    <meta property="og:description" content="Expert articles on sleep apnea surgery, treatment options, success rates, and recovery.">
    <meta property="og:url" content="https://sleepapneamatch.com/blog/">
    <meta property="og:type" content="website">

    <!-- Canonical -->
    <link rel="canonical" href="https://sleepapneamatch.com/blog/">

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
        "@type": "Blog",
        "name": "SleepApneaMatch Blog",
        "description": "Expert articles on sleep apnea surgery and treatment",
        "url": "https://sleepapneamatch.com/blog/",
        "publisher": {{
            "@type": "Organization",
            "name": "SleepApneaMatch.com"
        }}
    }}
    </script>
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
                            <a href="/uppp-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">UPPP Surgery</a>
                            <a href="/inspire-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">Inspire Therapy</a>
                            <a href="/mma-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">MMA Surgery</a>
                            <a href="/septoplasty-cost-guide/" class="block px-4 py-2 text-sm text-slate-600 hover:bg-slate-50 rounded-lg">Septoplasty</a>
                        </div>
                    </div>
                    <a href="/blog/" class="text-primary font-medium">Blog</a>
                    <a href="/faq/" class="text-slate-600 hover:text-primary">FAQ</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero -->
    <section class="bg-gradient-to-br from-primary to-secondary text-white py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">Sleep Apnea Surgery Blog</h1>
            <p class="text-xl text-blue-100 max-w-2xl mx-auto">Expert articles on sleep apnea surgery, treatment options, success rates, and recovery. All content medically reviewed by Dr. Igor I. Bussel, MD.</p>
        </div>
    </section>

    <!-- Medical Review Badge -->
    <div class="bg-white border-b">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <div class="flex items-center justify-center gap-4">
                <img src="/assets/images/dr_igor.jpg" alt="Dr. Igor I. Bussel, MD" class="w-10 h-10 rounded-full object-cover">
                <div class="flex items-center gap-2">
                    <span class="text-sm text-slate-700">All articles medically reviewed by <strong>Dr. Igor I. Bussel, MD</strong></span>
                    <svg class="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                    </svg>
                </div>
            </div>
        </div>
    </div>

    <!-- Blog Posts -->
    <section class="py-16">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                {posts_html}
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="bg-slate-100 py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl font-bold mb-4">Find Sleep Apnea Specialists</h2>
            <p class="text-slate-600 mb-8">Compare 45+ verified sleep surgery providers across the United States.</p>
            <a href="/locations/" class="inline-block bg-primary text-white px-8 py-4 rounded-xl font-semibold hover:bg-secondary transition-colors">
                Browse All Providers
            </a>
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
                        <li><a href="/uppp-cost-guide/" class="hover:text-white">UPPP Surgery</a></li>
                        <li><a href="/inspire-cost-guide/" class="hover:text-white">Inspire Therapy</a></li>
                        <li><a href="/mma-cost-guide/" class="hover:text-white">MMA Surgery</a></li>
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
    """Generate all blog pages"""
    print("Generating blog pages...")

    # Load FAQs
    faqs = load_faqs()

    # Create blog directory
    blog_dir = Path('blog')
    blog_dir.mkdir(exist_ok=True)

    # Generate blog index
    index_html = generate_blog_index(BLOG_POSTS, faqs)
    with open(blog_dir / 'index.html', 'w') as f:
        f.write(index_html)
    print(f"  Generated: blog/index.html")

    # Generate individual posts
    for post in BLOG_POSTS:
        faq = faqs.get(post['faq_id'])
        if not faq:
            print(f"  Warning: FAQ {post['faq_id']} not found, skipping")
            continue

        # Create post directory
        post_dir = blog_dir / post['slug']
        post_dir.mkdir(exist_ok=True)

        # Generate post
        post_html = generate_blog_post(post, faq)
        with open(post_dir / 'index.html', 'w') as f:
            f.write(post_html)
        print(f"  Generated: blog/{post['slug']}/index.html")

    print(f"\nTotal blog pages generated: {len(BLOG_POSTS) + 1}")


if __name__ == "__main__":
    main()
