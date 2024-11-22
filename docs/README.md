# Lab Diagnostics

This repository contains prototype code and resources for the **Lab Diagnostics** project. The goal is to streamline and automate diagnostic workflows for laboratories, enabling efficient and accurate data analysis.

## Key Features

- **DOCS:** Architecture Diagram and Documentation for prototype
- **INFRA:** To Deploy Glue jobs and Lambda and various AWS Resources using Terraform
- **SRC:** 
  - Extract: Extraction of raw file
  - Transform: AWS Glue or an additional Lambda function to transform the data.
  - Load: Final load to Target for Analytics
  - Utils : For Resuable library for spark and S3 functions
- **TEST:** Test cases for best practices

## Getting Started

Follow these steps to set up the project on your local machine:

### Prerequisites

Ensure you have the following installed:

- **Python 3.x** (recommended version: `3.8` or above)
- Required Python libraries (listed in `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ravi231987/Lab_Diagnostics.git
   cd Lab_Diagnostics
#
