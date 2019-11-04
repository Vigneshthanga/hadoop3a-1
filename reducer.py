#!/usr/bin/env python
"""reducer.py"""

import sys

_sum = 0
# input comes from STDIN
for line in sys.stdin:
    _sum += 1

# do not forget to output the last word if needed!
print(_sum)

