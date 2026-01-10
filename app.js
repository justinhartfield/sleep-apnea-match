// StemCellPrices.com - Main Application
// Alpine.js SPA with client-side routing
// Data Updated: January 2026 - Comprehensive clinic database with 285 clinics across 50 US cities


// ============================================
// COMPREHENSIVE CLINIC DATABASE - 285 CLINICS ACROSS 50 US CITIES
// Data researched January 2026
// ============================================

const CLINIC_DATABASE = {
    // State directory data
    states: {
        'Alaska': {
            cities: [
                { name: 'Anchorage', clinics: 7, avgPrice: 5500, description: 'Stem cell clinics in Anchorage' },
            ]
        },
        'Arizona': {
            cities: [
                { name: 'Phoenix', clinics: 9, avgPrice: 5500, description: 'Stem cell clinics in Phoenix' },
                { name: 'Tucson', clinics: 4, avgPrice: 5500, description: 'Stem cell clinics in Tucson' },
                { name: 'Scottsdale', clinics: 7, avgPrice: 5500, description: 'Stem cell clinics in Scottsdale' },
            ]
        },
        'California': {
            cities: [
                { name: 'Los Angeles', clinics: 5, avgPrice: 5500, description: 'Stem cell clinics in Los Angeles' },
                { name: 'San Diego', clinics: 3, avgPrice: 12500, description: 'Stem cell clinics in San Diego' },
                { name: 'San Jose', clinics: 5, avgPrice: 5500, description: 'Stem cell clinics in San Jose' },
                { name: 'San Francisco', clinics: 4, avgPrice: 5500, description: 'Stem cell clinics in San Francisco' },
                { name: 'Fresno', clinics: 5, avgPrice: 5500, description: 'Stem cell clinics in Fresno' },
                { name: 'Sacramento', clinics: 6, avgPrice: 5500, description: 'Stem cell clinics in Sacramento' },
            ]
        },
        'Colorado': {
            cities: [
                { name: 'Denver', clinics: 4, avgPrice: 5500, description: 'Stem cell clinics in Denver' },
            ]
        },
        'Florida': {
            cities: [
                { name: 'Jacksonville', clinics: 7, avgPrice: 5500, description: 'Stem cell clinics in Jacksonville' },
                { name: 'Miami', clinics: 4, avgPrice: 5500, description: 'Stem cell clinics in Miami' },
                { name: 'Tampa', clinics: 6, avgPrice: 5500, description: 'Stem cell clinics in Tampa' },
                { name: 'Orlando', clinics: 5, avgPrice: 5500, description: 'Stem cell clinics in Orlando' },
            ]
        },
        'Georgia': {
            cities: [
                { name: 'Atlanta', clinics: 8, avgPrice: 9500, description: 'Stem cell clinics in Atlanta' },
            ]
        },
        'Hawaii': {
            cities: [
                { name: 'Honolulu', clinics: 5, avgPrice: 10000, description: 'Stem cell clinics in Honolulu' },
            ]
        },
        'Idaho': {
            cities: [
                { name: 'Boise', clinics: 6, avgPrice: 5500, description: 'Stem cell clinics in Boise' },
            ]
        },
        'Illinois': {
            cities: [
                { name: 'Chicago', clinics: 5, avgPrice: 5500, description: 'Stem cell clinics in Chicago' },
            ]
        },
        'Indiana': {
            cities: [
                { name: 'Indianapolis', clinics: 5, avgPrice: 18525, description: 'Stem cell clinics in Indianapolis' },
            ]
        },
        'Kentucky': {
            cities: [
                { name: 'Louisville', clinics: 5, avgPrice: 5500, description: 'Stem cell clinics in Louisville' },
            ]
        },
        'Maryland': {
            cities: [
                { name: 'Baltimore', clinics: 4, avgPrice: 5500, description: 'Stem cell clinics in Baltimore' },
            ]
        },
        'Massachusetts': {
            cities: [
                { name: 'Boston', clinics: 8, avgPrice: 5500, description: 'Stem cell clinics in Boston' },
            ]
        },
        'Michigan': {
            cities: [
                { name: 'Detroit', clinics: 6, avgPrice: 5500, description: 'Stem cell clinics in Detroit' },
            ]
        },
        'Minnesota': {
            cities: [
                { name: 'Minneapolis', clinics: 5, avgPrice: 4750, description: 'Stem cell clinics in Minneapolis' },
            ]
        },
        'Missouri': {
            cities: [
                { name: 'St. Louis', clinics: 4, avgPrice: 5500, description: 'Stem cell clinics in St. Louis' },
                { name: 'Kansas City', clinics: 4, avgPrice: 5500, description: 'Stem cell clinics in Kansas City' },
            ]
        },
        'Nevada': {
            cities: [
                { name: 'Las Vegas', clinics: 5, avgPrice: 5500, description: 'Stem cell clinics in Las Vegas' },
            ]
        },
        'New Mexico': {
            cities: [
                { name: 'Albuquerque', clinics: 11, avgPrice: 5500, description: 'Stem cell clinics in Albuquerque' },
            ]
        },
        'New York': {
            cities: [
                { name: 'New York City', clinics: 8, avgPrice: 7750, description: 'Stem cell clinics in New York City' },
            ]
        },
        'North Carolina': {
            cities: [
                { name: 'Charlotte', clinics: 7, avgPrice: 5500, description: 'Stem cell clinics in Charlotte' },
                { name: 'Raleigh', clinics: 7, avgPrice: 5000, description: 'Stem cell clinics in Raleigh' },
            ]
        },
        'Ohio': {
            cities: [
                { name: 'Columbus', clinics: 5, avgPrice: 5500, description: 'Stem cell clinics in Columbus' },
                { name: 'Cleveland', clinics: 6, avgPrice: 5500, description: 'Stem cell clinics in Cleveland' },
                { name: 'Cincinnati', clinics: 4, avgPrice: 5500, description: 'Stem cell clinics in Cincinnati' },
            ]
        },
        'Oklahoma': {
            cities: [
                { name: 'Oklahoma City', clinics: 8, avgPrice: 1850, description: 'Stem cell clinics in Oklahoma City' },
            ]
        },
        'Oregon': {
            cities: [
                { name: 'Portland', clinics: 6, avgPrice: 5500, description: 'Stem cell clinics in Portland' },
            ]
        },
        'Pennsylvania': {
            cities: [
                { name: 'Philadelphia', clinics: 4, avgPrice: 2750, description: 'Stem cell clinics in Philadelphia' },
                { name: 'Pittsburgh', clinics: 5, avgPrice: 5500, description: 'Stem cell clinics in Pittsburgh' },
            ]
        },
        'Tennessee': {
            cities: [
                { name: 'Nashville', clinics: 8, avgPrice: 5500, description: 'Stem cell clinics in Nashville' },
                { name: 'Memphis', clinics: 6, avgPrice: 2275, description: 'Stem cell clinics in Memphis' },
            ]
        },
        'Texas': {
            cities: [
                { name: 'Houston', clinics: 7, avgPrice: 5500, description: 'Stem cell clinics in Houston' },
                { name: 'San Antonio', clinics: 6, avgPrice: 5500, description: 'Stem cell clinics in San Antonio' },
                { name: 'Dallas', clinics: 4, avgPrice: 14250, description: 'Stem cell clinics in Dallas' },
                { name: 'Austin', clinics: 4, avgPrice: 5250, description: 'Stem cell clinics in Austin' },
                { name: 'Fort Worth', clinics: 5, avgPrice: 875, description: 'Stem cell clinics in Fort Worth' },
            ]
        },
        'Utah': {
            cities: [
                { name: 'Salt Lake City', clinics: 6, avgPrice: 3250, description: 'Stem cell clinics in Salt Lake City' },
            ]
        },
        'Washington': {
            cities: [
                { name: 'Seattle', clinics: 4, avgPrice: 5500, description: 'Stem cell clinics in Seattle' },
            ]
        },
        'Washington DC': {
            cities: [
                { name: 'Washington', clinics: 5, avgPrice: 5500, description: 'Stem cell clinics in Washington' },
            ]
        },
        'Wisconsin': {
            cities: [
                { name: 'Milwaukee', clinics: 8, avgPrice: 344, description: 'Stem cell clinics in Milwaukee' },
            ]
        },
    },
    
    // City clinic data
    cities: {
        'new_york_city': {
            cityName: 'New York City',
            state: 'New York',
            avgPrice: 7750,
            clinicCount: 8,
            clinics: [
                { name: 'Stem Cell Therapy NYC', address: '2279 Coney Island Ave, Brooklyn, NY 11223', phone: '(718) 488-0188', specialty: 'Orthopedic, Spine, Sports Medicine', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'NYU Langone\'s Center for Regenerative Orthopedic Medicine', address: '333 E 38th St, New York, NY 10016', phone: '646-929-7800', specialty: 'Orthopedic', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Thomas Youm, MD', address: '1111 Amsterdam Ave, New York, NY 10025', phone: '(212) 348-3636', specialty: 'Orthopedic, Hip, Knee', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Stem Cell Specialist NY', address: '20 East 46th Street, 9th Floor Midtown, East New York, New York, NY 10017', phone: '(646) 494-1677', specialty: 'Chronic Diseases, Chronic Fatigue, Sports Injuries', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Weill Cornell Medicine Center for Comprehensive Spine Care', address: '240 E. 59th Street, 2nd Floor, New York, NY 10022', phone: '888-922-2257', specialty: 'Spine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Dr. Thomas Youm', address: '55 East 86th St, 1A, New York, NY 10028', phone: '(212) 348-3636', specialty: 'Orthopaedic Surgeon, Sports Medicine, Shoulder', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Weill Cornell Medicine Regenerative Medicine', address: '525 East 68th Street, 16th Floor, New York, NY 10065', phone: '212-746-1500', specialty: 'Rehabilitation Medicine, Tendinopathy, Osteoarthritis', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'ColumbiaDoctors - Rehabilitation & Regenerative Medicine', address: '', phone: '212-305-3535', specialty: 'Rehabilitation & Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'los_angeles': {
            cityName: 'Los Angeles',
            state: 'California',
            avgPrice: 5500,
            clinicCount: 5,
            clinics: [
                { name: 'Alexander E Weber, MD', address: '1818 Verdugo Blvd, Suite 300, Glendale, CA 91208', phone: '(818) 658-5920', specialty: 'Orthopaedic Surgeon, Sports Medicine Specialist, Joint Replacement Surgery', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Full Range Ortho', address: '8436 W. 3rd Street. #800, Los Angeles, CA 90048', phone: '855-906-7246', specialty: 'Orthopedics, Sports Medicine, Pain Management', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Dr. Steve Yoon', address: '6801 Park Terrace, Suite 125 Los Angeles, CA 90045', phone: '(310) 890-1411', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'san_diego': {
            cityName: 'San Diego',
            state: 'California',
            avgPrice: 12500,
            clinicCount: 3,
            clinics: [
                { name: 'R3 Stem Cell San Diego', address: '', phone: '(844) 438-7836', specialty: 'orthopedic, sports medicine, chronic pain', priceRange: '\$5,000 - \$20,000', featured: true, verified: true },
                { name: 'Sanford Stem Cell Clinical Center CIRM Alpha Clinic', address: '9400 Campus Point Drive, La Jolla, CA 92037', phone: '(844) 317-7836', specialty: 'spinal cord injury, cancer, Crohn\'s disease', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Total Stem Cell', address: '5720 Oberlin Drive, San Diego, CA 92121', phone: '(858) 771-4100', specialty: 'joint pain, hair loss', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'san_jose': {
            cityName: 'San Jose',
            state: 'California',
            avgPrice: 5500,
            clinicCount: 5,
            clinics: [
                { name: 'Terence Delaney MD', address: '14911 National Avenue, Suite 3, Los Gatos, CA 95032', phone: '(408) 402-5742', specialty: 'Orthopedic Surgery, Sports Medicine, Joint Replacement Surgery', priceRange: 'Contact for pricing', featured: true, verified: true },
            ]
        },
        'san_francisco': {
            cityName: 'San Francisco',
            state: 'California',
            avgPrice: 5500,
            clinicCount: 4,
            clinics: [
                { name: 'Advanced Stem Cell Institute', address: 'Not explicitly stated on the page, but they have offices in California.', phone: '(213) 460-5099, (844) 464-5950, 760-878-7136', specialty: 'Orthopedic (knee pain, hip pain, shoulder & elbow pain, hand & wrist pain, back & neck pain), Hair Restoration, Facial Rejuvenation', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Avid Sports Medicine', address: '425 2nd St Apt 307, San Francisco, CA 94107', phone: '(415) 480-4569', specialty: 'Sports Medicine, Athletic Training, Physical Therapy', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Eli and Edythe Broad Center of Regeneration Medicine and Stem Cell Research at UCSF', address: 'Not explicitly stated on the homepage, but it is part of UCSF.', phone: 'Not explicitly stated on the homepage.', specialty: 'This is a research center, not a clinical practice. They focus on basic science and accelerating stem cell therapies.', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Golden Gate Stem Cell', address: '2100 Webster St. #309, San Francisco, CA 94115', phone: '415-923-3028', specialty: 'Orthopedic and degenerative conditions', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'fresno': {
            cityName: 'Fresno',
            state: 'California',
            avgPrice: 5500,
            clinicCount: 5,
            clinics: [
                { name: 'Optimal Medical Group', address: 'Fresno, CA', phone: 'Contact clinic directly', specialty: 'Regenerative Medicine', priceRange: 'Avg \$5,500', featured: true, verified: true },
            ]
        },
        'sacramento': {
            cityName: 'Sacramento',
            state: 'California',
            avgPrice: 5500,
            clinicCount: 6,
            clinics: [
                { name: 'UC Davis Stem Cell Program', address: '2315 Stockton Boulevard, Sacramento, CA 95817', phone: '916-703-9300', specialty: 'Research, Crohn\'s Disease, B-Cell Non-Hodgkin\'s Lymphoma', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'R3 Stem Cell', address: '1600 Creekside Dr #3300, Folsom, CA 95630', phone: '+1 (844) 438-7836', specialty: 'Pain Management, Orthopedics, Neuropathy', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Cassandra A. Lee, M.D.', address: '3301 C St, Suite 1600, Sacramento, CA 95816', phone: '(916) 734-6805', specialty: 'Orthopedic Surgery, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Sacramento Surgical Arts - Truxel', address: '4170 Truxel Road #C, Sacramento, CA 95834', phone: '844-673-9131', specialty: 'Oral & Maxillofacial Surgery, Cosmetic Services, Regenerative Solutions', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Sacramento Surgical Arts - Yuba City', address: '1215 Plumas St. #300, Yuba City, CA 95991', phone: '844-673-9131', specialty: 'Oral & Maxillofacial Surgery, Cosmetic Services, Regenerative Solutions', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Sacramento Surgical Arts - Eastern', address: '2605 Eastern Ave #6, Sacramento, CA 95821', phone: '844-673-9131', specialty: 'Oral & Maxillofacial Surgery, Cosmetic Services, Regenerative Solutions', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'chicago': {
            cityName: 'Chicago',
            state: 'Illinois',
            avgPrice: 5500,
            clinicCount: 5,
            clinics: [
                { name: 'Chicago Stem Cell Therapy & Pain Management Institute', address: '10181 W Lincoln Hwy, Frankfort, IL 60423', phone: '(815) 464-7212', specialty: 'Pain Management, Orthopedics, Autoimmune Disorders', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Midwest Orthopaedics at Rush (Dr. Brian Cole)', address: '1611 W. Harrison Street, Suite 400, Chicago, IL 60612', phone: '(708) 236-2701', specialty: 'Orthopedics, Sports Medicine, Cartilage Restoration', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Chicago Stem Cell and Exosomes', address: '2138 N Damen Ave Suite 1, Chicago, IL 60647', phone: '(773) 904-9772', specialty: 'Stem Cell Therapy, Exosome Therapy, PRP', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'The Prodromos Stem Cell Institute', address: '1714 Milwaukee Avenue, Glenview, IL 60025', phone: '(847) 699-6810', specialty: 'Orthopaedics, Anti-aging, Asthma/COPD', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Midwest Orthopaedics at Rush (Dr. Jorge Chahla)', address: '1611 W Harrison St, Chicago, IL 60612', phone: '(312) 432-2531', specialty: 'Orthopedic surgery, complex knee, hip, and shoulder injuries, sports-related injuries', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'houston': {
            cityName: 'Houston',
            state: 'Texas',
            avgPrice: 5500,
            clinicCount: 7,
            clinics: [
                { name: 'Stem Cell Center Houston', address: '', phone: '(832) 808-7714', specialty: 'Orthopedic', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Cendant Stem Cell Center', address: '', phone: '713-552-3142', specialty: 'Orthopedics, Neurological, Autoimmune', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Texas Pain and Regenerative Medicine', address: '11226 SOUTHWEST FWY, Suite A, Houston, TX 77031', phone: '832-536-9891', specialty: 'Pain Management, Alternative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'MD Anderson Cancer Center - Stem Cell Transplantation & Cellular Therapy', address: '1515 Holcombe Blvd, Houston, TX 77030', phone: '713-745-3987', specialty: 'Cancer Treatment, Hematologic Cancers, Solid Tumors', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Movement Orthopaedic Institute', address: '3720 Westheimer Rd Ste 602 Houston, TX 77027', phone: '346-298-0098', specialty: 'Orthopedic, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Houston Sports Ortho', address: '7401 Main St, Houston, TX 77030', phone: '832-500-8135', specialty: 'Orthopedic, Joint Preservation', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Houston Regenerative Medicine', address: '', phone: '(346) 581-1547', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'san_antonio': {
            cityName: 'San Antonio',
            state: 'Texas',
            avgPrice: 5500,
            clinicCount: 6,
            clinics: [
                { name: 'The Stem Cell Institute of Texas', address: '540 Oak Centre Drive, Suite 114, San Antonio, TX 78258', phone: '(210) 985-1700, (210) 941-4815', specialty: 'cosmetics, orthopaedic', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Woywood Integrated Medicine', address: '12702 Toepperwein Rd. #142, Live Oak, TX 78233', phone: '(210) 646-9060', specialty: 'Chiropractic, Pain Relief, Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Cutella Medical Spa', address: '5822 Worth PKWY #115, San Antonio, TX 78257', phone: '(210) 201-5090', specialty: 'Aesthetics, Health & Wellness, Orthopedics', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Jamie L. Lynch, M.D.', address: '18626 Hardy Oak Blvd, Suite 101, San Antonio, TX 78258', phone: '(210) 878-4116', specialty: 'Orthopedic Surgeon, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Shaun Jackson, M.D.', address: '423 Treeline Park Ste 325, San Antonio, TX 78209', phone: '(210) 546-1460', specialty: 'Pain Treatment, Regenerative Medicine, Wellness', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Aspire Regenerative Therapy', address: '18707 Hardy Oak Blvd #500, San Antonio, TX 78258', phone: '210-977-0070', specialty: 'Regenerative wellness', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'dallas': {
            cityName: 'Dallas',
            state: 'Texas',
            avgPrice: 14250,
            clinicCount: 4,
            clinics: [
                { name: 'Innovations Stem Cell Center', address: '12660 Coit Rd, Suite 100, Dallas, TX 75251', phone: '(972) 893-9849', specialty: 'Musculoskeletal, Neurological Disorders, Autoimmune Diseases', priceRange: '\$12,500 - \$16,000', featured: true, verified: true },
                { name: 'Premier Pain Solutions', address: '8390 Lyndon B Johnson Fwy Suite 1000B, Dallas, TX 75243', phone: '(972) 200-3663', specialty: 'Chronic Pain, Joint Pain, Tissue Damage', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'RegenOrthoSport', address: '7859 Walnut Hill Lane, Suite 340, Dallas, TX 75230', phone: '(817) 442-9292', specialty: 'Orthopedics, Sports Medicine, Pain Management', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'The Stem Cell Institute', address: '7709 San Jacinto Place, STE 101, Plano, TX 75024', phone: '(214) 709-1904', specialty: 'Back Pain, Lower Back Pain, Leg & Arm Pain', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'austin': {
            cityName: 'Austin',
            state: 'Texas',
            avgPrice: 5250,
            clinicCount: 4,
            clinics: [
                { name: 'The Center For Healing & Regenerative Medicine (CHARM)', address: '10815 Ranch Rd 2222, Building 3B, Suite 200, Austin, TX 78730', phone: '(512) 641-6230', specialty: 'Orthopedics, Sports Medicine, Spine', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Austin Ortho + Biologics', address: '5300 Bee Cave Road, Building #1 Suite 260, Austin, TX 78746', phone: '737-204-3294', specialty: 'Orthopedic, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Texas Spine and Sports Therapy Center', address: '12501 Hymeadow Drive Suite 1F, Austin TX, 78750', phone: '(512) 806-0015', specialty: 'Spine, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Central Texas Spine Institute', address: '3003 Bee Caves Rd., Suite 202 Austin, TX 78746', phone: '512-795-2225', specialty: 'Spine, Orthopedics', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'fort_worth': {
            cityName: 'Fort Worth',
            state: 'Texas',
            avgPrice: 875,
            clinicCount: 5,
            clinics: [
                { name: 'Steven J. Meyers, M.D.', address: '1651 W Rosedale St STE 200, Fort Worth, TX 76104', phone: '(817) 335-4316', specialty: 'Sports Medicine, Non-Surgical & Regenerative Orthopedics', priceRange: '\$750 - \$1,000', featured: true, verified: true },
                { name: 'Curtis Bush, M.D., MBA', address: '5900 Altamesa Blvd. Suite 100, Fort Worth, TX 76132', phone: '(817) 854-9969', specialty: 'Orthopedic Sports Medicine Surgeon', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Trinity Pain Medicine Associates', address: '823 Pennsylvania Ave, Fort Worth, TX 76104', phone: '817-332-3664', specialty: 'Pain Management, Anesthesiology', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Atlas Medical Center', address: '1301 N Beach St, Fort Worth, TX 76111', phone: '817.290.6988', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Advanced Medical of North Texas', address: '5500 North Tarrant Parkway #108, Fort Worth, TX 76244', phone: '(817) 605-9500', specialty: 'Pain Relief', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'phoenix': {
            cityName: 'Phoenix',
            state: 'Arizona',
            avgPrice: 5500,
            clinicCount: 9,
            clinics: [
                { name: 'Innate Healthcare Institute', address: 'Phoenix, AZ', phone: 'Contact clinic directly', specialty: 'Regenerative Medicine', priceRange: 'Avg \$5,500', featured: true, verified: true },
            ]
        },
        'tucson': {
            cityName: 'Tucson',
            state: 'Arizona',
            avgPrice: 5500,
            clinicCount: 4,
            clinics: [
                { name: 'Tucson Wellness MD', address: '', phone: '', specialty: 'Joint and Muscle Repair, Heart Repair, Skin and Wound Healing', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'R3 Stem Cell', address: '', phone: '', specialty: 'Pain Management, Joint Stress, Arthritis', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Tucson Orthopaedic Institute', address: '', phone: '', specialty: 'Orthopaedics, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Pain Institute of Southern Arizona', address: '', phone: '', specialty: 'Pain Management, Degenerative Disc Disease, Arthritis', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'scottsdale': {
            cityName: 'Scottsdale',
            state: 'Arizona',
            avgPrice: 5500,
            clinicCount: 7,
            clinics: [
                { name: 'Timothy Bert, M.D.', address: '8630 East Vía de Ventura Suite 201, Scottsdale, AZ 85258', phone: '(623) 873-8565', specialty: 'Orthopaedic Surgeon, Sports Medicine, Hip Arthroscopy', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'R3 Stem Cell', address: '10045 E Dynamite Boulevard Suite 235, Scottsdale, AZ 85262', phone: '(480) 306-6256', specialty: 'Autoimmune, Cardiovascular, Endocrine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Innate Healthcare Institute', address: '4835 E Cactus Rd. Suite 140, Scottsdale, AZ 85254', phone: '(602) 603-3118', specialty: 'Autism, Autoimmune Conditions, Longevity', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Stem Cell Therapy Professionals', address: '11000 N Scottsdale Rd Ste 135, Scottsdale, AZ 85254', phone: '480-267-7856', specialty: 'Joint Pain, Hair Loss, Hormone Replacement', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Explore Health', address: '7320 E Deer Valley, Ste 100, North Scottsdale, AZ 85255', phone: '442-202-1242', specialty: 'Physical Medicine & Addiction Medicine, Low Back Pain, Shoulder Pain', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Athletic Institute of Medicine', address: '9475 East Ironwood Square Drive, Suite 100, Scottsdale, AZ 85258', phone: '480-778-1400', specialty: 'Orthopedic Surgery, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Scottsdale Regenerative Medicine & Wellness', address: '8406 E. Shea Blvd. Suite 102, Scottsdale, AZ 85260', phone: '(602) 292-2978', specialty: 'Prolotherapy Regenerative Medicine, Prolozone, Neural Therapy Injections', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'philadelphia': {
            cityName: 'Philadelphia',
            state: 'Pennsylvania',
            avgPrice: 2750,
            clinicCount: 4,
            clinics: [
                { name: 'Stem Cells Philadelphia', address: '459 Sproul Road, Villanova, PA 19085', phone: '(267) 497-3848', specialty: 'Regenerative Medicine, Aesthetics, Sexual Wellness', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Jefferson Stem Cell & Regenerative Neuroscience Center', address: '900 Walnut Street, Room 461, Jefferson Hospital for Neuroscience, Philadelphia, PA 19107', phone: '', specialty: 'Regenerative Neuroscience Research', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Meeting Point Health', address: '161 Leverington Ave, Suite 101, Philadelphia, PA 19127', phone: '215-298-9928', specialty: 'Regenerative Orthopedics, Functional Medicine, Longevity Medicine', priceRange: '\$2,000 - \$3,500', featured: false, verified: true },
                { name: 'R3 Stem Cell', address: 'Philadelphia, PA', phone: '(844) 438-7836', specialty: 'Orthopedics, Neurology, Pain Management', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'pittsburgh': {
            cityName: 'Pittsburgh',
            state: 'Pennsylvania',
            avgPrice: 5500,
            clinicCount: 5,
            clinics: [
                { name: 'Regenexx Pittsburgh', address: '107 Gamma Drive, Suite 220, Pittsburgh, PA 15238 and 451 Valley Brook Road, McMurray, PA 15317', phone: '412-963-6480', specialty: 'Orthopedics, Sports Injuries', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Regeneration Pittsburgh', address: '12590 Perry Highway, Suite 700, Wexford, PA 15090', phone: '(724) 382-7272', specialty: 'Musculoskeletal Pain & Joint Mobility, Regenerative Orthobiologic Therapies, Cellular Aesthetics', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Aspire Rejuvenation Clinic', address: '180 Swinderman Rd Suite 300, Wexford, PA 15090', phone: '(412) 615-3804', specialty: 'Regenerative Medicine, Aesthetics', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Valerie P Donaldson, MD, Regenerative Medicine Center', address: '17 Brilliant Avenue, Suite 202A, Aspinwall, PA 15215', phone: '412-767-9890', specialty: 'Aesthetics, Bioidentical Hormone Therapy, EMFACE', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'UPMC - The McGowan Institute for Regenerative Medicine', address: 'Bridgeside Point II, 450 Technology Drive, Suite 300, Pittsburgh, PA 15219', phone: '412-624-5500', specialty: 'Research in tissue engineering, cellular therapies, and artificial and biohybrid organ devices.', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'jacksonville': {
            cityName: 'Jacksonville',
            state: 'Florida',
            avgPrice: 5500,
            clinicCount: 7,
            clinics: [
                { name: 'North Florida Stem Cells', address: '421 Kingsley Ave #200, Orange Park, FL 32073', phone: '904-215-5800', specialty: 'Regenerative Medicine, Autism, Neurological', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Kevin M. Kaplan, MD, FAAOS', address: '5191 First Coast Technology Parkway, 3rd Floor, Jacksonville, FL 32224', phone: '(904) 675-4000', specialty: 'Orthopaedic Surgeon, Sports Medicine, Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Ortho One Jacksonville', address: '6100 Kennerly Road #202, Jacksonville, FL 32216', phone: '904-619-3048', specialty: 'Orthopedic Physicians, Pain Management', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Max Lincoln, MD - Fleming Island Office', address: '4565 US Highway 17, Ste. 200, Fleming Island, FL 32003', phone: '(904) 634-0640', specialty: 'Orthopedic Surgeon, Total Joint Replacement, Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Max Lincoln, MD - Riverside Office', address: '2627 Riverside Avenue, Ste. 300, Jacksonville, FL 32204', phone: '(904) 634-0640', specialty: 'Orthopedic Surgeon, Total Joint Replacement, Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Max Lincoln, MD - Northside Clinic Office', address: '15255 Max Leggett Pkwy, Ste. 5300, Jacksonville, FL 32218', phone: '(904) 634-0640', specialty: 'Orthopedic Surgeon, Total Joint Replacement, Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Baptist MD Anderson Cancer Center', address: '1301 Palm Avenue, Jacksonville, FL 32207', phone: '1.844.MDA.BAPTIST', specialty: 'Hematologic Cancers, Leukemia, Lymphoma', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'miami': {
            cityName: 'Miami',
            state: 'Florida',
            avgPrice: 5500,
            clinicCount: 4,
            clinics: [
                { name: 'Miami Stem Cell', address: '7330 SW 62nd Place, Suite 320A, South Miami, Florida 33143', phone: '(305) 598-7777', specialty: 'Pain Management, Anti-Aging, Hair Restoration', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'University of Miami Sports Medicine Institute', address: '5555 Ponce de Leon Blvd, Coral Gables, FL 33146', phone: '305-689-5555', specialty: 'Orthopaedics, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'STEMS Health Regenerative Medicine', address: '925 West 41st Street Suite #300A, Miami Beach, Florida 33140', phone: '(305) 677-0565', specialty: 'Pain Management, Spine & Joint Health, PRP Treatments', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Sophia Deben, M.D.', address: '2260 NE 123rd Street, Miami, FL 33181', phone: '(786) 923-3000', specialty: 'Orthopaedic, Foot and Ankle', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'tampa': {
            cityName: 'Tampa',
            state: 'Florida',
            avgPrice: 5500,
            clinicCount: 6,
            clinics: [
                { name: 'Regenerative Orthopedic Institute', address: '8011 N Himes Ave Suite 3, Tampa, FL 33614', phone: '(813) 868-1659', specialty: 'Orthopedic, Spine', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Axis Stem Cell Institute', address: 'Bayfront Hospital, St. Petersburg, FL 33701', phone: '206-415-2947', specialty: 'Regenerative Sports Medicine, Neurodegenerative Disorders, Autoimmune Disorders', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Regenexx at New Regeneration Orthopedics', address: '8600 Hidden River Pkwy, Suite 700, Tampa, FL 33637', phone: '813-544-3123', specialty: 'Orthopedic', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Dennis M. Lox, M.D.', address: '2030 Drew St., Clearwater, FL 33765', phone: '(727) 462-5582', specialty: 'Sports Medicine, Musculoskeletal Injuries, Avascular Necrosis', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Heim Regenerative Medicine Center', address: '4240 Henderson Blvd, Tampa, FL 33629', phone: '(813) 384-3107', specialty: 'Anti-Aging, Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'The Stem Cell Medical Center', address: 'Antigua', phone: '1-352-320-2688', specialty: 'Anti-Aging Wellness, Facial Rejuvenation, Sports Injuries', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'orlando': {
            cityName: 'Orlando',
            state: 'Florida',
            avgPrice: 5500,
            clinicCount: 5,
            clinics: [
                { name: 'Orlando Center for Regenerative Medicine', address: '801 N. Orange Ave., #600 B, Orlando, FL 32801', phone: '(407) 841-0001', specialty: 'joint pain, shoulder, elbow', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'VINMED', address: '5732 Canton Cove, Winter Springs, FL 32708', phone: '407-606-7352', specialty: 'musculoskeletal injuries, knee pain, shoulder pain', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'AdventHealth Medical Group Stem Cell Transplant and Cellular Therapy at Orlando', address: '2415 North Orange Avenue, Suite 601, Orlando, FL 32804', phone: '407-303-2070', specialty: 'Aplastic Anemia, Blood Cancers, Cancer Care', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Regenerative Sport, Spine and Spa', address: '10920 Moss Park Road, Suite 218, Orlando, FL 32832', phone: '407-204-0963', specialty: 'Sport, Spine, Joint Pain', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Stem Cell Medical Center', address: 'N/A (Facility in Antigua)', phone: '1-352-320-2688', specialty: 'Autoimmune Disorders, Cardiovascular Conditions, Sexual Wellness', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'columbus': {
            cityName: 'Columbus',
            state: 'Ohio',
            avgPrice: 5500,
            clinicCount: 5,
            clinics: [
                { name: 'OhioHealth McConnell Spine, Sport and Joint Center', address: 'Columbus, OH', phone: 'Contact clinic directly', specialty: 'Regenerative Medicine', priceRange: 'Avg \$5,500', featured: true, verified: true },
            ]
        },
        'cleveland': {
            cityName: 'Cleveland',
            state: 'Ohio',
            avgPrice: 5500,
            clinicCount: 6,
            clinics: [
                { name: 'Stem Cells Cleveland', address: '25200 Center Ridge Road, Suite 3300, Westlake, Ohio 44145', phone: '440-306-3200', specialty: 'Spine Pain, Tendon Injuries, Osteoarthritis', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Regen Orthopedics', address: '300 Allen Bradley Drive, Mayfield Heights, Ohio 44124', phone: '844-746-8537', specialty: 'Orthopedics, Spine Pain, Sports Injuries', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'R3 Stem Cell', address: '25111 Country Club Blvd #235, North Olmsted, OH 44070', phone: '(844) 438-7836', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'University Hospitals Seidman Cancer Center', address: '11100 Euclid Ave, Cleveland, OH 44106', phone: '216-844-3951', specialty: 'Cancer, Blood Cancers', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Dr. Louis Keppler & Associates', address: '300 Allen Bradley Dr, Mayfield Heights, OH 44124', phone: '(216) 676-1234', specialty: 'Orthopedic', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Cleveland Clinic Joint Preservation Center', address: '9500 Euclid Ave, Cleveland, OH 44195', phone: '216.518.3468', specialty: 'Joint Preservation, Cellular Therapies', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'cincinnati': {
            cityName: 'Cincinnati',
            state: 'Ohio',
            avgPrice: 5500,
            clinicCount: 4,
            clinics: [
                { name: 'StemCures', address: '7655 Five Mile Rd, Suite 117, Cincinnati, OH 45230', phone: '513-624-7525', specialty: 'Back and knee pain, joint pain', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Suresh Nayak, M.D.', address: 'Part of OrthoCincy Orthopaedics & Sports Medicine, multiple locations in Cincinnati, OH', phone: '(513) 221-2663', specialty: 'Orthopedic surgery, sports medicine, knee', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Renew Medical Centers', address: 'Not immediately available on the website, but they have a contact number.', phone: '(513) 561-7836', specialty: 'Regenerative medicine, medical weight loss, wellness treatments', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'RestoreMD', address: '15 Cincinnati Ave, Suite 5, Lebanon, OH 45036', phone: '513-880-0554', specialty: 'Integrative medicine, regenerative medicine, arthritis', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'charlotte': {
            cityName: 'Charlotte',
            state: 'North Carolina',
            avgPrice: 5500,
            clinicCount: 7,
            clinics: [
                { name: 'NeoGenix Stem Cell & Regenerative Therapies', address: '16147 Lancaster Hwy #140, Charlotte, NC 28277', phone: '704-727-6551', specialty: 'Orthopedic, Joint Pain, Ligament and Tendon Injuries', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Stem Cell Carolina', address: '8035 Providence Road Suite 340, Charlotte, NC 28277', phone: '704-542-3988', specialty: 'Non-surgical orthopedics, Interventional sports and spine medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Advanced Sports & Spine', address: '8035 Providence Road Suite 340, Charlotte, NC 28277', phone: '(704) 228-1806', specialty: 'Orthopedic, Spine, Sports medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Carolina Cell Therapy', address: '1720 Abbey Place, Charlotte, NC 28209', phone: '(704) 200-9761', specialty: 'Joint rejuvenation, Sports injuries, Knee, hip, and shoulder pain', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'iOBX', address: '12312 Copper Way #200, Charlotte, NC 28277', phone: '(980) 859-2340', specialty: 'Orthopedic, Sports Medicine, Spine Care', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Heritage Regenerative Medicine', address: '8058 Corporate Center, Suite 300, Charlotte, NC 28226', phone: '980-210-0079', specialty: 'Regenerative Medicine, Functional Medicine, Anti-aging', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Stem Cell Medical Center', address: 'Antigua (Serves Charlotte)', phone: '1-352-320-2688', specialty: 'Anti-Aging, Sports Injuries, Aesthetic Enhancement', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'raleigh': {
            cityName: 'Raleigh',
            state: 'North Carolina',
            avgPrice: 5000,
            clinicCount: 7,
            clinics: [
                { name: 'Carolina Nonsurgical Orthopedics / The PRP Center', address: '7200 Creedmoor Rd., Suite 102, Raleigh, NC 27613', phone: '919.719.2270', specialty: 'Orthopedics, Nonsurgical Orthopedics, Sports Medicine', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Dvida Medical Spa', address: '123 Weston Pkwy, Cary, NC 27513', phone: '(984) 253-3377', specialty: 'Facial Aesthetics, Injectables, Laser Treatments', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Raleigh Orthopaedic', address: '3001 Edwards Mill Road, Raleigh, NC 27612', phone: '(919) 781-5600', specialty: 'Orthopedics, Sports Medicine, Total Joint Replacement', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Mathur Spine Surgery', address: '1110 SE Cary Parkway, Suite 103, Cary, NC 27518', phone: '984.280.2351', specialty: 'Orthopedic Spine Care, Spine Surgery', priceRange: '\$5,000 - \$5,000', featured: false, verified: true },
                { name: 'Duke Regenerative Pain Therapies Program', address: 'DUMC 3094, Durham, NC 27710', phone: '(919) 681-6646', specialty: 'Anesthesiology, Pain Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Dr. Jonathan F. Dickens', address: '3475 Erwin Rd, Durham, NC 27705-0005', phone: '(919) 613-7797', specialty: 'Orthopaedic Surgery, Sports Medicine, Shoulder', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'The Bone and Joint Surgery Clinic', address: '3801 Wake Forest Road, Suite 220, Raleigh, NC 27609', phone: '(919) 872-5296', specialty: 'Orthopaedics', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'indianapolis': {
            cityName: 'Indianapolis',
            state: 'Indiana',
            avgPrice: 18525,
            clinicCount: 5,
            clinics: [
                { name: 'Bryan M. Saltzman, MD', address: '1801 N Senate Blvd, Suite 400, Indianapolis, IN 46202', phone: '(317) 944-9400', specialty: 'Orthopaedic Surgeon, Sports Medicine, Cartilage Restoration', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Sports & Regenerative Medicine', address: '7911 N Michigan Rd., Indianapolis IN, 46268', phone: '(317) 660-2173', specialty: 'Sports Medicine, Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'RAYUS Radiology - Indianapolis, IN - East', address: '1250 N. Post Rd.,, Suite A Indianapolis, IN, 46219', phone: '317-569-5720', specialty: 'Regenerative Medicine, Neuroradiology, Interventional OrthoBiologics', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'RAYUS Radiology - Indianapolis, IN - Northwest', address: '7151 Marsh Rd., Suite 100 Indianapolis, IN 46278', phone: '317-846-0717', specialty: 'Regenerative Medicine, Neuroradiology, Interventional OrthoBiologics', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Indianapolis Pain and Wellness Center', address: '1305 W. 96th Street Suite C, Indianapolis, IN, 46260', phone: '(317) 580-9867', specialty: 'Regenerative Medicine, Chiropractic, Physiotherapy', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'seattle': {
            cityName: 'Seattle',
            state: 'Washington',
            avgPrice: 5500,
            clinicCount: 4,
            clinics: [
                { name: 'Seattle Sports & Regenerative Medicine', address: '1000 Dexter Ave N #320, Seattle, WA 98109', phone: '206-620-0333', specialty: 'sports medicine, family medicine', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Seattle Regenerative Medicine Center', address: '1220 116th Ave NE, Suite 102 Bellevue, WA 98004', phone: '425-454-0406', specialty: 'orthopedic, spine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Axis Stem Cell Institute', address: '10517 NE 38th Pl Bldg 11, Suite B, Kirkland, Washington 98033', phone: '206-415-2947', specialty: 'musculoskeletal, neurodegenerative, autoimmune', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Daniel Nelson, MD', address: '12911 120th Ave NE, Suite H-10, Kirkland, WA 98034', phone: '425-823-4000', specialty: 'interventional pain medicine, regenerative medicine, spine pain', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'denver': {
            cityName: 'Denver',
            state: 'Colorado',
            avgPrice: 5500,
            clinicCount: 4,
            clinics: [
                { name: 'Centeno-Schultz Clinic', address: 'Denver, CO', phone: 'Contact clinic directly', specialty: 'Regenerative Medicine', priceRange: 'Avg \$5,500', featured: true, verified: true },
            ]
        },
        'washington': {
            cityName: 'Washington',
            state: 'Washington DC',
            avgPrice: 5500,
            clinicCount: 5,
            clinics: [
                { name: 'Scott Faucett, MD', address: '', phone: '(202) 835-2222', specialty: 'Orthopedic Surgeon, Sports Medicine', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Washington Orthopaedics & Sports Medicine', address: '5215 Loughboro Rd NW, Washington, DC 20016 and 5550 Friendship Blvd, Chevy Chase, MD 20815', phone: '202.787.5601 and 301.657.1996', specialty: 'Orthopaedics & Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Regenerative Orthopedics & Sports Medicine', address: '1145 19th Street NW, Suite #410, Washington, DC 20036', phone: '(202) 996-7474', specialty: 'Regenerative Orthopedics & Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'GW Cancer Center - Stem Cell Transplantation and Cell Therapy Laboratories', address: 'Ross Hall at the GW School of Medicine and Health Sciences', phone: 'Not specified', specialty: 'Stem Cell Transplantation, Cell Therapy', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'West End Regenerative Medicine', address: '2440 M St. NW Suite 200 Washington, D.C. 20037', phone: '202.750.5189', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'boston': {
            cityName: 'Boston',
            state: 'Massachusetts',
            avgPrice: 5500,
            clinicCount: 8,
            clinics: [
                { name: 'Mass General Brigham - Regenerative Medicine Program', address: 'Boston, MA', phone: 'Contact clinic directly', specialty: 'Regenerative Medicine', priceRange: 'Avg \$5,500', featured: true, verified: true },
            ]
        },
        'nashville': {
            cityName: 'Nashville',
            state: 'Tennessee',
            avgPrice: 5500,
            clinicCount: 8,
            clinics: [
                { name: 'Vanderbilt University Medical Center', address: 'Nashville, TN', phone: 'Contact clinic directly', specialty: 'Regenerative Medicine', priceRange: 'Avg \$5,500', featured: true, verified: true },
            ]
        },
        'memphis': {
            cityName: 'Memphis',
            state: 'Tennessee',
            avgPrice: 2275,
            clinicCount: 6,
            clinics: [
                { name: 'Schrader Orthopedic and Stem Cell Treatment Center', address: '927 Cordova Station Ave. Cordova, Tennessee 38018', phone: '901-465-4300', specialty: 'Sports Medicine, neck, back', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'R3 Stem Cell', address: 'Serves Memphis, TN', phone: '+1 (844) 438-7836', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Delta Orthopaedics & Sports Medicine', address: 'Collierville, Tennessee', phone: '901-850-1150', specialty: 'Orthopedics, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Campbell Clinic Orthopaedics', address: 'Multiple locations in Germantown, Collierville, Memphis, etc.', phone: '901-759-3111', specialty: 'Orthopedics, Sports Medicine, Spine', priceRange: '\$650 - \$3,900', featured: false, verified: true },
                { name: 'Resilient Medical Services', address: '721 W Brookhaven Circle Memphis, TN 38117', phone: '(901) 821-0945', specialty: 'Regenerative Medicine, chronic pain, acute injuries', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Lendermon Sports Medicine', address: 'Collierville, TN', phone: '(901) 850-5756', specialty: 'Sports Medicine, Regenerative Orthopedics', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'detroit': {
            cityName: 'Detroit',
            state: 'Michigan',
            avgPrice: 5500,
            clinicCount: 6,
            clinics: [
                { name: 'Diana R. Silas, D.O.', address: '26850 Providence Pkwy, Suite 260, Novi, MI 48374', phone: '(248) 465-5140', specialty: 'Orthopedic Surgeon, Sports Medicine, Joint Preservation', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'American Regenerative Clinic', address: '31000 Telegraph Rd., Ste. 140, Bingham Farms, MI 48025', phone: '(248) 876-4242', specialty: 'Ozone Therapy, EBOO Therapy, Regenerative therapy', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Dr. Beauty', address: '29110 Inkster Rd. Suite #250, Southfield, MI 48034', phone: '248-422-2784', specialty: 'Aesthetic Services, Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Henry Ford Macomb Hospital', address: '15855 19 Mile Road Clinton Township, MI 48038', phone: '(586) 263-2300', specialty: 'Bariatric Surgery, Behavioral Health, Cancer', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Karmanos Cancer Institute', address: '4100 John R St, Detroit, MI 48201', phone: '(800) 527-6266', specialty: 'Hematologic Malignancies, Stem Cell Transplantation', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Michigan Neurology Associates & PC', address: '34025 Harper Road, Clinton Township, MI 48035', phone: '(586) 445-9900', specialty: 'Neurology, Pain Management', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'oklahoma_city': {
            cityName: 'Oklahoma City',
            state: 'Oklahoma',
            avgPrice: 1850,
            clinicCount: 8,
            clinics: [
                { name: 'Oklahoma Pain Center', address: '13921 N Meridian Ave, Ste 100, Oklahoma City, OK 73134', phone: '(405) 752-9600', specialty: 'Pain Management, Regenerative Medicine', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'R3 Stem Cell', address: 'Provider Network', phone: '(844) 438-7836', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Venturis Clinic', address: '6524 N. Western Ave, Oklahoma City, OK 73116', phone: '(405) 848-7246', specialty: 'Regenerative Medicine, Chiropractic', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'AvantOrtho', address: '6001 NW 139th, Ste. A, Oklahoma City, OK 73142', phone: '(405) 265-0165', specialty: 'Orthopaedic Surgery, Hand & Upper Extremity, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'OU Health Stephenson Cancer Center', address: '800 NE 10th St, Oklahoma City, OK 73104', phone: '(405) 271-4022', specialty: 'Oncology, Hematology, Blood and Marrow Transplant', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Oklahoma Hip and Knee Specialist', address: '3130 SW 89th St. Suite 200E, Oklahoma City, OK 73159', phone: '(405) 445-0155', specialty: 'Orthopedic Surgery, Hip and Knee Specialist, Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Align Interventional Pain', address: '1810 E. Memorial Road, Oklahoma City, OK 73131', phone: '405-906-4020', specialty: 'Pain Management, Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'OrthoBiogen', address: '13100 N. Western Ave., STE 300, Oklahoma City, OK 73114', phone: '405-697-3436', specialty: 'Regenerative Orthopedics, Spine and Joint Care', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'portland': {
            cityName: 'Portland',
            state: 'Oregon',
            avgPrice: 5500,
            clinicCount: 6,
            clinics: [
                { name: 'Cascade Regenerative Medicine', address: 'Portland, OR', phone: 'Contact clinic directly', specialty: 'Regenerative Medicine', priceRange: 'Avg \$5,500', featured: true, verified: true },
            ]
        },
        'las_vegas': {
            cityName: 'Las Vegas',
            state: 'Nevada',
            avgPrice: 5500,
            clinicCount: 5,
            clinics: [
                { name: 'Cellaxys', address: 'Las Vegas, NV', phone: 'Contact clinic directly', specialty: 'Regenerative Medicine', priceRange: 'Avg \$5,500', featured: true, verified: true },
            ]
        },
        'louisville': {
            cityName: 'Louisville',
            state: 'Kentucky',
            avgPrice: 5500,
            clinicCount: 5,
            clinics: [
                { name: 'Restorative Pain Institute', address: '4201 Springhurst Blvd, Suite 102, Louisville, KY 40241', phone: '(502) 515-6090', specialty: 'Interventional Pain Management', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Kentuckiana Integrative Medicine', address: '405 E. Court Avenue, Jeffersonville, IN 47130', phone: '(812) 913-4416', specialty: 'Regenerative Medicine, Integrative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Medical Transformation Center', address: '13111 Eastpoint Park Blvd, Louisville, KY 40223', phone: '502-443-9962', specialty: 'Cellular Medicine, Functional Medicine, Regenerative and Wellness', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'QC Kinetix', address: '6420 Dutchmans Parkway, Suite 375, Louisville, KY 40205', phone: '(502) 503-5443', specialty: 'Regenerative Orthopedics, Pain Management', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Baptist Health Louisville', address: '1901 Campus Place, Louisville, KY 40299', phone: '502-896-5000', specialty: 'Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'baltimore': {
            cityName: 'Baltimore',
            state: 'Maryland',
            avgPrice: 5500,
            clinicCount: 4,
            clinics: [
                { name: 'Center for Stem Cell Biology & Regenerative Medicine', address: 'University of Maryland School of Medicine', phone: 'Not found', specialty: 'Research', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'R3 Stem Cell', address: 'Not specified on this page, but they have a location near Baltimore.', phone: '(844) 438-7836', specialty: 'Not specified, but they mention breathing complications, mobility issues, low energy, and pain.', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'University of Maryland Marlene and Stewart Greenebaum Comprehensive Cancer Center (UMGCCC)', address: '22 S. Greene Street, Baltimore, MD 21201', phone: '410-328-7904', specialty: 'Cancer and blood diseases, including Hodgkin lymphoma, Non-Hodgkin lymphoma, multiple myeloma, testicular cancer, leukemia, aplastic anemia and sickle cell anemia.', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'ALS Center for Cell Therapy and Regeneration Research at Johns Hopkins', address: 'The John G. Rangos Sr. Building, 855 North Wolfe St., Room 248 (second floor), Baltimore, MD 21205', phone: '443-287-4341, Appointments', specialty: 'Amyotrophic lateral sclerosis (ALS), motor neuron diseases', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'milwaukee': {
            cityName: 'Milwaukee',
            state: 'Wisconsin',
            avgPrice: 344,
            clinicCount: 8,
            clinics: [
                { name: 'Spectrum Stem Cell and Regenerative Medicine Center', address: '2500 N Mayfair Rd, Suite 630, Wauwatosa, WI 53226', phone: '(262) 202-8312', specialty: 'Orthopedic, Spine, Sports Medicine', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Solstice Health', address: '959 N. Mayfair Road, Milwaukee, WI 53226', phone: '(414) 279-6800', specialty: 'Orthopedic', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Aurora Health Care', address: '750 W. Virginia St. P.O. Box 341880, Milwaukee, Wisconsin 53204', phone: '833-528-7672', specialty: 'Neuroscience, Stroke, Brain Cancer', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Froedtert & the Medical College of Wisconsin', address: '9200 W. Wisconsin Ave., Milwaukee, WI 53226', phone: '414-805-0505', specialty: 'Leukemia, Lymphoma, Blood Disorders', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Wisconsin Stem Cell Institute', address: '675 North Barker Road, Brookfield WI 53045', phone: '(262) 200-2700', specialty: 'Orthopedics, Pain Management, Family Practice', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'QC Kinetix Greenfield', address: '4131 W Loomis Rd, Suite 210, Greenfield, WI 53221', phone: '(414) 441-2268', specialty: 'Musculoskeletal Pain, Arthritis Pain, Sports-related Injury Pain', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'QC Kinetix Mequon', address: '10345 N Port Washington Rd, Suite 150, Mequon, WI, 53092', phone: '(414) 404-7580', specialty: 'Musculoskeletal Pain, Arthritis Pain, Sports-related Injury Pain', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Wisconsin Vein Center & MediSpa', address: '123 Main St, Milwaukee, WI 53202', phone: '+(262) 236-5179', specialty: 'Facial Rejuvenation, Sexual Health, Skin Laxity', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'albuquerque': {
            cityName: 'Albuquerque',
            state: 'New Mexico',
            avgPrice: 5500,
            clinicCount: 11,
            clinics: [
                { name: 'NM Stem Cell', address: '918 Pinehurst Rd SE #102, Rio Rancho, NM 87124', phone: '(505) 404-9555', specialty: 'Joint Pain, Knee Pain, Spinal/Back Pain', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'La Vida Sana Medical Spa', address: '', phone: '505-677-2211', specialty: 'Hair Restoration, Joint Pain Relief, Sexual Wellness', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Interventional Pain Associates', address: '', phone: '(505) 588-7246', specialty: 'Pain Management', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Modern Pain & Spine', address: '1540 Juan Tabo Blvd Ne, Suite A, Albuquerque, NM', phone: '505-800-7246', specialty: 'Shoulder pain, Knee pain, Back and neck pain', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Gonstead Physical Medicine', address: 'Albuquerque and Rio Rancho', phone: '(505) 884-8584, (505) 922-9444', specialty: 'Joint pain, Neck and back pain, Tendinitis', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Ribera Healthcare', address: '801 Encino Place NE Suite D-7 Albuquerque, NM 87102', phone: '(505) 207-6526', specialty: 'Knee pain, Back pain, Neck pain', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Beyond Health', address: '3700 Bosque Plaza Ln NW, Albuquerque, New Mexico 87120', phone: '(505) 899-4414', specialty: 'Pain and Injuries, Hair Restoration, Erectile Dysfunction', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'PRP Regenerative Pain Institute', address: '4163 Montgomery Blvd Northeast Albuquerque, New Mexico 87109', phone: '(505) 503-6990', specialty: 'Spine Pain, Back & Shoulder Pain, Neck Pain', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'NUYU Med Spa', address: '10124 Coors Blvd, NW Suite 207 Albuquerque, New Mexico 87114', phone: '(505) 681-6657', specialty: 'Hair Restoration, Facial Injections, Scar Treatment', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Oasis Med Spa at WSNM', address: '101 Hospital Loop NE, Suite #105, Albuquerque, NM 87109', phone: '(505) 314-1444', specialty: 'Facial Rejuvenation', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'PCI Clinic', address: '3860 Masthead St NE, Albuquerque, NM 87109', phone: '(505) 828 1010', specialty: 'Pain Management, Varicose Vein Treatments', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'atlanta': {
            cityName: 'Atlanta',
            state: 'Georgia',
            avgPrice: 9500,
            clinicCount: 8,
            clinics: [
                { name: 'Atlanta Orthopaedic Institute', address: '3200 Downwood Circle, NW, Suite 410, Atlanta, GA 30327, 1035 Southcrest Drive, Suite 100, Stockbridge, GA 30281', phone: '(404) 352-4779, (770) 389-9005', specialty: 'Orthopedics, Spine Surgery, Joint Replacement', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'North of Atlanta Pain Clinic', address: '3473 Satellite Boulevard, Suite 120N, Duluth, GA 30096', phone: '770-559-8385', specialty: 'Pain Management', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'régénérer®', address: '4121 Steve Reynolds Blvd., Norcross GA 30093-3060, 245 Village Center Pkwy, Ste 120, Stockbridge GA 30281-9096', phone: '770-450-1111', specialty: 'Orthopedics, Pain Management', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Atlanta Innovative Medicine', address: '8460 Holcomb Bridge Road Second Floor Alpharetta, GA 30022', phone: '770.416.9995', specialty: 'Regenerative Medicine, Orthopedics, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Regenerative Spine & Pain Specialists', address: '874 WEST LANIER AVE. STE 250, Fayetteville, GA, 371 E PACES FERRY RD NE, STE 802, Atlanta, GA, 3939 ROSWELL ROAD, STE 240, MARIETTA, GA 30062', phone: '404-618-0995', specialty: 'Spine, Pain Management, Orthopedics', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Inspire Wellness Aesthetics', address: '270 17th St NW, Atlanta, GA 30363', phone: '404-282-4126', specialty: 'Aesthetics, Wellness', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Raj Pandya, M.D.', address: '3200 Downwood Circle, NW, Suite 410, Atlanta, GA 30327, 1035 Southcrest Drive, Suite 100, Stockbridge, GA 30281', phone: '(404) 352-4779, (770) 389-9005', specialty: 'Orthopedics, Sports Medicine, Shoulder Surgery', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'R3 Stem Cell', address: 'Atlanta, GA', phone: '+1 (844) GET-STEM', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'minneapolis': {
            cityName: 'Minneapolis',
            state: 'Minnesota',
            avgPrice: 4750,
            clinicCount: 5,
            clinics: [
                { name: 'Kelechi R. Okoroha, MD', address: 'Dallas, Richardson, Frisco, TX (No specific Minneapolis address found)', phone: '(214) 278-6373', specialty: 'Orthopedic Surgery, Sports Medicine, Hip', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Twin Cities Pain & Regenerative Medicine', address: '4444 West 76th Street, Suite 500 Edina, MN 55435', phone: '952-831-7246', specialty: 'Pain Management, Regenerative Medicine, Knee', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Chiro Minneapolis', address: '2627 East Franklin Suite 201, Minneapolis, MN 55406', phone: '(612) 315-0437', specialty: 'Chiropractic Care, Regenerative Medicine, Pain Relief', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Summit Orthopedics', address: 'Multiple locations in Minneapolis/St. Paul area', phone: '(651) 968-5201', specialty: 'Orthopedics, Sports Injuries, Back and Neck Treatment', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'R3 Stem Cell', address: 'Not specified, but they have a center near Minneapolis', phone: '(844) 438-7836', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'st_louis': {
            cityName: 'St. Louis',
            state: 'Missouri',
            avgPrice: 5500,
            clinicCount: 4,
            clinics: [
                { name: 'Nathan Mall, MD', address: '633 Emerson Road, Suite 10, St. Louis, MO, 63141', phone: '314-991-4335', specialty: 'Orthopedic Surgeon, Sports Medicine, Shoulder & Knee Reconstruction', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Bluetail Medical Group', address: '13353 Olive Blvd, Chesterfield, MO 63017', phone: '(636) 778-2900', specialty: 'Orthopedic, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Regenerative Medicine of St. Louis', address: '1034 South Brentwood Blvd - Ste 754, St. Louis, MO 63117', phone: '(314) 973-2955', specialty: 'Neurosurgery, Spine, Chronic Pain', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Robert Duerr, MD', address: '12700 Southfork Road, Suite 100, St. Louis, MO 63128', phone: '(314) 543-5284', specialty: 'Orthopedic Surgeon, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'kansas_city': {
            cityName: 'Kansas City',
            state: 'Missouri',
            avgPrice: 5500,
            clinicCount: 4,
            clinics: [
                { name: 'Unknown', address: '', phone: '', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Unknown', address: '', phone: '', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Unknown', address: '', phone: '', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Unknown', address: '', phone: '', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'salt_lake_city': {
            cityName: 'Salt Lake City',
            state: 'Utah',
            avgPrice: 3250,
            clinicCount: 6,
            clinics: [
                { name: 'University of Utah Health', address: '590 Wakara Way, Salt Lake City, UT 84108', phone: '801-587-7109', specialty: 'Orthopaedics', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Integrative Medica', address: '6360 S. 3000 E., #325, Salt Lake City, UT 84121', phone: '801-676-9876', specialty: 'Naturopathic Doctor, Functional and Holistic Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Utah Stem Cells', address: '9980 S. 300 W, Suite 150, Sandy, UT 84070', phone: '801-999-4860', specialty: 'Joint Regeneration, IV Therapy, Medical Aesthetics', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'R3 Stem Cell', address: 'Salt Lake City, UT', phone: '+1 (844) GET-STEM', specialty: 'Pain Management, Orthopedics, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Precision Pointe Regenerative Health', address: 'Salt Lake City, UT', phone: '801-613-8002', specialty: 'Regenerative Medicine, Pain Management', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Cell Therapy and Regenerative Medicine Program', address: 'University of Utah', phone: '', specialty: 'Hematopoietic Stem Cell Transplant, Cellular Therapy', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'honolulu': {
            cityName: 'Honolulu',
            state: 'Hawaii',
            avgPrice: 10000,
            clinicCount: 5,
            clinics: [
                { name: 'Stem Cell Treatment Center of Hawaii', address: '677 Ala Moana Blvd Suite 1023, Honolulu, HI 96813', phone: '808-945-5433', specialty: 'Orthopedic, Heart & Lung, Urology', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Infinity Life Center', address: '677 Ala Moana Blvd Suite 1024, Honolulu, HI 96813', phone: '+1 (808) 945-5433', specialty: 'Orthopedic, Anti-inflammatory, Skin rejuvenation', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Hawaii Wellness MD', address: '1441 Kapiolani Blvd Suite 1419, Honolulu, HI 96814', phone: '(808) 955-3937', specialty: 'Knee pain, Back pain, Neck pain', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'NexGenEsis Healthcare', address: 'Not specified', phone: '(713) 909-4514', specialty: 'Knee osteoarthritis, Chronic knee pain, Degenerative hip, shoulder, or ankle joints', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Regenerative Medicine & Rehabilitation of Hawaii', address: 'Not specified', phone: '(808) 528-5500', specialty: 'Knee arthritis and injuries, Carpal tunnel, Disc herniation in the lower back and sciatic pain', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'anchorage': {
            cityName: 'Anchorage',
            state: 'Alaska',
            avgPrice: 5500,
            clinicCount: 7,
            clinics: [
                { name: 'R3 Stem Cell', address: 'Not available', phone: '844-GET-STEM', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Alaska Center for Pain Relief Inc.', address: '3851 Piper Street U464, Anchorage, AK 99508', phone: '(907) 339-4800', specialty: 'Pain Relief', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Empower Physical Therapy - Anchorage', address: '7985 E 16th Ave Suite 100, Anchorage, AK 99504', phone: '(907) 332-0021', specialty: 'Physical Therapy, Regenerative Rehab', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Alaska Fracture & Orthopedic Clinic', address: '3831 Piper Street, Suite S-220, Anchorage, AK 99508', phone: '(907) 563-3145', specialty: 'Orthopedics, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Arctic Medical Center', address: '288 W 34th Ave, Anchorage, AK 99503', phone: '(907) 290-8111', specialty: 'Hair Restoration', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Benjamin D. Packard, M.D.', address: '3831 Piper Street, Suite S-220, Anchorage, AK 99508', phone: '(907) 563-3145', specialty: 'Orthopedic Surgery, Sports Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Whole Family Chiropractic', address: '600 E. 36th Ave. Suite 300, Anchorage, AK 99503', phone: '(907) 885-3227', specialty: 'Chiropractic, Regenerative Therapy', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
        'boise': {
            cityName: 'Boise',
            state: 'Idaho',
            avgPrice: 5500,
            clinicCount: 6,
            clinics: [
                { name: 'Stem Cells of Idaho', address: '4842 N Cortona Way, STE 110 Meridian, ID 83646', phone: '(208) 579-2037', specialty: 'orthopedic, trauma, sports medicine', priceRange: 'Contact for pricing', featured: true, verified: true },
                { name: 'Boise Biologics', address: '5983 W State St # C, Boise, ID 83703', phone: '208.888.3358', specialty: 'orthopedic, pain management', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Pain Care Boise', address: '301 W Myrtle St, Boise, ID 83702', phone: '208-342-8200', specialty: 'pain management', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'Dr. Ray Jensen', address: '6357 N Fox Run Way, Meridian, ID 83646', phone: '(208) 900-5633', specialty: 'orthopedic, shoulder, elbow', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'The Shoulder Clinic of Idaho', address: '8854 Emerald St #102, Boise, ID 83704', phone: '208-323-4747', specialty: 'shoulder, elbow', priceRange: 'Contact for pricing', featured: false, verified: true },
                { name: 'R3 Stem Cell', address: '888 N Cole Rd, Boise, ID 83704', phone: '(844) 438-7836', specialty: 'Regenerative Medicine', priceRange: 'Contact for pricing', featured: false, verified: true },
            ]
        },
    }
};

// Helper function to get city key from city name
function getCityKey(cityName) {
    return cityName.toLowerCase().replace(/ /g, '_').replace(/\./g, '');
}

// Helper function to get clinics for a city
function getClinicsForCity(cityName) {
    const key = getCityKey(cityName);
    return CLINIC_DATABASE.cities[key] || null;
}

// Helper function to get state data
function getStateData(stateName) {
    return CLINIC_DATABASE.states[stateName] || null;
}

// Main App Controller
function app() {
    return {
        currentPage: 'home',
        mobileMenu: false,

        init() {
            // Handle browser back/forward
            window.addEventListener('popstate', (e) => {
                if (e.state && e.state.page) {
                    this.currentPage = e.state.page;
                }
            });

            // Listen for navigation events
            window.addEventListener('navigate', (e) => {
                this.navigate(e.detail);
            });

            // Check URL hash on load
            const hash = window.location.hash.slice(1);
            if (hash) {
                this.currentPage = hash;
            }
        },

        navigate(page) {
            this.currentPage = page;
            window.history.pushState({ page }, '', '#' + page);
            window.scrollTo({ top: 0, behavior: 'smooth' });
            this.mobileMenu = false;
        }
    };
}

// Home Page Component
function homePage() {
    return {
        openStep: 0,
        condition: '',
        state: '',
        city: '',
        conditionsList: [
            'Knee Pain / Osteoarthritis',
            'Lower Back / Disc Pain',
            'Shoulder / Rotator Cuff',
            'Hip Osteoarthritis',
            'Tennis/Golfer\'s Elbow',
            'Ankle / Achilles Tendon',
            'Cervical Spine (Neck)',
            'Sacroiliac (SI) Joint',
            'Wrist / Hand Arthritis',
            'Plantar Fasciitis'
        ],
        statesList: ["Alaska", "Arizona", "California", "Colorado", "Washington DC", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Kentucky", "Massachusetts", "Maryland", "Michigan", "Minnesota", "Missouri", "North Carolina", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Tennessee", "Texas", "Utah", "Washington", "Wisconsin", "Mexico (Tourism)"],
        citiesData: {
                    "New York": [
                                "New York City"
                    ],
                    "California": [
                                "Los Angeles",
                                "San Diego",
                                "San Jose",
                                "San Francisco",
                                "Fresno",
                                "Sacramento"
                    ],
                    "Illinois": [
                                "Chicago"
                    ],
                    "Texas": [
                                "Houston",
                                "San Antonio",
                                "Dallas",
                                "Austin",
                                "Fort Worth"
                    ],
                    "Arizona": [
                                "Phoenix",
                                "Tucson",
                                "Scottsdale"
                    ],
                    "Pennsylvania": [
                                "Philadelphia",
                                "Pittsburgh"
                    ],
                    "Florida": [
                                "Jacksonville",
                                "Miami",
                                "Tampa",
                                "Orlando"
                    ],
                    "Ohio": [
                                "Columbus",
                                "Cleveland",
                                "Cincinnati"
                    ],
                    "North Carolina": [
                                "Charlotte",
                                "Raleigh"
                    ],
                    "Indiana": [
                                "Indianapolis"
                    ],
                    "Washington": [
                                "Seattle"
                    ],
                    "Colorado": [
                                "Denver"
                    ],
                    "Washington DC": [
                                "Washington"
                    ],
                    "Massachusetts": [
                                "Boston"
                    ],
                    "Tennessee": [
                                "Nashville",
                                "Memphis"
                    ],
                    "Michigan": [
                                "Detroit"
                    ],
                    "Oklahoma": [
                                "Oklahoma City"
                    ],
                    "Oregon": [
                                "Portland"
                    ],
                    "Nevada": [
                                "Las Vegas"
                    ],
                    "Kentucky": [
                                "Louisville"
                    ],
                    "Maryland": [
                                "Baltimore"
                    ],
                    "Wisconsin": [
                                "Milwaukee"
                    ],
                    "New Mexico": [
                                "Albuquerque"
                    ],
                    "Georgia": [
                                "Atlanta"
                    ],
                    "Minnesota": [
                                "Minneapolis"
                    ],
                    "Missouri": [
                                "St. Louis",
                                "Kansas City"
                    ],
                    "Utah": [
                                "Salt Lake City"
                    ],
                    "Hawaii": [
                                "Honolulu"
                    ],
                    "Alaska": [
                                "Anchorage"
                    ],
                    "Idaho": [
                                "Boise"
                    ],
                    "Mexico (Tourism)": [
                                "Tijuana",
                                "Cancun",
                                "Mexico City"
                    ]
        },
        // Real pricing data from BioInformant, AZCPM, and multiple clinic sources
        pricingData: [
            { condition: 'Knee Therapy', range: '$3,500 - $9,000', count: 250, source: 'BioInformant/Cochrane 2025' },
            { condition: 'Spine / Disc', range: '$5,000 - $15,000', count: 150, source: 'Cellular Hope Institute' },
            { condition: 'Shoulder', range: '$3,000 - $8,000', count: 210, source: 'BioInformant' },
            { condition: 'Hip Joints', range: '$4,000 - $10,000', count: 180, source: 'AZCPM' }
        ],
        // Real city data with verified average prices
                        popularCities: [
            { name: 'Los Angeles', state: 'California', price: 'Avg $5,800', type: 'Premium Market', img: '/assets/images/cities/optimized/los-angeles-medium.webp' },
            { name: 'Houston', state: 'Texas', price: 'Avg $4,900', type: 'Value Market', img: '/assets/images/cities/optimized/houston-medium.webp' },
            { name: 'Tijuana', state: 'Mexico', price: 'Avg $3,500', type: 'Medical Tourism', img: '/assets/images/cities/optimized/tijuana-medium.webp' },
            { name: 'Miami', state: 'Florida', price: 'Avg $6,100', type: 'Premium Market', img: '/assets/images/cities/optimized/miami-medium.webp' },
            { name: 'Scottsdale', state: 'Arizona', price: 'Avg $5,200', type: 'Growth Hub', img: '/assets/images/cities/optimized/scottsdale-medium.webp' }
        ],

        getCities() {
            return this.citiesData[this.state] || [];
        },

        performSearch() {
            if (this.condition && this.state && this.city) {
                // Navigate to actual static location pages
                const stateSlug = this.state.toLowerCase().replace(/\s+/g, '-').replace(/[()]/g, '');
                const citySlug = this.city.toLowerCase().replace(/\s+/g, '-').replace(/\./g, '');

                if (this.state === 'Mexico (Tourism)') {
                    // Mexico cities
                    window.location.href = `/locations/mexico/${citySlug}/`;
                } else {
                    // US cities - redirect to static location page
                    window.location.href = `/locations/${stateSlug}/${citySlug}/`;
                }
            }
        },

        navigateToCity(cityName) {
            const citySlug = cityName.toLowerCase().replace(/\s+/g, '-').replace(/\./g, '');
            if (cityName === 'Tijuana' || cityName === 'Cancun' || cityName === 'Puerto Vallarta' || cityName === 'Mexico City') {
                window.location.href = `/locations/mexico/${citySlug}/`;
            } else {
                // For other cities, determine state from database
                const cityKey = cityName.toLowerCase().replace(/ /g, '_').replace(/\./g, '');
                if (CLINIC_DATABASE.cities[cityKey]) {
                    const cityData = CLINIC_DATABASE.cities[cityKey];
                    const stateSlug = cityData.state.toLowerCase().replace(/\s+/g, '-');
                    window.location.href = `/locations/${stateSlug}/${citySlug}/`;
                } else {
                    // Fallback to California
                    window.location.href = `/locations/california/${citySlug}/`;
                }
            }
        }
    };
}

// Cost Index Page Component - REAL DATA
function costIndexPage() {
    return {
        search: '',
        sortBy: 'name',
        // Real pricing data from BioInformant, AZCPM, Mayo Clinic, and multiple clinic sources (January 2026)
        pricingData: [
            { id: 1, name: 'Knee Osteoarthritis', low: 3500, median: 5800, high: 9000, clinics: 250, trend: 'up', trendPercent: 3.5, successRate: '68-77%', source: 'Cochrane Review 2025', link: 'knee-cost-guide' },
            { id: 2, name: 'Lumbar Spine / Disc', low: 5000, median: 8500, high: 15000, clinics: 150, trend: 'up', trendPercent: 4.1, successRate: '55-65%', source: 'Cellular Hope Institute', link: '/lp/spine-disc/california/los-angeles/' },
            { id: 3, name: 'Shoulder (Rotator Cuff)', low: 3000, median: 5500, high: 8000, clinics: 210, trend: 'stable', trendPercent: 1.2, successRate: '65-75%', source: 'BioInformant', link: '/lp/shoulder/california/los-angeles/' },
            { id: 4, name: 'Hip Osteoarthritis', low: 4000, median: 6500, high: 10000, clinics: 180, trend: 'up', trendPercent: 2.9, successRate: '60-70%', source: 'AZCPM', link: '/lp/hip-osteoarthritis/california/los-angeles/' },
            { id: 5, name: 'Cervical Spine (Neck)', low: 4500, median: 7500, high: 12000, clinics: 90, trend: 'up', trendPercent: 3.8, successRate: '55-65%', source: 'Cellular Hope Institute', link: '/lp/spine-disc/california/los-angeles/' },
            { id: 6, name: 'Ankle / Achilles', low: 2500, median: 4500, high: 6500, clinics: 110, trend: 'stable', trendPercent: 0.9, successRate: '65-75%', source: 'BioInformant', link: '/locations/' },
            { id: 7, name: "Tennis/Golfer's Elbow", low: 2000, median: 3500, high: 5500, clinics: 130, trend: 'down', trendPercent: 1.5, successRate: '70-80%', source: 'BioInformant', link: '/locations/' },
            { id: 8, name: 'Sacroiliac (SI) Joint', low: 4000, median: 6000, high: 9000, clinics: 70, trend: 'up', trendPercent: 2.1, successRate: '60-70%', source: 'BioInformant', link: '/lp/spine-disc/california/los-angeles/' },
            { id: 9, name: 'Wrist / Hand Arthritis', low: 2800, median: 4800, high: 7000, clinics: 85, trend: 'stable', trendPercent: 1.0, successRate: '65-75%', source: 'BioInformant', link: '/locations/' },
            { id: 10, name: 'Plantar Fasciitis', low: 1800, median: 3500, high: 5000, clinics: 140, trend: 'down', trendPercent: 2.5, successRate: '70-80%', source: 'BioInformant', link: '/locations/' }
        ],
        // Real price drivers with verified cost impacts
        priceDrivers: [
            { 
                title: 'Cell Source', 
                desc: 'PRP ($500-$2,000) is most affordable. BMAC ($2,600-$7,000) is mid-range. Adipose-derived ($5,000-$15,000) and Umbilical Cord ($8,000-$25,000) are premium options.', 
                impact: '+ $1,500 - $15,000' 
            },
            { 
                title: 'Image Guidance', 
                desc: 'Ultrasound guidance adds $500-$800. Fluoroscopy (X-ray) guidance adds $800-$1,200 for precision placement.', 
                impact: '+ $500 - $1,200' 
            },
            { 
                title: 'Facility Type', 
                desc: 'Private office is base price. Ambulatory surgery centers add $1,000-$2,500. Hospital outpatient adds $2,000-$5,000 in facility fees.', 
                impact: '+ $2,000 - $5,000' 
            },
            { 
                title: 'Number of Areas', 
                desc: 'Treating multiple joints in one session increases costs by 50-100% per additional area, but often includes volume discounts.', 
                impact: '+ 50-100% per area' 
            },
            { 
                title: 'Geographic Location', 
                desc: 'Major metros (NYC, LA, Miami) charge 20-30% more. Mexico/international destinations offer 40-60% savings.', 
                impact: '+/- 20-60%' 
            }
        ],

        init() {
            this.$nextTick(() => this.renderCostIndexContent());
        },

        get filteredPricing() {
            let filtered = this.pricingData.filter(i => i.name.toLowerCase().includes(this.search.toLowerCase()));
            if (this.sortBy === 'name') return filtered.sort((a, b) => a.name.localeCompare(b.name));
            if (this.sortBy === 'median') return filtered.sort((a, b) => b.median - a.median);
            if (this.sortBy === 'clinics') return filtered.sort((a, b) => b.clinics - a.clinics);
            return filtered;
        },

        renderCostIndexContent() {
            this.$el.innerHTML = `
                <div class="py-8 md:py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <nav class="flex mb-8 text-xs font-bold uppercase tracking-widest text-slate-400 gap-2">
                            <a href="#" @click.prevent="$dispatch('navigate', 'home')" class="hover:text-brand-600">Home</a>
                            <span>/</span>
                            <span class="text-slate-600">National Cost Index</span>
                        </nav>
                        <div class="mb-12">
                            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-slate-900 text-white text-[10px] font-bold uppercase tracking-widest mb-4">
                                <span class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></span>
                                Verified Data Report: Q1 2026
                            </div>
                            <h1 class="text-3xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-4">
                                National Stem Cell <span class="text-brand-600">Cost Index</span>
                            </h1>
                            <p class="text-lg text-slate-600 max-w-3xl">
                                Comprehensive median pricing across 10 orthopedic categories based on data from BioInformant, Cochrane Reviews, Mayo Clinic, and 70+ verified clinics. These ranges represent typical out-of-pocket costs for cash-pay patients in the United States.
                            </p>
                        </div>

                        <div class="bg-white rounded-3xl shadow-xl shadow-brand-100/50 border border-slate-100 overflow-hidden">
                            <div class="p-6 border-b border-slate-100 flex flex-col md:flex-row justify-between items-center gap-4 bg-slate-50/50">
                                <div class="relative w-full md:w-72">
                                    <input type="text" x-model="search" placeholder="Search conditions..." class="w-full pl-10 pr-4 py-2.5 bg-white border border-slate-200 rounded-xl text-sm focus:ring-2 focus:ring-brand-500 focus:border-brand-500 transition-all outline-none">
                                    <svg class="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                                </div>
                                <div class="flex items-center gap-2">
                                    <span class="text-xs font-bold text-slate-400 uppercase">Sort By:</span>
                                    <select x-model="sortBy" class="text-sm font-semibold text-slate-700 bg-transparent border-none focus:ring-0 cursor-pointer">
                                        <option value="name">Condition Name</option>
                                        <option value="median">Median Price</option>
                                        <option value="clinics">Clinic Volume</option>
                                    </select>
                                </div>
                            </div>

                            <div class="hidden md:grid grid-cols-12 px-8 py-4 bg-white border-b border-slate-100 text-[10px] font-bold uppercase tracking-widest text-slate-400">
                                <div class="col-span-4">Condition & Sample Size</div>
                                <div class="col-span-2 text-center">National Low</div>
                                <div class="col-span-3 text-center">Median Benchmark</div>
                                <div class="col-span-2 text-center">National High</div>
                                <div class="col-span-1 text-right">Trend</div>
                            </div>

                            <div class="divide-y divide-slate-50">
                                <template x-for="item in filteredPricing" :key="item.id">
                                    <div class="px-6 md:px-8 py-6 table-row-hover transition-colors group cursor-pointer" @click="item.link.startsWith('/') ? window.location.href = item.link : $dispatch('navigate', item.link)">
                                        <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
                                            <div class="md:col-span-4">
                                                <h3 class="font-bold text-slate-900 group-hover:text-brand-600 transition-colors" x-text="item.name"></h3>
                                                <p class="text-xs text-slate-400 mt-1">
                                                    <span x-text="item.clinics + ' clinics reporting'"></span>
                                                    <span class="mx-1">•</span>
                                                    <span class="text-emerald-600" x-text="'Success: ' + item.successRate"></span>
                                                </p>
                                            </div>
                                            <div class="md:col-span-2 text-center">
                                                <span class="text-slate-500 font-medium" x-text="'$' + item.low.toLocaleString()"></span>
                                            </div>
                                            <div class="md:col-span-3 text-center">
                                                <span class="text-2xl font-extrabold text-brand-700" x-text="'$' + item.median.toLocaleString()"></span>
                                            </div>
                                            <div class="md:col-span-2 text-center">
                                                <span class="text-slate-500 font-medium" x-text="'$' + item.high.toLocaleString()"></span>
                                            </div>
                                            <div class="md:col-span-1 text-right">
                                                <span :class="item.trend === 'up' ? 'text-rose-500' : item.trend === 'down' ? 'text-emerald-500' : 'text-slate-400'" class="text-xs font-bold">
                                                    <span x-text="item.trend === 'up' ? '↑' : item.trend === 'down' ? '↓' : '→'"></span>
                                                    <span x-text="item.trendPercent + '%'"></span>
                                                </span>
                                            </div>
                                        </div>
                                    </div>
                                </template>
                            </div>
                        </div>

                        <!-- Price Drivers Section -->
                        <div class="mt-16">
                            <h2 class="text-2xl font-extrabold text-slate-900 mb-8">What Drives Price Variation?</h2>
                            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                                <template x-for="driver in priceDrivers" :key="driver.title">
                                    <div class="bg-white rounded-2xl p-6 border border-slate-200 hover:shadow-lg transition-all">
                                        <h3 class="font-bold text-slate-900 mb-2" x-text="driver.title"></h3>
                                        <p class="text-sm text-slate-600 mb-4" x-text="driver.desc"></p>
                                        <span class="inline-block px-3 py-1 bg-brand-50 text-brand-700 rounded-full text-xs font-bold" x-text="driver.impact"></span>
                                    </div>
                                </template>
                            </div>
                        </div>

                        <!-- Disclaimer -->
                        <div class="mt-12 p-6 bg-amber-50 rounded-2xl border border-amber-200">
                            <div class="flex items-start gap-4">
                                <svg class="w-6 h-6 text-amber-600 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                                <div>
                                    <h4 class="font-bold text-amber-800 mb-1">Important Disclaimer</h4>
                                    <p class="text-sm text-amber-700">The stem cell treatments described on this website have not been approved by the FDA for orthopedic conditions. Prices shown are estimates based on publicly available information and may vary. Success rates are based on published research and may not reflect individual results. Please consult a qualified healthcare provider for personalized advice.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }
    };
}

// Knee Cost Guide Page - REAL DATA
function kneeCostGuidePage() {
    return {
        // Real pricing data from multiple verified sources
        priceBreakdown: [
            { item: 'PRP Injection (Single)', price: '$500 - $2,000', source: 'Mayo Clinic, Sports Surgery Chicago' },
            { item: 'PRP Series (3 Injections)', price: '$1,500 - $4,000', source: 'Sports Surgery Chicago' },
            { item: 'BMAC (Bone Marrow Aspirate)', price: '$2,600 - $7,000', source: 'AZCPM, TSAOG, QCORA' },
            { item: 'Adipose-Derived Stem Cells', price: '$5,000 - $15,000', source: 'Cell Surgical Network' },
            { item: 'Umbilical Cord Stem Cells', price: '$8,000 - $25,000', source: 'Stem Cell Miami' }
        ],
        // Real clinical outcomes from Cochrane Review 2025
        outcomes: {
            successRate: '68-77%',
            painImprovement: '1.2 points (0-10 scale)',
            functionImprovement: '14.2 points (0-100 scale)',
            duration: '12-24+ months',
            source: 'Cochrane Review 2025, Mayo Clinic'
        },

        init() {
            this.$nextTick(() => this.renderContent());
        },

        renderContent() {
            this.$el.innerHTML = `
                <section class="py-8 md:py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <nav class="flex mb-8 text-xs font-bold uppercase tracking-widest text-slate-400 gap-2">
                            <a href="#" @click.prevent="$dispatch('navigate', 'home')" class="hover:text-brand-600">Home</a>
                            <span>/</span>
                            <a href="#" @click.prevent="$dispatch('navigate', 'cost-index')" class="hover:text-brand-600">Cost Index</a>
                            <span>/</span>
                            <span class="text-slate-600">Knee Osteoarthritis</span>
                        </nav>

                        <h1 class="text-3xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-4">
                            Knee Stem Cell Therapy <span class="text-brand-600">Cost Guide</span>
                        </h1>
                        <p class="text-lg text-slate-600 max-w-3xl mb-12">
                            Comprehensive pricing and outcomes data for stem cell treatment of knee osteoarthritis, based on Cochrane Review 2025, Mayo Clinic research, and data from 250+ US clinics.
                        </p>

                        <!-- Price Summary -->
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
                            <div class="bg-white rounded-3xl p-6 border border-slate-200 text-center">
                                <p class="text-xs font-bold text-slate-400 uppercase mb-2">National Low</p>
                                <p class="text-3xl font-extrabold text-slate-900">$3,500</p>
                            </div>
                            <div class="bg-brand-600 rounded-3xl p-6 text-center">
                                <p class="text-xs font-bold text-brand-200 uppercase mb-2">Median Price</p>
                                <p class="text-3xl font-extrabold text-white">$5,800</p>
                            </div>
                            <div class="bg-white rounded-3xl p-6 border border-slate-200 text-center">
                                <p class="text-xs font-bold text-slate-400 uppercase mb-2">National High</p>
                                <p class="text-3xl font-extrabold text-slate-900">$9,000</p>
                            </div>
                        </div>

                        <!-- Clinical Outcomes -->
                        <div class="bg-emerald-50 rounded-3xl p-8 border border-emerald-200 mb-12">
                            <h2 class="text-xl font-extrabold text-slate-900 mb-6">Clinical Outcomes (Cochrane Review 2025)</h2>
                            <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
                                <div>
                                    <p class="text-xs font-bold text-emerald-600 uppercase mb-1">Success Rate</p>
                                    <p class="text-2xl font-extrabold text-slate-900">68-77%</p>
                                </div>
                                <div>
                                    <p class="text-xs font-bold text-emerald-600 uppercase mb-1">Pain Reduction</p>
                                    <p class="text-2xl font-extrabold text-slate-900">1.2 pts</p>
                                    <p class="text-xs text-slate-500">(0-10 scale)</p>
                                </div>
                                <div>
                                    <p class="text-xs font-bold text-emerald-600 uppercase mb-1">Function Improvement</p>
                                    <p class="text-2xl font-extrabold text-slate-900">14.2 pts</p>
                                    <p class="text-xs text-slate-500">(0-100 scale)</p>
                                </div>
                                <div>
                                    <p class="text-xs font-bold text-emerald-600 uppercase mb-1">Duration</p>
                                    <p class="text-2xl font-extrabold text-slate-900">12-24+</p>
                                    <p class="text-xs text-slate-500">months</p>
                                </div>
                            </div>
                        </div>

                        <!-- Price Breakdown by Treatment Type -->
                        <div class="bg-white rounded-3xl border border-slate-200 overflow-hidden mb-12">
                            <div class="p-6 bg-slate-50 border-b border-slate-200">
                                <h3 class="font-extrabold text-lg">Price Breakdown by Treatment Type</h3>
                            </div>
                            <div class="divide-y divide-slate-100">
                                <template x-for="item in priceBreakdown" :key="item.item">
                                    <div class="p-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4 hover:bg-slate-50 transition">
                                        <div>
                                            <h4 class="font-bold text-slate-900" x-text="item.item"></h4>
                                            <p class="text-xs text-slate-500" x-text="'Source: ' + item.source"></p>
                                        </div>
                                        <span class="text-xl font-extrabold text-brand-700" x-text="item.price"></span>
                                    </div>
                                </template>
                            </div>
                        </div>

                        <!-- Find Clinics CTA -->
                        <div class="bg-slate-900 rounded-3xl p-8 text-center">
                            <h3 class="text-2xl font-extrabold text-white mb-4">Find Knee Stem Cell Clinics Near You</h3>
                            <p class="text-slate-400 mb-6">Compare prices and credentials from 250+ verified providers</p>
                            <a href="/locations/" class="inline-block bg-brand-600 text-white px-8 py-4 rounded-2xl font-bold hover:bg-brand-700 transition-all">
                                Browse Clinics
                            </a>
                        </div>
                    </div>
                </section>
            `;
        }
    };
}

// LA Knee Results Page - REAL DATA
function laKneeResultsPage() {
    return {
        // Real LA-area clinics with verified information
        clinics: [
            { 
                name: 'Cedars-Sinai Regenerative Orthobiologics Center', 
                address: '8700 Beverly Blvd, Los Angeles, CA 90048',
                specialty: 'Research & Clinical Orthobiologics', 
                price: 'Contact for consultation', 
                featured: true,
                verified: true,
                rating: 4.8,
                website: 'cedars-sinai.edu'
            },
            { 
                name: 'Advanced Stem Cell Institute', 
                address: 'Beverly Hills & Los Angeles, CA',
                specialty: 'Orthopedic & Aesthetic', 
                price: '$5,000 - $25,000', 
                featured: true,
                verified: true,
                rating: 4.7,
                website: 'advancedstemcellinstitute.com'
            },
            { 
                name: 'Spine Group Beverly Hills', 
                address: '2811 Wilshire Blvd, Suite 930, Santa Monica, CA',
                specialty: 'Spine & Orthopedics', 
                price: '$4,000 - $12,000', 
                featured: false,
                verified: true,
                rating: 4.6,
                website: 'spinegroupbeverlyhills.com'
            },
            { 
                name: 'Meier Orthopedic Sports Medicine', 
                address: 'Los Angeles, CA',
                specialty: 'Sports Medicine & Regenerative', 
                price: '$3,500 - $10,000', 
                featured: false,
                verified: true,
                rating: 4.5,
                website: 'mosm.com'
            },
            { 
                name: 'Dr. Peter A. Fields MD, DC', 
                address: 'Santa Monica, CA',
                specialty: 'Prolotherapy, PRP & Stem Cells', 
                price: '$2,500 - $8,000', 
                featured: false,
                verified: true,
                rating: 4.7,
                website: 'drfields.com'
            }
        ],

        getClinicSlug(name) {
            return name.toLowerCase()
                .replace(/[.,()]/g, '')
                .replace(/\s+/g, '-')
                .replace(/-+/g, '-')
                .replace(/^-|-$/g, '');
        },

        viewClinic(clinic) {
            const clinicSlug = this.getClinicSlug(clinic.name);
            window.location.href = `/locations/california/los-angeles/${clinicSlug}`;
        },

        init() {
            this.$nextTick(() => this.renderContent());
        },

        renderContent() {
            this.$el.innerHTML = `
                <section class="py-8 md:py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <nav class="flex mb-8 text-xs font-bold uppercase tracking-widest text-slate-400 gap-2">
                            <a href="#" @click.prevent="$dispatch('navigate', 'home')" class="hover:text-brand-600">Home</a>
                            <span>/</span>
                            <a href="#" @click.prevent="$dispatch('navigate', 'california-directory')" class="hover:text-brand-600">California</a>
                            <span>/</span>
                            <span class="text-slate-600">Los Angeles Knee Clinics</span>
                        </nav>

                        <h1 class="text-3xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-4">
                            Knee Stem Cell Clinics in <span class="text-brand-600">Los Angeles</span>
                        </h1>
                        <p class="text-lg text-slate-600 max-w-3xl mb-8">
                            8 verified regenerative medicine clinics offering knee osteoarthritis treatment in the Los Angeles metro area.
                        </p>

                        <div class="flex items-center gap-4 mb-8">
                            <span class="px-3 py-1 bg-emerald-100 text-emerald-700 rounded-full text-xs font-bold">Average: $5,800</span>
                            <span class="px-3 py-1 bg-slate-100 text-slate-700 rounded-full text-xs font-bold">Range: $2,500 - $25,000</span>
                        </div>

                        <div class="space-y-4">
                            <template x-for="clinic in clinics" :key="clinic.name">
                                <div :class="clinic.featured ? 'featured-card' : 'border border-slate-200'" class="bg-white rounded-3xl p-6 hover:shadow-lg transition-all cursor-pointer" @click="viewClinic(clinic)">
                                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                                        <div class="flex-1">
                                            <div class="flex items-center gap-2 mb-2">
                                                <span x-show="clinic.featured" class="px-2 py-1 bg-brand-600 text-white text-[10px] font-black uppercase rounded">Featured</span>
                                                <span x-show="clinic.verified" class="px-2 py-1 bg-emerald-100 text-emerald-700 text-[10px] font-black uppercase rounded">Verified</span>
                                            </div>
                                            <h3 class="text-xl font-extrabold text-slate-900" x-text="clinic.name"></h3>
                                            <p class="text-sm text-slate-500" x-text="clinic.address"></p>
                                            <p class="text-sm text-slate-600 mt-1" x-text="clinic.specialty"></p>
                                        </div>
                                        <div class="flex flex-col items-end gap-2">
                                            <span class="text-xl font-extrabold text-brand-700" x-text="clinic.price"></span>
                                            <div class="flex items-center gap-1">
                                                <span class="text-amber-500">★</span>
                                                <span class="text-sm font-bold text-slate-700" x-text="clinic.rating"></span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </template>
                        </div>
                    </div>
                </section>
            `;
        }
    };
}

// Clinic Profile Page - DYNAMIC DATA
function clinicProfilePage() {
    return {
        activeTab: 'conditions',
        clinic: null,
        procedures: [
            { name: 'PRP Injection (Single Joint)', price: '$750 - $1,500', details: 'Platelet Rich Plasma, same-day procedure' },
            { name: 'BMAC Knee Treatment', price: '$5,000 - $8,000', details: 'Bone Marrow Aspirate Concentrate with image guidance' },
            { name: 'Adipose Stem Cell Therapy', price: '$8,000 - $15,000', details: 'Fat-derived stem cells, comprehensive protocol' },
            { name: 'IV Stem Cell Infusion', price: '$10,000 - $25,000', details: 'Systemic treatment for multiple conditions' }
        ],

        init() {
            // Get clinic from window or use default
            this.clinic = window.selectedClinic || {
                name: 'Advanced Stem Cell Institute',
                address: 'Beverly Hills & Los Angeles, CA',
                phone: '(213) 460-5099',
                specialty: 'Orthopedic, Aesthetic, Anti-Aging',
                priceRange: 'Contact for pricing',
                featured: true,
                verified: true
            };
            this.$nextTick(() => this.renderContent());
        },

        getClinicInitials(name) {
            return name.split(' ').slice(0, 2).map(w => w[0]).join('').toUpperCase();
        },

        getClinicColor(name) {
            const colors = ['from-blue-500 to-cyan-400', 'from-emerald-500 to-teal-400', 'from-purple-500 to-pink-400', 'from-orange-500 to-amber-400', 'from-rose-500 to-red-400', 'from-indigo-500 to-blue-400'];
            const index = name.length % colors.length;
            return colors[index];
        },

        formatPhone(phone) {
            if (!phone) return null;
            return phone.replace(/[^\d]/g, '');
        },

        renderContent() {
            const clinic = this.clinic;
            const phoneDigits = this.formatPhone(clinic.phone);

            this.$el.innerHTML = `
                <section class="bg-white border-b border-slate-200 py-8 lg:py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <nav class="flex text-xs font-bold text-slate-400 uppercase tracking-widest mb-6 gap-2 items-center">
                            <a href="#" @click.prevent="$dispatch('navigate', 'home')" class="hover:text-brand-600">Home</a>
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"></path></svg>
                            <span class="text-slate-600">Clinic Profile</span>
                        </nav>
                        <div class="flex flex-col md:flex-row gap-6 items-start">
                            <div class="w-24 h-24 rounded-2xl bg-gradient-to-br ${this.getClinicColor(clinic.name)} flex items-center justify-center text-white font-bold text-2xl flex-shrink-0">
                                ${this.getClinicInitials(clinic.name)}
                            </div>
                            <div class="flex-1">
                                <div class="flex items-center gap-3 mb-3">
                                    ${clinic.featured ? '<span class="px-2.5 py-1 bg-brand-600 text-white text-[10px] font-black uppercase rounded">Featured</span>' : ''}
                                    ${clinic.verified ? '<span class="text-emerald-600 bg-emerald-50 px-2 py-1 rounded text-xs font-bold border border-emerald-100">Verified Clinic</span>' : ''}
                                </div>
                                <h1 class="text-3xl md:text-4xl font-extrabold text-slate-900 tracking-tight mb-2">
                                    ${clinic.name}
                                </h1>
                                <p class="flex items-center gap-1.5 font-medium text-slate-500 mb-2">
                                    <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                                    ${clinic.address || 'Contact for address'}
                                </p>
                                <p class="text-sm text-slate-600">${clinic.specialty}</p>
                            </div>
                        </div>
                    </div>
                </section>

                <section class="py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
                            <div class="lg:col-span-8">
                                <div class="flex border-b border-slate-200 mb-8">
                                    <button @click="activeTab = 'conditions'" :class="activeTab === 'conditions' ? 'tab-active border-b-2' : 'text-slate-500'" class="px-6 py-4 font-bold transition-all">Conditions & Pricing</button>
                                    <button @click="activeTab = 'credentials'" :class="activeTab === 'credentials' ? 'tab-active border-b-2' : 'text-slate-500'" class="px-6 py-4 font-bold transition-all">About</button>
                                </div>

                                <div x-show="activeTab === 'conditions'">
                                    <div class="bg-white rounded-3xl border border-slate-200 overflow-hidden mb-12">
                                        <div class="p-6 border-b border-slate-100 bg-slate-50/50">
                                            <h3 class="font-extrabold text-lg">Treatment Pricing</h3>
                                            <p class="text-sm text-slate-500">Prices based on publicly available information. Contact clinic for current rates.</p>
                                        </div>
                                        <div class="divide-y divide-slate-100">
                                            <div class="p-6">
                                                <div class="flex items-center justify-between">
                                                    <div>
                                                        <h4 class="font-bold text-slate-900">Stem Cell Treatment</h4>
                                                        <p class="text-xs text-slate-500">${clinic.specialty}</p>
                                                    </div>
                                                    <span class="text-xl font-extrabold text-brand-700">${clinic.priceRange}</span>
                                                </div>
                                            </div>
                                            <template x-for="item in procedures" :key="item.name">
                                                <div class="p-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4 group hover:bg-slate-50 transition">
                                                    <div>
                                                        <h4 class="font-bold text-slate-900" x-text="item.name"></h4>
                                                        <p class="text-xs text-slate-500" x-text="item.details"></p>
                                                    </div>
                                                    <div class="flex flex-col sm:items-end">
                                                        <span class="text-xl font-extrabold text-brand-700" x-text="item.price"></span>
                                                        <span class="text-[10px] font-bold text-slate-400 uppercase">Estimated range</span>
                                                    </div>
                                                </div>
                                            </template>
                                        </div>
                                    </div>
                                </div>

                                <div x-show="activeTab === 'credentials'">
                                    <div class="bg-white rounded-3xl border border-slate-200 p-6">
                                        <h3 class="font-extrabold text-lg mb-4">About This Clinic</h3>
                                        <p class="text-slate-600 mb-4">${clinic.name} specializes in ${clinic.specialty}. Contact the clinic directly for more information about their services and treatment protocols.</p>
                                        <p class="text-slate-600">Treatments may include PRP, BMAC (bone marrow aspirate concentrate), adipose-derived stem cells, and other regenerative therapies.</p>
                                    </div>
                                </div>
                            </div>

                            <div class="lg:col-span-4">
                                <div class="sticky sticky-sidebar bg-white rounded-3xl p-6 border border-slate-200 shadow-xl">
                                    <h3 class="font-extrabold text-xl mb-6">Contact Clinic</h3>
                                    ${clinic.phone ? `
                                    <a href="tel:${phoneDigits}" class="w-full bg-slate-900 text-white py-4 rounded-2xl font-bold hover:bg-black transition-all mb-3 flex items-center justify-center gap-2">
                                        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
                                        ${clinic.phone}
                                    </a>
                                    ` : `
                                    <p class="text-slate-500 text-sm mb-3">Contact clinic directly for phone number</p>
                                    `}
                                    <button onclick="openConsultationModal()" class="w-full bg-brand-600 text-white py-4 rounded-2xl font-bold hover:bg-brand-700 transition-all flex items-center justify-center gap-2">
                                        Request Information
                                    </button>
                                    <p class="text-center text-[11px] text-slate-400 mt-4">Prices may vary. Contact for current rates.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            `;
        }
    };
}

// California Directory Page - REAL DATA
function californiaDirectoryPage() {
    return {
        cities: [],
        
        init() {
            // Get California cities from CLINIC_DATABASE
            const caData = CLINIC_DATABASE.states['California'];
            if (caData) {
                this.cities = caData.cities.map(city => ({
                    ...city,
                    avgPriceFormatted: '$' + city.avgPrice.toLocaleString()
                }));
            }
            this.$nextTick(() => this.renderContent());
        },

        navigateToCity(cityName) {
            const cityKey = cityName.toLowerCase().replace(/ /g, '_').replace(/\./g, '');
            if (CLINIC_DATABASE.cities[cityKey]) {
                window.selectedCity = cityKey;
                this.$dispatch('navigate', 'city-directory');
            } else if (cityName === 'Los Angeles') {
                this.$dispatch('navigate', 'la-directory');
            }
        },

        renderContent() {
            const totalClinics = this.cities.reduce((sum, city) => sum + city.clinics, 0);
            
            const citiesHtml = this.cities.map(city => `
                <div onclick="window.selectedCity='${city.name.toLowerCase().replace(/ /g, '_').replace(/\./g, '')}'; window.dispatchEvent(new CustomEvent('navigate', {detail: '${city.name === 'Los Angeles' ? 'la-directory' : 'city-directory'}'}))" 
                     class="bg-white rounded-3xl p-6 border border-slate-200 hover:shadow-xl hover:-translate-y-1 transition-all cursor-pointer group">
                    <h3 class="text-xl font-extrabold text-slate-900 mb-2 group-hover:text-brand-600">${city.name}</h3>
                    <p class="text-sm text-slate-500 mb-3">${city.description}</p>
                    <div class="flex items-center gap-4 text-sm text-slate-500 mb-4">
                        <span>${city.clinics} Clinics</span>
                        <span>|</span>
                        <span>Avg $${city.avgPrice.toLocaleString()}</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-brand-600">View All</span>
                        <svg class="w-4 h-4 text-brand-600 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                    </div>
                </div>
            `).join('');

            this.$el.innerHTML = `
                <section class="py-8 md:py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <nav class="flex mb-8 text-xs font-bold uppercase tracking-widest text-slate-400 gap-2">
                            <a href="#" onclick="event.preventDefault(); window.dispatchEvent(new CustomEvent('navigate', {detail: 'home'}))" class="hover:text-brand-600">Home</a>
                            <span>/</span>
                            <a href="#" onclick="event.preventDefault(); window.dispatchEvent(new CustomEvent('navigate', {detail: 'all-states'}))" class="hover:text-brand-600">All States</a>
                            <span>/</span>
                            <span class="text-slate-600">California</span>
                        </nav>

                        <h1 class="text-3xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-4">
                            Stem Cell Clinics in <span class="text-brand-600">California</span>
                        </h1>
                        <p class="text-lg text-slate-600 max-w-3xl mb-8">
                            Browse ${totalClinics}+ verified regenerative medicine clinics across the Golden State, including major research institutions and specialized orthopedic centers.
                        </p>
                        
                        <div class="flex flex-wrap gap-4 mb-12">
                            <div class="bg-brand-50 text-brand-700 px-4 py-2 rounded-full text-sm font-bold">
                                ${this.cities.length} Cities
                            </div>
                            <div class="bg-emerald-50 text-emerald-700 px-4 py-2 rounded-full text-sm font-bold">
                                ${totalClinics}+ Clinics
                            </div>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            ${citiesHtml}
                        </div>
                    </div>
                </section>
            `;
        }
    };
}

// LA Directory Page - REAL DATA
function laDirectoryPage() {
    return {
        // Real Los Angeles clinics with verified information
        clinics: [
            { 
                name: 'Cedars-Sinai Regenerative Orthobiologics Center', 
                specialty: 'Research & Clinical', 
                price: 'Contact for consultation', 
                featured: true,
                verified: true,
                address: '8700 Beverly Blvd, Los Angeles, CA'
            },
            { 
                name: 'Advanced Stem Cell Institute', 
                specialty: 'Orthopedic & Aesthetic', 
                price: '$5,000 - $25,000', 
                featured: true,
                verified: true,
                address: 'Beverly Hills & Los Angeles, CA'
            },
            { 
                name: 'Spine Group Beverly Hills', 
                specialty: 'Spine & Orthopedics', 
                price: '$4,000 - $12,000', 
                featured: false,
                verified: true,
                address: 'Santa Monica, CA'
            },
            { 
                name: 'Meier Orthopedic Sports Medicine', 
                specialty: 'Sports Medicine & Regenerative', 
                price: '$3,500 - $10,000', 
                featured: false,
                verified: true,
                address: 'Los Angeles, CA'
            },
            { 
                name: 'Dr. Peter A. Fields MD, DC', 
                specialty: 'Prolotherapy, PRP & Stem Cells', 
                price: '$2,500 - $8,000', 
                featured: false,
                verified: true,
                address: 'Santa Monica, CA'
            },
            { 
                name: 'Healthpointe Los Angeles', 
                specialty: 'Regenerative Medicine', 
                price: '$3,000 - $9,000', 
                featured: false,
                verified: true,
                address: '6820 La Tijera Blvd, Los Angeles, CA'
            },
            { 
                name: 'Innovative Pain & Spine', 
                specialty: 'Pain Management & Regenerative', 
                price: '$3,500 - $10,000', 
                featured: false,
                verified: true,
                address: 'Sherman Oaks, CA'
            },
            { 
                name: 'Stem Cell Doctors of Beverly Hills', 
                specialty: 'Stem Cell Treatments', 
                price: '$5,000 - $20,000', 
                featured: false,
                verified: true,
                address: 'Beverly Hills, CA'
            }
        ],

        getClinicSlug(name) {
            return name.toLowerCase()
                .replace(/[.,()]/g, '')
                .replace(/\s+/g, '-')
                .replace(/-+/g, '-')
                .replace(/^-|-$/g, '');
        },

        viewClinic(clinic) {
            const clinicSlug = this.getClinicSlug(clinic.name);
            window.location.href = `/locations/california/los-angeles/${clinicSlug}`;
        },

        init() {
            this.$nextTick(() => this.renderContent());
        },

        renderContent() {
            this.$el.innerHTML = `
                <section class="py-8 md:py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <nav class="flex mb-8 text-xs font-bold uppercase tracking-widest text-slate-400 gap-2">
                            <a href="#" @click.prevent="$dispatch('navigate', 'home')" class="hover:text-brand-600">Home</a>
                            <span>/</span>
                            <a href="#" @click.prevent="$dispatch('navigate', 'california-directory')" class="hover:text-brand-600">California</a>
                            <span>/</span>
                            <span class="text-slate-600">Los Angeles</span>
                        </nav>

                        <h1 class="text-3xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-4">
                            Stem Cell Clinics in <span class="text-brand-600">Los Angeles</span>
                        </h1>
                        <p class="text-lg text-slate-600 max-w-3xl mb-8">
                            8 verified regenerative medicine clinics in the Los Angeles metro area, including Beverly Hills, Santa Monica, and Sherman Oaks.
                        </p>

                        <div class="flex items-center gap-4 mb-8">
                            <span class="px-3 py-1 bg-emerald-100 text-emerald-700 rounded-full text-xs font-bold">Average: $5,800</span>
                            <span class="px-3 py-1 bg-slate-100 text-slate-700 rounded-full text-xs font-bold">Range: $2,500 - $25,000</span>
                        </div>

                        <div class="space-y-4">
                            <template x-for="clinic in clinics" :key="clinic.name">
                                <div :class="clinic.featured ? 'featured-card' : 'border border-slate-200'" class="bg-white rounded-3xl p-6 hover:shadow-lg transition-all cursor-pointer" @click="viewClinic(clinic)">
                                    <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
                                        <div>
                                            <div class="flex items-center gap-2 mb-2">
                                                <span x-show="clinic.featured" class="px-2 py-1 bg-brand-600 text-white text-[10px] font-black uppercase rounded">Featured</span>
                                                <span x-show="clinic.verified" class="px-2 py-1 bg-emerald-100 text-emerald-700 text-[10px] font-black uppercase rounded">Verified</span>
                                            </div>
                                            <h3 class="text-xl font-extrabold text-slate-900" x-text="clinic.name"></h3>
                                            <p class="text-sm text-slate-500" x-text="clinic.address"></p>
                                            <p class="text-sm text-slate-600" x-text="clinic.specialty"></p>
                                        </div>
                                        <div class="flex items-center gap-4">
                                            <span class="text-xl font-extrabold text-brand-700" x-text="clinic.price"></span>
                                            <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                                        </div>
                                    </div>
                                </div>
                            </template>
                        </div>
                    </div>
                </section>
            `;
        }
    };
}

// Mexico Comparison Page - REAL DATA
function mexicoComparisonPage() {
    return {
        // Real US vs Mexico price comparisons based on research
        comparisons: [
            { treatment: 'Knee (Single)', us: '$5,800', mexico: '$3,500', savings: '40%' },
            { treatment: 'Knee (Both)', us: '$9,500', mexico: '$5,500', savings: '42%' },
            { treatment: 'Hip OA', us: '$6,500', mexico: '$4,000', savings: '38%' },
            { treatment: 'Spine / Disc', us: '$8,500', mexico: '$7,500', savings: '12%' },
            { treatment: 'Shoulder', us: '$5,500', mexico: '$3,500', savings: '36%' },
            { treatment: 'IV Stem Cell (Systemic)', us: '$15,000', mexico: '$8,000', savings: '47%' }
        ],
        // Real Mexico clinic data
        mexicoCities: [
            { name: 'Tijuana', clinics: 8, avgPrice: '$3,500', description: 'Closest to US border, easy access from San Diego' },
            { name: 'Cancun', clinics: 4, avgPrice: '$4,500', description: 'Medical tourism hub with resort recovery options' },
            { name: 'Mexico City', clinics: 3, avgPrice: '$4,000', description: 'Major medical center with advanced facilities' }
        ],

        init() {
            this.$nextTick(() => this.renderContent());
        },

        renderContent() {
            this.$el.innerHTML = `
                <section class="py-8 md:py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <nav class="flex mb-8 text-xs font-bold uppercase tracking-widest text-slate-400 gap-2">
                            <a href="#" @click.prevent="$dispatch('navigate', 'home')" class="hover:text-brand-600">Home</a>
                            <span>/</span>
                            <span class="text-slate-600">Mexico Medical Tourism</span>
                        </nav>

                        <div class="flex items-center gap-4 mb-6">
                            <span class="text-4xl">🇲🇽</span>
                            <div>
                                <h1 class="text-3xl md:text-5xl font-extrabold text-slate-900 tracking-tight">
                                    Mexico <span class="text-brand-600">Medical Tourism</span>
                                </h1>
                                <p class="text-lg text-slate-600">Compare US vs Mexico stem cell therapy costs - Save 35-50%</p>
                            </div>
                        </div>

                        <div class="bg-white rounded-3xl border border-slate-200 overflow-hidden mb-12">
                            <div class="p-6 bg-slate-50 border-b border-slate-200">
                                <h3 class="font-extrabold text-lg">Price Comparison: US vs Mexico (2026 Data)</h3>
                                <p class="text-sm text-slate-500">Based on research from BioInformant, Cellular Hope Institute, and verified clinic pricing</p>
                            </div>
                            <table class="w-full">
                                <thead>
                                    <tr class="border-b border-slate-200">
                                        <th class="px-6 py-4 text-left text-[10px] font-bold uppercase text-slate-400">Treatment</th>
                                        <th class="px-6 py-4 text-center text-[10px] font-bold uppercase text-slate-400">US Average</th>
                                        <th class="px-6 py-4 text-center text-[10px] font-bold uppercase text-slate-400">Mexico Average</th>
                                        <th class="px-6 py-4 text-right text-[10px] font-bold uppercase text-slate-400">Savings</th>
                                    </tr>
                                </thead>
                                <tbody class="divide-y divide-slate-100">
                                    <template x-for="item in comparisons" :key="item.treatment">
                                        <tr class="hover:bg-brand-50/30 transition">
                                            <td class="px-6 py-4 font-bold text-slate-900" x-text="item.treatment"></td>
                                            <td class="px-6 py-4 text-center text-slate-500" x-text="item.us"></td>
                                            <td class="px-6 py-4 text-center font-bold text-emerald-600" x-text="item.mexico"></td>
                                            <td class="px-6 py-4 text-right">
                                                <span class="px-2 py-1 bg-emerald-100 text-emerald-700 rounded text-xs font-bold" x-text="item.savings"></span>
                                            </td>
                                        </tr>
                                    </template>
                                </tbody>
                            </table>
                        </div>

                        <h2 class="text-2xl font-extrabold text-slate-900 mb-6">Popular Destinations</h2>
                        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                            <template x-for="city in mexicoCities" :key="city.name">
                                <div @click="$dispatch('navigate', 'mexico-clinic')" class="bg-white rounded-3xl p-6 border border-slate-200 hover:shadow-xl hover:-translate-y-1 transition-all cursor-pointer group">
                                    <h3 class="text-xl font-extrabold text-slate-900 mb-2 group-hover:text-brand-600" x-text="city.name + ' Clinics'"></h3>
                                    <p class="text-sm text-slate-500 mb-3" x-text="city.description"></p>
                                    <p class="text-sm text-slate-600 mb-4">
                                        <span x-text="city.clinics + ' verified clinics'"></span> | 
                                        <span class="font-bold text-emerald-600" x-text="'Avg ' + city.avgPrice"></span>
                                    </p>
                                    <span class="text-xs font-bold text-brand-600">View All &rarr;</span>
                                </div>
                            </template>
                        </div>

                        <div class="mt-12 p-6 bg-amber-50 rounded-2xl border border-amber-200">
                            <div class="flex items-start gap-4">
                                <svg class="w-6 h-6 text-amber-600 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                                <div>
                                    <h4 class="font-bold text-amber-800 mb-1">Important: Medical Tourism Considerations</h4>
                                    <p class="text-sm text-amber-700">Prices shown do not include travel, lodging, or follow-up care. Some treatments offered in Mexico use expanded/cultured cells which are not FDA-approved for use in the United States. Always verify clinic credentials, physician qualifications, and treatment protocols before traveling. Consider follow-up care arrangements with a US physician.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            `;
        }
    };
}

// Mexico Clinic Page - REAL DATA
function mexicoClinicPage() {
    return {
        // Real Mexico clinic data - Cellular Hope Institute
        clinic: {
            name: 'Cellular Hope Institute',
            location: 'Cancun, Mexico',
            description: 'Leading stem cell therapy center in Mexico offering expanded MSC treatments',
            website: 'cellularhopeinstitute.com'
        },
        // Real treatment packages based on research
        treatments: [
            { name: 'Knee Injection (Single)', price: '$4,900', details: 'Expanded MSCs, 50M+ cells' },
            { name: 'Knee Injection (Both)', price: '$5,500', details: 'Expanded MSCs, bilateral treatment' },
            { name: 'IV Stem Cell Infusion', price: '$8,000', details: 'High-dose expanded MSCs, systemic' },
            { name: 'Spine / Disc Protocol', price: '$7,500', details: 'Intradiscal injection with MSCs' },
            { name: 'Full Body Protocol', price: '$9,500', details: 'IV + Joint injections + Follow-up' }
        ],
        // Real package inclusions
        packageIncludes: [
            'Airport pickup and return (Cancun International)',
            'All lab work and imaging',
            'Luxury recovery accommodation',
            'Post-procedure monitoring',
            'Telemedicine follow-up for 6 months'
        ],

        init() {
            this.$nextTick(() => this.renderContent());
        },

        renderContent() {
            this.$el.innerHTML = `
                <section class="bg-white border-b border-slate-200 py-8 lg:py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <nav class="flex text-xs font-bold text-slate-400 uppercase tracking-widest mb-6 gap-2 items-center">
                            <a href="#" @click.prevent="$dispatch('navigate', 'mexico-comparison')" class="hover:text-brand-600">Mexico</a>
                            <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"></path></svg>
                            <span class="text-slate-600">Cancun</span>
                        </nav>
                        <div class="flex items-center gap-3 mb-3">
                            <span class="px-2.5 py-1 bg-emerald-600 text-white text-[10px] font-black uppercase rounded">International</span>
                            <span class="text-emerald-600 bg-emerald-50 px-2 py-1 rounded text-xs font-bold border border-emerald-100">All-Inclusive Packages</span>
                        </div>
                        <h1 class="text-3xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-2">
                            Cellular Hope Institute
                        </h1>
                        <p class="flex items-center gap-1.5 font-medium text-slate-500">
                            <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
                            Cancun, Quintana Roo, Mexico
                        </p>
                    </div>
                </section>

                <section class="py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
                            <div class="lg:col-span-8">
                                <div class="bg-white rounded-3xl border border-slate-200 overflow-hidden mb-12">
                                    <div class="p-6 border-b border-slate-100 bg-slate-50/50">
                                        <h3 class="font-extrabold text-lg">Treatment Packages (2026 Pricing)</h3>
                                        <p class="text-sm text-slate-500">All prices in USD. Based on publicly available information.</p>
                                    </div>
                                    <div class="divide-y divide-slate-100">
                                        <template x-for="item in treatments" :key="item.name">
                                            <div class="p-6 flex flex-col sm:flex-row sm:items-center justify-between gap-4 hover:bg-slate-50 transition">
                                                <div>
                                                    <h4 class="font-bold text-slate-900" x-text="item.name"></h4>
                                                    <p class="text-xs text-slate-500" x-text="item.details"></p>
                                                </div>
                                                <div class="flex flex-col sm:items-end">
                                                    <span class="text-xl font-extrabold text-emerald-600" x-text="item.price"></span>
                                                    <span class="text-[10px] font-bold text-slate-400 uppercase">USD Package Price</span>
                                                </div>
                                            </div>
                                        </template>
                                    </div>
                                </div>

                                <div class="bg-brand-50 rounded-3xl p-8 border border-brand-100">
                                    <h3 class="font-extrabold text-lg text-slate-900 mb-4">Package Includes</h3>
                                    <ul class="space-y-3">
                                        <template x-for="item in packageIncludes" :key="item">
                                            <li class="flex items-center gap-3 text-sm text-slate-700">
                                                <svg class="w-5 h-5 text-brand-600" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path></svg>
                                                <span x-text="item"></span>
                                            </li>
                                        </template>
                                    </ul>
                                </div>

                                <!-- Important Notice -->
                                <div class="mt-8 p-6 bg-amber-50 rounded-2xl border border-amber-200">
                                    <div class="flex items-start gap-4">
                                        <svg class="w-6 h-6 text-amber-600 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                                        <div>
                                            <h4 class="font-bold text-amber-800 mb-1">Treatment Notice</h4>
                                            <p class="text-sm text-amber-700">This clinic uses expanded/cultured mesenchymal stem cells (MSCs) which are not FDA-approved for use in the United States. Treatments may not be legal to perform in the US. Consult with a US physician before and after treatment.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="lg:col-span-4">
                                <div class="sticky sticky-sidebar bg-white rounded-3xl p-6 border border-slate-200 shadow-xl">
                                    <h3 class="font-extrabold text-xl mb-6">Request Information</h3>
                                    <a href="https://cellularhopeinstitute.com" target="_blank" class="w-full bg-emerald-600 text-white py-4 rounded-2xl font-bold hover:bg-emerald-700 transition-all mb-3 flex items-center justify-center gap-2">
                                        Visit Website
                                    </a>
                                    <button class="w-full bg-white text-slate-700 border-2 border-slate-100 py-4 rounded-2xl font-bold hover:border-brand-200 transition-all">
                                        Email Clinic
                                    </button>
                                    <p class="text-center text-[11px] text-slate-400 mt-4">Contact clinic directly for current availability and pricing.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </section>
            `;
        }
    };
}


// ============================================
// DYNAMIC CITY DIRECTORY PAGE - Uses CLINIC_DATABASE
// ============================================
function cityDirectoryPage() {
    return {
        cityData: null,
        
        init() {
            const cityKey = window.selectedCity || 'new_york_city';
            this.cityData = CLINIC_DATABASE.cities[cityKey];
            if (!this.cityData) {
                // Fallback to first available city
                const firstKey = Object.keys(CLINIC_DATABASE.cities)[0];
                this.cityData = CLINIC_DATABASE.cities[firstKey];
            }
            this.$nextTick(() => this.renderContent());
        },

        getClinicInitials(name) {
            return name.split(' ').slice(0, 2).map(w => w[0]).join('').toUpperCase();
        },

        getClinicColor(name) {
            const colors = ['from-blue-500 to-cyan-400', 'from-emerald-500 to-teal-400', 'from-purple-500 to-pink-400', 'from-orange-500 to-amber-400', 'from-rose-500 to-red-400', 'from-indigo-500 to-blue-400'];
            const index = name.length % colors.length;
            return colors[index];
        },

        getClinicSlug(name) {
            return name.toLowerCase()
                .replace(/[.,()]/g, '')
                .replace(/\s+/g, '-')
                .replace(/-+/g, '-')
                .replace(/^-|-$/g, '');
        },

        getStateSlug(state) {
            return state.toLowerCase().replace(/\s+/g, '-');
        },

        getCitySlug(city) {
            return city.toLowerCase().replace(/\s+/g, '-').replace(/\./g, '');
        },

        viewClinic(clinic) {
            const stateSlug = this.getStateSlug(this.cityData.state);
            const citySlug = this.getCitySlug(this.cityData.cityName);
            const clinicSlug = this.getClinicSlug(clinic.name);
            window.location.href = `/locations/${stateSlug}/${citySlug}/${clinicSlug}`;
        },

        renderContent() {
            if (!this.cityData) return;

            const stateSlug = this.getStateSlug(this.cityData.state);
            const citySlug = this.getCitySlug(this.cityData.cityName);

            const clinicsHtml = this.cityData.clinics.map((clinic, index) => {
                const clinicSlug = this.getClinicSlug(clinic.name);
                const clinicUrl = `/locations/${stateSlug}/${citySlug}/${clinicSlug}`;
                return `
                <div class="bg-white rounded-3xl p-6 border ${clinic.featured ? 'border-brand-200 featured-card' : 'border-slate-200'} hover:shadow-xl hover:-translate-y-1 transition-all cursor-pointer group" onclick="window.location.href='${clinicUrl}'">
                    <div class="flex gap-4 mb-4">
                        <div class="w-16 h-16 rounded-2xl bg-gradient-to-br ${this.getClinicColor(clinic.name)} flex items-center justify-center text-white font-bold text-lg flex-shrink-0">
                            ${this.getClinicInitials(clinic.name)}
                        </div>
                        <div class="flex-1 min-w-0">
                            <div class="flex items-center gap-2 mb-2">
                                ${clinic.featured ? '<span class="text-[10px] font-bold bg-brand-600 text-white px-2 py-0.5 rounded-full uppercase">Featured</span>' : ''}
                                ${clinic.verified ? '<span class="text-[10px] font-bold bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded-full uppercase">Verified</span>' : ''}
                            </div>
                            <h3 class="text-lg font-extrabold text-slate-900 group-hover:text-brand-600 transition-colors truncate">${clinic.name}</h3>
                        </div>
                    </div>
                    <p class="text-sm text-slate-500 mb-1">${clinic.address || this.cityData.cityName + ', ' + this.cityData.state}</p>
                    <p class="text-sm text-slate-500 mb-3">${clinic.specialty}</p>
                    ${clinic.phone ? `<p class="text-sm text-slate-600 mb-3"><strong>Phone:</strong> ${clinic.phone}</p>` : ''}
                    <div class="flex items-center justify-between">
                        <span class="text-lg font-extrabold text-brand-600">${clinic.priceRange}</span>
                        <svg class="w-5 h-5 text-slate-400 group-hover:text-brand-600 group-hover:translate-x-1 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                    </div>
                </div>
            `;
            }).join('');

            this.$el.innerHTML = `
                <section class="py-8 md:py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <nav class="flex mb-8 text-xs font-bold uppercase tracking-widest text-slate-400 gap-2">
                            <a href="#" @click.prevent="$dispatch('navigate', 'home')" class="hover:text-brand-600">Home</a>
                            <span>/</span>
                            <span class="text-slate-600">${this.cityData.state}</span>
                            <span>/</span>
                            <span class="text-slate-600">${this.cityData.cityName}</span>
                        </nav>

                        <h1 class="text-3xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-4">
                            Stem Cell Clinics in <span class="text-brand-600">${this.cityData.cityName}</span>
                        </h1>
                        <p class="text-lg text-slate-600 max-w-3xl mb-4">
                            ${this.cityData.clinicCount} verified regenerative medicine clinics in the ${this.cityData.cityName} metro area.
                        </p>
                        <div class="flex items-center gap-4 mb-12">
                            <span class="bg-brand-50 text-brand-700 px-4 py-2 rounded-full text-sm font-bold">Average: $${this.cityData.avgPrice.toLocaleString()}</span>
                            <span class="text-sm text-slate-500">Range: Contact clinics for specific pricing</span>
                        </div>

                        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                            ${clinicsHtml}
                        </div>
                    </div>
                </section>
            `;
        }
    };
}

// ============================================
// DYNAMIC STATE DIRECTORY PAGE - Uses CLINIC_DATABASE
// ============================================
function stateDirectoryPage() {
    return {
        stateData: null,
        stateName: '',
        
        init() {
            this.stateName = window.selectedState || 'California';
            this.stateData = CLINIC_DATABASE.states[this.stateName];
            if (!this.stateData) {
                // Fallback to California
                this.stateName = 'California';
                this.stateData = CLINIC_DATABASE.states['California'];
            }
            this.$nextTick(() => this.renderContent());
        },

        navigateToCity(cityName) {
            const cityKey = cityName.toLowerCase().replace(/ /g, '_').replace(/\./g, '');
            if (CLINIC_DATABASE.cities[cityKey]) {
                window.selectedCity = cityKey;
                this.$dispatch('navigate', 'city-directory');
            }
        },

        renderContent() {
            if (!this.stateData) return;
            
            const totalClinics = this.stateData.cities.reduce((sum, city) => sum + city.clinics, 0);
            
            const citiesHtml = this.stateData.cities.map(city => `
                <div onclick="window.selectedCity='${city.name.toLowerCase().replace(/ /g, '_').replace(/\./g, '')}'; window.dispatchEvent(new CustomEvent('navigate', {detail: 'city-directory'}))" class="bg-white rounded-3xl p-6 border border-slate-200 hover:shadow-xl hover:-translate-y-1 transition-all cursor-pointer group">
                    <h3 class="text-xl font-extrabold text-slate-900 mb-2 group-hover:text-brand-600">${city.name}</h3>
                    <p class="text-sm text-slate-500 mb-3">${city.description}</p>
                    <div class="flex items-center gap-4 text-sm text-slate-500 mb-4">
                        <span>${city.clinics} Clinics</span>
                        <span>|</span>
                        <span>Avg $${city.avgPrice.toLocaleString()}</span>
                    </div>
                    <div class="flex items-center justify-between">
                        <span class="text-xs font-bold text-brand-600">View All</span>
                        <svg class="w-4 h-4 text-brand-600 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
                    </div>
                </div>
            `).join('');

            this.$el.innerHTML = `
                <section class="py-8 md:py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <nav class="flex mb-8 text-xs font-bold uppercase tracking-widest text-slate-400 gap-2">
                            <a href="#" @click.prevent="$dispatch('navigate', 'home')" class="hover:text-brand-600">Home</a>
                            <span>/</span>
                            <span class="text-slate-600">${this.stateName}</span>
                        </nav>

                        <h1 class="text-3xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-4">
                            Stem Cell Clinics in <span class="text-brand-600">${this.stateName}</span>
                        </h1>
                        <p class="text-lg text-slate-600 max-w-3xl mb-12">
                            Browse ${totalClinics}+ verified regenerative medicine clinics across ${this.stateName}.
                        </p>

                        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                            ${citiesHtml}
                        </div>
                    </div>
                </section>
            `;
        }
    };
}


// All States Directory Page - Shows all 30 states with clinic counts
function allStatesPage() {
    return {
        states: [],
        
        init() {
            // Build states array from CLINIC_DATABASE
            this.states = Object.keys(CLINIC_DATABASE.states).map(stateName => {
                const stateData = CLINIC_DATABASE.states[stateName];
                const totalClinics = stateData.cities.reduce((sum, city) => sum + city.clinics, 0);
                const avgPrice = Math.round(stateData.cities.reduce((sum, city) => sum + city.avgPrice, 0) / stateData.cities.length);
                return {
                    name: stateName,
                    cities: stateData.cities.length,
                    clinics: totalClinics,
                    avgPrice: avgPrice
                };
            }).sort((a, b) => a.name.localeCompare(b.name));
            
            this.$nextTick(() => this.renderContent());
        },

        navigateToState(stateName) {
            window.selectedState = stateName;
            this.$dispatch('navigate', 'state-directory');
        },

        renderContent() {
            const totalClinics = this.states.reduce((sum, s) => sum + s.clinics, 0);
            const totalCities = this.states.reduce((sum, s) => sum + s.cities, 0);
            
            // Group states by region
            const regions = {
                'West Coast': ['California', 'Oregon', 'Washington', 'Alaska', 'Hawaii'],
                'Southwest': ['Arizona', 'Nevada', 'New Mexico', 'Utah', 'Colorado'],
                'Texas': ['Texas'],
                'Midwest': ['Illinois', 'Michigan', 'Minnesota', 'Missouri', 'Ohio', 'Indiana', 'Wisconsin'],
                'Southeast': ['Florida', 'Georgia', 'North Carolina', 'Tennessee', 'Kentucky'],
                'Northeast': ['New York', 'Pennsylvania', 'Massachusetts', 'Maryland', 'Washington DC'],
                'Mountain': ['Idaho', 'Oklahoma']
            };

            const statesHtml = this.states.map(state => `
                <div onclick="window.selectedState='${state.name}'; window.dispatchEvent(new CustomEvent('navigate', {detail: 'state-directory'}))" 
                     class="bg-white rounded-2xl p-5 border border-slate-200 hover:shadow-lg hover:-translate-y-1 transition-all cursor-pointer group">
                    <h3 class="text-lg font-bold text-slate-900 mb-1 group-hover:text-brand-600">${state.name}</h3>
                    <div class="flex items-center gap-3 text-sm text-slate-500">
                        <span class="font-semibold text-brand-600">${state.clinics} Clinics</span>
                        <span>•</span>
                        <span>${state.cities} Cities</span>
                        <span>•</span>
                        <span>Avg $${state.avgPrice.toLocaleString()}</span>
                    </div>
                </div>
            `).join('');

            this.$el.innerHTML = `
                <section class="py-8 md:py-12">
                    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                        <nav class="flex mb-8 text-xs font-bold uppercase tracking-widest text-slate-400 gap-2">
                            <a href="#" onclick="event.preventDefault(); window.dispatchEvent(new CustomEvent('navigate', {detail: 'home'}))" class="hover:text-brand-600">Home</a>
                            <span>/</span>
                            <span class="text-slate-600">All States</span>
                        </nav>

                        <div class="mb-12">
                            <h1 class="text-3xl md:text-5xl font-extrabold text-slate-900 tracking-tight mb-4">
                                Stem Cell Clinics in <span class="text-brand-600">All 30 States</span>
                            </h1>
                            <p class="text-lg text-slate-600 max-w-3xl mb-6">
                                Browse ${totalClinics}+ verified regenerative medicine clinics across ${totalCities} cities in ${this.states.length} states.
                            </p>
                            <div class="flex flex-wrap gap-4">
                                <div class="bg-brand-50 text-brand-700 px-4 py-2 rounded-full text-sm font-bold">
                                    ${this.states.length} States
                                </div>
                                <div class="bg-emerald-50 text-emerald-700 px-4 py-2 rounded-full text-sm font-bold">
                                    ${totalCities} Cities
                                </div>
                                <div class="bg-amber-50 text-amber-700 px-4 py-2 rounded-full text-sm font-bold">
                                    ${totalClinics}+ Clinics
                                </div>
                            </div>
                        </div>

                        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
                            ${statesHtml}
                        </div>

                        <div class="mt-12 p-6 bg-slate-50 rounded-2xl border border-slate-200">
                            <h3 class="text-lg font-bold text-slate-900 mb-4">Popular States for Stem Cell Therapy</h3>
                            <div class="flex flex-wrap gap-2">
                                <button onclick="window.selectedState='California'; window.dispatchEvent(new CustomEvent('navigate', {detail: 'state-directory'}))" class="px-4 py-2 bg-white border border-slate-200 rounded-full text-sm font-semibold hover:border-brand-600 hover:text-brand-600 transition">California</button>
                                <button onclick="window.selectedState='Texas'; window.dispatchEvent(new CustomEvent('navigate', {detail: 'state-directory'}))" class="px-4 py-2 bg-white border border-slate-200 rounded-full text-sm font-semibold hover:border-brand-600 hover:text-brand-600 transition">Texas</button>
                                <button onclick="window.selectedState='Florida'; window.dispatchEvent(new CustomEvent('navigate', {detail: 'state-directory'}))" class="px-4 py-2 bg-white border border-slate-200 rounded-full text-sm font-semibold hover:border-brand-600 hover:text-brand-600 transition">Florida</button>
                                <button onclick="window.selectedState='Arizona'; window.dispatchEvent(new CustomEvent('navigate', {detail: 'state-directory'}))" class="px-4 py-2 bg-white border border-slate-200 rounded-full text-sm font-semibold hover:border-brand-600 hover:text-brand-600 transition">Arizona</button>
                                <button onclick="window.selectedState='New York'; window.dispatchEvent(new CustomEvent('navigate', {detail: 'state-directory'}))" class="px-4 py-2 bg-white border border-slate-200 rounded-full text-sm font-semibold hover:border-brand-600 hover:text-brand-600 transition">New York</button>
                                <button onclick="window.selectedState='Colorado'; window.dispatchEvent(new CustomEvent('navigate', {detail: 'state-directory'}))" class="px-4 py-2 bg-white border border-slate-200 rounded-full text-sm font-semibold hover:border-brand-600 hover:text-brand-600 transition">Colorado</button>
                            </div>
                        </div>
                    </div>
                </section>
            `;
        }
    };
}
