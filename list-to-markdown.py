#!/usr/bin/env python3

import csv

DATABASE_FILE = 'list.csv'
OUTPUT_FILE = 'table.md'

class Entry:
    def __init__(self, name, types):
        self.name = name
        self.types = types

    def __repr__(self):
        return "{%s, types:%s}" % (self.name, self.types)

def read_csv(filename)-> [Entry]:
    entries = []
    
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Ignore headers
        for row in reader:
            entries.append(Entry(row[0], row[2].split()))

    return entries

def generate_markdown_array(entries, types) -> str:
    longuest_file_name = sorted([entry.name for entry in entries], key=lambda s: len(s))[-1]
    longuest_file_name_length = len(longuest_file_name)
    yield '|' + ' ' * longuest_file_name_length + '|' + '|'.join(types) + '|'
    yield '|' + '-' * longuest_file_name_length + '|' + '|'.join(['-' * len(t) for t in types]) + '|'
    for entry in entries:
        name_length = len(entry.name)
        yield '|' + entry.name + ' ' * (longuest_file_name_length - name_length) + '|' + '|'.join([('x' if t in entry.types else ' ') + ' ' * (len(t) - 1) for t in types]) + '|'

def main():
    entries = read_csv(DATABASE_FILE)
    types = sorted(list(set(item for sublist in [entry.types for entry in entries] for item in sublist)))
    array = '\n'.join([line for line in generate_markdown_array(entries, types)])
    print(array)

if __name__ == '__main__':
    main()
