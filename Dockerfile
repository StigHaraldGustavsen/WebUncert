FROM python:3.13-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache
EXPOSE 5000
# Not production grade, change to wsgi then. so no parralelism and it is a slow cal aswell
CMD ["uv", "run", "flask", "--app", "webuncert/app", "run", "--port=5000","--host=0.0.0.0"]
