# Cloud

Cloud concepts and AWS, Azure, and general cloud architecture questions.

[Back to the question-bank index](../README.md)

## What is EC2, S3 AND IAM?

**Answer**

EC2 (Elastic Compute Cloud): A web service that provides resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers.
S3 (Simple Storage Service): A scalable object storage service that allows you to store and retrieve any amount of data at any time, from anywhere on the web.
IAM (Identity and Access Management): A web service that helps you securely control access to AWS services and resources for your users. It allows you to create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources.

## What is AWS Cloud Watch

**Answer**

AWS CloudWatch is a monitoring and observability service provided by Amazon Web Services (AWS). It allows you to collect, monitor, and analyze metrics, logs, and events from your AWS resources and applications. Here are some key features and functionalities of AWS CloudWatch:
Metrics Monitoring:
Collects and tracks metrics from AWS services such as EC2, RDS, Lambda, and more.
Custom metrics can also be created and monitored.
Logs Management:
Collects and stores log data from AWS services, applications, and custom sources.
Allows you to search, filter, and analyze log data.
Alarms:
Set alarms to monitor specific metrics and receive notifications when thresholds are breached.
Supports actions such as sending notifications via SNS, executing Auto Scaling policies, or triggering Lambda functions.
Dashboards:
Create custom dashboards to visualize metrics and logs in real-time.
Supports a variety of widgets for different types of visualizations.
Events:
Monitors and responds to changes in your AWS environment using CloudWatch Events.

**Can trigger automated responses to specific events, such as invoking Lambda functions or sending notifications.**

Insights:
Provides advanced analytics capabilities for logs and metrics.
CloudWatch Logs Insights allows you to query and analyze log data interactively.
Integration:
Integrates with other AWS services such as AWS Lambda, AWS SNS, AWS S3, and more.
Supports integration with third-party tools and services for extended monitoring and alerting capabilities.

## Explain a bit about AWS Technologies below?

**Answer**

AWS CloudFormation is a service that allows you to model and set up your Amazon Web Services resources so that you can spend less time managing those resources and more time focusing on your applications. You create a template that describes all the AWS resources that you want (like Amazon EC2 instances or Amazon RDS DB instances), and AWS CloudFormation takes care of provisioning and configuring those resources for you.
AWS Config is a service that enables you to assess, audit, and evaluate the configurations of your AWS resources. AWS Config continuously monitors and records your AWS resource configurations and allows you to automate the evaluation of recorded configurations against desired configurations. This helps in compliance auditing, security analysis, resource change tracking, and troubleshooting.
AWS OpsWorks is a configuration management service that provides managed instances of Chef and Puppet. These are automation platforms that allow you to use code to automate the configurations of your servers. OpsWorks lets you define the architecture of your application and the specification of each component including package installation, software configuration, and resources such as storage.
Amazon CloudWatch is a monitoring and observability service built for DevOps engineers, developers, site reliability engineers (SREs), and IT managers. CloudWatch provides you with data and actionable insights to monitor your applications, respond to system-wide performance changes, optimize resource utilization, and get a unified view of operational health. It collects monitoring and operational data in the form of logs, metrics, and events, providing a unified view of AWS resources, applications, and services that run on AWS and on-premises servers.
Amazon EC2 is a web service that provides resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers.
Scalability: Easily scale up or down based on your needs.
Flexibility: Choose from a wide variety of instance types optimized for different use cases.
Control: Full control over your instances, including root access and the ability to stop and start instances.
Integration: Integrates with other AWS services such as S3, RDS, and VPC.
Amazon EKS (Elastic Kubernetes Service) is a managed service that makes it easy to run Kubernetes on AWS without needing to manage the Kubernetes control plane.
Managed Kubernetes: AWS manages the Kubernetes control plane, including scaling and patching.
Integration: Integrates with other AWS services such as IAM, VPC, and CloudWatch.
Scalability: Automatically scales your Kubernetes clusters based on demand.
Security: Provides built-in security features such as IAM roles for service accounts and VPC isolation.
Amazon ECS (Elastic Container Service) is a fully managed container orchestration service that makes it easy to run, stop, and manage Docker containers on a cluster.
Managed Service: AWS handles the orchestration and management of your containers.
Integration: Integrates with other AWS services such as IAM, VPC, and CloudWatch.
Scalability: Automatically scales your containerized applications based on demand.
Flexibility: Supports both EC2 and Fargate launch types for running containers.
AWS Fargate is a serverless compute engine for containers that works with both Amazon ECS and Amazon EKS. It allows you to run containers without having to manage the underlying infrastructure.
Serverless: No need to provision or manage servers; AWS handles the infrastructure.
Scalability: Automatically scales your containers based on demand.
Cost-Effective: Pay only for the resources you use, with no upfront costs.
Integration: Works seamlessly with Amazon ECS and Amazon EKS, providing a consistent experience.

## What is AWS IAM

**Answer**

AWS Identity and Access Management (IAM) Roles
IAM Roles are a way to grant permissions to entities that you trust. They are not associated with a specific user or group but can be assumed by trusted entities. Here are the entities that can assume IAM roles:
AWS Users Only:
IAM roles are not limited to AWS users only.
AWS Services and Users:
IAM roles can be assumed by AWS services (such as EC2, Lambda) and AWS users.
External User Identities Federated with IAM:
IAM roles can be assumed by external identities that are federated with AWS IAM, such as users from an external identity provider (e.g., SAML, OpenID Connect).

## What are different Azure Features

**Answer**

Compute
Azure Virtual Machines: Provides scalable, on-demand computing resources with support for Windows and Linux.
Azure App Service: A fully managed platform for building, deploying, and scaling web apps and APIs.
Azure Functions: A serverless compute service that allows you to run event-driven code without managing infrastructure.
Azure Kubernetes Service (AKS): Simplifies the deployment, management, and operations of Kubernetes.
Storage
Azure Blob Storage: Object storage solution for unstructured data such as text or binary data.
Azure Disk Storage: High-performance, durable block storage for Azure VMs.
Azure File Storage: Fully managed file shares in the cloud that are accessible via the SMB protocol.
Azure Data Lake Storage: Scalable and secure data lake for high-performance analytics workloads.
Networking
Azure Virtual Network: Enables secure communication between Azure resources and on-premises networks.
Azure Load Balancer: Distributes incoming network traffic across multiple virtual machines.
Azure VPN Gateway: Establishes secure, cross-premises connectivity between Azure and on-premises networks.
Azure Content Delivery Network (CDN): Delivers high-bandwidth content to users globally with low latency.
Databases
Azure SQL Database: Fully managed relational database service based on SQL Server.
Azure Cosmos DB: Globally distributed, multi-model database service for high availability and low latency.
Azure Database for MySQL: Managed MySQL database service for app development.
Azure Database for PostgreSQL: Managed PostgreSQL database service for app development.
Analytics
Azure Synapse Analytics: Integrated analytics service for big data and data warehousing.
Azure HDInsight: Fully managed, full-spectrum, open-source analytics service for enterprises.
Azure Databricks: Fast, easy, and collaborative Apache Spark-based analytics platform.
Azure Data Factory: Cloud-based data integration service for creating ETL and ELT pipelines.
AI and Machine Learning
Azure Machine Learning: Comprehensive service for building, training, and deploying machine learning models.
Azure AI services: Pre-built APIs and models for vision, speech, language, and related AI capabilities (formerly Azure Cognitive Services).
Azure Bot Service: Platform for building intelligent, enterprise-grade bots.
Security
Microsoft Defender for Cloud: Security posture management and workload protection across cloud and hybrid environments (formerly Azure Security Center).
Microsoft Entra ID: Identity and access management for users, applications, and resources (formerly Azure Active Directory).
Azure Key Vault: Securely stores and manages sensitive information such as keys, secrets, and certificates.
Management and Governance
Azure Monitor: Comprehensive solution for collecting, analyzing, and acting on telemetry from cloud and on-premises environments.
Azure Policy: Enforces organizational standards and assesses compliance at scale.
Azure Cost Management and Billing: Tools for monitoring, allocating, and optimizing cloud costs.
DevOps
Azure DevOps: Services for planning, developing, delivering, and operating applications, including Azure Repos, Azure Pipelines, Azure Boards, and more.
Azure DevTest Labs: Service for quickly creating environments in Azure while minimizing waste and controlling cost.

## Explain common Azure managed data services.

**Answer**

Azure SQL Database is a fully managed relational database service provided by Microsoft Azure. It is based on the Microsoft SQL Server engine and offers high availability, scalability, and security.
Automatic Backups: Automated backups and point-in-time restore.
Scaling: Easily scale up or down based on your workload requirements.
Security: Built-in security features such as data encryption, threat detection, and advanced threat protection.
Managed Service: Microsoft handles maintenance, patching, and updates.
Azure Cosmos DB is a globally distributed, multi-model database service designed for high availability and low latency. It supports multiple data models, including document, key-value, graph, and column-family.
Global Distribution: Distribute data across multiple regions with automatic replication.
Multi-Model Support: Supports various data models and APIs, including SQL, MongoDB, Cassandra, Gremlin, and Table.
Low Latency: Designed for low-latency point operations when the data model, region placement,
partitioning, consistency level, SDK, and provisioned capacity fit the workload; verify the precise
SLA instead of claiming a blanket latency guarantee.
Elastic Scalability: Automatically scales throughput and storage based on demand.
Azure Database for MySQL is a fully managed relational database service based on the MySQL community edition. It offers high availability, scalability, and security.
Managed Service: Microsoft handles maintenance, patching, and updates.
High Availability: Built-in high availability with automatic failover.
Scaling: Easily scale compute and storage resources independently.
Security: Advanced security features such as data encryption, firewall rules, and virtual network integration.
Azure Database for PostgreSQL is a fully managed relational database service based on the PostgreSQL community edition. It offers high availability, scalability, and security. Key features include:
Managed Service: Microsoft handles maintenance, patching, and updates.
High Availability: Built-in high availability with automatic failover.
Scaling: Easily scale compute and storage resources independently.
Security: Advanced security features such as data encryption, firewall rules, and virtual network integration.

## Explain a bit about Azure Technologies mentioned below?

**Answer**

Azure Traffic Manager is a DNS-based traffic load balancer that enables you to distribute traffic optimally to services across global Azure regions while providing high availability and responsiveness.
Traffic Routing: Supports multiple routing methods such as priority, weighted, performance, and geographic routing.
High Availability: Automatically directs traffic to the nearest available endpoint, ensuring high availability.
Health Monitoring: Continuously monitors the health of endpoints and reroutes traffic in case of endpoint failure.
Global Reach: Distributes traffic across multiple regions, improving performance and reliability.
Azure Front Door is a scalable and secure entry point for fast delivery of your global applications. It provides application acceleration, load balancing, and security features.
Global Load Balancing: Distributes traffic across multiple regions for high availability and performance.
Application Acceleration: Uses Anycast and split TCP to accelerate application performance.
Web Application Firewall (WAF): Protects your applications from common web vulnerabilities and attacks.
SSL Offloading: Terminates SSL connections at the edge, reducing the load on your backend servers.
Azure DNS is a hosting service for DNS domains, providing name resolution using Microsoft Azure infrastructure.
DNS Hosting: Host your DNS domains and manage DNS records using the same credentials, APIs, tools, and billing as your other Azure services.
Global Reach: Provides fast and reliable DNS resolution using a global network of name servers.
Integration: Integrates with other Azure services, allowing you to manage DNS records programmatically using Azure Resource Manager.
Security: Supports DNSSEC to protect against DNS spoofing and other attacks.
Azure ExpressRoute is a service that enables you to create private connections between Azure data centers and your on-premises infrastructure or colocation environment.
Private Connectivity: Provides a private, dedicated connection that does not go over the public internet, ensuring higher security and reliability.
High Bandwidth: Supports high bandwidth connections, making it suitable for large-scale data transfer and mission-critical workloads.
Low Latency: Offers lower latency compared to typical internet connections, improving performance for latency-sensitive applications.
Hybrid Cloud: Facilitates hybrid cloud scenarios by enabling seamless integration between on-premises infrastructure and Azure services.

## What is Google Analytics?

**Answer**

Google Analytics is a powerful web analytics service offered by Google that tracks and reports website traffic. It provides detailed insights into how users interact with a website, helping website owners and marketers understand user behavior, measure performance, and make data-driven decisions to improve their online presence.
Traffic Analysis:
Visitor Tracking: Tracks the number of visitors to a website, including new and returning visitors.
Traffic Sources: Identifies where visitors are coming from, such as search engines, social media, direct visits, or referral links.
User Behavior:
Page Views: Monitors the number of views each page on the website receives.
Bounce Rate: Measures the percentage of visitors who leave the site after viewing only one page.
Session Duration: Tracks the average time visitors spend on the website.
Audience Insights:
Demographics: Provides information about the age, gender, and interests of website visitors.
Geolocation: Shows the geographic locations of visitors, including countries, regions, and cities.
Conversion Tracking:
Goals: Allows users to set and track specific goals, such as form submissions, product purchases, or newsletter sign-ups.
E-commerce Tracking: Monitors online sales, revenue, and other e-commerce metrics.
Real-Time Data:
Live Tracking: Provides real-time data on current website activity, including active users, page views, and traffic sources.
Custom Reports and Dashboards:
Customization: Users can create custom reports and dashboards to focus on specific metrics and data points relevant to their business.
Integration with Other Tools:
Google Ads: Integrates with Google Ads to track the performance of advertising campaigns.
Google Search Console: Connects with Google Search Console to provide insights into search engine optimization (SEO) performance.

## I have a website where I have added the Google Analytics tool. Users are visiting my website, and it is showing in the logs, but when I go to the Analytics platform, it is not recording anything. What could be the issue?

**Answer**

Verify Tracking Code Installation:
Correct Placement: Ensure that the Google Analytics tracking code (GA4 or Universal Analytics) is correctly placed in the <head> section of your HTML on all pages you want to track.
Correct Code: Verify that you are using the correct tracking ID (e.g., G-XXXXXXXXXX for GA4 or UA-XXXXXXXX-X for Universal Analytics).
Check for JavaScript Errors:
Console Errors: Open your website in a browser and check the developer console (F12 or right-click > Inspect > Console) for any JavaScript errors that might be preventing the tracking code from executing.
Network Requests:
Network Tab: In the browser's developer tools, go to the Network tab and filter by "collect" to see if requests are being sent to Google Analytics. If no requests are being sent, the tracking code might not be firing correctly.
Ad Blockers and Privacy Extensions:
Disable Extensions: Some ad blockers and privacy extensions can block Google Analytics scripts. Disable these extensions temporarily to see if they are causing the issue.
Tracking Code Duplication:
Single Instance: Ensure that the tracking code is not duplicated on the same page, as this can cause tracking issues.
Property and View Settings:
Correct Property: Verify that you are looking at the correct property and view in the Google Analytics platform.
Filters: Check if any filters are applied to the view that might be excluding data.
Real-Time Reports:
Real-Time Data: Check the Real-Time reports in Google Analytics to see if any data is being recorded. This can help determine if the issue is with data processing or tracking.
Consent Management:
Cookie Consent: If your website uses a cookie consent banner, ensure that users are accepting the necessary cookies for Google Analytics to function.
Debugging Tools:
Google Tag Assistant: Use the Google Tag Assistant Chrome extension to diagnose issues with your Google Analytics implementation.
GA Debugger: Use the Google Analytics Debugger Chrome extension to get detailed logs of what data is being sent to Google Analytics.
Time Lag:
Data Processing Delay: Keep in mind that there can be a slight delay in data processing. Wait for a few hours to see if the data appears in Google Analytics.

## What are CI/CD pipelines and what are some best deployment strategies.

**Answer**

CI/CD Pipelines
CI (Continuous Integration): The practice of automatically integrating code changes from multiple contributors into a shared repository several times a day. This typically involves automated testing to ensure that the new code does not break the existing codebase.
CD (Continuous Deployment/Delivery): The practice of automatically deploying every change that passes the automated tests to production (Continuous Deployment) or to a staging environment (Continuous Delivery).
Best Deployment Strategies
Blue-Green Deployment:
Two identical environments (blue and green) are maintained.
Traffic is switched from the blue environment to the green environment after deployment.
Allows for quick rollback if issues are detected.
Canary Deployment:
New code is gradually rolled out to a small subset of users before being deployed to the entire user base.
Allows for monitoring and rollback if issues are detected.
Rolling Deployment:
New code is deployed to a few servers at a time, gradually replacing the old version.
Ensures that there is no downtime and allows for rollback if issues are detected.
A/B Testing:
Different versions of the application are deployed to different user groups.
Used to test new features and gather user feedback.
Feature Toggles:
New features are deployed in the codebase but are hidden behind feature flags.
Allows for enabling/disabling features without deploying new code.
Immutable Infrastructure:
Instead of updating existing servers, new servers are created with the new code, and the old servers are decommissioned.
Ensures consistency and reduces configuration drift.

## How would you upgrade your application with 0 downtime in the production environment?

**Answer**

Blue-Green Deployment: Maintain two identical environments (Blue and Green) and switch traffic between them for zero downtime.
Canary Deployment: Gradually roll out the new version to a small subset of users before rolling it out to the entire user base.
Rolling Deployment: Gradually replace old instances with new instances, ensuring no downtime.
Feature Toggles: Deploy new features turned off by default and gradually enable them for specific users or groups.
Best Practices: Automated testing, monitoring and logging, backward-compatible database migrations, load balancing, and a clear rollback plan.

## What is Grafana?

**Answer**

Grafana is an open-source platform for monitoring, visualization, and analysis of metrics and logs. It allows you to create and share interactive and dynamic dashboards to visualize data from various sources. Here are some key features and functionalities of Grafana:
Data Source Integration:
Supports a wide range of data sources including Prometheus, InfluxDB, Graphite, Elasticsearch, MySQL, PostgreSQL, AWS CloudWatch, and many others.
Allows you to query and visualize data from multiple sources in a single dashboard.
Customizable Dashboards:
Provides a rich set of visualization options including graphs, charts, tables, heatmaps, and more.
Dashboards are highly customizable with drag-and-drop functionality and a variety of panel options.
Alerting:
Allows you to set up alerts based on your data and receive notifications via email, Slack, PagerDuty, and other channels.
Supports alert rules, notification channels, and alert history.
Templating:
Supports the use of variables and templates to create dynamic and reusable dashboards.
Allows you to filter and customize views based on variable inputs.
Annotations:
Enables you to add annotations to your graphs to highlight specific events or time periods.
Annotations can be added manually or automatically based on data from your sources.
Plugins:
Extensible through a wide range of plugins for data sources, panels, and apps.
The Grafana community and Grafana Labs provide many plugins to extend functionality.
User Management:
Supports user authentication and role-based access control.
Allows you to manage user permissions and share dashboards with specific users or teams.
Enterprise Features:
Grafana Enterprise offers additional features such as enhanced security, reporting, and support for large-scale deployments.

## What is Matomo?

**Answer**

Matomo (formerly known as Piwik) is an open-source web analytics platform that provides detailed insights into website traffic and user behavior. It is a popular alternative to proprietary analytics services like Google Analytics, offering full control over data and privacy. Here are some key features and functionalities of Matomo:
Web Analytics:
Tracks and reports website traffic, user behavior, and interactions.
Provides metrics such as page views, unique visitors, bounce rates, and conversion rates.
Privacy and Data Ownership:
Ensures full control over your data, as it can be hosted on your own servers.
Complies with privacy regulations such as GDPR, offering features like anonymizing IP addresses and respecting Do Not Track settings.
Customizable Dashboards:
Allows you to create and customize dashboards to display the most relevant metrics and reports.
Supports a variety of widgets for different types of visualizations.
Ecommerce Tracking:
Provides detailed insights into e-commerce performance, including product views, cart additions, and sales conversions.
Tracks revenue, average order value, and other key e-commerce metrics.
Goal Tracking and Funnels:
Enables you to set up and track goals to measure conversions and user engagement.
Supports funnel analysis to understand the steps users take before converting.
Heatmaps and Session Recording:
Offers heatmaps to visualize where users click, move, and scroll on your website.
Provides session recording to watch real user sessions and understand user behavior.
Tag Manager:
Includes a built-in tag manager to manage and deploy marketing and analytics tags without modifying the website code.
Supports a wide range of tags and triggers.
Integrations and Plugins:
Extensible through a wide range of plugins and integrations with other tools and platforms.
The Matomo Marketplace offers many plugins to extend functionality.
APIs and Reporting:
Provides a comprehensive API to access and manipulate data programmatically.
Supports automated reporting and email reports.
User Management:
Supports user authentication and role-based access control.
Allows you to manage user permissions and share reports with specific users or teams.

## In the context of cloud-native applications, why is it important to include ephemeral data sources, such as in-memory data grids or caches, in your observability strategy?

**Answer**

Ephemeral data sources like in-memory data grids or caches play a critical role in the performance and reliability of cloud-native applications. These components are often used to store transient data that can significantly impact the application's behavior and performance. If these ephemeral components fail or experience performance issues, it can lead to cascading failures in dependent services, affecting the entire application's stability and user experience.
Critical Role in Performance:
Ephemeral data sources are used to speed up data access and reduce latency by storing frequently accessed data in memory.
Performance issues in these components can lead to increased latency and degraded performance for the entire application.
Dependency on Ephemeral Components:
Many services within a cloud-native application may rely on caches or in-memory data grids for quick data retrieval.
If these components fail, the dependent services may experience timeouts, increased load on primary databases, or complete failure.
Cascading Failures:
A failure in an ephemeral data source can propagate to other parts of the system, causing a chain reaction of failures.
Observability helps in detecting and mitigating such issues before they escalate.
Resource Management:
Monitoring ephemeral data sources helps in understanding resource utilization and managing capacity.
It ensures that these components are not overburdened, which can lead to performance degradation.
Troubleshooting and Debugging:
Including ephemeral data sources in your observability strategy provides visibility into their state and behavior.
This visibility is crucial for troubleshooting and debugging issues related to data access and performance.

## When measuring system latency in observability, what is the key difference between tracking average latency and percentile latency (e.g., p99 latency)?

**Answer**

Average Latency:
Definition: Average latency is the mean time taken for a request to be processed. It is calculated by summing the total latency of all requests and dividing by the number of requests.
Limitation: Average latency can be skewed by outliers (extremely high or low values) and does not provide a clear picture of the worst-case scenarios that users might experience.
Percentile Latency (e.g., p99 latency):
Definition: Percentile latency measures the latency at a specific percentile. For example, p99 latency means that 99% of the requests are faster than this value, and only 1% are slower.
Advantage: Percentile latency provides a better indication of user experience as it accounts for outliers and variability. It shows how the majority of users experience the system, especially in scenarios where latency can vary significantly.
User Experience:
Average Latency: May not accurately reflect the user experience, especially if there are significant outliers.
Percentile Latency: Provides a more accurate representation of the user experience by showing the latency experienced by the majority of users.
Handling Outliers:
Average Latency: Can be heavily influenced by outliers, leading to misleading conclusions.
Percentile Latency: Accounts for outliers by focusing on the distribution of latency values, providing a clearer picture of performance.
Variability:
Average Latency: Does not capture the variability in latency.
Percentile Latency: Highlights the variability and helps identify performance issues that affect a subset of users.
Example:
Average Latency: If you have 100 requests with latencies of 10ms each and one request with a latency of 1000ms, the average latency would be (100 * 10 + 1000) / 101 ≈ 19.8ms. This does not reflect the fact that most users experienced 10ms latency.
Percentile Latency (p99): In the same scenario, the p99 latency would be 10ms, indicating that 99% of the requests were processed within 10ms, providing a clearer picture of the typical user experience.

## Explain the following terms

**Answer**

Throttling: Throttling is a mechanism to limit the rate of incoming requests or data to a system, but it is not specifically about handling mismatches in data flow rates between components.
Caching: Caching involves storing data temporarily to improve retrieval times, but it does not address the issue of data flow rate mismatches.
Load shedding: Load shedding involves dropping or rejecting excess load to protect the system from being overwhelmed, but it does not provide a mechanism for managing data flow rates between components.
Buffering: Buffering involves temporarily storing data in memory to smooth out differences in data flow rates, but it does not provide a feedback mechanism to control the rate of data transmission.
Backpressure is the term used to describe the mechanism that allows a system to cope with data flow rate mismatches, specifically when a component is receiving data faster than it can process. Backpressure provides a way for the system to signal upstream components to slow down the rate of data transmission, ensuring that the receiving component is not overwhelmed and can process the data at a manageable rate

## How can you get the content of a webpage from the command line (for instance you don't have a browser)?

**Answer**

Using curl:
curl http://www.example.com
Using wget:
wget -qO- http://www.example.com
Using httpie:
http GET http://www.example.com
Using powershell on Windows:
Invoke-WebRequest -Uri http://www.example.com -UseBasicParsing

## What UNIX command can be used to quickly grab the most recent entries in a log file?

**Answer**

The tail command in UNIX can be used to quickly grab the most recent entries in a log file. By default, tail displays the last 10 lines of a file, but you can specify a different number of lines if needed.
tail -n 20 /path/to/logfile.log

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

## What is the use of Jenkins cron expression?

**Answer**

Jenkins uses five-field cron expressions to schedule jobs:

```text
MINUTE HOUR DAY-OF-MONTH MONTH DAY-OF-WEEK
```

For example, `H 2 * * 1-5` schedules a job around 02:00 on weekdays. Jenkins adds the `H`
(hash) token to spread jobs across a time range and avoid many jobs starting simultaneously. Use
`Build periodically` when the schedule itself should start the job; use `Poll SCM` only when the
schedule should check source control for changes.
