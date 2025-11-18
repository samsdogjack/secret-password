#!/usr/bin/env python3
"""
Build script for creating standalone password generator executable.
Uses PyInstaller to create a single-file executable.
"""

import subprocess
import sys
import os

def build_executable():
    """Build the standalone executable using PyInstaller."""
    print("Building standalone password generator...")

    # PyInstaller command
    cmd = [
        "pyinstaller",
        "--onefile",           # Create a single executable file
        "--name=password-gen", # Name of the executable
        "--clean",             # Clean PyInstaller cache
        "password.py"
    ]

    try:
        subprocess.run(cmd, check=True)
        print("\n Build successful!")
        print(f"Executable location: {os.path.join('dist', 'password-gen')}")
        print("\nTo run: ./dist/password-gen")
    except subprocess.CalledProcessError as e:
        print(f" Build failed: {e}", file=sys.stderr)
        sys.exit(1)
    except FileNotFoundError:
        print(" PyInstaller not found. Install it with: pip install pyinstaller", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    build_executable()
