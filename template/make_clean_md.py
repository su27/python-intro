#!/usr/bin/env python
# coding=utf-8

import re
import sys

IGNORE_RE = re.compile(
    r'^name:.*|'
    '^layout:.*|'
    '^class:.*|'
    '^template:.*|'
    '^\.pull-left.*|'
    '^\.pull-right.*|'
    '^\.right-column.*|'
    '^\]$'
    )

IGNORE_SECTION_RE = re.compile(
    '^\.left-column.*'
    )

SECTION_END_RE = re.compile('^\].*')

def main():
    stop_output = False
    for line in sys.stdin:
        if stop_output:
            if SECTION_END_RE.match(line.strip()):
                stop_output = False
            continue

        if IGNORE_SECTION_RE.match(line.strip()):
            stop_output = True
            continue

        m = IGNORE_RE.match(line.strip())
        if not m:
            sys.stdout.write(line)

if __name__ == '__main__':
    main()
