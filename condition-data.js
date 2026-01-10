/**
 * Condition Data for Cost Guide Pages
 * All clinical data and pricing for stem cell treatments by condition
 */

const CONDITIONS = {
  'knee': {
    name: 'Knee Osteoarthritis',
    shortName: 'Knee',
    slug: 'knee-cost-guide',
    description: 'Comprehensive pricing and outcomes data for stem cell treatment of knee osteoarthritis, based on Cochrane Review 2025, Mayo Clinic research, and data from 250+ US clinics.',

    // Price ranges (in USD)
    priceRange: {
      low: 3500,
      median: 5800,
      high: 9000
    },

    // Clinical outcomes
    outcomes: {
      successRate: '68-77%',
      painReduction: '1.2 pts',
      painScale: '0-10 scale',
      functionImprovement: '14.2 pts',
      functionScale: '0-100 scale',
      duration: '12-24+',
      durationUnit: 'months',
      source: 'Cochrane Review 2025, Mayo Clinic'
    },

    // Treatment types with pricing
    treatments: [
      { name: 'PRP Injection (Single)', priceRange: '$500 - $2,000', source: 'Mayo Clinic, Sports Surgery Chicago' },
      { name: 'PRP Series (3 Injections)', priceRange: '$1,500 - $4,000', source: 'Sports Surgery Chicago' },
      { name: 'BMAC (Bone Marrow Aspirate)', priceRange: '$2,600 - $7,000', source: 'AZCPM, TSAOG, QCORA' },
      { name: 'Adipose-Derived Stem Cells', priceRange: '$5,000 - $15,000', source: 'Cell Surgical Network' },
      { name: 'Umbilical Cord Stem Cells', priceRange: '$8,000 - $25,000', source: 'Stem Cell Miami' }
    ],

    // FAQ content
    faqs: [
      {
        question: 'How much does knee stem cell therapy cost?',
        answer: 'Knee stem cell therapy typically costs between $3,500 and $9,000, with the national median at $5,800. Prices vary based on treatment type: PRP injections start around $500, while umbilical cord stem cells can reach $25,000.'
      },
      {
        question: 'What is the success rate of stem cell therapy for knee osteoarthritis?',
        answer: 'According to the Cochrane Review 2025, stem cell therapy for knee osteoarthritis has a 68-77% success rate, with patients experiencing an average pain reduction of 1.2 points on a 0-10 scale and function improvement of 14.2 points.'
      },
      {
        question: 'Is stem cell therapy for knees covered by insurance?',
        answer: 'Most stem cell therapies for knee osteoarthritis are not covered by insurance as they are considered experimental. However, some clinics offer financing options, and PRP treatments may have partial coverage in some cases.'
      }
    ]
  },

  'spine': {
    name: 'Lumbar Spine / Disc',
    shortName: 'Back & Spine',
    slug: 'spine-cost-guide',
    description: 'Comprehensive pricing and outcomes data for stem cell treatment of lumbar disc degeneration and lower back pain, based on clinical studies and data from 200+ US spine centers.',

    priceRange: {
      low: 4000,
      median: 7500,
      high: 15000
    },

    outcomes: {
      successRate: '55-70%',
      painReduction: '2.1 pts',
      painScale: '0-10 scale',
      functionImprovement: '18.5 pts',
      functionScale: 'ODI scale',
      duration: '12-18',
      durationUnit: 'months',
      source: 'NIH Regenerative Medicine Database, Clinical Pain Studies 2024'
    },

    treatments: [
      { name: 'Epidural PRP Injection', priceRange: '$800 - $2,500', source: 'Pain Management Centers' },
      { name: 'Intradiscal PRP', priceRange: '$2,000 - $5,000', source: 'Spine Specialists Network' },
      { name: 'BMAC Disc Injection', priceRange: '$4,000 - $10,000', source: 'Regenerative Spine Institute' },
      { name: 'Adipose SVF (Disc)', priceRange: '$6,000 - $15,000', source: 'Cell Surgical Network' },
      { name: 'Umbilical Cord MSC (Spine)', priceRange: '$10,000 - $30,000', source: 'Advanced Spine Centers' }
    ],

    faqs: [
      {
        question: 'How much does stem cell therapy for back pain cost?',
        answer: 'Stem cell therapy for lumbar disc and lower back conditions typically costs between $4,000 and $15,000, with the national median at $7,500. Intradiscal treatments are generally more expensive than epidural approaches.'
      },
      {
        question: 'What is the success rate of stem cell therapy for disc degeneration?',
        answer: 'Clinical studies show a 55-70% success rate for stem cell treatments targeting lumbar disc degeneration, with patients reporting an average pain reduction of 2.1 points and improved function scores of 18.5 points on the ODI scale.'
      },
      {
        question: 'How long do results last for spine stem cell treatment?',
        answer: 'Results from lumbar spine stem cell treatments typically last 12-18 months. Some patients experience longer-lasting benefits, especially when combined with physical therapy and lifestyle modifications.'
      }
    ]
  },

  'shoulder': {
    name: 'Shoulder (Rotator Cuff)',
    shortName: 'Shoulder',
    slug: 'shoulder-cost-guide',
    description: 'Comprehensive pricing and outcomes data for stem cell treatment of rotator cuff injuries and shoulder conditions, based on orthopedic research and data from 180+ US sports medicine clinics.',

    priceRange: {
      low: 3000,
      median: 5500,
      high: 12000
    },

    outcomes: {
      successRate: '65-78%',
      painReduction: '2.8 pts',
      painScale: '0-10 scale',
      functionImprovement: '22.4 pts',
      functionScale: 'ASES score',
      duration: '12-24',
      durationUnit: 'months',
      source: 'Journal of Shoulder and Elbow Surgery 2024, Sports Medicine Research'
    },

    treatments: [
      { name: 'PRP Injection (Shoulder)', priceRange: '$500 - $2,000', source: 'Sports Medicine Clinics' },
      { name: 'PRP Series (Rotator Cuff)', priceRange: '$1,500 - $4,500', source: 'Orthopedic Sports Institute' },
      { name: 'BMAC (Shoulder)', priceRange: '$3,000 - $8,000', source: 'Regenerative Orthopedics Network' },
      { name: 'Adipose-Derived (Shoulder)', priceRange: '$5,000 - $12,000', source: 'Cell Surgical Network' },
      { name: 'Umbilical Cord Stem Cells', priceRange: '$8,000 - $20,000', source: 'Advanced Orthopedic Centers' }
    ],

    faqs: [
      {
        question: 'How much does stem cell therapy for rotator cuff injuries cost?',
        answer: 'Rotator cuff stem cell therapy typically costs between $3,000 and $12,000, with the national median at $5,500. PRP treatments for partial tears start around $500, while comprehensive stem cell protocols can reach $20,000.'
      },
      {
        question: 'Can stem cells heal a torn rotator cuff?',
        answer: 'Stem cell therapy shows a 65-78% success rate for rotator cuff injuries, with best results for partial tears. Complete tears may still require surgical repair, but stem cells can enhance post-surgical healing.'
      },
      {
        question: 'Is stem cell therapy better than shoulder surgery?',
        answer: 'For partial rotator cuff tears, stem cell therapy offers a non-surgical alternative with significant pain reduction (2.8 pts) and function improvement (22.4 pts). However, complete tears often require surgical intervention.'
      }
    ]
  },

  'hip': {
    name: 'Hip Osteoarthritis',
    shortName: 'Hip',
    slug: 'hip-cost-guide',
    description: 'Comprehensive pricing and outcomes data for stem cell treatment of hip osteoarthritis, based on orthopedic research and data from 150+ US regenerative medicine clinics.',

    priceRange: {
      low: 4000,
      median: 6500,
      high: 14000
    },

    outcomes: {
      successRate: '60-72%',
      painReduction: '1.8 pts',
      painScale: '0-10 scale',
      functionImprovement: '16.8 pts',
      functionScale: 'HOOS score',
      duration: '12-18',
      durationUnit: 'months',
      source: 'Arthritis Care & Research 2024, Hip Preservation Society'
    },

    treatments: [
      { name: 'PRP Injection (Hip)', priceRange: '$600 - $2,200', source: 'Hip Preservation Clinics' },
      { name: 'PRP Series (Hip)', priceRange: '$1,800 - $5,000', source: 'Sports Medicine Network' },
      { name: 'BMAC (Hip Joint)', priceRange: '$4,000 - $9,000', source: 'Regenerative Joint Institute' },
      { name: 'Adipose-Derived (Hip)', priceRange: '$6,000 - $14,000', source: 'Cell Surgical Network' },
      { name: 'Umbilical Cord MSC (Hip)', priceRange: '$10,000 - $25,000', source: 'Advanced Hip Centers' }
    ],

    faqs: [
      {
        question: 'How much does stem cell therapy for hip arthritis cost?',
        answer: 'Hip osteoarthritis stem cell therapy typically costs between $4,000 and $14,000, with the national median at $6,500. Costs vary based on the severity of degeneration and treatment protocol used.'
      },
      {
        question: 'Can stem cells delay or prevent hip replacement?',
        answer: 'For patients with mild to moderate hip osteoarthritis, stem cell therapy shows a 60-72% success rate in reducing pain and improving function, potentially delaying the need for hip replacement by several years.'
      },
      {
        question: 'What is the recovery time for hip stem cell injections?',
        answer: 'Most patients can resume normal activities within 1-2 weeks after hip stem cell injections. Full benefits typically develop over 6-12 weeks as the regenerative process progresses.'
      }
    ]
  },

  'neck': {
    name: 'Cervical Spine (Neck)',
    shortName: 'Neck',
    slug: 'neck-cost-guide',
    description: 'Comprehensive pricing and outcomes data for stem cell treatment of cervical disc degeneration and neck pain, based on spine research and data from 120+ US pain management centers.',

    priceRange: {
      low: 4500,
      median: 8000,
      high: 18000
    },

    outcomes: {
      successRate: '58-68%',
      painReduction: '2.3 pts',
      painScale: '0-10 scale',
      functionImprovement: '15.2 pts',
      functionScale: 'NDI score',
      duration: '10-16',
      durationUnit: 'months',
      source: 'Spine Journal 2024, Cervical Spine Research Society'
    },

    treatments: [
      { name: 'Cervical Epidural PRP', priceRange: '$1,000 - $3,000', source: 'Pain Management Specialists' },
      { name: 'Cervical Facet PRP', priceRange: '$1,500 - $4,000', source: 'Spine Care Network' },
      { name: 'BMAC (Cervical Disc)', priceRange: '$5,000 - $12,000', source: 'Advanced Spine Institute' },
      { name: 'Adipose SVF (Cervical)', priceRange: '$7,000 - $16,000', source: 'Cell Surgical Network' },
      { name: 'Umbilical Cord MSC (Neck)', priceRange: '$12,000 - $35,000', source: 'Cervical Regenerative Centers' }
    ],

    faqs: [
      {
        question: 'How much does stem cell therapy for neck pain cost?',
        answer: 'Cervical spine stem cell therapy typically costs between $4,500 and $18,000, with the national median at $8,000. Neck treatments often cost more than lumbar procedures due to the precision required.'
      },
      {
        question: 'Is stem cell therapy effective for cervical disc degeneration?',
        answer: 'Clinical studies show a 58-68% success rate for cervical disc stem cell treatments, with patients experiencing an average pain reduction of 2.3 points and improved neck function scores of 15.2 points.'
      },
      {
        question: 'What are the risks of cervical stem cell injections?',
        answer: 'When performed by experienced specialists, cervical stem cell injections have a low complication rate. Common side effects include temporary soreness and swelling. Serious complications are rare but require proper imaging guidance.'
      }
    ]
  },

  'si-joint': {
    name: 'Sacroiliac (SI) Joint',
    shortName: 'SI Joint',
    slug: 'si-joint-cost-guide',
    description: 'Comprehensive pricing and outcomes data for stem cell treatment of sacroiliac joint dysfunction, based on pain medicine research and data from 100+ US interventional pain clinics.',

    priceRange: {
      low: 3500,
      median: 6000,
      high: 12000
    },

    outcomes: {
      successRate: '62-75%',
      painReduction: '2.5 pts',
      painScale: '0-10 scale',
      functionImprovement: '19.3 pts',
      functionScale: 'ODI score',
      duration: '12-20',
      durationUnit: 'months',
      source: 'Pain Medicine Journal 2024, SI Joint Research Consortium'
    },

    treatments: [
      { name: 'SI Joint PRP Injection', priceRange: '$700 - $2,000', source: 'Interventional Pain Clinics' },
      { name: 'SI Joint PRP Series', priceRange: '$1,800 - $4,500', source: 'Pain Management Network' },
      { name: 'BMAC (SI Joint)', priceRange: '$3,500 - $8,000', source: 'Regenerative Pain Institute' },
      { name: 'Adipose-Derived (SI)', priceRange: '$5,000 - $12,000', source: 'Cell Surgical Network' },
      { name: 'Umbilical Cord MSC (SI)', priceRange: '$8,000 - $22,000', source: 'Advanced Pain Centers' }
    ],

    faqs: [
      {
        question: 'How much does stem cell therapy for SI joint pain cost?',
        answer: 'SI joint stem cell therapy typically costs between $3,500 and $12,000, with the national median at $6,000. Treatment costs depend on whether single or bilateral injections are needed.'
      },
      {
        question: 'Can stem cells help SI joint dysfunction?',
        answer: 'Stem cell therapy shows a 62-75% success rate for SI joint dysfunction, with patients experiencing significant pain reduction (2.5 pts) and improved mobility scores (19.3 pts on ODI).'
      },
      {
        question: 'How does SI joint stem cell therapy compare to fusion surgery?',
        answer: 'Stem cell therapy offers a less invasive alternative to SI joint fusion, with faster recovery and lower complication rates. However, severe instability cases may still require surgical intervention.'
      }
    ]
  }
};

// City-specific pricing data (used for local market prices)
const CITY_PRICES = {
  'los-angeles': { name: 'Los Angeles', state: 'California', stateSlug: 'california', priceModifier: 1.15 },
  'san-diego': { name: 'San Diego', state: 'California', stateSlug: 'california', priceModifier: 1.10 },
  'san-francisco': { name: 'San Francisco', state: 'California', stateSlug: 'california', priceModifier: 1.20 },
  'houston': { name: 'Houston', state: 'Texas', stateSlug: 'texas', priceModifier: 0.95 },
  'dallas': { name: 'Dallas', state: 'Texas', stateSlug: 'texas', priceModifier: 0.98 },
  'austin': { name: 'Austin', state: 'Texas', stateSlug: 'texas', priceModifier: 1.02 },
  'miami': { name: 'Miami', state: 'Florida', stateSlug: 'florida', priceModifier: 1.12 },
  'phoenix': { name: 'Phoenix', state: 'Arizona', stateSlug: 'arizona', priceModifier: 0.92 },
  'denver': { name: 'Denver', state: 'Colorado', stateSlug: 'colorado', priceModifier: 1.00 },
  'chicago': { name: 'Chicago', state: 'Illinois', stateSlug: 'illinois', priceModifier: 1.05 },
  'new-york-city': { name: 'New York City', state: 'New York', stateSlug: 'new-york', priceModifier: 1.25 },
  'atlanta': { name: 'Atlanta', state: 'Georgia', stateSlug: 'georgia', priceModifier: 0.98 },
  'seattle': { name: 'Seattle', state: 'Washington', stateSlug: 'washington', priceModifier: 1.08 },
  'boston': { name: 'Boston', state: 'Massachusetts', stateSlug: 'massachusetts', priceModifier: 1.18 },
  'las-vegas': { name: 'Las Vegas', state: 'Nevada', stateSlug: 'nevada', priceModifier: 0.95 },
  'san-antonio': { name: 'San Antonio', state: 'Texas', stateSlug: 'texas', priceModifier: 0.90 },
  'philadelphia': { name: 'Philadelphia', state: 'Pennsylvania', stateSlug: 'pennsylvania', priceModifier: 1.08 },
  'tampa': { name: 'Tampa', state: 'Florida', stateSlug: 'florida', priceModifier: 1.00 },
  'orlando': { name: 'Orlando', state: 'Florida', stateSlug: 'florida', priceModifier: 0.98 },
  'nashville': { name: 'Nashville', state: 'Tennessee', stateSlug: 'tennessee', priceModifier: 0.95 },
  'charlotte': { name: 'Charlotte', state: 'North Carolina', stateSlug: 'north-carolina', priceModifier: 0.96 },
  'raleigh': { name: 'Raleigh', state: 'North Carolina', stateSlug: 'north-carolina', priceModifier: 0.98 },
  'minneapolis': { name: 'Minneapolis', state: 'Minnesota', stateSlug: 'minnesota', priceModifier: 1.02 },
  'detroit': { name: 'Detroit', state: 'Michigan', stateSlug: 'michigan', priceModifier: 0.92 },
  'portland': { name: 'Portland', state: 'Oregon', stateSlug: 'oregon', priceModifier: 1.05 },
  'sacramento': { name: 'Sacramento', state: 'California', stateSlug: 'california', priceModifier: 1.08 },
  'scottsdale': { name: 'Scottsdale', state: 'Arizona', stateSlug: 'arizona', priceModifier: 1.05 },
  'san-jose': { name: 'San Jose', state: 'California', stateSlug: 'california', priceModifier: 1.18 },
  'jacksonville': { name: 'Jacksonville', state: 'Florida', stateSlug: 'florida', priceModifier: 0.94 },
  'kansas-city': { name: 'Kansas City', state: 'Missouri', stateSlug: 'missouri', priceModifier: 0.90 }
};

// Helper function to get adjusted prices for a city
function getCityPrices(conditionSlug, citySlug) {
  const condition = CONDITIONS[conditionSlug];
  const city = CITY_PRICES[citySlug];

  if (!condition || !city) return null;

  const modifier = city.priceModifier;

  return {
    condition: condition,
    city: city,
    prices: {
      low: Math.round(condition.priceRange.low * modifier / 100) * 100,
      median: Math.round(condition.priceRange.median * modifier / 100) * 100,
      high: Math.round(condition.priceRange.high * modifier / 100) * 100
    }
  };
}

// Helper to format price as currency
function formatPrice(amount) {
  return '$' + amount.toLocaleString('en-US');
}

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { CONDITIONS, CITY_PRICES, getCityPrices, formatPrice };
}
