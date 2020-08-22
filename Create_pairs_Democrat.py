#!/usr/bin/python3
# coding: utf-8

import fileinput #to iterate over lines from files
import re
import string
import itertools
import glob, os
from os import path

'''
##=============================
Ce script permet à partir d'un fichier csv contenant les mentions de générer toutes les pairs de mentions possibles en utilisant la formule 
mathématique du nCr ===> https://www.aplustopper.com/combination-formula-ncr/
##=============================
'''

# La fonction tessa permet d'appliquer la formule du nCr et retourne le résultat sous forme de list contenant les paires de mentions
def tessa(source):
        result = []
        for p1 in range(len(source)):
                for p2 in range(p1+1,len(source)):
                        result.append([source[p1],source[p2]])
        return result

def read_csv():
	fin = open('test.csv', "r")
	content = fin.read().splitlines()
	del content[0]
	pairings = tessa(content)
	fin.close()
	return pairings

def write_cvs(l):
	csv_file = open("pair_mentions.csv", "w+")
	csv_file.write("mention1,annotation1,Singulier1,genre1,CT1,mention2,annotation2,Singulier2,genre2,CT2\n") 
	for pair in l:
		separator = ','
		csv_file.write(separator.join(pair) + "\n")
		#writer.writerow({"mention1": pair[0].split(",")[0], "annotation1":pair[0].split(",")[1],"Singulier1": pair[0].split(",")[2], "genre1":pair[0].split(",")[3], "CT1":pair[0].split(",")[4], "mention2": pair[1].split(",")[0], "annotation2":pair[1].split(",")[1],"Singulier2": pair[1].split(",")[2], "genre2":pair[1].split(",")[3], "CT2":pair[1].split(",")[4]})
	csv_file.close()

lapo = read_csv()
write_cvs(lapo)

