#!/usr/bin/env python
from pyfoo.foo import bar
import sys

if len(sys.argv)!=2:
    print("Usage: foobar.py N")
else:
    res = bar(int(sys.argv[1]))
    print('result:', res)
