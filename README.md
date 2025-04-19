# Coles Item Checker

A simple Python script to check the availability of Nongshim Shin Ramyun Black 4-Pack on the Coles Australia website and send a notification via WxPusher when the product is available.

## Features

- Checks product availability from Coles' online store.
- Sends a notification using WxPusher when the product is in stock.
- Can be run manually or scheduled via GitHub Actions.

## Requirements

- Python 3.7+
- `requests` library

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/coles-item-checker.git
   cd coles-item-checker
   ```

2. **Install dependencies:**
   ```bash
   pip install requests
   ```

3. **Set your WxPusher token:**
   - Obtain your WxPusher token.
   - Set the environment variable `WXPUSHER_TOKEN`:
     ```bash
     export WXPUSHER_TOKEN=your_token_here
     ```

## Usage

Run the script locally:
```bash
python nongshim-checker.py
```

## GitHub Actions

You can automate the checker using GitHub Actions.

1. **Add your `WXPUSHER_TOKEN` as a repository secret:**
   - Go to your repository on GitHub.
   - Navigate to `Settings > Secrets and variables > Actions > New repository secret`.
   - Add `WXPUSHER_TOKEN` with your token value.

2. **Workflow Example:**
   The repository includes a sample workflow at `.github/workflows/checker.yml` that runs the script hourly and on manual trigger.

## License

MIT License
