import sys
import os

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print("Installed packages:")
for pkg in sys.modules.keys():
    print(f"  - {pkg}")

print("\nEnvironment variables:")
for key, value in os.environ.items():
    print(f"  {key}={value}")
