# Containerization

## Packaging Your API with Docker

You now have a working FastAPI application that loads a trained Pipeline and serves predictions. It runs on your machine. But the moment you hand it to a client or deploy it to a server, the first question is: *"How do i run this?"*

The answer is **Docker**, a tool that packages your application, its dependencies, and its runtime environment into a single, portable unit called a **container**. A container is like a lightweight virtual machine: it runs the same way on your laptop, your client's server, or a cloud platform.

## Why Containerization Matters for Freelancers

| **Problem Without Docker** | **Solution With Docker** |
| :--- | :--- |
| *"It works on my machine.*" - The client can't reproduce your Python environment | The container **is** the environment. It runs identically everywhere. |
| Client has Python 3.10 but you built on 3.13 | The container ships with the exact Python version. |
| `pip install` installs different versions on different machines | Dependencies are frozen inside the container. 
| Client doesnt' know how to install scikit-learn, uvicorn, etc. | The client runs **one command**: `docker run`. |

## Key Concepts

### Images vs. Containers

These two terms are used constantly and it's critical to understand the difference:

| | **Image** | **Container** |
| :--- | :--- | :--- |
| **What** | A read-only blueprint/template | A running instance of an image | 
| **Analogy** | A recipe | A dish cooked from the recipe |
| **Created by** | `docker build` | `docker run` |
| **State** | Immutable (never changes) | Mutable (has running processes, can be stopped/restarted) |
| **Stored** | On disk (can be pushed to a registry like Docker Hub) | Im memory (running on a host) | 

You **build** an image once, then **run** it as many containers as you want.

### Dockerfile
A `Dockerlife` is a text file containing step-by-step instructions to build an image. Think of it as a recipe:

```dockerfile
FROM python:3.13-slim                   # Start from a base image
COPY . /app                             # Copy your code into the image
RUN pip install -r requirements.txt     # Install dependencies
CMD["uvicorn", "main:app"]              # Define what runs when the container starts
```

Each line creates a **layer**. Docker caches layers, so if you change your code but not your dependencies, only the changed layers are rebuilt, making subsequent builds fast.

### Docker Compose

When your application has multiple services (e.g., an API + a database), **Docker Compose** lets you define and run them together using a single `docker-compose.yml` file. For our Iris API it's optional but a noce convenience, it saves you from typing long `docker run` commands.

## What You'll Learn
1. **[Docker Fundamentals](./01_docker_fundamentals.ipynb)**: Images, containers, the Dockerfile instruction set, building, running, layer caching, and essential CLI commands. Everything you need to containerize any Python application.
2. **[Dockerizing an ML API](./02_dockerizing_an_ml_api.ipynb)**: Applying Docker to our Iris FastAPI application. We'll write a production Dockerfile, handle model artifact copying, and use Docker Compose for a clean one command workflow.

After completing this section, you'll be able to ship the entire Iris API to anyone with `docker compose up`.