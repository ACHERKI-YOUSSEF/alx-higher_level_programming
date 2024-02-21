#!/usr/bin/python3
"""Reads from standard input and computes metrics
"""

import sys
from collections import defaultdict

def print_stats(size, status_codes):
    """Print accumulated metrics
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))

if __name__ == "__main__":
    size = 0
    status_codes = defaultdict(int)
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}

    try:
        for i, line in enumerate(sys.stdin, 1):  # Using enumerate to count lines
            line = line.strip()  # Strip whitespace from the line
            
            # Splitting line by space and extracting relevant parts
            parts = line.split()
            if len(parts) != 7:  # Ensure line has all necessary parts
                continue

            # Extracting status code and file size
            status_code = parts[-2]
            file_size = parts[-1]

            if status_code in valid_codes:  # Check if status code is valid
                size += int(file_size)  # Accumulate total file size
                status_codes[status_code] += 1  # Update status code count

            if i % 10 == 0:  # Print stats every 10 lines
                print_stats(size, status_codes)
    except KeyboardInterrupt:
        # Handle keyboard interruption gracefully
        print_stats(size, status_codes)

