#!/usr/bin/env python3
"""
Script to reproduce the linting issues described in the CI failure.
This script runs the same pre-commit hooks that are failing in CI.
"""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and return the result."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    print('='*60)
    
    result = subprocess.run(cmd, capture_output=True, text=True, cwd="/lca-workspace/repos/hacs__integration")
    
    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        print(f"STDERR:\n{result.stderr}")
    
    return result.returncode == 0

def main():
    """Main function to reproduce the linting issues."""
    print("Reproducing CI linting failures...")
    
    # Change to the repository directory
    os.chdir("/lca-workspace/repos/hacs__integration")
    
    # Test 1: Run pyupgrade
    pyupgrade_success = run_command([
        "pre-commit", "run", "--hook-stage", "manual", "pyupgrade", 
        "--all-files", "--config", ".github/pre-commit-config.yaml"
    ], "pyupgrade check")
    
    # Test 2: Run black
    black_success = run_command([
        "pre-commit", "run", "--hook-stage", "manual", "black", 
        "--all-files", "--config", ".github/pre-commit-config.yaml"
    ], "black check")
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY:")
    print(f"pyupgrade: {'PASS' if pyupgrade_success else 'FAIL'}")
    print(f"black: {'PASS' if black_success else 'FAIL'}")
    
    if not pyupgrade_success or not black_success:
        print("\nThe repository has linting issues that need to be fixed.")
        return 1
    else:
        print("\nAll linting checks passed!")
        return 0

if __name__ == "__main__":
    sys.exit(main())