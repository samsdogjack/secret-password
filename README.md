# secret-password
Password generator written in Python using the cryptographically secure `secrets` library.

## Security
This password generator uses Python's `secrets` module, which is specifically designed for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets. Passwords generated are truly random and non-reproducible.

## Usage

### Option 1: Run Python Script
```bash
python3 password.py
```

### Option 2: Standalone Executable
Run the pre-built standalone app (no Python required):
```bash
./dist/password-gen
```

## Building Standalone Application

1. Install dependencies:
```bash
pip3 install -r requirements.txt
```

2. Build the executable:
```bash
python3 build.py
```

The standalone executable will be created at `dist/password-gen` and can be run on any macOS system without Python installed.

## Configuration
Length of password can be changed on line 10 of password.py with `pwd_length`.
