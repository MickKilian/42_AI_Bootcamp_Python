# my_minipack/progress.py

def show_progress(current, total):
    percentage = (current / total) * 100
    bar = ('#' * int(percentage // 2)) + ('-' * (50 - int(percentage // 2)))
    print(f"[{bar}] {percentage:.2f}%")
