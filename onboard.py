"""Onboarding script to verify developer environment setup."""

import argparse
import os
import shutil
import sys
import time

import pkg_resources
import requests


def check_python_version():
    """Check if Python version is 3.10 or higher."""
    v = sys.version_info
    version_str = f"{v.major}.{v.minor}.{v.micro}"
    if v.major >= 3 and v.minor >= 10:
        return True, f"Python version: {version_str} (>= 3.10 required)"
    return False, f"Python version: {version_str} (WARNING: needs 3.10+)"


def check_virtual_env():
    """Check if script is running inside a virtual environment."""
    in_venv = sys.prefix != sys.base_prefix
    if in_venv:
        venv_name = os.path.basename(sys.prefix)
        return True, f"Virtual environment: Active ({venv_name})"
    return False, "Virtual environment: NOT active (please activate one)"


def check_package(package_name):
    """Check if a specific package is installed and return its version."""
    try:
        version = pkg_resources.get_distribution(package_name).version
        return True, f"{package_name} installed: version {version}"
    except pkg_resources.DistributionNotFound:
        return False, f"{package_name} NOT installed"


def check_internet():
    """Check internet connectivity by hitting a known URL."""
    try:
        requests.get("https://www.google.com", timeout=5)
        return True, "Internet connectivity: OK"
    except requests.ConnectionError:
        return False, "Internet connectivity: FAILED"


def list_installed_packages():
    """Return a formatted list of all installed packages."""
    # pylint: disable=not-an-iterable
    packages = sorted(
        [f"{p.project_name}=={p.version}" for p in pkg_resources.working_set]
    )
    # pylint: enable=not-an-iterable
    return packages


def check_disk_space():
    """Check if disk space is sufficient (warn if < 1GB free)."""
    usage = shutil.disk_usage(".")
    free_gb = usage.free / (1024**3)
    if free_gb >= 1:
        return True, f"Disk space: {free_gb:.2f} GB free"
    return False, f"Disk space: {free_gb:.2f} GB free (WARNING: less than 1GB!)"


def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Developer Onboarding Check")
    parser.add_argument("--verbose", action="store_true", help="Show extra detail")
    parser.add_argument(
        "--fix", action="store_true", help="Auto-install missing packages"
    )
    return parser.parse_args()


def generate_report(results):
    """Generate a summary report and save it to setup_report.txt."""
    lines = ["=== Developer Onboarding Check ===\n"]
    passed = 0
    for status, message in results:
        prefix = "[PASS]" if status else "[FAIL]"
        lines.append(f"{prefix} {message}")
        if status:
            passed += 1

    lines.append(f"\n---\nResult: {passed}/{len(results)} checks passed")
    if passed == len(results):
        lines.append("✓ All checks passed!")

    report = "\n".join(lines)
    print(report)

    with open("setup_report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    print("\nReport saved to: setup_report.txt")


def main():
    """Run all onboarding checks and generate the report."""
    args = parse_arguments()
    total_start = time.time()

    skip_fix = ("Python Version", "Virtual Environment", "Internet", "Disk Space")
    checks = [
        ("Python Version", check_python_version),
        ("Virtual Environment", check_virtual_env),
        ("pylint", lambda: check_package("pylint")),
        ("black", lambda: check_package("black")),
        ("Internet", check_internet),
        ("numpy", lambda: check_package("numpy")),
        ("Disk Space", check_disk_space),
    ]

    results = []
    for name, check_func in checks:
        start = time.time()
        status, message = check_func()
        elapsed = time.time() - start

        if args.verbose:
            print(f"  [{elapsed:.3f}s] {message}")

        if not status and args.fix and name not in skip_fix:
            print(f"  [FIX] Attempting to install {name}...")
            os.system(f"pip install {name}")
            status, message = check_func()

        results.append((status, message))

    if args.verbose:
        print("\n--- Installed Packages ---")
        for pkg in list_installed_packages():
            print(pkg)
        print("--------------------------\n")

    generate_report(results)

    total_elapsed = time.time() - total_start
    print(f"Total execution time: {total_elapsed:.3f}s")


if __name__ == "__main__":
    main()
