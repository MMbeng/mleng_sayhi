FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN useradd -m app && mkdir -p /app/data && chown -R app:app /app
USER app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
ENTRYPOINT ["python","/app/app.py"]


CMD ["fastapi", "run", "main:app", "--host", "0.0.0.0", "--port", "8000"]
