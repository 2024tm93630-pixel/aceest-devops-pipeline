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

## Continuous Integration (GitHub Actions)

The workflow file `.github/workflows/main.yml` (included in this repo) performs:

1. Checkout repository  
2. Verify presence of `Dockerfile` and `requirements.txt`  
3. Build the Docker image using Buildx (with caching)  
4. Run tests inside the container (Pytest)  


## Jenkins Build Integration

Jenkins is configured as a Freestyle project that pulls the GitHub repository and performs a clean build.

Steps executed by Jenkins:
1. Install dependencies from requirements.txt
2. Execute Pytest unit tests
3. Build Docker container

This ensures the code compiles and integrates successfully in a controlled build environment.