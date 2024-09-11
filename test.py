

# Usage
from pytimer2 import Timer
import time

# Create a Timer instance
timer = Timer()

# Start the countdown with a duration of 500 seconds
timer.start_countdown(duration=500)

# Access the current countdown value
print(f"Current countdown: {timer.get_countdown()} seconds")

# Let it run for a few seconds and then pause
time.sleep(3)
timer.pause_countdown()
print(f"Countdown paused: {timer.get_countdown()} seconds")

# Wait and then resume the countdown
time.sleep(5)
print(f"Countdown still paused: {timer.get_countdown()} seconds")
timer.resume_countdown()
print("Timer resumed...")

# Run for a few more seconds
time.sleep(2)
print(f"Countdown resumed and current time: {timer.get_countdown()} seconds")

# Stop the countdown
timer.stop_countdown()
print(f"Countdown stopped at: {timer.get_countdown()} seconds")