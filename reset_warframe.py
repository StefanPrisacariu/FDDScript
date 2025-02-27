name: Daily Warframe Reset

on:
  schedule:
    - cron: "0 0 * * *"  # Runs at 00:00 UTC daily

jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'  # Use the Python version you prefer

      - name: Install dependencies (if needed)
        run: |
          # If you have any dependencies, uncomment and add them
          # pip install -r requirements.txt

      - name: Run script
        run: python reset_warframe.py  # Run your script
