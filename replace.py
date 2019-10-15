#!/usr/bin/env python
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage:', sys.argv[0], 'filename'
        exit()
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        content = f.read()
    res = content.replace(' ', '').replace('\t', '').replace('\n', '')
    print 'Result:', res

