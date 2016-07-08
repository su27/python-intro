#!/usr/bin/env python
# coding=utf-8

import re
import sys

IMPORT_RE = re.compile(r'^__IMPORT_(?P<filename>.*)__$')


def main():
    for line in sys.stdin:
        m = IMPORT_RE.match(line.strip())
        if not m:
            sys.stdout.write(line)
        else:
            sys.stdout.write(open(m.group('filename')).read())


if __name__ == '__main__':
    main()
