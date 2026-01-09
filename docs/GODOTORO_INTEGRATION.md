# GoDotoro Integration Guide for StemCellPrices.com

## Overview

This document provides all the information needed for GoDotoro to set up programmatic ad campaigns for StemCellPrices.com. The site is a stem cell therapy clinic directory covering 30 US states, 50 cities, and 102+ verified clinics.

---

## 1. Data API Endpoints

### Primary Data Files

| Endpoint | Description | Format |
|----------|-------------|--------|
| `/api/data.json` | Master data file with conditions, states, cities | JSON |
| `/api/clinics.json` | Complete clinic database with all details | JSON |
| `/api/ad-campaigns.json` | Campaign templates and audience segments | JSON |

### Data Structure Overview

```
stemcellprices.com/
├── api/
│   ├── data.json          # Conditions, states, cities summary
│   ├── clinics.json       # 102 clinic records with full details
│   └── ad-campaigns.json  # Campaign templates for dynamic ads
```

---

## 2. Database Schema

### Conditions (8 total)

| Field | Type | Example |
|-------|------|---------|
| `id` | string | "knee-osteoarthritis" |
| `name` | string | "Knee Osteoarthritis" |
| `slug` | string | "knee-osteoarthritis" |
| `price_low` | number | 3500 |
| `price_high` | number | 9000 |
| `avg_price` | number | 5800 |
| `clinic_count` | number | 250 |
| `success_rate` | string | "68-77%" |
| `treatments` | array | ["PRP", "BMAC", "Adipose-Derived"] |
| `keywords` | array | ["stem cell knee", "knee stem cell therapy cost"] |

### States (30 total)

| Field | Type | Example |
|-------|------|---------|
| `id` | string | "california" |
| `name` | string | "California" |
| `abbr` | string | "CA" |
| `clinic_count` | number | 17 |
| `city_count` | number | 6 |
| `avg_price` | number | 5366 |

### Cities (50 total)

| Field | Type | Example |
|-------|------|---------|
| `id` | string | "los-angeles" |
| `name` | string | "Los Angeles" |
| `state` | string | "california" |
| `state_abbr` | string | "CA" |
| `clinic_count` | number | 5 |
| `avg_price` | number | 5500 |
| `url` | string | "/locations/california/los-angeles/" |

### Clinics (102 total)

| Field | Type | Example |
|-------|------|---------|
| `id` | string | "clinic-001" |
| `name` | string | "Alexander E Weber, MD" |
| `slug` | string | "alexander-e-weber-md" |
| `state` | string | "california" |
| `city` | string | "los-angeles" |
| `address` | string | "16311 Ventura Blvd, Encino, CA" |
| `phone` | string | "(818) 658-5920" |
| `price_low` | number | 4000 |
| `price_high` | number | 8000 |
| `avg_price` | number | 6000 |
| `specialty` | string | "Orthopedic Regenerative Medicine" |
| `featured` | boolean | true |
| `verified` | boolean | true |
| `url` | string | "/locations/california/los-angeles/alexander-e-weber-md.html" |
| `keywords` | array | ["stem cell therapy los angeles", "alexander e weber md stem cell"] |

---

## 3. URL Structure

### SEO-Friendly URLs

```
Home:           https://stemcellprices.com/
All States:     https://stemcellprices.com/locations/
State:          https://stemcellprices.com/locations/{state}/
City:           https://stemcellprices.com/locations/{state}/{city}/
Clinic:         https://stemcellprices.com/locations/{state}/{city}/{clinic}.html
Landing Page:   https://stemcellprices.com/lp/{condition}/{state}/{city}/
```

### URL Parameters for Tracking

| Parameter | Description | Example |
|-----------|-------------|---------|
| `utm_source` | Traffic source | google, meta, reddit |
| `utm_medium` | Marketing medium | cpc, display, social |
| `utm_campaign` | Campaign identifier | knee_la_jan2026 |
| `utm_content` | Ad variation | headline_a |
| `utm_term` | Keyword | stem+cell+knee+los+angeles |
| `gclid` | Google Click ID | Auto-captured |
| `fbclid` | Facebook Click ID | Auto-captured |

---

## 4. Campaign Templates

### Template 1: City + Condition Campaigns

**Campaign Name Pattern:** `Stem Cell {{condition}} - {{city}}, {{state_abbr}}`

**Headlines (rotate):**
1. `{{condition}} Treatment in {{city}}`
2. `Stem Cell Therapy {{city}} | ${{price_low}}+`
3. `{{city}} {{condition}} Specialists`
4. `Compare {{condition}} Costs in {{city}}`

**Descriptions (rotate):**
1. `Find verified stem cell clinics in {{city}} for {{condition}}. Average cost ${{avg_price}}. Compare prices from {{clinic_count}} providers.`
2. `{{condition}} stem cell therapy in {{city}}, {{state_abbr}}. Prices from ${{price_low}}-${{price_high}}. Get free consultation today.`

**Landing URL:** `/lp/{{condition_slug}}/{{state_slug}}/{{city_slug}}/?utm_source={{source}}&utm_medium=cpc&utm_campaign={{campaign_id}}`

### Template 2: Clinic-Specific Campaigns

**Campaign Name Pattern:** `{{clinic_name}} - {{city}}`

**Headlines:**
1. `{{clinic_name}} | Stem Cell Therapy`
2. `{{specialty}} in {{city}}`
3. `{{clinic_name}} - From ${{price_low}}`

**Landing URL:** `{{clinic_url}}?utm_source={{source}}&utm_medium=cpc&utm_campaign={{campaign_id}}`

### Template 3: State Awareness Campaigns

**Campaign Name Pattern:** `Stem Cell Clinics - {{state}}`

**Headlines:**
1. `Stem Cell Therapy in {{state}}`
2. `{{state}} Stem Cell Clinics | Compare Prices`
3. `Find {{state}} Regenerative Medicine`

**Landing URL:** `/locations/{{state_slug}}/?utm_source={{source}}&utm_medium=cpc&utm_campaign={{campaign_id}}`

---

## 5. Keyword Templates

### Condition + City Keywords
```
stem cell {{condition}} {{city}}
{{condition}} stem cell therapy {{city}}
{{condition}} treatment {{city}} cost
best {{condition}} clinic {{city}}
{{condition}} regenerative medicine {{city}}
```

### General City Keywords
```
stem cell therapy {{city}}
stem cell clinic {{city}}
regenerative medicine {{city}}
stem cell injection {{city}}
stem cell treatment cost {{city}}
```

### High-Intent Keywords
```
stem cell therapy near me
stem cell clinic near me
how much does stem cell therapy cost
stem cell therapy cost {{condition}}
```

---

## 6. Audience Segments

### Segment 1: Knee Pain Seekers
- **Conditions:** Knee Osteoarthritis
- **Age Range:** 45-65
- **Interests:** Orthopedics, joint health, sports medicine, arthritis treatment
- **Estimated Monthly Searches:** 22,000+

### Segment 2: Back Pain Seekers
- **Conditions:** Spine/Disc Pain
- **Age Range:** 35-60
- **Interests:** Back pain relief, spine health, chronic pain, disc problems
- **Estimated Monthly Searches:** 18,000+

### Segment 3: Sports Injury
- **Conditions:** Sports Injury, Shoulder, Elbow
- **Age Range:** 25-50
- **Interests:** Sports medicine, athletic recovery, fitness
- **Estimated Monthly Searches:** 12,000+

### Segment 4: General Regenerative
- **Conditions:** All
- **Age Range:** 40-70
- **Interests:** Regenerative medicine, alternative medicine, anti-aging
- **Estimated Monthly Searches:** 35,000+

---

## 7. Budget Recommendations

### By City Tier (Daily Budget)

| Tier | Cities | Daily Budget |
|------|--------|--------------|
| Tier 1 | Los Angeles, NYC, Chicago, Houston, Miami | $50/city |
| Tier 2 | Dallas, Phoenix, Seattle, Boston, Atlanta | $30/city |
| Tier 3 | All others | $15/city |

### By Condition (Daily Budget)

| Volume | Conditions | Daily Budget |
|--------|------------|--------------|
| High | Knee OA, Spine/Disc | $100/condition |
| Medium | Shoulder, Hip, Sports Injury | $50/condition |
| Low | Elbow, Ankle, Wrist | $25/condition |

---

## 8. Conversion Tracking

### Google Analytics 4
- **Property ID:** G-B61C6SRXP7
- **Conversion Events:**
  - `generate_lead` - Form submission
  - `click` (phone_click) - Phone number click
  - `view_item` - Clinic page view

### PostHog
- **Project Key:** phc_stemcellprices
- **Events:**
  - `lead_submitted`
  - `phone_clicked`
  - `clinic_viewed`
  - `search_performed`
  - `form_opened`

### Custom Dimensions (GA4)
- `dimension1`: page_type (home, state, city, clinic, landing_page)
- `dimension2`: state
- `dimension3`: city
- `dimension4`: clinic
- `dimension5`: utm_source
- `dimension6`: utm_campaign

---

## 9. Lead Data Structure

When a lead is submitted, the following data is captured:

```json
{
  "name": "John Smith",
  "email": "john@example.com",
  "phone": "(555) 123-4567",
  "condition": "Knee Osteoarthritis",
  "message": "I've had knee pain for 2 years...",
  "clinic_name": "Alexander E Weber, MD",
  "clinic_phone": "(818) 658-5920",
  "city": "Los Angeles",
  "state": "California",
  "timestamp": "2026-01-09T12:00:00Z",
  "source_url": "https://stemcellprices.com/lp/knee-osteoarthritis/california/los-angeles/",
  "utm_source": "google",
  "utm_medium": "cpc",
  "utm_campaign": "knee_la_jan2026"
}
```

---

## 10. Landing Pages

### Pre-Built Landing Pages (50 total)

Located at `/lp/{condition}/{state}/{city}/`

**Conditions covered:**
- Knee Osteoarthritis
- Back & Spine Pain
- Shoulder & Rotator Cuff
- Hip Osteoarthritis
- Sports Injury

**Cities covered:**
- Los Angeles, New York City, Houston, Miami, Chicago
- Phoenix, Dallas, Atlanta, Denver, Seattle

### Landing Page Features
- Sticky CTA bar
- Trust indicators (clinic count, success rate, avg price)
- Lead capture form with condition pre-filled
- FAQ section with condition-specific content
- Mobile-optimized design
- Full tracking integration

---

## 11. API Access Examples

### Fetch All Clinics
```javascript
fetch('https://stemcellprices.com/api/clinics.json')
  .then(res => res.json())
  .then(data => {
    console.log(`Total clinics: ${data.meta.total_clinics}`);
    data.clinics.forEach(clinic => {
      console.log(`${clinic.name} - ${clinic.city}, ${clinic.state}`);
    });
  });
```

### Fetch Campaign Templates
```javascript
fetch('https://stemcellprices.com/api/ad-campaigns.json')
  .then(res => res.json())
  .then(data => {
    const template = data.campaign_templates.city_condition;
    console.log('Headlines:', template.headline_templates);
  });
```

---

## 12. Contact & Support

**Website:** https://stemcellprices.com
**Admin Panel:** https://stemcellprices.com/admin/leads.html
**Landing Page Index:** https://stemcellprices.com/lp/

For technical questions about the integration, please contact the development team.

---

*Last Updated: January 9, 2026*
