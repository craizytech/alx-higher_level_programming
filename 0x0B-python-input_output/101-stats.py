#!/usr/bin/python3
"""Log parsing module"""

import sys


def print_metrics(total_size, status_counts):
    """
    This method prints the total file size and counts for each status code

    Args:
        total_size: total size of the file
        status_counts: the counts of each status code
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def main():
    """This is the main method """

    total_size = 0
    line_count = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0,
                     405: 0, 500: 0}

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) < 7:
                continue

            status_code = int(parts[-2])
            file_size = int(parts[-1])

            total_size += file_size

            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1
            if line_count % 10 == 0:
                print_metrics(total_size, status_counts)
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)
        sys.exit(0)

    print_metrics(total_size, status_counts)


if __name__ == "__main__":
    main()
