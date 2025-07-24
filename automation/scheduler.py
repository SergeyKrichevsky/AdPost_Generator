import time
import schedule

# Import the main task
from automation.runner import run_once

# Schedule the task to run once every day at 10:00 AM
schedule.every().day.at("10:00").do(run_once)
# Testing Code Line:
# schedule.every(1).minutes.do(run_once)

print("🔁 Scheduler started. Running daily at 10:00...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Check once per minute
