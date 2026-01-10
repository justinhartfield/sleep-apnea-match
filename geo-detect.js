/**
 * Geo-Detection for StemCellPrices.com
 * Uses IP-based geolocation to detect user's location
 */

/**
 * Detect user's location via IP geolocation
 * @returns {Promise<Object>} Location object with city, state, stateCode, country
 */
async function detectUserLocation() {
    // First check localStorage for saved preference
    const saved = localStorage.getItem('userLocation');
    if (saved) {
        try {
            const location = JSON.parse(saved);
            if (location.city && location.state) {
                console.log('Using saved location:', location.city, location.state);
                return location;
            }
        } catch (e) {
            // Invalid saved data, continue to detect
        }
    }

    // Try IP-based geolocation
    try {
        const response = await fetch('https://ipapi.co/json/', {
            method: 'GET',
            headers: {
                'Accept': 'application/json'
            }
        });

        if (!response.ok) {
            throw new Error('Geolocation service unavailable');
        }

        const data = await response.json();

        // Only use US locations
        if (data.country_code !== 'US') {
            console.log('Non-US location detected, using default');
            return getDefaultLocation();
        }

        const location = {
            city: data.city,
            state: data.region,
            stateCode: data.region_code,
            country: data.country_code,
            postal: data.postal,
            latitude: data.latitude,
            longitude: data.longitude
        };

        console.log('Detected location:', location.city, location.state);
        return location;

    } catch (error) {
        console.warn('Geo-detection failed:', error.message);
        return getDefaultLocation();
    }
}

/**
 * Get default location (Los Angeles - highest traffic market)
 * @returns {Object} Default location object
 */
function getDefaultLocation() {
    return {
        city: 'Los Angeles',
        state: 'California',
        stateCode: 'CA',
        country: 'US'
    };
}

/**
 * Find the nearest supported city based on detected location
 * @param {Object} detectedLocation - Location from geo-detection
 * @returns {string|null} City slug if found, null otherwise
 */
function findNearestSupportedCity(detectedLocation) {
    if (!detectedLocation || !detectedLocation.city) return null;

    const cityName = detectedLocation.city.toLowerCase();
    const stateName = detectedLocation.state ? detectedLocation.state.toLowerCase() : '';

    // Direct match by city name
    for (const [slug, city] of Object.entries(CITY_PRICES)) {
        if (city.name.toLowerCase() === cityName) {
            return slug;
        }
    }

    // Match by slug (handles "New York City" -> "new-york-city")
    const normalizedSlug = cityName.replace(/\s+/g, '-');
    if (CITY_PRICES[normalizedSlug]) {
        return normalizedSlug;
    }

    // Fallback: find any city in the same state
    for (const [slug, city] of Object.entries(CITY_PRICES)) {
        if (city.state.toLowerCase() === stateName) {
            console.log('Using same-state fallback:', city.name);
            return slug;
        }
    }

    return null;
}

/**
 * Save user's location preference
 * @param {string} citySlug - The city slug to save
 * @param {Object} cityData - The city data from CITY_PRICES
 */
function saveLocationPreference(citySlug, cityData) {
    if (!citySlug || !cityData) return;

    const location = {
        citySlug: citySlug,
        city: cityData.name,
        state: cityData.state,
        stateSlug: cityData.stateSlug,
        savedAt: new Date().toISOString()
    };

    localStorage.setItem('userLocation', JSON.stringify(location));
    console.log('Location preference saved:', location.city, location.state);
}

/**
 * Clear saved location preference
 */
function clearLocationPreference() {
    localStorage.removeItem('userLocation');
    console.log('Location preference cleared');
}

/**
 * Get state code from full state name
 * @param {string} stateName - Full state name
 * @returns {string} Two-letter state code
 */
function getStateCode(stateName) {
    const stateCodes = {
        'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
        'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
        'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
        'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
        'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
        'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
        'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
        'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
        'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
        'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
        'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
        'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV',
        'Wisconsin': 'WI', 'Wyoming': 'WY', 'District of Columbia': 'DC'
    };

    return stateCodes[stateName] || stateName.substring(0, 2).toUpperCase();
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        detectUserLocation,
        getDefaultLocation,
        findNearestSupportedCity,
        saveLocationPreference,
        clearLocationPreference,
        getStateCode
    };
}
