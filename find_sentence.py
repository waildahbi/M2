#!/usr/bin/python3
# coding: utf-8

import fileinput #to iterate over lines from files
import re
import string
import itertools
import csv
import glob, os
from os import path
import sys

'''
##=============================
Ce script permet de trouver le numéro de la phrase dont figure une mention
##=============================
'''

def find(p):
	if path.exists('/home/wail/Documents/mind_the_gap_v1.2/data/french/ANNODIS/' + p + '.ac'):
		f1 = open('/home/wail/Documents/mind_the_gap_v1.2/data/french/Tmp4/' + p + 'CT', "r")
		f2 = open('/home/wail/Documents/mind_the_gap_v1.2/data/french/ANNODIS/' + p + '.ac', "r")
		f3 = open('/home/wail/Documents/mind_the_gap_v1.2/data/french/Tmp4/' + p + 'CTS', "a")
		data1 = f1.readlines()
		data2 = f2.readlines()
		for line in data1:
			if "\t" in line:
				mention = line.split("\t")[0]
				for line2 in data2:
					if " " + mention + " " in line2 or re.match(r"^" + mention + " ", line2):
						i = data2.index(line2)
						sentence = data2.index(line2) + 1
						f3.write(line.strip() + "|" + str(sentence) + "\n")
						data2[i].replace(mention, "xxx")
						break
					else:
						data2[data2.index(line2)] = "xxx\n"
			else:
				f3.write(line)
		f1.close()
		f2.close()
		f3.close()


directory = '/home/wail/Documents/mind_the_gap_v1.2/data/french/Tmp4/'
for filename in os.listdir(directory):
	filename = filename.replace("CT", "")
	#find(str(sys.argv[1]))
	find(filename)
