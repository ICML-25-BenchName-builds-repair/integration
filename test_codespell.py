#!/usr/bin/env python3
"""
Script to test the codespell issue.
"""
import subprocess
import sys

def run_codespell():
    """Run codespell on the repository."""
    try:
        result = subprocess.run(
            ["pre-commit", "run", "--hook-stage", "manual", "codespell", "--all-files", "--config", ".github/pre-commit-config.yaml"],
            capture_output=True,
            text=True,
            check=True,
        )
        print("Codespell check passed!")
        return True
    except subprocess.CalledProcessError as e:
        print("Codespell check failed!")
        print(e.stdout)
        print(e.stderr)
        return False

if __name__ == "__main__":
    success = run_codespell()
    sys.exit(0 if success else 1)