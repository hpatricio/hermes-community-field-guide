# Support and services

This page describes how this community guide can be supported and which help may be
available around it. It is an initial, low-risk offer: the guide remains free to
read, and no service, response time, compatibility guarantee or payment option is
active unless it is explicitly configured below.

## Who this is for

The guide is intended for people who are evaluating Hermes Agent, setting up a
first installation, learning the extension model, or troubleshooting a bounded
problem. It is useful when a reader needs a practical starting point, but it is
not a replacement for the [upstream repository](https://github.com/NousResearch/hermes-agent)
or the [official documentation](https://hermes-agent.nousresearch.com/docs/).

The value offered today is curated orientation, reproducible checklists and clear
boundaries around what is official, observed, community guidance or unverified.
This repository does not publish usage, audience, customer, revenue or conversion
metrics; demand for any paid offer is therefore unvalidated.

## The initial offer

**Keep the guide free, and support its maintenance through voluntary sponsorship.**

- [Support maintenance with GitHub Sponsors](https://github.com/sponsors/hpatricio)
- Sponsorship is voluntary and does not buy priority support, private access,
  guaranteed compatibility, a response-time commitment or influence over the
  editorial policy.
- The guide's license and the upstream project's terms continue to apply. A
  sponsorship payment does not transfer copyright or grant permission to reuse
  third-party material.

This is the only payment CTA currently configured in this repository. The link is
owned by the project maintainer and must be kept accurate if ownership changes.

## Possible extensions (not active)

The following are proposals for validation, not current products. Do not describe
them as available until the maintainer completes the configuration and rights
checks.

### Bounded consulting or implementation review

A maintainer could offer a short, clearly scoped review of a Hermes installation,
configuration or documentation change. Any engagement would need a written scope,
explicit inputs, data-retention limits, deliverable, price, availability and
support boundary. No access to credentials, private runtime state or personal
archives should be requested by default.

Activation requirements: configure a real contact or booking destination,
confirm legal/tax handling, define a service scope and acceptance criteria, and
publish a privacy notice appropriate to the information collected.

### Team training or workshop

A future workshop could use the public guide for onboarding, extension concepts,
and troubleshooting practice. It must state duration, audience, materials,
interaction model, cancellation terms and whether examples are tested against a
specific Hermes version. Training is not an upstream certification.

Activation requirements: configure a real inquiry destination, confirm the
maintainer's availability and rights to all teaching material, and publish the
terms before accepting payment.

### Optional premium editorial material

A future paid companion could provide maintained checklists, annotated examples,
or release-oriented briefings while keeping the core guide and attribution intact.
It must not copy private Hermod material, upstream material beyond its license, or
third-party content without permission. A premium layer should only be tested
after there is evidence that the free guide is useful and the editorial boundary
is maintainable.

Activation requirements: define the exact original content, license and update
policy; configure a real delivery/payment provider; document refund, privacy and
support terms; and test access removal and data deletion.

## Configuration before adding another CTA

Replace the marked placeholders only after the maintainer has made the relevant
human decisions. Do not commit secrets, API keys, private tokens or provider
session data.

- `CONTACT_URL`: a real public contact, issue, form or booking URL approved by the
  maintainer. It is currently **not configured**.
- `PAYMENT_URL`: a real payment or checkout URL, with owner, currency, refund and
  tax handling confirmed. It is currently **not configured**.
- `PREMIUM_DELIVERY_URL`: a real delivery/access URL and its privacy policy. It is
  currently **not configured**.
- `SPONSOR_OWNER`: the GitHub Sponsors owner. It is currently `hpatricio` in
  `.github/FUNDING.yml`; update both that file and this page if ownership moves.

Before publishing a new CTA:

1. Replace the placeholder with the exact approved URL and purpose.
2. Verify the destination in an unauthenticated browser and read back the public
   page, without entering credentials or payment details.
3. Add the scope, price or “request a quote” wording only when the maintainer has
   decided it.
4. State what the buyer receives, what is excluded, support expectations and
   cancellation/refund terms.
5. Re-run `python3 scripts/check-docs.py`, `git diff --check` and the repository's
   credential-pattern checks.
6. Review the rendered page on desktop and mobile before announcing it.

## Launch checklist

- [ ] The maintainer has approved the offer, owner and public contact route.
- [ ] The current CC BY 4.0 license and upstream/third-party terms were reviewed.
- [ ] No private runtime data, credentials, evaluator exports or personal archives
      are used as deliverables.
- [ ] Any third-party content, trademarks, screenshots and examples have a rights
      and attribution decision.
- [ ] Payment, tax, invoicing, consumer-protection, refund and privacy obligations
      have been checked for the maintainer's jurisdiction.
- [ ] The public destination works without a fake, private or temporary URL.
- [ ] Scope, exclusions, availability and compatibility disclaimers are visible.
- [ ] The CTA is present in the README and this page, but is not repeated
      intrusively throughout the guide.
- [ ] Local documentation, link, secret-pattern and diff checks pass.
- [ ] A rollback is prepared: remove the CTA/configuration and restore the previous
      page if the destination, rights or privacy review fails.

## Initial metrics and review gates

Collect only the minimum aggregate information needed to decide whether to keep
or change the offer. Do not add tracking scripts or collect personal data merely
to measure interest.

Useful first signals are:

- outbound clicks on the configured support CTA, if the provider supplies an
  aggregate report;
- voluntary sponsorship count and amount, reported by the provider;
- qualified inquiries that state a real problem the guide helped clarify;
- recurring questions, documentation corrections and requests for training or
  implementation help;
- time required to keep the guide accurate after upstream changes.

These are signals, not promises or targets. Record the observation period and
source before making a decision. A paid engagement should be treated as evidence
only after its scope, payment and delivery are verified; do not publish a
customer story or testimonial without explicit permission.

## Boundaries

- This page is an independent community offer, not an official Hermes Agent
  support channel.
- Sponsorship or a future service does not imply endorsement by Nous Research.
- The guide remains documentation, not a managed Hermes runtime or hosted service.
- No compatibility guarantee, security warranty or emergency response is offered.
- Public questions must not contain secrets, private logs, personal data or
  provider credentials.
- License, privacy, consumer-protection and tax questions require qualified advice
  for the applicable jurisdiction; this page is not legal or tax advice.

Last reviewed: 2026-08-21
