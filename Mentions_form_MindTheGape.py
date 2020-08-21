#!/usr/bin/python3
# coding: utf-8

import fileinput
import re
import string
import itertools
import csv
import glob, os
import re

'''
##=============================
Ce script permet d'extreaire les mentions de la sortie disbrackets de mindTheGap
##=============================
'''

def parenthetic_contents(string):
    stack = []
    for i, c in enumerate(string):
        if c == '(':
            stack.append(i)
        elif c == ')' and stack:
            start = stack.pop()
            yield (len(stack), string[start + 1: i])


def format(s):
	line = ""
	for i,j in s:
		if j.startswith("NP "):
			j = re.sub(r'\(+[A-Z]*\+*[A-Z]+', '', j)
			j = re.sub(r'[()]', '', j)
			j = ''.join([y for y in j if not y.isdigit()])
			j = j.replace("=", "")
			j = j.replace("+", "")
			j = j.replace("-LRB-", "(")
			j = j.replace("-RRB-", ")")
			print(j + """\n""")
			print("""---------------""")
			line = line + j
	return line

def getmentions(p):
	mentions = []
	annotations = []
	result = []
	f = open('/home/wail/Documents/mind_the_gap_v1.2/data/french/Tmp/' + os.path.splitext(p)[0] + ".txt", "a")
	with open('/home/wail/Documents/mind_the_gap_v1.2/data/french/Tmp/' + p) as search:
    		for line in search:
        		line = line.rstrip()  # remove '\n' at end of line
			line = list(parenthetic_contents(line))
			line = format(line)
			f.write(str(line))
			f.write("\n")
	f.close()


directory = '/home/wail/Documents/mind_the_gap_v1.2/data/french/Tmp/'
for filename in os.listdir(directory):
	getmentions(filename) 

