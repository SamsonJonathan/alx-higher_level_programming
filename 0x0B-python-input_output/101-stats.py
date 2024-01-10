#!/usr/bin/python3
"""
    Initialize Module
"""


import sys
from collections import defaultdict

def print_statistics(total_size, status_counts):
    print(f"Total file size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        print(f"{status_code}: {status_counts[status_code]}")

def main():
    total_size = 0
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            # Parse the input line
            try:
                _, _, _, _, status_code, file_size = line.split()[0], line.split()[3][1:], line.split()[5], line.split()[8], line.split()[10]
                status_code = int(status_code)
                file_size = int(file_size)
            except ValueError:
                print("Invalid input format. Skipping line:", line.strip())
                continue

            # Update metrics
            total_size += file_size
            status_counts[status_code] += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
                print()

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print("\nScript interrupted. Printing final statistics:")
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()

