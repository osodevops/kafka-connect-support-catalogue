# Security and connector maintenance

This document explains how to scope connector maintenance with OSO. Binding obligations are set in the applicable product policy and signed support schedule.

## Agree the maintenance owner

| Component | Responsibility to record |
|---|---|
| OSO-maintained connector | OSO releases fixes for supported versions under the published product policy; the customer approves and deploys production changes. |
| Third-party connector | Identify whether OSO supplies diagnosis and upstream coordination, or also undertakes code remediation, dependency updates, backports or a maintained fork. |
| Custom connector | Agree source ownership, supported versions, release rights, test environments and continuing security maintenance. |
| Connect worker, Java, container image and operator | Identify who supplies updated images and compatibility evidence, and who deploys them. Platform support does not automatically include every infrastructure component. |
| Cloud service, source system and production estate | The customer and its vendors retain their responsibilities unless an explicit service scope allocates work to OSO. |

## A complete maintenance cycle

1. **Inventory:** record plugin versions, bundled dependencies, Java/runtime versions, images, licences, lifecycle and release provenance.
2. **Identify:** review dependency and image scan results, supplier advisories and reported vulnerabilities. Static code review alone does not establish that dependencies or deployed images are free of known vulnerabilities.
3. **Triage:** confirm affected versions and reachable code, severity, exploitability, exposure and business impact. Separate a vulnerability report from a live production incident.
4. **Contain:** agree immediate controls for active exploitation or an urgent exposure. Isolation, credential rotation or disabling affected functionality may be needed before a patch exists.
5. **Remediate:** prepare a patch, dependency upgrade or supported upstream release within the agreed engineering scope. Record any upstream dependency and the available mitigation.
6. **Test:** verify unit/integration behaviour, authentication, offset recovery, retries, throughput and sink effects against the supported configuration. Supply release notes and rollback guidance.
7. **Deploy:** the authorised production owner approves and applies the change. Record the deployed version and validate that the mitigation or patch is effective.
8. **Close:** retain evidence and track any remaining risk. Exceptions need an owner, expiry date, compensating controls and a review date.

## Published OSO product commitments

The current Salesforce and ServiceNow policies describe acknowledgement within two business days, severity assessment within five, and a fix or published mitigation for critical/high issues in supported versions within ten business days. They also describe backports to the supported minor releases and dependency monitoring. See the product policies for the complete scope and supported version window:

- [Salesforce support](https://github.com/osodevops/kafka-connect-salesforce-oss/blob/main/SUPPORT.md) and [security](https://github.com/osodevops/kafka-connect-salesforce-oss/blob/main/SECURITY.md).
- [ServiceNow support](https://github.com/osodevops/kafka-connect-servicenow-oss/blob/main/SUPPORT.md) and [security](https://github.com/osodevops/kafka-connect-servicenow-oss/blob/main/SECURITY.md).

These product commitments do not automatically apply to third-party projects or newly commissioned connectors. Their support schedule must state the clock start, coverage calendar, remediation obligation and escalation route. Publishing a fixed plugin version and deploying it in a customer environment are separate activities.

## Routine and emergency changes

Agree a routine review and maintenance cadence for the supported estate. Critical/high findings and active exploitation need an exception to the routine release cycle where warranted by risk. A capacity allowance for planned engineering work must explicitly state how urgent security remediation is handled; a release-count allowance must not be mistaken for the vulnerability response obligation.

Upstream fixes may arrive outside OSO's control. Any maintained-fork obligation requires an agreed licence review, repository/release arrangement and continuing engineering scope.

## UK security guidance

NCSC Cyber Essentials requirements use a 14-day deployment window from release for certain high/critical security updates on in-scope software. This is a scheme requirement, not a universal statutory patch deadline, and is distinct from a supplier's patch-development target. Map the customer's own standards and certification scope to the complete release-and-deployment process.

Reference: [NCSC Cyber Essentials requirements](https://www.ncsc.gov.uk/files/cyber-essentials-requirements-for-it-infrastructure-v3-3.pdf).

## Confidential reports and diagnostics

Use each product's private vulnerability-reporting channel. Redact credentials and personal data from diagnostics. Agree permitted support locations, processors and transfer safeguards before sharing personal data; screen sharing and diagnostic exports may also involve processing.
