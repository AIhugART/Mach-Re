import os
import sys

history_path = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt')
if os.path.exists(history_path):
    print("History file exists.")
    with open(history_path, 'r', encoding='utf-8', errors='replace') as f:
        lines = f.readlines()
    print(f"Total history lines: {len(lines)}")
    # Print the last 100 lines
    for line in lines[-100:]:
        sys.stdout.buffer.write(line.encode('utf-8'))
else:
    print(f"History file does not exist at: {history_path}")
