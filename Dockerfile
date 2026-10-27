FROM python:3.12.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py test_app.py ./
RUN useradd --create-home --uid 10001 appuser \
    && mkdir -p /data \
    && chown -R appuser:appuser /app /data

USER appuser

ENV DATA_DIR=/data

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]