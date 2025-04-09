#!/bin/bash
set -e

echo "Running pyupgrade check..."
pre-commit run --hook-stage manual pyupgrade --all-files --config .github/pre-commit-config.yaml

echo "Running black check..."
pre-commit run --hook-stage manual black --all-files --config .github/pre-commit-config.yaml

echo "All checks passed!"