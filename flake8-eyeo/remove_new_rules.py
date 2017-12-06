#!/usr/bin/python
import re
import sys

# After running flake8 on files, use this to discover how many bugs are now
# being caught by your new rules. Add new error codes to the regex.

if len(sys.argv) < 2:
    print 'Input a filename. Ex:\n    ./remove_new_rules.py output_file'
    sys.exit()

file = sys.argv[1]

infile = open(file, 'r')

# Clear the outfile's old data, and re-open it for appending
outfile = open('outfile', 'w')
outfile.write('')
outfile = open('outfile', 'a')

new_bugs = 0
old_bugs = 0
total_lines = 0

for line in infile:
    total_lines += 1
    match = re.search(r'(A371|A370|A305|A306|A304|A420)', line)
    if match:
        new_bugs += 1
    else:
        outfile.write(line)
        old_bugs += 1


print 'Found {} new bugs and {} old bugs out of {} total bugs.'.format(
      new_bugs, old_bugs, total_lines)
