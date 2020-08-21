#!/usr/bin/python3
# coding: utf-8

from bs4 import BeautifulSoup

f = open('articleswiki.xml', 'r')
content = f.read()

soup = BeautifulSoup(content)

f2 = open('articleswiki-urs.xml', 'r')
content2 = f2.read()

f3 = open('articleswiki-urs-CT', 'w')

soup2 = BeautifulSoup(content2)



def get_mention_text(start,end):
	m = ""
	for w in soup.find_all('w'):
		n = [int(s) for s in w['id'].split("_") if s.isdigit()]
		if n[0] >= start and n[0]<=end:
			for text in w.find_all("txm:form"):
				m = m + text.getText() + " "
	return m
 
def get_mention(n):
	for m in soup2.find_all('span'):
		num = [int(s) for s in m['id'].split("-") if s.isdigit()]
		if num[0] == n:
			start = [int(s) for s in m['from'].split("_") if s.isdigit()]
			end = [int(s) for s in m['to'].split("_") if s.isdigit()]
			l = get_mention_text(start[0], end[0])
			return l

cp = 1
for c in soup2.find_all('link'):
	m = [int(s) for s in c['target'].split("-") if s.isdigit()]	
	st = str(cp)+"\n"
	f3.write (st.encode('utf-8'))
	for mention in m:
		st = get_mention(mention) + "\n"
		f3.write (st.encode('utf-8'))
	cp = cp + 1
	f3.write ("\n".encode('utf-8'))
f3.close()
f2.close()
f.close()
