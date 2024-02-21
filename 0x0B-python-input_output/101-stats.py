#!/usr/bin/python3
"""Reads from standard input and computes metrics
"""

import sys
from collections import defaultdict

def print_stats(total_size, status_codes):
    """Print accumulated metrics
    """
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))

def parse_line(line, status_codes, valid_codes):
    """Parse a line and update metrics accordingly
    """
    parts = line.split()
    try:
        file_size = int(parts[-1])
        total_size[0] += file_size
    except (IndexError, ValueError):
        pass

    try:
        status_code = parts[-2]
        if status_code in valid_codes:
            status_codes[status_code] += 1
    except IndexError:
        pass

def main():
    total_size = [0]  # Using a list for mutable integer
    status_codes = defaultdict(int)
    valid_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parse_line(line, status_codes, valid_codes)
            if line_count % 10 == 0:
                print_stats(total_size[0], status_codes)
    except KeyboardInterrupt:
        print_stats(total_size[0], status_codes)

if __name__ == "__main__":
    main()

