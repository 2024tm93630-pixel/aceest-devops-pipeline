# ACEest Fitness – Flask Web Application

[![CI – Build & Test](https://github.com/2024tm93630-pixel/aceest-devops-pipeline)](https://github.com/2024tm93630-pixel/aceest-devops-pipeline/blob/main/.github/workflows/main.yml)

A minimal, production-friendly Flask application for ACEest_Fitness & Gym. Users can log workouts and view a list of logged workouts. The project is designed to demonstrate fundamental DevOps practices: version control with Git/GitHub, automated testing with Pytest, containerization with Docker, and CI with GitHub Actions.


Table of Contents
1. Features  
2. Tech Stack  
3. Project Structure  
4. Requirements 
5. Local Setup  
6. Running the App  
7. Testing 
8. Docker Usage  
9. API Endpoints
10.Continuous Integration (GitHub Actions)  
11.License

## Features

- Log workouts (e.g., exercise name + duration).
- View a list of recent workouts.
- Health check endpoint for simple uptime monitoring.
- CI workflow that builds the image and runs tests on every push/PR.

---

## Tech Stack

- Backend: Python, Flask  
- Testing: Pytest  
- Containerization:Docker   
- CI/CD:GitHub Actions

---

## Project Structure

```
aceest-fitness
├── app.py                     # Main entry point (Flask application)
├── templates/
│   └── index.html             # Main HTML template
├── test_app.py            # Unit/functional tests
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration (production-friendly)
└── README.md                  # This file
```


## Requirements

- Python 3.10+
- pip
- Git
- Docker (for containerized usage)

## Local Setup

```bash
# Clone the repository
git clone https://github.com/2024tm93630-pixel/aceest-devops-pipeline
cd aceest-devops-pipeline


# Install dependencies
pip install -r requirements.txt

## Running the App

```bash
python app.py
# App will listen on http://127.0.0.1:5000/

# Quick manual checks
curl -i http://127.0.0.1:5000/
curl -i http://127.0.0.1:5000/health
```

---

## Testing

Run the full test suite:

```bash
pytest -q
```
## Docker Usage

Build and run the container:

```bash
# Build the image
docker build -t aceest-fitness:latest .

# Run the container (maps host port 5000 -> container 5000)
docker run --rm -p 5000:5000 --name ace-fitness aceest-fitness:latest

# Verify
curl -i http://127.0.0.1:5000/health
```

Run tests inside the container:

```bash
docker run --rm aceest-fitness:latest pytest -q
```

Using docker-compose

```bash
docker compose up --build
# or
docker-compose up --build
```

Quick checks:

```bash
curl -i http://127.0.0.1:5000/
```

## Branching Strategy

This project follows a simplified GitFlow branching strategy:

- **main** → Production-ready code  
- **develop** → Integration branch for features  
- **feature/** → Individual feature development  

Workflow:

1. Feature branches are created from `develop`
2. Changes are merged via Pull Requests into `develop`
3. After testing, `develop` is merged into `main`

The CI pipeline runs on both `main` and `develop` branches, and also validates Pull Requests before merging.

## CI/CD Pipeline

The pipeline is implemented using GitHub Actions and Jenkins.

### GitHub Actions (CI)

Triggered on:
- Push to `main` and `develop`
- Pull Requests

Steps:
1. Checkout code
2. Install dependencies
3. Run Pytest
4. Build Docker image

### Jenkins (Build & Quality Gate)

Jenkins is deployed on a Linux VM and performs:

1. Pull latest code from GitHub
2. Install dependencies
3. Run tests
4. Build Docker image

This acts as a secondary validation layer to ensure build stability.