FROM python:3.15.2-slim-trixie AS base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
RUN useradd --create-home --uid 10001 app

FROM base AS validate
COPY . .
USER app
ENTRYPOINT ["python", "tools/validate_cassettes.py", "--root", "/app"]

FROM base AS check
COPY requirements-dev.txt .
RUN pip install --no-cache-dir --root-user-action=ignore --require-hashes -r requirements-dev.txt
RUN chown app:app /app
COPY --chown=app . .
USER app
CMD ["sh", "-c", "ruff check . && ruff format --check . && mypy && pytest"]
