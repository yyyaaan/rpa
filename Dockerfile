FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# 1. Setup environment
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# 2. Install dependencies first (for caching)
# We copy pyproject.toml; if uv.lock exists, we copy that too.
COPY pyproject.toml ./
COPY uv.lock* ./

# If uv.lock is missing, this will create it.
RUN uv sync --no-install-project --no-dev

# 3. Copy the rest of the code
COPY . .

# Ensure the app uses the virtualenv
ENV PATH="/app/.venv/bin:$PATH"

CMD ["python", "agent.py"]