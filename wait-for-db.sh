#!/bin/sh

# wait until PostgreSQL is ready
echo "Waiting for PostgreSQL..."

# Use wait-for-it to wait for PostgreSQL on port 5432
/usr/local/bin/wait-for-it db:5432 --timeout=30 --strict -- echo "PostgreSQL started"

# Additional check using netcat (optional redundancy)
while ! nc -z db 5432; do
  sleep 0.5
done

echo "PostgreSQL started. Launching FastAPI..."

# Run the CMD from Dockerfile
exec "$@"
