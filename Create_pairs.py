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
	fin = open('/home/wail/Documents/mind_the_gap_v1.2/data/french/Tmp3/mentions.csv', "r")
	content = fin.read().splitlines()
	del content[0]
	pairings = tessa(content)
	fin.close()
	return pairings

def write_cvs(l):
	csv_file = open("/home/wail/Documents/mind_the_gap_v1.2/data/french/Tmp3/pair_mentions.csv", "w+")
	csv_file.write("mention,fichier,annotation,genre,nombre,N°fichier,CT,mention2,fichier2,annotation2,genre2,nombre2,N°fichier2,CT2\n") 
	for pair in l:
		separator = ','
		csv_file.write(separator.join(pair) + "\n")
		#writer.writerow({"mention": pair[0].split(",")[0], "fichier":pair[0].split(",")[1],"annotation": pair[0].split(",")[2], "genre":pair[0].split(",")[3], "nombre":pair[0].split(",")[4],"N°fichier":pair[0].split(",")[5] , "CT":pair[0].split(",")[6], "mention2": pair[1].split(",")[0], "fichier2":pair[1].split(",")[1],"annotation2": pair[1].split(",")[2], "genre2":pair[1].split(",")[3], "nombre2":pair[1].split(",")[4], "N°fichier2":pair[1].split(",")[5], "CT2":pair[1].split(",")[6]})
	csv_file.close()

lapo = read_csv()
write_cvs(lapo)

