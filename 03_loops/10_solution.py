import time

wait_time = 1
max_retries = 5
attemts = 0

while attemts < max_retries:
    print("Attemts", attemts+1, "wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attemts += 1