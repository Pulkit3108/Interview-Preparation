# Web Analytics

Client-side analytics platforms, implementation, privacy, and troubleshooting.

[Back to the question-bank index](../README.md)

## What is Google Analytics?

**Answer**

Google Analytics is a hosted analytics service for measuring website and application interactions.
Google Analytics 4 collects events and can report acquisition, engagement, retention, and conversion
behavior. It can integrate with products such as Google Ads and BigQuery.

Analytics data is sampled, modeled, filtered, and subject to consent and retention configuration; it
is not an authoritative transaction ledger. Define an event taxonomy, avoid sending personal or
sensitive data, validate collection, and apply the privacy and consent rules relevant to the users.

## Why might visits appear in server logs but not in Google Analytics?

**Answer**

Server logs prove that the server received a request, not that the browser executed and transmitted
an analytics event. Check the path in order:

1. Confirm the correct GA4 measurement ID is deployed on the affected pages and that a Tag Manager
   container was published.
2. Use browser developer tools and Tag Assistant to verify the tag runs and sends the expected
   collection request without JavaScript, content-security-policy, or network errors.
3. Check consent state, browser privacy controls, ad blockers, and internal-traffic or data filters.
4. Confirm the correct property and data stream, then inspect Realtime or DebugView before waiting
   for standard reports to process.
5. Avoid deploying both the Google tag and an equivalent Tag Manager tag unless duplicate collection
   is deliberately configured.

Use a controlled test browser with consent granted to distinguish a broken implementation from
expected privacy blocking.

## What is Matomo?

**Answer**

Matomo is a web analytics platform available as a self-hosted product and a hosted cloud service. It
supports traffic and conversion reporting, events, goals, e-commerce measurement, tag management,
and optional behavior-analysis features.

Self-hosting provides more control over storage and retention but also makes the operator responsible
for security, upgrades, backups, availability, and lawful configuration. No analytics product makes
an implementation automatically compliant; data minimization, consent, retention, and access rules
still need explicit decisions.

## References

- [Troubleshoot Google Analytics 4 tag setup](https://support.google.com/analytics/answer/9311124)
- [Google consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode)
- [Matomo documentation](https://matomo.org/docs/)
