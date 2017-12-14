#!/usr/bin/python
import re
import sys

# After running flake8 on files, use this to discover how many bugs are now
# being caught by your new rules. Add new error codes to the regex.

if len(sys.argv) < 4:
    print 'Input a filename. Ex:\n    ./remove_new_rules.py input_file out_us out_eyeo'
    sys.exit()

file = sys.argv[1]

infile = open(file, 'r')
out_us = open(sys.argv[2], 'a')
out_eyeo = open(sys.argv[3], 'a')

new_bugs = 0
old_bugs = 0
total_lines = 0



for line in infile:
    total_lines += 1
    match = re.search(r'(A371|A370|A200|A421|A422|A423|A424)', line)
    if match:
        new_bugs += 1
        out_us.write(line)
    else:
        old_bugs += 1
        out_eyeo.write(line)


print 'Found {} new bugs and {} old bugs out of {} total bugs.'.format(
      new_bugs, old_bugs, total_lines)
