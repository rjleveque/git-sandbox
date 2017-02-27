#!/usr/bin/env python

"""
Sample test script.

"""

# use print function so this script works in Python 2 or 3:
from __future__ import print_function

x = 1
y = 2
z = x + y
expected_sum = 3

# informative error message in case test fails:
error_message = 'x = %g, y = %g, x+y=%g disagrees with expected sum = %g' \
    % (x,y,z,expected_sum)

# the real test:
assert z==expected_sum, error_message

print("Runs fine!")  # only if assert passes

