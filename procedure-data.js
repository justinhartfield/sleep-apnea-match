// SleepApneaMatch.com - Procedure Data
// Data researched January 2026 - Comprehensive procedure database

const PROCEDURE_DATA = {
    uppp: {
        id: 'uppp',
        name: 'UPPP (Uvulopalatopharyngoplasty)',
        shortName: 'UPPP',
        slug: 'uppp',
        description: 'Surgical removal and repositioning of excess tissue in the throat including the uvula, soft palate, and tonsils to widen the airway.',
        category: 'Soft Palate Surgery',
        priceRange: {
            low: 5000,
            median: 10000,
            high: 15000,
            currency: 'USD'
        },
        outcomes: {
            successRate: { min: 40, max: 60, unit: '%' },
            cureRate: { min: 15, max: 25, unit: '%' },
            ahiReduction: { min: 30, max: 50, unit: '%' }
        },
        recovery: {
            time: '2-4 weeks',
            hospitalStay: '1 day or outpatient',
            workReturn: '1-2 weeks'
        },
        anesthesia: 'General',
        insuranceCovered: true,
        cptCodes: ['42145'],
        bestFor: 'Patients with palate-level obstruction who have failed CPAP',
        considerations: 'One of the most common sleep apnea surgeries. Success rates vary based on patient anatomy.',
        keywords: ['UPPP', 'uvulopalatopharyngoplasty', 'palate surgery', 'throat surgery', 'sleep apnea surgery']
    },

    inspire: {
        id: 'inspire',
        name: 'Inspire (Hypoglossal Nerve Stimulation)',
        shortName: 'Inspire',
        slug: 'inspire',
        description: 'FDA-approved implantable device that stimulates the hypoglossal nerve to keep the airway open during sleep by moving the tongue forward.',
        category: 'Neuromodulation',
        priceRange: {
            low: 30000,
            median: 45000,
            high: 65000,
            currency: 'USD'
        },
        outcomes: {
            successRate: { min: 66, max: 75, unit: '%' },
            cureRate: { min: 20, max: 30, unit: '%' },
            ahiReduction: { min: 60, max: 70, unit: '%' }
        },
        recovery: {
            time: '1-2 weeks',
            hospitalStay: 'Outpatient or 1 day',
            workReturn: '1 week'
        },
        anesthesia: 'General',
        insuranceCovered: true,
        cptCodes: ['64568'],
        bestFor: 'Moderate to severe OSA, BMI < 35, CPAP intolerant, age 18+',
        considerations: 'Requires drug-induced sleep endoscopy (DISE) evaluation. Device requires periodic battery replacement.',
        keywords: ['Inspire', 'hypoglossal nerve stimulation', 'HNS', 'nerve stimulator', 'sleep apnea implant']
    },

    mma: {
        id: 'mma',
        name: 'MMA (Maxillomandibular Advancement)',
        shortName: 'MMA Surgery',
        slug: 'mma',
        description: 'Major surgical procedure that advances both the upper jaw (maxilla) and lower jaw (mandible) to enlarge the airway.',
        category: 'Skeletal Surgery',
        priceRange: {
            low: 40000,
            median: 65000,
            high: 100000,
            currency: 'USD'
        },
        outcomes: {
            successRate: { min: 85, max: 95, unit: '%' },
            cureRate: { min: 40, max: 50, unit: '%' },
            ahiReduction: { min: 80, max: 90, unit: '%' }
        },
        recovery: {
            time: '4-6 weeks',
            hospitalStay: '1-2 days',
            workReturn: '2-4 weeks'
        },
        anesthesia: 'General',
        insuranceCovered: true,
        cptCodes: ['21141', '21196'],
        bestFor: 'Severe OSA, patients with skeletal deficiency, failed other surgeries',
        considerations: 'Most effective surgical option but most invasive. May alter facial appearance. Requires oral and maxillofacial surgeon.',
        keywords: ['MMA', 'maxillomandibular advancement', 'jaw surgery', 'orthognathic surgery', 'skeletal surgery']
    },

    septoplasty: {
        id: 'septoplasty',
        name: 'Septoplasty',
        shortName: 'Septoplasty',
        slug: 'septoplasty',
        description: 'Surgical correction of a deviated nasal septum to improve nasal airflow and reduce obstruction.',
        category: 'Nasal Surgery',
        priceRange: {
            low: 3000,
            median: 6000,
            high: 10000,
            currency: 'USD'
        },
        outcomes: {
            successRate: { min: 70, max: 90, unit: '%' },
            cureRate: { min: 5, max: 15, unit: '%' },
            ahiReduction: { min: 10, max: 25, unit: '%' }
        },
        recovery: {
            time: '1-2 weeks',
            hospitalStay: 'Outpatient',
            workReturn: '1 week'
        },
        anesthesia: 'General or local',
        insuranceCovered: true,
        cptCodes: ['30520'],
        bestFor: 'Patients with nasal obstruction due to deviated septum',
        considerations: 'Often combined with other procedures. May improve CPAP tolerance but rarely cures OSA alone.',
        keywords: ['septoplasty', 'deviated septum', 'nasal surgery', 'nasal obstruction']
    },

    'turbinate-reduction': {
        id: 'turbinate-reduction',
        name: 'Turbinate Reduction',
        shortName: 'Turbinate Reduction',
        slug: 'turbinate-reduction',
        description: 'Surgical reduction of the inferior turbinates to improve nasal airflow.',
        category: 'Nasal Surgery',
        priceRange: {
            low: 2000,
            median: 3500,
            high: 5000,
            currency: 'USD'
        },
        outcomes: {
            successRate: { min: 70, max: 85, unit: '%' },
            cureRate: { min: 5, max: 10, unit: '%' },
            ahiReduction: { min: 5, max: 15, unit: '%' }
        },
        recovery: {
            time: '1 week',
            hospitalStay: 'Outpatient',
            workReturn: '2-3 days'
        },
        anesthesia: 'Local or general',
        insuranceCovered: true,
        cptCodes: ['30140'],
        bestFor: 'Chronic nasal congestion, turbinate hypertrophy',
        considerations: 'Minimally invasive. Often performed with septoplasty. May improve CPAP compliance.',
        keywords: ['turbinate reduction', 'turbinectomy', 'nasal surgery', 'nasal congestion']
    },

    tonsillectomy: {
        id: 'tonsillectomy',
        name: 'Tonsillectomy',
        shortName: 'Tonsillectomy',
        slug: 'tonsillectomy',
        description: 'Surgical removal of the tonsils, often combined with adenoidectomy for sleep apnea treatment.',
        category: 'Soft Palate Surgery',
        priceRange: {
            low: 3000,
            median: 5000,
            high: 8000,
            currency: 'USD'
        },
        outcomes: {
            successRate: { min: 75, max: 82, unit: '%' },
            cureRate: { min: 50, max: 70, unit: '%' },
            ahiReduction: { min: 50, max: 75, unit: '%' }
        },
        recovery: {
            time: '1-2 weeks',
            hospitalStay: 'Outpatient or 1 day',
            workReturn: '1-2 weeks'
        },
        anesthesia: 'General',
        insuranceCovered: true,
        cptCodes: ['42826'],
        bestFor: 'Children with OSA, adults with enlarged tonsils',
        considerations: 'First-line treatment for pediatric OSA. Higher success rate in children than adults.',
        keywords: ['tonsillectomy', 'adenoidectomy', 'T&A', 'tonsil removal', 'pediatric sleep apnea']
    },

    'genioglossus-advancement': {
        id: 'genioglossus-advancement',
        name: 'Genioglossus Advancement',
        shortName: 'GA',
        slug: 'genioglossus-advancement',
        description: 'Surgical procedure to advance the genioglossus muscle attachment, pulling the tongue forward to prevent airway collapse.',
        category: 'Tongue Surgery',
        priceRange: {
            low: 8000,
            median: 12000,
            high: 20000,
            currency: 'USD'
        },
        outcomes: {
            successRate: { min: 39, max: 65, unit: '%' },
            cureRate: { min: 15, max: 25, unit: '%' },
            ahiReduction: { min: 30, max: 50, unit: '%' }
        },
        recovery: {
            time: '2-3 weeks',
            hospitalStay: '1 day',
            workReturn: '1-2 weeks'
        },
        anesthesia: 'General',
        insuranceCovered: true,
        cptCodes: ['21199'],
        bestFor: 'Tongue base obstruction, often combined with other procedures',
        considerations: 'Usually performed as part of multi-level surgery. Addresses tongue-base collapse.',
        keywords: ['genioglossus advancement', 'tongue surgery', 'tongue base', 'GA procedure']
    },

    tors: {
        id: 'tors',
        name: 'TORS (Transoral Robotic Surgery)',
        shortName: 'TORS',
        slug: 'tors',
        description: 'Minimally invasive robotic surgery to remove tissue at the base of the tongue causing airway obstruction.',
        category: 'Tongue Surgery',
        priceRange: {
            low: 15000,
            median: 25000,
            high: 40000,
            currency: 'USD'
        },
        outcomes: {
            successRate: { min: 60, max: 68, unit: '%' },
            cureRate: { min: 20, max: 30, unit: '%' },
            ahiReduction: { min: 50, max: 60, unit: '%' }
        },
        recovery: {
            time: '2-3 weeks',
            hospitalStay: '1-2 days',
            workReturn: '2 weeks'
        },
        anesthesia: 'General',
        insuranceCovered: true,
        cptCodes: ['41530'],
        bestFor: 'Tongue base obstruction, lingual tonsil hypertrophy',
        considerations: 'Requires specialized robotic equipment and trained surgeon. Less invasive than traditional tongue surgery.',
        keywords: ['TORS', 'transoral robotic surgery', 'robotic surgery', 'tongue base surgery', 'lingual tonsillectomy']
    }
};

// Category groupings
const PROCEDURE_CATEGORIES = {
    'soft_palate': {
        name: 'Soft Palate Surgery',
        description: 'Procedures targeting the soft palate, uvula, and tonsils',
        procedures: ['uppp', 'tonsillectomy']
    },
    'nasal': {
        name: 'Nasal Surgery',
        description: 'Procedures to improve nasal airflow',
        procedures: ['septoplasty', 'turbinate-reduction']
    },
    'tongue': {
        name: 'Tongue Surgery',
        description: 'Procedures targeting tongue base obstruction',
        procedures: ['genioglossus-advancement', 'tors']
    },
    'skeletal': {
        name: 'Skeletal Surgery',
        description: 'Jaw advancement procedures',
        procedures: ['mma']
    },
    'neuromodulation': {
        name: 'Neuromodulation',
        description: 'Implantable nerve stimulation devices',
        procedures: ['inspire']
    }
};

// Price summary for quick reference
const PROCEDURE_PRICE_SUMMARY = {
    lowest: { procedure: 'turbinate-reduction', price: 2000 },
    highest: { procedure: 'mma', price: 100000 },
    mostCommon: { procedure: 'uppp', priceRange: '$5,000 - $15,000' },
    newestTechnology: { procedure: 'inspire', priceRange: '$30,000 - $65,000' }
};

// Success rate summary
const PROCEDURE_SUCCESS_RATES = {
    highest: { procedure: 'mma', rate: '85-95%' },
    lowest: { procedure: 'genioglossus-advancement', rate: '39-65%' },
    bestCureRate: { procedure: 'mma', rate: '40-50%' }
};

// Helper functions
function getProcedureById(id) {
    return PROCEDURE_DATA[id] || null;
}

function getProceduresByCategory(category) {
    return Object.values(PROCEDURE_DATA).filter(p => p.category === category);
}

function getAllProcedures() {
    return Object.values(PROCEDURE_DATA);
}

function formatPriceRange(procedure) {
    const p = PROCEDURE_DATA[procedure];
    if (!p) return '';
    return `$${p.priceRange.low.toLocaleString()} - $${p.priceRange.high.toLocaleString()}`;
}

function formatSuccessRate(procedure) {
    const p = PROCEDURE_DATA[procedure];
    if (!p) return '';
    return `${p.outcomes.successRate.min}-${p.outcomes.successRate.max}%`;
}

// Export for use in pages
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { PROCEDURE_DATA, PROCEDURE_CATEGORIES, PROCEDURE_PRICE_SUMMARY, PROCEDURE_SUCCESS_RATES };
}
