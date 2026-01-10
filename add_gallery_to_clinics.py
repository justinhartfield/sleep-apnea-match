#!/usr/bin/env python3
"""
Script to add image gallery component to all clinic profile pages.
Replaces the single image with a dynamic gallery that supports multiple images.
"""

import os
import re
from pathlib import Path

# The old single image pattern (supports .jpg, .webp, and .png)
OLD_IMAGE_PATTERN = r'''<!-- Clinic Image -->
                    <div class="clinic-main-image mb-6 rounded-xl overflow-hidden">
                        <img src="https://cfls\.b-cdn\.net/stem-cell-clinics/([^/]+)/primary\.(jpg|webp|png)" alt="[^"]*" class="w-full h-64 object-cover" loading="lazy" onerror="this\.parentElement\.style\.display='none'">
                    </div>'''

def get_new_gallery_html(clinic_slug):
    """Generate the new gallery HTML for a clinic"""
    return f'''<!-- Clinic Image Gallery -->
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
                    </div>'''

def get_script_tag():
    """Return the script tag to include the gallery JS"""
    return '    <script src="/assets/js/clinic-gallery.js"></script>\n'

def get_clinic_slug_from_filename(filepath):
    """Extract clinic slug from the filename"""
    filename = os.path.basename(filepath)
    return filename.replace('.html', '')

# Pattern for pages without an existing image (insert before "About This Clinic")
NO_IMAGE_PATTERN = r'''(                    </div>\s+<h2 class="text-2xl font-bold text-slate-900 mb-4">About This Clinic</h2>)'''

def update_clinic_file(filepath):
    """Update a single clinic profile file with the gallery component"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has gallery
    if 'clinicGallery' in content:
        return False, "Already has gallery"

    # Check if this file has the old image pattern
    match = re.search(OLD_IMAGE_PATTERN, content)
    if match:
        clinic_slug = match.group(1)
        # Replace the old image section with the new gallery
        new_gallery = get_new_gallery_html(clinic_slug)
        content = re.sub(OLD_IMAGE_PATTERN, new_gallery, content)
    else:
        # Try to add gallery before "About This Clinic" for pages without images
        no_image_match = re.search(NO_IMAGE_PATTERN, content)
        if no_image_match:
            clinic_slug = get_clinic_slug_from_filename(filepath)
            new_gallery = get_new_gallery_html(clinic_slug)
            # Insert gallery before the "About This Clinic" section
            replacement = f'''                    </div>

                    {new_gallery}

                    <h2 class="text-2xl font-bold text-slate-900 mb-4">About This Clinic</h2>'''
            content = re.sub(NO_IMAGE_PATTERN, replacement, content)
        else:
            return False, "No matching pattern found"

    # Add the gallery script if not already present
    if 'clinic-gallery.js' not in content:
        # Add before </head>
        content = content.replace('</head>', get_script_tag() + '</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True, clinic_slug

def main():
    """Main function to update all clinic profile pages"""
    locations_dir = Path('locations')
    updated = 0
    skipped = 0
    errors = []

    # Find all clinic profile HTML files (not index.html)
    for html_file in locations_dir.rglob('*.html'):
        if html_file.name == 'index.html':
            continue

        try:
            success, result = update_clinic_file(html_file)
            if success:
                print(f"Updated: {html_file} (slug: {result})")
                updated += 1
            else:
                skipped += 1
        except Exception as e:
            errors.append((html_file, str(e)))
            print(f"Error: {html_file} - {e}")

    print(f"\n{'='*50}")
    print(f"Summary:")
    print(f"  Updated: {updated} files")
    print(f"  Skipped: {skipped} files")
    print(f"  Errors: {len(errors)} files")

    if errors:
        print(f"\nErrors:")
        for filepath, error in errors:
            print(f"  {filepath}: {error}")

if __name__ == '__main__':
    main()
