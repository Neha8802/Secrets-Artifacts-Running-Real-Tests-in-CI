import datetime
import os
import platform
import sys

print("--- CI System Check ---")
print(f"Run Timestamp: {datetime.datetime.now(datetime.timezone.utc)}")
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"Python Version: {platform.python_version()}")

# Check if a required file exists
required_file = "config.txt"

if not os.path.exists(required_file):
    print(f"ERROR: '{required_file}' is missing! Exiting with non-zero code 1.")
    sys.exit(1)  # Non-zero exit code -> Fails the GitHub Actions pipeline

print(f"SUCCESS: '{required_file}' found! Exiting with code 0.")
sys.exit(0)      # Zero exit code -> Passes the GitHub Actions pipeline
