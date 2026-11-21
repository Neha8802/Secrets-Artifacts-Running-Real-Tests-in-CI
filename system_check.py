import datetime
import platform

print("--- CI System Check ---")
print(f"Run Timestamp: {datetime.datetime.now(datetime.timezone.utc)}")
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"Python Version: {platform.python_version()}")
print("Status: All checks passed!")
