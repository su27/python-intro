#!/usr/bin/env python
# coding=utf-8

import re
import sys

IGNORE_RE = re.compile(
    r'^name:.*|'
    '^layout:.*|'
    '^class:.*|'
    '^\.pull-left.*|'
    '^\.pull-right.*|'
    '^\.left-column.*|'
    '^\.right-column.*|'
    '^\]$'
    )


def main():
    for line in sys.stdin:
        m = IGNORE_RE.match(line.strip())
        if not m:
            sys.stdout.write(line)

if __name__ == '__main__':
    main()

