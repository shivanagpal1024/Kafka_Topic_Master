
For full details on the existing Kafka platform see - https://github.optum.com/DataExternalization/ops_playbooks/blob/master/platform/core/application/kafka/kafka.md

## What is this repo?
This repo is a catch-all of `csv` kafka topic definitions that don't fit elsewhere.  All topics that are currently part of kaas-alpha need to be defined here - https://github.optum.com/Kafka/kaas-alpha and kaas prod, here - https://github.optum.com/Kafka/kaas-prod

Each folder within ./topics is associated with a cluster. It has `csv` files that define what topics should exist on the cluster, they fall in to 3 cateogires

### Deleting Topics
This repo does not handle the deletion of topics for you. This must be done manually through the kafka topics manager. 
Link [here](https://github.optum.com/DataExternalization/ops_playbooks/blob/master/platform/core/application/kafka/kafka.md#deleting-select-topics-and-their-acls). The credentials for this command can be found in the secrets repo [here](https://github.optum.com/DataExternalization/secrets/blob/master/kaas-exts-topics-user.json). You must decrypt yourself.


### On prem bespoke clusters
Clusters in our data centers that run on VM's or baremetal servers directly. Most of these are legacy

#### prod-kafka-eligibility ctc/elr
These are bespoke clusters, they run on baremetal servers and are only for eligibility workloads.  They also have the `,OU=Data Externalization,O=UnitedHealth Group Inc.,L=Plymouth,ST=Minnesota,C=US` suffix, with venafi signed certs. We don't want to add new worklaods to these clusters, and at some point in 2020 will be migrating them to CLaaS, cluster as a service.

### Legacy Azure Clusters
These legacy azure kafka clusters primarily to support EBaaS. The legacy topic manager (not prm) is currently connected to them.

|Cluster name | End point | grafana |
|-----| -----| ---- |
|dev-kafka-hemi-azure|dev-hemi-kafka.eastus.cloudapp.azure.com:443 | http://grafana-data-exts-platform.origin-elr-core.optum.com/d/akljflaskjda/kafka-azure?orgId=1&refresh=15m&from=now-3h&to=now&var-datasource=Thanos-Dev-CTC&var-kafka_minion_datasource=Thanos-K8s-Lab-HCC-Core-East-01-Azure&var-cluster=azure-dev-hemi |
|lab-kafka-ebaasenc-azure|lab-ebaasenc-kafka.eastus.cloudapp.azure.com:443 | http://grafana-data-exts-platform.origin-elr-core.optum.com/d/akljflaskjda/kafka-azure?orgId=1&refresh=15m&from=now-3h&to=now&var-datasource=Thanos-Dev-CTC&var-kafka_minion_datasource=Thanos-K8s-Lab-HCC-Core-East-01-Azure&var-cluster=azure-lab-ebaasenc |
|lab-kafka-ebaasenc-azure|lab-ebaasenc-kafka.eastus.cloudapp.azure.com:443 | http://grafana-data-exts-platform.origin-elr-core.optum.com/d/akljflaskjda/kafka-azure?orgId=1&refresh=15m&from=now-3h&to=now&var-datasource=Thanos-Dev-CTC&var-kafka_minion_datasource=Thanos-K8s-Lab-HCC-Core-East-01-Azure&var-cluster=azure-lab-ebaas |
|prod-kafka-claims360-azure|prod-claims360-kafka.eastus.cloudapp.azure.com:443 | http://grafana-data-exts-platform.origin-elr-core.optum.com/d/akljflaskjda/kafka-azure?orgId=1&from=now-5m&to=now&refresh=5s&var-datasource=Thanos-Prod-ELR&var-kafka_minion_datasource=Thanos-K8s-Prod-HCC-Core-East-08-Azure&var-cluster=azure-prod-claims360 |
|prod-kafka-ebaasenc-mnr-azure|prod-ebaasenc-mnr-kafka.eastus.cloudapp.azure.com:443 | http://grafana-data-exts-platform.origin-elr-core.optum.com/d/akljflaskjda/kafka-azure?orgId=1&from=now-5m&to=now&refresh=5s&var-datasource=Thanos-Prod-ELR&var-kafka_minion_datasource=Thanos-K8s-Prod-HCC-Core-East-08-Azure&var-cluster=azure-prod-ebaasenc-mnr |
|prod-kafka-hcp-azure|prod-hcp-kafka.eastus.cloudapp.azure.com:443 | http://grafana-data-exts-platform.origin-elr-core.optum.com/d/akljflaskjda/kafka-azure?orgId=1&from=now-5m&to=now&refresh=5s&var-datasource=Thanos-Prod-ELR&var-kafka_minion_datasource=Thanos-K8s-Prod-HCC-Core-East-08-Azure&var-cluster=azure-prod-hcp |
|prod-kafka-mnr-02-azure|prod-mnr-02-kafka.eastus.cloudapp.azure.com:443 | http://grafana-data-exts-platform.origin-elr-core.optum.com/d/akljflaskjda/kafka-azure?orgId=1&from=now-5m&to=now&refresh=5s&var-datasource=Thanos-Prod-ELR&var-kafka_minion_datasource=Thanos-K8s-Prod-HCC-Core-East-08-Azure&var-cluster=azure-prod-mnr-02 |
|prod-kafka-mnr-azure|prod-mnr-kafka.eastus.cloudapp.azure.com:443 | http://grafana-data-exts-platform.origin-elr-core.optum.com/d/akljflaskjda/kafka-azure?orgId=1&from=now-5m&to=now&refresh=5s&var-datasource=Thanos-Prod-ELR&var-kafka_minion_datasource=Thanos-K8s-Prod-HCC-Core-East-08-Azure&var-cluster=azure-prod-mnr |
|prod-kafka-shared-azure|prod-shared-kafka.eastus.cloudapp.azure.com:443 | http://grafana-data-exts-platform.origin-elr-core.optum.com/d/akljflaskjda/kafka-azure?orgId=1&from=now-5m&to=now&refresh=5s&var-datasource=Thanos-Prod-ELR&var-kafka_minion_datasource=Thanos-K8s-Prod-HCC-Core-East-08-Azure&var-cluster=azure-prod-shared |


### Clusters running on CLaaS, cluster as a service on K8's
These clusters run in our own K8's data nodes as part of CLaaS. We're still working through the specifics of what it entails and will be publishing more details later.

These clusters have connection strings distinct from kaas-alpha, kaas-prod. The teams that own them are responsible for sharing these connection strings.

Only people on the Kafka platform team should be creating new folders associated with CLaaS, as prework is required to connect these clusters to the legacy topic manager.

Connection information for these cluters can be found here - https://github.optum.com/EAIP/pep-hcc-trinity/tree/master/kafka/connection

#### prod-kafka-rxclaims CTC/ELR
ACL prefix associated with kaas-prod,however post PRM Migration KaaS-Prod cert will not work for this Cluster. 
Certs automation is enabled for this cluster `,OU=KaaS,O=Optum,L=Eden Prairie,ST=Minnesota,C=US`
ELR connection `elr5hz1-01-s05.uhc.com:16010,elr6hz1-04-s29.uhc.com:16010,elr5hz1-01-s13.uhc.com:16010,elr6hz1-04-s27.uhc.com:16010,elr5hz1-01-s07.uhc.com:16010`
CTC connection `ctc5hz1-01-s14.uhc.com:16013,ctc5hz1-01-s03.uhc.com:16013,ctc5hz1-01-s05.uhc.com:16013,ctc5hz1-01-s11.uhc.com:16013,ctc5hz1-01-s09.uhc.com:1601`

#### streamit-ingestion-store-dev
ACL prefix associated with kaas-prod,however post PRM Migration KaaS-Prod cert will not work for this Cluster. 
Certs automation is enabled for this cluster `,OU=KaaS-alpha,O=Optum,L=Eden Prairie,ST=Minnesota,C=US`
CTC connection `ctc5hz1-01-s10.uhc.com:16014,ctc2hz1-03-s26.uhc.com:16014,ctc5hz1-01-s12.uhc.com:16014,ctc5hz1-01-s04.uhc.com:16014,apslp1559.uhc.com:16014`
Elr connection `elr6hz1-04-s28.uhc.com:16011,elr5hz1-01-s04.uhc.com:16011,elr5hz1-01-s08.uhc.com:16011,elr5hz1-01-s03.uhc.com:16011,elr6hz1-04-s33.uhc.com:1601`

#### streamit-ingestion-store-prod
ACL prefix was earlier associated with kaas-prod,however post PRM Migration KaaS-Prod cert will not work for this Cluster. Certs automation is enabled for this cluster `,OU=KaaS,O=Optum,L=Eden Prairie,ST=Minnesota,C=US`
ELR connection `elr6hz1-04-s33.uhc.com:16012,elr5hz1-01-s16.uhc.com:16012,elr6hz1-04-s31.uhc.com:16012,elr6hz1-04-s43.uhc.com:16012,elr5hz1-01-s15.uhc.com:16012,elr6hz1-04-s28.uhc.com:16012,elr6hz1-04-s30.uhc.com:16012`
CTC connection `ctc2hz1-03-s39.uhc.com:16016,apslp1548.uhc.com:16016,ctc5hz1-01-s12.uhc.com:16016,ctc2hz1-03-s18.uhc.com:16016,apslp1406.uhc.com:16016,ctc2hz1-03-s40.uhc.com:16016,apslp1555.uhc.com:16016`

Note: In this cluster ELR is being userd as prod, and ctc is being used as stage. Since CDC classifies stage as a non-prod environment, but Kafka team classifies it as prod-like, CDC is using their non-prod certs on the cluster. Thus their non-prod attunity cert was explicitly given write permissions to all topics (since the OU didn't match)


### Kafka-topics cert source

This link can be referred to get details for certificate reissuing of topics present in kafka-topics repo:

https://github.optum.com/DataExternalization/ops_playbooks/blob/master/platform/core/application/kafka/kafka.md#kafka-topics-cert-source


### Topic Naming Conventions

The following is a suggested naming convention, this is not mandated for all teams.

Topic names should be well constructed when we have control over them following this pattern:

`<namespace>.<datacenter>.<topic-type>.<optional-classifier>.<name>.<version>`

An example may be an integration stream of `CDC` data coming from the `DC1` datacenter that represents
`CDB` data from the `L_CNSM_SRCH` table.

Some examples:

```
DE_STREAMS.elr.fact.cdb_security.v1
DE_STREAMS.ctc.cmd.publish_eligibility.v1
DE_STREAMS.elr.cdc.foundational.eligibility.v1
```

__namespace__

The team which owns this topic.  

__datacenter__

This represents the well known name of the data cener tin which the topic data originates. This is useful for active-active replication between datacenters.  
Examples: `ctc` or `elr`

__topic-type__

  * _cdc_: change data capture, changes to a domain entity in the system (member, policy, etc).  Typically CDC topics are good candidates for Compaction.
  * _fact_: An outcome of a command or a new fact about a domain entity (member registered, policy expired, member eligibility changed, etc)
  * _cmd_: Something the system needs to do (present tense verb) (register member, begin plan audit, etc.)

__optional-classifier__

A logical classifier/grouping for the topic.  Some examples would be `foundational` or `deadletter` to group topics with
similar functionality together.

__name__

The name of the topic, it should represent something commonly understood or could reuse a stable name that is used in
the source system.  An example would be `l_cnsm_search` whose source is a stream of _cdc_ data originating from the CDB
table `L_CNSM_SEARCH`.

__version__

The version of the topic.  Breaking changes to the event formats would generally result in a new version of the topic.

### Non-Integrated Entities

Non-integrated entities may consume from Azure Kafka topics registered in this repo, if proper process is followed:
1. EIS should approve consumption for the NIE
1. The topic owner(s) should work with the NIE to understand what IP addresses the NIE will use to access Kafka, and get those IPs whitelisted via an "Azure KaaS IP Allowlisting Request": https://github.optum.com/DataExternalization/support-intake/issues/new/choose
1. The topic owner(s) should PR the necessary files to request a Consumer/Producer CN on behalf of the NIE and securely share the generated certificate with the appropriate contacts.
1. The HCP Stream Platform Team must whitelist the desired topic schemas from Schema Registry to be shared with the NIE.

##### Rally
* The Rally Dataship team has already had their IP addresses whitelisted
* The Rally Dataship team has already had a prod and nonprod certifiate sent to them.  These CNs can be reused if Dataship requires access to additional topics:
  * rally-health-nonprod
  * rally-health-prod
