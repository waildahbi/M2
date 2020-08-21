# -*- coding: utf-8 -*-

from tempfile import NamedTemporaryFile
import shutil
import csv

filename = "pairs.csv"
tempfile = NamedTemporaryFile(mode="w", delete=False)

fields = ["mention 1", "annotation 1", "N° phrase 1", "fichier", "mention 2", "annotation 2", "N° phrase 2","resultat"]


with open(filename, "r") as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    for row in reader:
        if row["annotation 1"].split("/")[0] == row["annotation 2"].split("/")[0]:
        	print("updating row", row["resultat"])
            	row["resultat"] = "oui"
	else:
		row["resultat"] = "non"	
        writer.writerow(row)

shutil.move(tempfile.name, filename)
