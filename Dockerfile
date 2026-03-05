FROM ghcr.io/astral-sh/uv:debian-slim

WORKDIR /app
COPY . .

RUN uv sync --dev

CMD ["uv", "run", "pytest", "tests/", "-v"]