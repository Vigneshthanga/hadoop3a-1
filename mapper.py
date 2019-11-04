#!/usr/bin/env python
"""mapper.py"""

import sys
rc =0
val=0
cc = 0
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    #Ignore the first row as it is the feature names row
    if (rc == 0):
        rc+=1
        continue
    # split the line into words
    cc = 0
    words = line.split(',')

    for word in words:
        #Column index of GRADES_9_12_G is 19
        if (cc == 19):
            #The word can be Null as well
            if (word):
                val = float(word)

            # Mapper prints the value itself and Reducer counts the number of line
                if (val < 5000):
                    print(val)
            #break here optimizes the code as we no need to run for the non-interested columns
            break
        cc += 1

