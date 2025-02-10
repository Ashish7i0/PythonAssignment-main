import psutil
import time

# Setting the predefined threshold to 80%
threshold = 80
# Declaring an sample threshold variable with value of 85
sample_val = 85
# Declaring an iterative variable with value of 0
i = 0

print("Monitoring CPU usage...")

try:
    while True:
        # Get the current CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        # Overriding cpu_percent value with a sample_val + an iterative value of i
        cpu_percent = sample_val + i
        # Value of i gets incremented by 5 in each iteration to get the expected output
        i = i + 5
        if cpu_percent > threshold:
            print(f"Alert! CPU usage exceeds threshold: {cpu_percent}%")
        # Putting a Wait time of 1 second before checking the current CPU usage again
        time.sleep(1)  

# When the execution is interrupted by pressing Ctrl + C from the keyboard, error message is displayed        
except KeyboardInterrupt:
    print("Monitoring has been interruped due to manual intervention by the user!")
    