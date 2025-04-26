#!/bin/sh

echo "⏳ Waiting for PostgreSQL to start..."

# Change `db:5432` if  Render Postgres URL is different!
wait-for-it db:5432 --timeout=30 --strict -- echo "✅ PostgreSQL is up!"

# Very important: run CMD passed by Docker (your uvicorn command)
exec "$@"
