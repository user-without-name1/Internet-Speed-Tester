# Installation & Usage

## 1. Install Python (if not installed)

Download from [python.org](https://python.org)

During installation, check **"Add Python to PATH"**

## 2. Install speedtest-cli library

Open terminal (or PowerShell) and run:

```powershell
py -m pip install speedtest-cli
```

## 3. Run the Python script

Navigate to the folder containing `speed_test.py` and run:

```powershell
py speed_test.py
```

The script will automatically:
- find the best available server
- run download and upload speed tests with a live loading animation
- display results including Download (Mbit/s), Upload (Mbit/s), and Ping (ms)

## Example output
Download: 95.23 Mbit/s
Upload:   42.87 Mbit/s
Ping:     12 ms
*(values depend on your internet connection)*

## Prerequisites

- Python 3.x
- Active internet connection

## License

Free to use. No restrictions.
