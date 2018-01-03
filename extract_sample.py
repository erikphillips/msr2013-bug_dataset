
# Created by Erik Phillips
# January 3, 2018


import json
import sys
import os
from pprint import pprint

FIELDS = [
    "assigned_to",
    "bug_status",
    # "cc",
    "component",
    # "op_sys",
    "priority",
    # "product",
    # "reports",
    "resolution",
    # "severity",
    "short_desc",
    # "version"
]


def extract_file_contents(filename):
    with open(filename) as infile:
        data = json.load(infile)
    return data


def extract_all_contents(directory):
    all_data = {}

    print "Starting field extraction..."
    for name in FIELDS:
        print "Extracting '{}'...".format(name)
        path = os.path.join(directory, (name + ".json"))
        data = extract_file_contents(path)
        all_data[name] = data[name]

    print "Finished extracting fields."
    return all_data   


def extract_sample(data):
    pass         
        

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--dir', help='directory to process')

    args = parser.parse_args()

    data = extract_all_contents(args.dir)

    pprint(data)
    # sample_data = extract_sample(data)


if __name__ == '__main__':
    main()
