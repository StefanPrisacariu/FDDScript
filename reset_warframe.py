import time
from datetime import datetime, timezone

def log_success():
    now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
    print(f"✅ Script executed successfully at {now_utc} UTC.")

log_success()
