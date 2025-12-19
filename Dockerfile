FROM python:3.9-slim

# Create non-root user
RUN useradd -m appuser

# Set working directory
WORKDIR /app

# Copy application source code
COPY api/ .

# Update system and install dependencies
RUN apt-get update && apt-get upgrade -y \
    && pip install --no-cache-dir flask \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch to non-root user
USER appuser

# Expose application port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
