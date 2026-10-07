# OSO Kafka Connect support catalogue

Commercial connector support and engineering services from OSO.

**[Download the OSO service overview (PDF)](output/pdf/OSO_Kafka_Connect_Support_and_Services.pdf)**

We build and maintain Kafka Connect products, support selected third-party integrations, and help teams deliver an event platform with clear operational ownership. This catalogue describes available services. Your support agreement names the approved versions, environments, coverage and engineering responsibilities.

## OSO-maintained connectors

| Product | Direction | Capabilities | Source and support policy |
|---|---|---|---|
| Salesforce | Source and sink | Pub/Sub CDC and Platform Events, Bulk API backfill, SObject and Platform Event sinks, legacy streaming source | [Source](https://github.com/osodevops/kafka-connect-salesforce-oss), [support](https://github.com/osodevops/kafka-connect-salesforce-oss/blob/main/SUPPORT.md), [security](https://github.com/osodevops/kafka-connect-salesforce-oss/blob/main/SECURITY.md) |
| ServiceNow | Source and sink | REST Table API ingestion and CRUD delivery | [Source](https://github.com/osodevops/kafka-connect-servicenow-oss), [support](https://github.com/osodevops/kafka-connect-servicenow-oss/blob/main/SUPPORT.md), [security](https://github.com/osodevops/kafka-connect-servicenow-oss/blob/main/SECURITY.md) |

Both products are Apache 2.0 licensed. Commercial support includes maintained releases and the security obligations in the linked product policies. Kafka Connect platform support is a separate service.

## Third-party connectors

We assess the plugin, licence, dependencies and deployment before including a third-party connector in a support schedule.

| Integration | Direction | Upstream | Assessment focus |
|---|---|---|---|
| Debezium PostgreSQL | CDC source | [Debezium](https://github.com/debezium/debezium), Apache 2.0 | Snapshots, replication slots, WAL, offsets, failover and recovery |
| Aiven HTTP | Sink | [Aiven Open](https://github.com/Aiven-Open/http-connector-for-apache-kafka), Apache 2.0 | POST payloads, authentication, batching, retries, rate limits and duplicate delivery |
| HTTP ingestion | Source | Plugin selected during assessment | API polling or webhooks, authentication, pagination and incremental capture |
| JDBC, Azure storage and other CDC families | Source or sink as selected | Plugin selected during assessment | Exact implementation, licence, runtime and source-system prerequisites |

Third-party support can cover installation, configuration, incident diagnosis, recovery and upstream coordination. Code remediation, security backports and a maintained fork must be explicitly agreed. Upstream projects control their own releases. Aiven's HTTP plugin is a sink, not a source.

## Platform and delivery services

- **Kafka Connect platform support:** worker configuration, plugin packaging, resource sizing, task/rebalance diagnosis, internal state topics, upgrades and recovery.
- **Architecture and implementation:** Kubernetes and Strimzi, AKS, Azure Event Hubs, GitOps with Argo CD, tenant isolation, topic naming, security and operational readiness.
- **Backstage self-service:** approved connector templates, configuration validation, secret references, ownership metadata and reviewed GitOps deployment workflows.
- **Custom connector engineering:** JVM source/sink development, tests, packaging and documentation, with an agreed maintenance plan.
- **Data contracts and integration:** sample-driven event modelling, schema compatibility, transformations, error handling and reconciliation.
- **Archive, replay and portability:** assess durable object storage, backup/restore and migration procedures against retention and recovery requirements.

## How support works

The customer normally retains production access, monitoring, first-line triage and execution of changes. OSO provides specialist technical diagnosis (L2) and agreed engineering assistance (L3), using the support portal, secure diagnostics and incident calls. No standing production access is required for this model.

Product subscriptions follow their published support policies. Extended regional hours, weekends, holidays and continuous 24-hour coverage can be scoped under a separate agreement. Response targets describe acknowledgement and the start of investigation; restoration depends on the incident and the agreed responsibilities.

See [Security and connector maintenance](SECURITY-MAINTENANCE.md) for maintenance responsibilities, vulnerability handling and release/deployment controls.

## Compatibility and onboarding

The linked product policies define supported runtime windows. Each engagement records exact Connect, Java, operator, plugin and source-system versions. Azure Event Hubs combinations are assessed for the required Kafka behaviour, compacted state hubs, authentication, quotas and recovery. This catalogue does not certify every version combination.

We begin with a requirements and architecture review, agree the supported estate and operating model, prove a first integration, then expand through reusable templates and measured acceptance criteria.

## Contact

- Commercial enquiries: [sales@oso.sh](mailto:sales@oso.sh)
- Website: [oso.sh](https://oso.sh)
- Book a discussion: [Sion Smith](https://meetings-eu1.hubspot.com/sion-smith)

Public issues are for catalogue corrections and general questions. Use the contracted support channel for incidents and the product's private reporting channel for vulnerabilities. Never include credentials or private production data in a public issue.

## Document source and licences

The PDF is built from [the service overview source](docs/service-overview.json) using [scripts/build_pdf.py](scripts/build_pdf.py). See [BUILD.md](BUILD.md) for regeneration instructions and [LICENSE](LICENSE) for this repository's terms. Upstream connectors retain their own licences.
