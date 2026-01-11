#!/usr/bin/env python3
"""
Generate FAQ Page for SleepApneaMatch.com
Creates a comprehensive FAQ page with all 20 questions
"""

import json
from pathlib import Path


def load_faqs():
    """Load FAQ data from JSON file"""
    with open('api/faqs.json', 'r') as f:
        data = json.load(f)
    return data['faqs']


def generate_faq_page(faqs):
    """Generate the FAQ page HTML"""

    # Group FAQs by category
    categories = {}
    for faq in faqs:
        cat = faq.get('category', 'General')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(faq)

    # Build FAQ items HTML
    faq_items_html = ""
    schema_items = []

    for i, faq in enumerate(faqs):
        # Truncate answer for display (first 500 chars)
        short_answer = faq['answer'][:500] + '...' if len(faq['answer']) > 500 else faq['answer']
        short_answer = short_answer.replace('\n\n', ' ').replace('\n', ' ')

        faq_items_html += f'''
            <div class="bg-white rounded-xl shadow-sm overflow-hidden" x-data="{{ open: false }}">
                <button @click="open = !open" class="w-full px-6 py-4 text-left flex justify-between items-center hover:bg-slate-50 transition-colors">
                    <span class="font-semibold text-slate-800 pr-4">{faq['question']}</span>
                    <svg class="w-5 h-5 text-slate-400 flex-shrink-0 transition-transform" :class="{{ 'rotate-180': open }}" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                    </svg>
                </button>
                <div x-show="open" x-collapse class="px-6 pb-4">
                    <p class="text-slate-600 leading-relaxed">{short_answer}</p>
                    <span class="inline-block mt-2 text-xs bg-primary/10 text-primary px-2 py-1 rounded">{faq.get('category', 'General')}</span>
                </div>
            </div>
        '''

        # Schema.org FAQPage item
        schema_items.append({
            "@type": "Question",
            "name": faq['question'],
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq['answer'][:1000]
            }
        })

    schema_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": schema_items
    }, indent=2)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sleep Apnea Surgery FAQ | 20 Common Questions Answered | SleepApneaMatch.com</title>
    <meta name="description" content="Get answers to 20 common questions about sleep apnea surgery, including costs, success rates, insurance coverage, and recovery times. Medically reviewed by Dr. Igor I. Bussel, MD.">

    <!-- Open Graph -->
    <meta property="og:title" content="Sleep Apnea Surgery FAQ | SleepApneaMatch.com">
    <meta property="og:description" content="Get answers to 20 common questions about sleep apnea surgery, including costs, success rates, and recovery.">
    <meta property="og:url" content="https://sleepapneamatch.com/faq/">
    <meta property="og:type" content="website">

    <!-- Canonical -->
    <link rel="canonical" href="https://sleepapneamatch.com/faq/">

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

    <!-- Alpine.js for accordion -->
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>

    <!-- Schema.org FAQPage -->
    <script type="application/ld+json">
    {schema_json}
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
                    <a href="/blog/" class="text-slate-600 hover:text-primary">Blog</a>
                    <a href="/faq/" class="text-primary font-medium">FAQ</a>
                </div>
            </div>
        </div>
    </nav>

    <!-- Hero -->
    <section class="bg-gradient-to-br from-primary to-secondary text-white py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h1 class="text-4xl md:text-5xl font-bold mb-4">Sleep Apnea Surgery FAQ</h1>
            <p class="text-xl text-blue-100">Get answers to the 20 most common questions about sleep apnea surgery, costs, success rates, and recovery.</p>
        </div>
    </section>

    <!-- Medical Review Badge -->
    <div class="bg-white border-b">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
            <div class="flex items-center justify-center gap-4">
                <img src="/assets/images/dr_igor.jpg" alt="Dr. Igor I. Bussel, MD" class="w-10 h-10 rounded-full object-cover">
                <div class="flex items-center gap-2">
                    <span class="text-sm text-slate-700">All answers medically reviewed by <strong>Dr. Igor I. Bussel, MD</strong></span>
                    <svg class="w-5 h-5 text-green-500" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
                    </svg>
                </div>
            </div>
        </div>
    </div>

    <!-- FAQ Section -->
    <section class="py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="space-y-4">
                {faq_items_html}
            </div>
        </div>
    </section>

    <!-- CTA -->
    <section class="bg-slate-100 py-16">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
            <h2 class="text-3xl font-bold mb-4">Still Have Questions?</h2>
            <p class="text-slate-600 mb-8">Connect with a verified sleep apnea specialist who can answer your specific questions.</p>
            <div class="flex flex-wrap justify-center gap-4">
                <a href="/locations/" class="bg-primary text-white px-8 py-4 rounded-xl font-semibold hover:bg-secondary transition-colors">
                    Find Providers
                </a>
                <a href="/blog/" class="bg-white text-primary px-8 py-4 rounded-xl font-semibold border border-primary hover:bg-primary/10 transition-colors">
                    Read Our Blog
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


def main():
    """Generate the FAQ page"""
    print("Generating FAQ page...")

    # Load FAQs
    faqs = load_faqs()

    # Create faq directory
    faq_dir = Path('faq')
    faq_dir.mkdir(exist_ok=True)

    # Generate FAQ page
    html = generate_faq_page(faqs)
    with open(faq_dir / 'index.html', 'w') as f:
        f.write(html)

    print(f"  Generated: faq/index.html with {len(faqs)} questions")


if __name__ == "__main__":
    main()
