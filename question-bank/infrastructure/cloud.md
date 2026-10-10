# Cloud

Cloud concepts and AWS, Azure, and general cloud architecture questions.

[Back to the question-bank index](../README.md)

## What are Amazon EC2, Amazon S3, and AWS IAM?

**Answer**

- **Amazon EC2** provides configurable virtual-machine compute instances. The customer chooses the
  instance type, image, networking, storage, and lifecycle and remains responsible for the guest
  operating system and workload.
- **Amazon S3** is an object store. It stores objects in buckets and supports policies, versioning,
  lifecycle management, and multiple storage classes; it is not a mounted block filesystem by
  default.
- **AWS IAM** controls authentication and authorization for AWS APIs through identities, roles,
  policies, and trust relationships. Prefer federation and temporary role credentials over
  long-lived IAM user access keys.

## What is Amazon CloudWatch?

**Answer**

Amazon CloudWatch is AWS's monitoring and observability service. It receives service and custom
metrics, stores and queries logs, builds dashboards, evaluates alarms, and provides application and
infrastructure monitoring features.

An alarm evaluates a metric or metric-math expression and can notify or invoke supported actions.
CloudWatch Logs Insights provides interactive log queries. Event routing formerly branded as
CloudWatch Events evolved into **Amazon EventBridge**, so new event-driven designs should use current
EventBridge terminology.

## What do CloudFormation, AWS Config, CloudWatch, EC2, EKS, ECS, and Fargate provide?

**Answer**

- **AWS CloudFormation:** provisions and updates AWS resources from declarative templates and tracks
  them as stacks.
- **AWS Config:** records supported resource configurations and evaluates them against rules for
  inventory, change tracking, and compliance evidence.
- **Amazon CloudWatch:** supplies monitoring, logs, metrics, dashboards, and alarms.
- **Amazon EC2:** supplies virtual-machine compute with customer control of the guest environment.
- **Amazon EKS:** manages the Kubernetes control plane; customers still design and operate workloads
  and choose how worker compute is supplied.
- **Amazon ECS:** AWS-native container orchestration using task definitions, services, and clusters.
- **AWS Fargate:** supplies managed compute capacity for eligible ECS tasks and EKS Pods so customers
  do not manage the underlying worker instances.

These services do not automatically scale every workload. Scaling policies, capacity configuration,
networking, identity, health checks, and application behavior must still be designed. AWS OpsWorks
is a legacy service and should not be the default recommendation for a new architecture.

## What is an AWS IAM role, and who can assume one?

**Answer**

An IAM role is an AWS identity with permission policies and a trust policy, but no standard long-term
password or access key. An authorized principal assumes the role and receives temporary credentials
for a bounded session.

Depending on the trust policy, principals can include IAM users or roles in the same or another
account, AWS service principals such as EC2 or Lambda, and identities federated through SAML or
OpenID Connect. Permissions require both trust to assume the role and authorization for the requested
resource action. Apply least privilege and prefer roles over embedded long-term credentials.

## What are the main categories of Azure services?

**Answer**

Representative categories include:

- **Compute:** Virtual Machines, App Service, Functions, and Azure Kubernetes Service.
- **Storage:** Blob Storage for objects, managed disks for VMs, Azure Files for managed file shares,
  and Data Lake Storage for analytics-oriented object storage.
- **Networking:** Virtual Network, Load Balancer, Application Gateway, Front Door, VPN Gateway, and
  ExpressRoute.
- **Data and analytics:** Azure SQL Database, Azure Cosmos DB, managed PostgreSQL, Data Factory,
  Synapse, and Azure Databricks.
- **Identity and security:** Microsoft Entra ID, Key Vault, and Defender for Cloud.
- **Operations and governance:** Azure Monitor, Azure Policy, Resource Manager, and Cost Management.
- **Developer delivery:** Azure DevOps and related repository, pipeline, board, and artifact services.

In an interview, compare services by responsibility, operating model, scaling unit, availability,
security boundary, and cost rather than attempting to memorize the entire product catalog.

## Explain common Azure managed data services.

**Answer**

- **Azure SQL Database:** managed relational service based on the SQL Server engine, with automated
  backups, patching, availability options, and several purchasing and scaling models.
- **Azure Database for PostgreSQL / MySQL:** managed open-source relational engines. Exact supported
  versions, extensions, high-availability modes, and scaling constraints depend on the selected
  service tier.
- **Azure Cosmos DB:** distributed database family with multiple APIs and data models, partitioned
  throughput, consistency choices, and multi-region options.

"Managed" shifts routine infrastructure work to the provider but does not remove data modeling,
indexes, capacity planning, backup-retention decisions, access control, network design, upgrades, or
query tuning. Choose from workload semantics and measured access patterns, not feature count.

## How do Azure Traffic Manager, Front Door, DNS, and ExpressRoute differ?

**Answer**

- **Traffic Manager** makes DNS-based endpoint-routing decisions. Clients then connect directly to
  the selected endpoint, so DNS caching affects failover speed.
- **Front Door** is a global HTTP(S) reverse proxy and application-delivery service with edge
  termination, health-based routing, acceleration, and web-application-firewall integration.
- **Azure DNS** hosts public or private DNS zones and offers resolver services. Public authoritative
  zones can be signed with DNSSEC, but DNSSEC signing and recursive validation are different
  capabilities.
- **ExpressRoute** provides private connectivity from an on-premises or colocation network into
  Microsoft cloud services through a connectivity provider. It is not encryption by itself, so add
  encryption when the threat model requires it.

The services operate at different layers and can be combined. Choose by protocol, traffic path,
failover objective, private-connectivity requirement, and security controls.

## What is a managed queue service?

**Answer**

A managed queue service stores messages until consumers can process them. It decouples producers
from consumers, absorbs temporary traffic spikes, and supports retries when processing fails. A
complete design should discuss delivery semantics, visibility or acknowledgment timeouts, retry and
dead-letter policies, ordering requirements, idempotent consumers, message retention, and
observability. Examples include Amazon SQS, Azure Queue Storage, and Google Cloud Tasks.

Do not assume that a queue guarantees exactly-once business processing. A consumer should normally
be able to handle a message more than once without corrupting state.

## How would you process Amazon SQS messages with a dedicated Python event handler?

**Answer**

Encapsulate the SQS client, queue URL, message processing, and acknowledgment behavior. Use long
polling, delete a message only after successful processing, and let a failed message become visible
again or move to a configured dead-letter queue after repeated failures.

```python
import json
import boto3


class EventHandler:
    def __init__(self, queue_url: str) -> None:
        self.queue_url = queue_url
        self.sqs = boto3.client("sqs")

    def process(self, body: str) -> None:
        event = json.loads(body)
        # Perform an idempotent business operation for event.

    def poll_once(self) -> None:
        response = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=10,
            WaitTimeSeconds=20,
        )
        for message in response.get("Messages", []):
            self.process(message["Body"])
            self.sqs.delete_message(
                QueueUrl=self.queue_url,
                ReceiptHandle=message["ReceiptHandle"],
            )
```

Production code should add bounded retries, logging and metrics, graceful shutdown, visibility
timeout management for long work, schema validation, least-privilege IAM, and idempotency. Catch an
exception only when it can be classified or recorded; deleting a failed message would lose work.

## References

- [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/)
- [AWS IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
- [Azure service documentation](https://learn.microsoft.com/en-us/azure/?product=popular)
- [Azure DNS security](https://learn.microsoft.com/en-us/azure/networking/design-guide/dns-security)
- [Azure Cosmos DB APIs](https://learn.microsoft.com/en-us/azure/cosmos-db/choose-api)
