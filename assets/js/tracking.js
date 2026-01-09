/**
 * StemCellPrices.com - Analytics & Tracking Script
 * Includes: Google Analytics 4, PostHog, Meta Pixel, Reddit Pixel
 * For GoDotoro Programmatic Ad Integration
 */

(function() {
  'use strict';

  // Configuration
  const CONFIG = {
    GA4_ID: 'G-B61C6SRXP7',
    POSTHOG_KEY: 'phc_stemcellprices', // Replace with actual PostHog key
    POSTHOG_HOST: 'https://app.posthog.com',
    META_PIXEL_ID: '', // Add Meta Pixel ID when available
    REDDIT_PIXEL_ID: '', // Add Reddit Pixel ID when available
    DEBUG: false
  };

  // Utility functions
  const log = (msg, data) => {
    if (CONFIG.DEBUG) {
      console.log(`[SCP Tracking] ${msg}`, data || '');
    }
  };

  // Get UTM parameters from URL
  const getUTMParams = () => {
    const params = new URLSearchParams(window.location.search);
    return {
      utm_source: params.get('utm_source') || 'direct',
      utm_medium: params.get('utm_medium') || 'none',
      utm_campaign: params.get('utm_campaign') || 'none',
      utm_content: params.get('utm_content') || 'none',
      utm_term: params.get('utm_term') || 'none',
      gclid: params.get('gclid') || null,
      fbclid: params.get('fbclid') || null
    };
  };

  // Get page context
  const getPageContext = () => {
    const path = window.location.pathname;
    const parts = path.split('/').filter(p => p);
    
    let context = {
      page_type: 'home',
      state: null,
      city: null,
      clinic: null
    };

    if (parts[0] === 'locations') {
      if (parts.length === 1) {
        context.page_type = 'all_states';
      } else if (parts.length === 2) {
        context.page_type = 'state';
        context.state = parts[1];
      } else if (parts.length === 3) {
        context.page_type = 'city';
        context.state = parts[1];
        context.city = parts[2];
      } else if (parts.length >= 4) {
        context.page_type = 'clinic';
        context.state = parts[1];
        context.city = parts[2];
        context.clinic = parts[3].replace('.html', '');
      }
    }

    return context;
  };

  // =====================
  // Google Analytics 4
  // =====================
  const initGA4 = () => {
    // Load gtag.js
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${CONFIG.GA4_ID}`;
    document.head.appendChild(script);

    window.dataLayer = window.dataLayer || [];
    window.gtag = function() { dataLayer.push(arguments); };
    gtag('js', new Date());
    
    // Configure with enhanced measurement
    gtag('config', CONFIG.GA4_ID, {
      send_page_view: true,
      cookie_flags: 'SameSite=None;Secure',
      custom_map: {
        'dimension1': 'page_type',
        'dimension2': 'state',
        'dimension3': 'city',
        'dimension4': 'clinic',
        'dimension5': 'utm_source',
        'dimension6': 'utm_campaign'
      }
    });

    // Send page context
    const context = getPageContext();
    const utm = getUTMParams();
    
    gtag('event', 'page_context', {
      page_type: context.page_type,
      state: context.state,
      city: context.city,
      clinic: context.clinic,
      utm_source: utm.utm_source,
      utm_campaign: utm.utm_campaign
    });

    log('GA4 initialized', CONFIG.GA4_ID);
  };

  // =====================
  // PostHog Analytics
  // =====================
  const initPostHog = () => {
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys onSessionId".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    
    posthog.init(CONFIG.POSTHOG_KEY, {
      api_host: CONFIG.POSTHOG_HOST,
      loaded: function(posthog) {
        // Identify page context
        const context = getPageContext();
        const utm = getUTMParams();
        
        posthog.register({
          page_type: context.page_type,
          state: context.state,
          city: context.city,
          clinic: context.clinic,
          ...utm
        });

        log('PostHog initialized');
      }
    });
  };

  // =====================
  // Meta (Facebook) Pixel
  // =====================
  const initMetaPixel = () => {
    if (!CONFIG.META_PIXEL_ID) {
      log('Meta Pixel ID not configured');
      return;
    }

    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    
    fbq('init', CONFIG.META_PIXEL_ID);
    fbq('track', 'PageView');

    // Track page context
    const context = getPageContext();
    fbq('trackCustom', 'PageContext', {
      page_type: context.page_type,
      state: context.state,
      city: context.city,
      clinic: context.clinic
    });

    log('Meta Pixel initialized', CONFIG.META_PIXEL_ID);
  };

  // =====================
  // Reddit Pixel
  // =====================
  const initRedditPixel = () => {
    if (!CONFIG.REDDIT_PIXEL_ID) {
      log('Reddit Pixel ID not configured');
      return;
    }

    !function(w,d){if(!w.rdt){var p=w.rdt=function(){p.sendEvent?p.sendEvent.apply(p,arguments):p.callQueue.push(arguments)};p.callQueue=[];var t=d.createElement("script");t.src="https://www.redditstatic.com/ads/pixel.js",t.async=!0;var s=d.getElementsByTagName("script")[0];s.parentNode.insertBefore(t,s)}}(window,document);
    
    rdt('init', CONFIG.REDDIT_PIXEL_ID);
    rdt('track', 'PageVisit');

    log('Reddit Pixel initialized', CONFIG.REDDIT_PIXEL_ID);
  };

  // =====================
  // Conversion Tracking
  // =====================
  window.SCP_Track = {
    // Track lead form submission
    leadSubmit: function(data) {
      const context = getPageContext();
      const utm = getUTMParams();
      
      const eventData = {
        ...data,
        page_type: context.page_type,
        state: context.state,
        city: context.city,
        clinic: context.clinic,
        ...utm
      };

      // GA4
      if (window.gtag) {
        gtag('event', 'generate_lead', {
          currency: 'USD',
          value: 50, // Estimated lead value
          ...eventData
        });
      }

      // PostHog
      if (window.posthog) {
        posthog.capture('lead_submitted', eventData);
      }

      // Meta Pixel
      if (window.fbq) {
        fbq('track', 'Lead', eventData);
      }

      // Reddit Pixel
      if (window.rdt) {
        rdt('track', 'Lead', eventData);
      }

      log('Lead tracked', eventData);
    },

    // Track phone click
    phoneClick: function(phone, clinicName) {
      const context = getPageContext();
      
      const eventData = {
        phone: phone,
        clinic_name: clinicName,
        state: context.state,
        city: context.city
      };

      if (window.gtag) {
        gtag('event', 'click', {
          event_category: 'contact',
          event_label: 'phone_click',
          ...eventData
        });
      }

      if (window.posthog) {
        posthog.capture('phone_clicked', eventData);
      }

      log('Phone click tracked', eventData);
    },

    // Track clinic view
    clinicView: function(clinicData) {
      const utm = getUTMParams();
      
      const eventData = {
        ...clinicData,
        ...utm
      };

      if (window.gtag) {
        gtag('event', 'view_item', {
          currency: 'USD',
          value: clinicData.avg_price || 5000,
          items: [{
            item_id: clinicData.clinic_id,
            item_name: clinicData.clinic_name,
            item_category: 'clinic',
            price: clinicData.avg_price
          }]
        });
      }

      if (window.posthog) {
        posthog.capture('clinic_viewed', eventData);
      }

      if (window.fbq) {
        fbq('track', 'ViewContent', {
          content_name: clinicData.clinic_name,
          content_category: 'clinic',
          content_ids: [clinicData.clinic_id],
          value: clinicData.avg_price,
          currency: 'USD'
        });
      }

      log('Clinic view tracked', eventData);
    },

    // Track search/filter
    search: function(searchData) {
      if (window.gtag) {
        gtag('event', 'search', {
          search_term: searchData.query,
          ...searchData
        });
      }

      if (window.posthog) {
        posthog.capture('search_performed', searchData);
      }

      log('Search tracked', searchData);
    },

    // Track form open
    formOpen: function(clinicName) {
      const context = getPageContext();
      
      if (window.gtag) {
        gtag('event', 'form_open', {
          clinic_name: clinicName,
          state: context.state,
          city: context.city
        });
      }

      if (window.posthog) {
        posthog.capture('form_opened', { clinic_name: clinicName });
      }

      log('Form open tracked', clinicName);
    }
  };

  // =====================
  // Initialize All Tracking
  // =====================
  const init = () => {
    initGA4();
    initPostHog();
    initMetaPixel();
    initRedditPixel();

    // Auto-track clinic page views
    const context = getPageContext();
    if (context.page_type === 'clinic' && context.clinic) {
      // Extract clinic data from page if available
      const clinicName = document.querySelector('h1')?.textContent || context.clinic;
      window.SCP_Track.clinicView({
        clinic_id: context.clinic,
        clinic_name: clinicName,
        state: context.state,
        city: context.city
      });
    }

    log('All tracking initialized');
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
