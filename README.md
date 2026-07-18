# AI DevOps Repository Automation Assistant

## Overview

I built this project to automate common repository maintenance activities that engineering teams perform regularly.

When teams manage multiple repositories, tasks like checking repository standards, updating labels, validating Terraform versions, and creating maintenance pull requests can become repetitive and time-consuming.

This project uses automation, GitHub APIs, and AI capabilities to simplify these activities and provide a centralized way to analyze and maintain repositories.

## Project Goals

The goal of this project is to build an assistant that can:

- Scan GitHub repositories
- Identify repository configurations
- Manage repository labels automatically
- Validate Terraform versions
- Generate recommendations
- Create automated pull requests for required changes

## Current Features

### Repository Analysis

The application scans repositories and collects information such as:

- Repository details
- Programming language
- Configuration files
- Infrastructure files

### Repository Governance Automation

The assistant can identify missing standards and automate:

- Label management
- Repository metadata updates
- Configuration checks

### Terraform Validation

The system analyzes Terraform files and checks:

- Terraform version requirements
- Infrastructure configuration standards
- Potential upgrade needs

## Technology Stack

### Programming

- Python
- FastAPI

### Cloud & AI

- Google Cloud Platform
- Vertex AI
- Generative AI concepts

### DevOps

- GitHub API
- Terraform
- GitHub Actions

## Project Architecture
