# README  for Stock Ai
## Decisions and Assumptions

### 1. Data Preparation

- Schema Design: 
    - Design a database schema suitable for your stock data (tables, columns, relationships).
- ETL Pipeline:
    - Create a process to pull CSV data from S3.
    - Cleanse and transform data if needed.
    - Load into your database (consider automation for regular updates).

### 2. LLM Selection & Training

- Model Choice: Evaluate pre-trained LLMs suitable for query translation. Consider fine-tuning on a stock-specific dataset if needed.
- Training Data:
If not using a pre-trained model, collate pairs of natural language queries and their corresponding SQL equivalents.
Aim for a diverse dataset covering the types of queries you expect.
### 3. System Architecture

- Backend:
    Python, Stream Lit
    - Implement API endpoints to receive user queries and return results.
- Frontend:
    - Design a user interface for query input and displaying results (web-based or other).
- Integration:
    - Connect frontend to backend.
    - LLM component to parse natural language and generate SQL.
    - Database connectivity for query execution.
### 4. Deployment

- Infrastructure: 
    - AWS EC2 for application
    - Amazon Athena
    - EC2 for backend/LLM.

- CI/CD (Optional): 
    - Github
    - CodeDeploy

### 5. Testing & Iteration

- Query Testing: Test extensively with various query types to ensure the LLM translates correctly and the results are accurate.
- Refinement: Iterate on LLM training and system logic based on testing feedback.


# LLM Choice