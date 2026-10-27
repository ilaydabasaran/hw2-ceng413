# HW-2: Two Services with Docker Compose

## Project Overview

This project runs a Flask web application and a Redis service using Docker Compose.

The application provides the following endpoints:

- `/health` — checks whether the application is running.
- `/greet?name=Ada` — returns a greeting.
- `/visit` — increments and returns a visit counter stored in Redis.
- `/whoami` — returns the application's container hostname.

## Requirements

- Docker
- Docker Compose

## Configuration

The application supports the following environment variables:

- `APP_GREETING`: greeting prefix; defaults to `Hello`.
- `REDIS_HOST`: Redis service hostname.
- `REDIS_PORT`: Redis port; defaults to `6379`.
- `DATA_DIR`: directory used for file-based counter storage when Redis is not configured.

## Run the Application

```bash
docker compose up -d --build
docker compose ps
```

## Test the Endpoints

```bash
curl.exe http://localhost:8000/health
curl.exe "http://localhost:8000/greet?name=Ada"
curl.exe http://localhost:8000/visit
curl.exe http://localhost:8000/whoami
```

## Stop the Application

```bash
docker compose down
```

To remove the persistent Redis volume as well:

```bash
docker compose down -v
```

## Test Results

Complete this section after running the application and verifying the results.

## Test Results

- Application status: Running
- Redis health status: Healthy
- `/health` response: `{"status":"ok"}`
- `/greet` response: Tested successfully
- `/visit` response: `{"storage":"redis","visits":2}`
- `/whoami` response: Not tested
- Persistence: Data survived app container removal and `docker compose down`; data was reset after `docker compose down -v`.
- Tests: `5 passed`
- Screenshot filename: `screenshot.png`