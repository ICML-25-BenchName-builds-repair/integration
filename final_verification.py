#!/usr/bin/env python3
"""Final verification script to ensure all lint issues are resolved."""

import subprocess
import sys
import os

def run_command(cmd, description):
    """Run a command and return the result."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {cmd}")
    print('='*60)
    
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    print(f"Exit code: {result.returncode}")
    if result.stdout:
        print(f"STDOUT:\n{result.stdout}")
    if result.stderr:
        print(f"STDERR:\n{result.stderr}")
    
    return result.returncode == 0

def main():
    """Main verification function."""
    os.chdir('/lca-workspace/repos/hacs__integration')
    
    # List of all checks from the CI workflow
    checks = [
        'pyupgrade',
        'black', 
        'codespell',
        'check-executables-have-shebangs',
        'check-json',
        'requirements-txt-fixer',
        'check-ast',
        'mixed-line-ending'
    ]
    
    results = {}
    
    for check in checks:
        success = run_command(
            f'pre-commit run --hook-stage manual {check} --all-files --config .github/pre-commit-config.yaml',
            f'{check} check'
        )
        results[check] = success
    
    # Summary
    print(f"\n{'='*60}")
    print("FINAL VERIFICATION SUMMARY")
    print('='*60)
    
    all_passed = True
    for check, passed in results.items():
        status = 'PASS' if passed else 'FAIL'
        print(f"{check:35}: {status}")
        if not passed:
            all_passed = False
    
    print('='*60)
    if all_passed:
        print("✅ ALL LINT CHECKS PASSED! The CI workflow should now succeed.")
        return 0
    else:
        print("❌ Some lint checks failed. Please review the output above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())