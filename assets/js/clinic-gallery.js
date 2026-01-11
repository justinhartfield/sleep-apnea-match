/**
 * Clinic Image Gallery Component
 * Dynamically loads and displays multiple clinic images with lightbox support
 */

function clinicGallery(clinicSlug, maxImages = 6) {
    return {
        clinicSlug: clinicSlug,
        images: [],
        currentIndex: 0,
        lightboxOpen: false,
        loading: true,
        baseUrl: 'https://cfls.b-cdn.net/sleep-apnea-clinics',

        init() {
            // Try loading images in parallel
            this.tryLoadImages();
        },

        async tryLoadImages() {
            const formats = ['jpg', 'webp', 'png'];
            const loadedImages = [];

            // Try primary image
            for (const fmt of formats) {
                const url = `${this.baseUrl}/${this.clinicSlug}/primary.${fmt}`;
                const exists = await this.checkImage(url);
                if (exists) {
                    loadedImages.push({ url, alt: 'Clinic primary image' });
                    break; // Found primary, stop checking formats
                }
            }

            // Try numbered images 2-6
            for (let i = 2; i <= maxImages; i++) {
                let found = false;
                for (const fmt of formats) {
                    const url = `${this.baseUrl}/${this.clinicSlug}/${i}.${fmt}`;
                    const exists = await this.checkImage(url);
                    if (exists) {
                        loadedImages.push({ url, alt: `Clinic image ${i}` });
                        found = true;
                        break; // Found this number, stop checking formats
                    }
                }
                if (!found) break; // Stop if we hit a missing number
            }

            this.images = loadedImages;
            this.loading = false;
        },

        checkImage(url) {
            return new Promise((resolve) => {
                const img = new Image();
                let resolved = false;
                img.onload = () => {
                    if (!resolved) { resolved = true; resolve(true); }
                };
                img.onerror = () => {
                    if (!resolved) { resolved = true; resolve(false); }
                };
                img.src = url;
                // Timeout fallback
                setTimeout(() => {
                    if (!resolved) { resolved = true; resolve(false); }
                }, 3000);
            });
        },

        get hasMultipleImages() {
            return this.images.length > 1;
        },

        get currentImage() {
            return this.images[this.currentIndex] || null;
        },

        openLightbox(index) {
            this.currentIndex = index;
            this.lightboxOpen = true;
            document.body.style.overflow = 'hidden';
        },

        closeLightbox() {
            this.lightboxOpen = false;
            document.body.style.overflow = '';
        },

        nextImage() {
            this.currentIndex = (this.currentIndex + 1) % this.images.length;
        },

        prevImage() {
            this.currentIndex = (this.currentIndex - 1 + this.images.length) % this.images.length;
        },

        handleKeydown(e) {
            if (!this.lightboxOpen) return;
            if (e.key === 'Escape') this.closeLightbox();
            if (e.key === 'ArrowRight') this.nextImage();
            if (e.key === 'ArrowLeft') this.prevImage();
        }
    };
}
