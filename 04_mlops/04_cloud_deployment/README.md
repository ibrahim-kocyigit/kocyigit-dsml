# Cloud Deployment

## Putting Your API on the Internet

You now have a Dockerized ML API that runs on your machine. But your clients, their users, and their applications can't reach `localhost:8000`. To make the API accessible from anywhere in the world, you need to **deploy** it to a cloud platform. 

This section bridges the gap between *"it runs on my laptop"* and *"anyone can send a request to this URL and get a prediction back"*. 

## The Deployment Landscape

There are dozens of cloud platforms and deployment strategies. As a freelance data scientist, you don't need to master all of them. You need to understand the **categories** so you can pick the right one for your project.

### Deployment Categories

| **Category** | **What You Manage** | **Examples** | **Best For** |
| :--- | :--- | :--- | :--- |
| **PaaS** (Platform as a Service) | Just your code | Railway, Render, Fly.io, Heroku | Small-to-medium APIs, freelance projects, quick deploys |
| **CaaS** (Container as a Service) | Your container | Google Cloud Run, AWS App Runner, Azure Container Apps | Docker-based apps, auto-scaling, pay-per-request | 
| **IaaS** (Infrastructure as a Service) | The entire server | AWS EC2, Google Compute Engine, Azure VMs | Full control, complex architectures, GPU workloads |
| **Serverless** | Individual functions | AWS Lambda, Google Cloud Functions | Lightweight, event-driven, infrequent traffic |

### The Freelancer's Sweet Spot

For most freelance ML projects, **PaaS** and **CaaS** are the right choice. They let you deploy quickly without managing servers, SSL certificates, or networking.

```
Your Docker image
    → Push to a cloud platform
    → Platform gives your a public URL
    → Clients send requsts to that URL
    → You pay only for what you use
````

## CI/CD: Automating Deployment

Manually deploying every time you update the model or fix a bug is tedious and error-prone. **CI/CD (Continuous Integration / Continuous Deployment)** automates this:

- **CI** (Continuous Integration): Every time you push code to GitHub, automated checks run (tests, linting, build verification).
- **CD** (Continuous Deployment): If the checks pass, the new version is automatically deployed to the cloud.

**GitHub Actions** is Github's built-in CI/CD platform. It's free for public repositories and has generous free tier for private ones. Since your code already lives on Github, it's the natural choice.

## What You'll Learn

1. **[Deployment Options Overview](./01_deployment_options_overview.ipynb):** A practical comparison of cloud platforms and deployment strategies. How to choose the right one for a given project and budget.
2. **[Deploying to a Cloud Platform](./02_deploying_to_a_cloud_platform.ipynb):** A step-by-step walkthrough of deploying our Dockerized Iris API to **Railway**, a PaaS that's fast, free-tier friendy, and requires no cloud provider expertise.
3. **[CI/CD Basics with GitHub Actions](./03_ci_cd_basics_with_github_actions.ipynb):** Writing a GitHub Actions workflow that automatically tests and deploys your API whenever your push to `main`.