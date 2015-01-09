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
        entry_date = date(int(split_date[2]), int(split_date[0]), 
                int(split_date[1]))
        entry[0] = entry_date
                
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

def sort_entries(entries, reverse):
    if reverse:
        return sorted(entries, key=lambda entry: entry[0], reverse=True) 

    return sorted(entries, key=lambda entry: entry[0])

def process_entries(entries, reference_date):
    processed_entries = []
    
    for entry in entries:
        days_diff = entry[0] - reference_date
        result_string = entry[1] + ":\n\t" + str(abs(days_diff.days)) + ' days'
        
        if days_diff.days < 0:
            result_string = result_string + ' ago'
        elif days_diff.days == 0:
            result_string = result_string + ', today!'

        weeks = abs(days_diff.days) / 7
        weekdays = abs(days_diff.days) % 7

        result_string = result_string + "\n\t" + str(weeks) + ' weeks, ' + str(weekdays) + ' days'
        
        if days_diff.days < 0:
            result_string = result_string + ' ago' 

        processed_entries.append(result_string)

    return processed_entries

def main():
    args = get_options()
    entries = read_file(args.file)
    if args.sort or args.reverse:
        entries = sort_entries(entries, args.reverse)

    processed_entries = process_entries(entries, date.today())

    for entry in processed_entries:
        print entry

if __name__ == "__main__":
    sys.exit(main())

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
