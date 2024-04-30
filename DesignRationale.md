# Choice of AWS Athena
- **Reasoning**: 
    - Athena is a serverless, interactive query service that makes it easy to analyze large amounts of data in S3 using standard SQL. 
    - It is well-suited for ad-hoc querying and analysis, which aligns with the requirements of a natural language query system.
    - Athena integrates seamlessly with S3 and other AWS services, providing a scalable and cost-effective solution for querying stock data.
## Amazon Athena: Is the ideal choice for the following reasons:
- Optimized for CSV in S3: Athena natively works on CSV files stored in S3, providing a simple and seamless setup.
- Cost-effective: With a pay-per-query model and your moderate data size, you'll only pay for actual usage.
- Freshness Tolerance: The hourly delay is perfectly acceptable for Athena's metadata refresh approach.
- Low-latency Queries: Athena is designed to be performant for simple SELECT queries, fitting your needs.

## Simplified Process

1. Upload to S3: Your daily CSVs land in a designated S3 bucket.
2. ETL (Minimal): A Lambda function updates Athena's table metadata to include the new files.
3. Query: LLM creates the query and the app interacts with Athena using SQL to retrieve and analyze the data. LLM presents the output.