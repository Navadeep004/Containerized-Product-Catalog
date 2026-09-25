# Containerized Product Catalog with Jenkins CI/CD & Kubernetes

A containerized Product Catalog REST API built with Python FastAPI and MongoDB, deployed using Docker and Kubernetes, with Jenkins used to automate the CI/CD workflow.

## Project Overview

This project demonstrates a practical DevOps workflow for building, containerizing, testing, and deploying a backend application.

### Technologies Used

- Python
- FastAPI
- MongoDB
- Docker
- Docker Compose
- Kubernetes
- Jenkins
- Docker Hub
- Git
- GitHub

## Architecture

Developer
    ↓
GitHub
    ↓
Jenkins
    ↓
Build & Test
    ↓
Docker Image
    ↓
Docker Hub
    ↓
Kubernetes
    ↓
Product API
    ↓
MongoDB

## Application

The Product Catalog API provides endpoints for working with products.

Current endpoints:

- `GET /health` - Application and database health check
- `GET /products` - Retrieve products

FastAPI Swagger documentation is available at:

`/docs`

## Docker

The application is packaged using a multi-stage Dockerfile.

The Docker image is published to Docker Hub and used by Kubernetes for deployment.

## Docker Compose

Docker Compose is used for local development and testing.

It runs:

- FastAPI application
- MongoDB

## Kubernetes

The application is deployed to Kubernetes using:

- Namespace
- Deployment
- Service
- MongoDB Deployment
- MongoDB Service
- Kubernetes Secret
- Liveness Probe
- Readiness Probe
- CPU and Memory Requests/Limits

The Product API runs with two replicas.

## CI/CD

Jenkins is used to automate the deployment workflow.

Planned pipeline:

1. Checkout source code from GitHub
2. Install dependencies
3. Run tests
4. Build Docker image
5. Push image to Docker Hub
6. Deploy/update application in Kubernetes
7. Verify deployment

## Project Structure

product-catalog/
│
├── k8s/
│   ├── namespace.yaml
│   ├── product-api-deployment.yaml
│   ├── product-api-service.yaml
│   ├── mongodb-deployment.yaml
│   └── mongodb-service.yaml
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .gitignore
└── README.md