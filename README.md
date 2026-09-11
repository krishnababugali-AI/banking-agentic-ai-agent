# Banking Agentic AI Agent

A production-oriented Agentic AI banking assistant built using Python,
FastAPI, Google ADK, MCP, RAG, Kafka, and cloud-native infrastructure.

## Business Problem

Banking customers frequently need help understanding transactions,
account activity, banking policies, and unfamiliar charges.

Traditional chatbots can answer static FAQs but cannot safely retrieve
customer-specific information or execute controlled banking workflows.

This project builds an Agentic AI system that can reason about a
customer request, select appropriate tools, retrieve authorized banking
data, use enterprise knowledge through RAG, and return a grounded response.

## Use Case

Customer:

> "I see a $149 transaction on my credit card yesterday.
> What is this charge?"

The system should:

1. Authenticate the customer.
2. Authorize access to the requested account.
3. Understand the customer's intent.
4. Retrieve the transaction using a backend banking service.
5. Retrieve relevant banking policies when necessary.
6. Generate a grounded response using an LLM.
7. Protect sensitive PII and financial information.
8. Record appropriate audit and observability events.
9. Handle failures, timeouts, and retries safely.

## High-Level Architecture

Customer
    |
    v
Banking Application
    |
    v
API Gateway
    |
    v
FastAPI Backend
    |
    v
Agentic AI Layer
Google ADK + Gemini
    |
    +------ MCP Tools ------> Banking Microservices
    |                            |
    |                            +--> Account Service
    |                            +--> Transaction Service
    |                            +--> Dispute Service
    |
    +------ RAG -----------> Banking Knowledge Base
    |
    +------ Events --------> Kafka

## Technology Stack

### Backend
- Python
- FastAPI
- Pydantic
- AsyncIO

### Agentic AI
- Google ADK
- Gemini
- MCP

### Knowledge / RAG
- Embeddings
- Vector Search
- Enterprise banking documents

### Data
- PostgreSQL
- Redis

### Event-Driven Architecture
- Apache Kafka

### Production Engineering
- Structured Logging
- Error Handling
- Timeouts
- Retry with Exponential Backoff
- Rate Limiting
- Authentication
- Authorization
- Audit Logging
- PII Protection

### Infrastructure
- Docker
- Kubernetes / GKE

### CI/CD
- GitHub
- Automated Testing
- Security Checks
- Docker Image Build
- Deployment Pipeline
- Rollback Strategy

## Project Status

Phase 1: Project setup and business requirements.