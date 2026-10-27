import os
import socket
from pathlib import Path

from flask import Flask, jsonify, request

app = Flask(__name__)

GREETING = os.environ.get("APP_GREETING", "Hello")
DATA_DIR = Path(os.environ.get("DATA_DIR", "/data"))
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = int(os.environ.get("REDIS_PORT", "6379"))

_redis = None


def get_redis():
    global _redis

    if REDIS_HOST and _redis is None:
        import redis

        _redis = redis.Redis(
            host=REDIS_HOST,
            port=REDIS_PORT,
            socket_connect_timeout=2,
            decode_responses=True,
        )

    return _redis


def _counter_file():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR / "visits.txt"


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/greet")
def greet():
    name = request.args.get("name", "world")
    return jsonify(message=f"{GREETING}, {name}!")


@app.get("/visit")
def visit():
    client = get_redis()

    if client is not None:
        return jsonify(
            visits=int(client.incr("visits")),
            storage="redis",
        )

    counter_file = _counter_file()
    current = int(counter_file.read_text()) if counter_file.exists() else 0
    current += 1
    counter_file.write_text(str(current))

    return jsonify(visits=current, storage="file")


@app.get("/whoami")
def whoami():
    return jsonify(hostname=socket.gethostname())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)