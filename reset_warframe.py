import requests
from datetime import datetime, timezone
import random

# Firebase URLs
FIREBASE_TODAY_URL = "https://framedle-default-rtdb.firebaseio.com/warframeOfTheDay/today.json"
FIREBASE_YESTERDAY_URL = "https://framedle-default-rtdb.firebaseio.com/warframeOfTheDay/yesterday.json"

# Warframe count (adjust if needed)
TOTAL_WARFRAMES = 106  

def get_random_warframe():
    """Returns a random Warframe index from 0 to TOTAL_WARFRAMES-1"""
    return random.randint(0, TOTAL_WARFRAMES - 1)

def get_current_warframe():
    """Fetches the current Warframe of the Day from Firebase"""
    response = requests.get(FIREBASE_TODAY_URL)
    if response.status_code == 200:
        return response.json()
    return None

def update_warframe():
    """Updates the Warframe of the Day at exactly 00:00 UTC"""
    now_utc = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    # Step 1: Get the current Warframe of the Day
    current_warframe = get_current_warframe()
    
    # Step 2: Move today's Warframe to yesterday's entry
    if current_warframe:
        requests.patch(FIREBASE_YESTERDAY_URL, json=current_warframe)

    # Step 3: Pick a new Warframe for today
    new_warframe = {
        "number": get_random_warframe(),
        "timestamp": now_utc  # Store exact reset time
    }

    # Step 4: Update Firebase
    response = requests.patch(FIREBASE_TODAY_URL, json=new_warframe)
    
    if response.status_code == 200:
        print(f"✅ Warframe updated successfully at {now_utc} UTC")
    else:
        print(f"❌ Failed to update Warframe! Response: {response.text}")

if __name__ == "__main__":
    update_warframe()
