#!/bin/bash

set -e

case "$1" in
  build)
    echo "🔨 Building Docker images..."
    docker compose build
    ;;

  up)
    echo "🚀 Starting services..."
    docker compose up -d
    ;;

  down)
    echo "🛑 Stopping services..."
    docker compose down
    ;;

  logs)
    echo "📜 Showing logs..."
    docker compose logs -f
    ;;

  ingest)
    echo "📥 Running ingestion..."
    docker compose run --rm backend python app/ingest.py
    ;;

  *)
    echo "Usage: ./docker.sh {build|up|down|logs|ingest}"
    exit 1
    ;;
esac
