import sys
"""
This script counts the lines in stardard input.
Input: text from the system
Output: something
Author: Yilmaz, Begum
"""

count=0
for line in sys.stdin:
	count + = 1

print (count,"lines in standard input")
