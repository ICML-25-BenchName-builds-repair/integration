#!/usr/bin/env python3
"""Script to test and verify lint fixes."""

import subprocess
import sys
import os


def run_command(cmd, description):
    """Run a command and return the result."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    print("=" * 60)

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        print(f"STDERR:\n{result.stderr}")

    return result.returncode == 0


def main():
    """Main test function."""
    os.chdir("/lca-workspace/repos/hacs__integration")

    # Test pyupgrade
    pyupgrade_success = run_command(
        "pre-commit run --hook-stage manual pyupgrade --all-files --config .github/pre-commit-config.yaml",
        "pyupgrade check",
    )

    # Test black
    black_success = run_command(
        "pre-commit run --hook-stage manual black --all-files --config .github/pre-commit-config.yaml",
        "black check",
    )

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print("=" * 60)
    print(f"pyupgrade: {'PASS' if pyupgrade_success else 'FAIL'}")
    print(f"black: {'PASS' if black_success else 'FAIL'}")

    if pyupgrade_success and black_success:
        print("\n✅ All lint checks PASSED!")
        return 0
    else:
        print("\n❌ Some lint checks FAILED!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
