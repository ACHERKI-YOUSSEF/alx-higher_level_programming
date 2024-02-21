#!/usr/bin/python3
import sys
from collections import defaultdict

def print_statistics(total_file_size, status_counts):
    print("File size:", total_file_size)
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def main():
    total_file_size = 0
    status_counts = defaultdict(int)
    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                file_size = int(parts[-1])
                status_code = parts[-2]
                total_file_size += file_size
                status_counts[status_code] += 1
            except (IndexError, ValueError):
                pass
            if line_count % 10 == 0:
                print_statistics(total_file_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_counts)

if __name__ == "__main__":
    main()

