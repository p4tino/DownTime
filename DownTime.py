#! /usr/bin/python
# Basic countdown timer script. Reads a file containing sample dates and it
# tells how much time before and after the dates specified in the script.

import sys
import argparse
import time
from datetime import date

def read_file(path):
    entries = []
    with open(path) as f:
        entries = f.readlines()
    
    parsed_entries = []

    for entry in entries:
        entry = entry.strip()
        entry = entry.split(',')    
        split_date = entry[0].split('/')
        print split_date
        entry_date = date(int(split_date[2]), int(split_date[0]), 
                int(split_date[1]))
        entry[0] = split_date
                
        parsed_entries.append(entry)

    return parsed_entries

def get_options():
    parser = argparse.ArgumentParser(
        description="countdown timer script which reads a date file and "
            "reports time before and after those dates")
    order_group = parser.add_mutually_exclusive_group(required=False)
    order_group.add_argument("-n", "--nosort",
        help="don\'t sort the dates, "
            "report them in the order listed in the file (default)",
        action="store_true")
    order_group.add_argument("-s", "--sort",
        help="sort the dates from oldest to newest",
        action="store_true")
    order_group.add_argument("-r", "--reverse",
        help="sort the dates in reverse chronological order, "
            "from newest to oldest",
        action="store_true")
    parser.add_argument("-f", "--file",
        help="specify a different file to search for dates in. " 
            "default=./dates.csv",
        default="./dates.csv")
    parser.add_argument("-v", "--verbose",
        help="have the script display verbose output messages " 
            "regarding file parsing errors",
        action="store_true")
    args = parser.parse_args()
    
    return args

def main():
    args = get_options()
    entries = read_file(args.file)

if __name__ == "__main__":
    sys.exit(main())

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
