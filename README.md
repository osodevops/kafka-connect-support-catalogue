# OSO Kafka Connect support catalogue

Commercial connector support and engineering services from OSO.

**[Download the OSO service overview (PDF)](output/pdf/OSO_Kafka_Connect_Support_and_Services.pdf)**

We build and maintain Kafka Connect products, support all Debezium connector families and Aiven Open Kafka Connect implementations, and help teams deliver an event platform with clear operational ownership. This catalogue describes available services. Your support agreement names the approved versions, environments, coverage and engineering responsibilities.

## OSO-maintained connectors

| Product | Direction | Capabilities | Source and support policy |
|---|---|---|---|
| Salesforce | Source and sink | Pub/Sub CDC and Platform Events, Bulk API backfill, SObject and Platform Event sinks, legacy streaming source | [Source](https://github.com/osodevops/kafka-connect-salesforce-oss), [support](https://github.com/osodevops/kafka-connect-salesforce-oss/blob/main/SUPPORT.md), [security](https://github.com/osodevops/kafka-connect-salesforce-oss/blob/main/SECURITY.md) |
| ServiceNow | Source and sink | REST Table API ingestion and CRUD delivery | [Source](https://github.com/osodevops/kafka-connect-servicenow-oss), [support](https://github.com/osodevops/kafka-connect-servicenow-oss/blob/main/SUPPORT.md), [security](https://github.com/osodevops/kafka-connect-servicenow-oss/blob/main/SECURITY.md) |
| Oracle Database CDC | Source | Upcoming OSO open-source connector. Release profile and publication details to follow. | Open-source release forthcoming; [contact OSO](mailto:sales@oso.sh) |

The published Salesforce and ServiceNow products are Apache 2.0 licensed. Oracle is listed as upcoming until its public release. Commercial support includes maintained releases and the security obligations in the linked product policies. Kafka Connect platform support is a separate service.

## Third-party connectors

**OSO offers commercial support across all Debezium connector families and all Aiven Open Kafka Connect connectors listed below.** Onboarding records the exact plugin versions, licences, dependencies, runtimes, source/target systems and environments. The support schedule states code remediation, backports and any maintained-fork obligations.

### Debezium

The list includes the upstream documented source/sink families and additional connector projects maintained under the Debezium organisation. Upstream maturity is shown separately from OSO's support availability. Incubating and development implementations require a release-specific production-readiness decision.

| Connector | Direction | Upstream | Upstream status | Notes |
|---|---|---|---|---|
| MongoDB | Source | [Source](https://github.com/debezium/debezium) | Documented connector family | Change streams, snapshots and resume tokens. |
| MariaDB | Source | [Source](https://github.com/debezium/debezium) | Documented connector family | Binlog capture, snapshots and replication position. |
| MySQL | Source | [Source](https://github.com/debezium/debezium) | Documented connector family | Binlog capture, snapshots, GTIDs and recovery. |
| PostgreSQL | Source | [Source](https://github.com/debezium/debezium) | Documented connector family | Logical decoding, replication slots, WAL and snapshots. |
| SQL Server | Source | [Source](https://github.com/debezium/debezium) | Documented connector family | SQL Server CDC prerequisites, change tables and snapshots. |
| Oracle | Source | [Source](https://github.com/debezium/debezium) | Documented connector family | Oracle capture configuration, snapshots and recovery; distinct from the upcoming OSO connector. |
| IBM Db2 | Source | [Source](https://github.com/debezium/debezium-connector-db2) | Documented connector family | Database-specific CDC prerequisites and source-side dependencies. |
| Apache Cassandra | Source | [Source](https://github.com/debezium/debezium-connector-cassandra) | Documented connector family | Node-local JVM CDC adapter, not a Kafka Connect worker plugin; validate database/connector versions. |
| Vitess | Source | [Source](https://github.com/debezium/debezium-connector-vitess) | Incubating in upstream connector index | VStream capture and topology prerequisites. |
| Google Cloud Spanner | Source | [Source](https://github.com/debezium/debezium-connector-spanner) | Incubating in upstream connector index | Change streams, credentials and recovery. |
| IBM Informix | Source | [Source](https://github.com/debezium/debezium-connector-informix) | Incubating in upstream connector index | Informix CDC prerequisites and database configuration. |
| CockroachDB | Source | [Source](https://github.com/debezium/debezium-connector-cockroachdb) | Incubating in upstream connector index | Native changefeed configuration and source/recovery semantics. |
| YashanDB | Source | [Source](https://github.com/debezium/debezium-connector-yashandb) | Incubating in upstream connector index | YStream and database/client dependencies. |
| Actian Ingres | Source | [Source](https://github.com/debezium/debezium-connector-ingres) | Incubating in upstream connector index | Upstream identifies missing features and production-readiness limitations. |
| Milvus | Source | [Source](https://github.com/debezium/debezium-connector-milvus) | Incubating in upstream connector index | Source capture from collections and message-queue channels; upstream describes early development. |
| JDBC | Sink | [Source](https://github.com/debezium/debezium/tree/main/debezium-connector-jdbc) | Documented sink family | Apply change events to relational databases; validate driver and target semantics. |
| MongoDB | Sink | [Source](https://github.com/debezium/debezium/blob/main/debezium-connector-mongodb/src/main/java/io/debezium/connector/mongodb/MongoDbSinkConnector.java) | Preview/version-specific | Writes relational Debezium change events to MongoDB; distinguish from the MongoDB source. |
| IBM i (AS/400) | Source | [Source](https://github.com/debezium/debezium-connector-ibmi) | Incubating/development project | Journal-based CDC; check documented datatype, failover and journal-loss limitations. |
| SQLite | Source | [Source](https://github.com/debezium/debezium-connector-sqlite) | Incubating/development project | Trigger/log-table CDC; upstream identifies active development. |
| TiDB | Source | [Source](https://github.com/debezium/debezium-connector-tidb) | Incubating/development project | Incubating adapter for TiCDC changefeeds; validate current implementation and release availability. |
| Elasticsearch | Sink | [Source](https://github.com/debezium/debezium-connector-elasticsearch) | Incubating/development project | Incubating sink applying document writes/deletes; not an Elasticsearch CDC source. |

All listed Debezium projects use Apache 2.0 for their connector code. Database drivers, capture agents and other dependencies may have separate licence or installation requirements. Cassandra is a node-local adapter rather than a Kafka Connect worker plugin.

**Upstream project tracking:** [Debezium Neo4j](https://github.com/debezium/debezium-connector-neo4j) currently contains a project scaffold only. It is tracked for future coverage; there is no runnable connector to deploy at the verification date.

### Aiven Open

These are Aiven's open-source Kafka Connect implementations. OSO support is provided by OSO for the agreed deployment and does not require buying Aiven's managed Kafka service or imply Aiven provides the support.

| Connector | Direction | Upstream | Upstream status | Notes |
|---|---|---|---|---|
| JDBC | Source | [Source](https://github.com/Aiven-Open/jdbc-connector-for-apache-kafka) | Active upstream repository | Relational database polling over JDBC. |
| JDBC | Sink | [Source](https://github.com/Aiven-Open/jdbc-connector-for-apache-kafka) | Active upstream repository | Relational database writes over JDBC. |
| HTTP | Sink | [Source](https://github.com/Aiven-Open/http-connector-for-apache-kafka) | Active upstream repository | POST delivery; authentication, batching and retries. No HTTP source in this project. |
| Elasticsearch | Sink | [Source](https://github.com/Aiven-Open/elasticsearch-connector-for-apache-kafka) | Active upstream repository | Index records in Elasticsearch. |
| OpenSearch | Sink | [Source](https://github.com/Aiven-Open/opensearch-connector-for-apache-kafka) | Active upstream repository | Index records in OpenSearch. |
| Google BigQuery | Sink | [Source](https://github.com/Aiven-Open/bigquery-connector-for-apache-kafka) | Active upstream repository | Write Kafka records to BigQuery. |
| Amazon S3 | Sink | [Source](https://github.com/Aiven-Open/cloud-storage-connectors-for-apache-kafka/tree/main/s3-sink-connector) | Active upstream repository | Write records to S3 objects; current combined repository. |
| Amazon S3 | Source | [Source](https://github.com/Aiven-Open/cloud-storage-connectors-for-apache-kafka/tree/main/s3-source-connector) | Active upstream repository | Read S3 objects into Kafka topics. |
| Google Cloud Storage | Sink | [Source](https://github.com/Aiven-Open/cloud-storage-connectors-for-apache-kafka/tree/main/gcs-sink-connector) | Active upstream repository | Write records to GCS objects; current combined repository. |
| Azure Blob Storage | Sink | [Source](https://github.com/Aiven-Open/cloud-storage-connectors-for-apache-kafka/tree/main/azure-sink-connector) | Active upstream repository | Write records to Azure Blob Storage. |
| Salesforce | Source | [Source](https://github.com/Aiven-Open/salesforce-connector-for-apache-kafka/tree/main/source) | Active upstream repository | Aiven Open implementation; separate from the OSO Salesforce suite. |
| Salesforce | Sink | [Source](https://github.com/Aiven-Open/salesforce-connector-for-apache-kafka/tree/main/sink) | Active upstream repository | Aiven Open implementation; separate from the OSO Salesforce suite. |
| AMQP | Source | [Source](https://github.com/Aiven-Open/amqp-connector-for-apache-kafka) | Active upstream repository | Read from AMQP providers; current project documents a source connector. |

All listed Aiven Open connector projects use Apache 2.0. The cloud storage connectors share a repository; each source/sink implementation is listed separately above. Aiven HTTP is a sink. AMQP currently provides a source.

### Aiven legacy repositories

OSO can support existing deployments of these legacy implementations, with the maintained artifact and upgrade/migration route recorded in the schedule. Archived upstream repositories do not receive new releases there.

| Connector | Direction | Upstream | Upstream status | Notes |
|---|---|---|---|---|
| Amazon S3 (legacy standalone) | Sink | [Source](https://github.com/Aiven-Open/s3-connector-for-apache-kafka) | Archived legacy repository | Archived repository; current implementation is in cloud-storage-connectors-for-apache-kafka. |
| Google Cloud Storage (legacy standalone) | Sink | [Source](https://github.com/Aiven-Open/gcs-connector-for-apache-kafka) | Archived legacy repository | Archived repository; current implementation is in cloud-storage-connectors-for-apache-kafka. |
| Google BigQuery (legacy fork) | Sink | [Source](https://github.com/Aiven-Open/kafka-connect-bigquery) | Archived legacy repository | Archived/deprecated fork; current implementation is bigquery-connector-for-apache-kafka. |

### Related connector components

We also cover associated [Aiven SMTs](https://github.com/Aiven-Open/transforms-for-apache-kafka-connect) and can include connector framework, commons, configuration utilities and test-kit issues as part of an agreed connector engineering scope. These are supporting components, not additional source/sink connectors. Aiven's Flink connectors and general database/backup tools are separate products outside this Kafka Connect inventory.

### Further connector development

HTTP sources and other integrations can be scoped where a suitable supported plugin is needed. API polling and webhook receivers have different requirements. Third-party incident support includes configuration, diagnosis, recovery and upstream coordination; code remediation, security backports and a maintained fork are recorded explicitly. Upstream projects control their own releases.

**Inventory checked:** 7 October 2026 against upstream documentation, repository READMEs, connector implementations and repository archive flags. [Machine-readable catalogue](docs/connector-catalogue.json). New upstream additions are reviewed and added to this list.

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
