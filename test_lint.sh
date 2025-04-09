#!/bin/bash

cd /lca-workspace/repos/hacs__integration

echo "Running pyupgrade..."
pre-commit run --hook-stage manual pyupgrade --all-files --config .github/pre-commit-config.yaml

echo "Running black..."
pre-commit run --hook-stage manual black --all-files --config .github/pre-commit-config.yaml

echo "Done!"