import os, sys
import re
import collections
import codecs
import csv

data = open("CTF1.log", "r")

#output csv
f = open("output.csv", "wb")
writer = csv.writer(f)
writer.writerow( ('Vulnerability', 'Log Content', 'False Positive?') )


#File Inclusion - In fileinclusion.txt
with open('Dictionary/fileinclusion.txt') as db1:
	fileinclusions = db1.readlines()
	fileinclusions = [x.strip().lower() for x in fileinclusions]

#SQL Injection flaws - In injection.txt
with open('Dictionary/injection.txt') as db2:
	injections = db2.readlines()
	injections = [x.strip().lower() for x in injections]

#XSS flaws - In xss.txt
with open('Dictionary/xss.txt') as db3:
	xsss = db3.readlines()
	xsss = [x.strip().lower() for x in xsss]

#webshell - In shell.txt - lower case
with open('Dictionary/shell.txt') as db4: 
	webshells = db4.readlines()
	webshells = [x.strip().lower() for x in webshells]

#enumerating through the log
for line in data:
	#enumerating through the webshells list
	for webshell in webshells:
		if line.lower().find(webshell)>-1:
			print("Found %s" % webshell)
			#output to output.csv
			writer.writerow(['Potential Webshell',line,'Pending'])
			break
	
	#enumeration through the sqli list
	for injection in injections:
		if line.lower().find(injection)>-1 and (line.lower().find('select')>-1 or line.lower().find('delete')>-1 or line.lower().find('insert')>-1 or line.lower().find('truncate')>-1 or line.lower().find('drop')>-1):
			print("Found %s" % injection)
			#output to output.csv
			writer.writerow(['Potential Injection',line,'Pending'])
			break
	
	#enumeration through the file inclusion list
	for fileinclusion in fileinclusions:
		if line.lower().find(fileinclusion)>-1:
			print("Found %s" % fileinclusion)
			#output to output.csv
			writer.writerow(['Potential File Inclusion',line,'Pending'])
			break
			
	#enumeration through the xss list
	for xss in xsss:
		if line.lower().find(xss)>-1:
			print("Found %s" % xss)
			#output to output.csv
			writer.writerow(['Potential XSS',line,'Pending'])
			break
			