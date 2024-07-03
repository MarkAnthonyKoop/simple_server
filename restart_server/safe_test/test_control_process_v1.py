#!/usr/bin/env python3
import subprocess
import time

# Simulating a long-running process
long_running_process = subprocess.Popen(["sleep", "60"])
print(f"Started long-running process with PID: {long_running_process.pid}")

# Simulate some operations
time.sleep(10)

# Attempt to gracefully terminate the long-running process
long_running_process.terminate()
print("Sent terminate signal to long-running process.")

# Wait a bit to ensure the process has time to terminate
time.sleep(5)

# Restart the process
restarted_process = subprocess.Popen(["sleep", "60"])
print(f"Restarted process with PID: {restarted_process.pid}")

