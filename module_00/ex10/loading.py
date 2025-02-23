import time

def ft_progress(lst):
    total = len(lst)  # Total number of elements in the list
    start_time = time.time()  # Record the start time
    for i, elem in enumerate(lst):
        # Calculate elapsed time
        elapsed_time = time.time() - start_time
        # Calculate percentage progress
        progress = (i + 1) / total
        # Calculate the ETA
        eta = elapsed_time / progress - elapsed_time if progress != 0 else 0
        
        # Create the progress bar
        bar = '=' * int(40 * progress)  # 40 is the length of the bar
        spaces = ' ' * (40 - len(bar))  # Remaining space in the bar
        percent = int(progress * 100)  # Percentage completed
        
        # Print progress bar with info
        print(f"\rETA: {eta:.2f}s [{percent}%][{bar}{spaces}] {i + 1}/{total} | elapsed time {elapsed_time:.2f}s", end="")
        
        # Yield the current element
        yield elem

# Example usage:
listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)  # Simulate work

print()  # To move to the next line after the progress bar
print(ret)
