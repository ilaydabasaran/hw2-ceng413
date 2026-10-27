# HW-2 Answers

## 1. How does calling the second service by name work?

Docker Compose creates a network for the services and provides DNS resolution between them. In this project, the application connects to Redis using the service name `cache`. Docker resolves this name to the Redis container's IP address. On the default `docker run` bridge network, containers do not get the same automatic name-based DNS resolution; a user-defined network is needed for that.

## 2. Which service is stateless and which is stateful?

The `app` service is stateless because the visit counter is stored in Redis rather than in the application's local filesystem. The `cache` service is stateful because Redis stores the counter data, which is persisted using the `redisdata` named volume.

### Test Results

- Initial `/visit` response: `{"storage":"redis","visits":1}`
- `/visit` response after recreating the app container: `{"storage":"redis","visits":2}`
- `/visit` response after `docker compose down` and restarting: `{"storage":"redis","visits":3}`
- `/visit` response after deleting the volume and restarting: `{"storage":"redis","visits":1}`

## 3. Where should a database password come from?

Passwords and other secrets should be provided through environment variables or a secrets manager instead of being hardcoded in source code. Secret files such as `.env` should not be committed to Git. Even in a private repository, credentials can be exposed through account compromise or accidental sharing. If a password is accidentally committed, it should be considered exposed and changed.

## Test Environment

- Operating system: Microsoft Windows 10.0.26300.9711
- Docker version: 29.8.2
- Docker Compose version: 5.6.0
- Test date: 2026-10-27

## AI Assistant Usage

I used an AI assistant to check my code and configuration files for possible spelling mistakes, syntax errors, and logical issues. I used the feedback to review the files and understand any suggested corrections.
