#!/usr/bin/env python
# coding=utf-8

import re
import sys

IMPORT_RE = re.compile(r'^__IMPORT_(?P<filename>.*)__$')


def main():
    for line in sys.stdin:
        # js, hosted = 'remark-0.4.6.min.js', 'http://gnab.github.com/remark/downloads/'
        # if js in line:
        #     line = line.replace(js, hosted + js)
        m = IMPORT_RE.match(line.strip())
        if not m:
            sys.stdout.write(line)
        else:
            sys.stdout.write(open(m.group('filename')).read())


if __name__ == '__main__':
    main()
