Additional payload checks for each vulnerabilities can be added into files in Dictionary Folder:

1) fileinclusion.txt
2) injection.txt
3) shell.txt
4) xss.txt

For additional vulnerability type, you can alter the source code: 

1) Add an additional dictionary file (for e.g. cryptography.txt)

2) Adding the logic under "for line in data:" to enumerate through the cryptography.txt file


CSV format could also be altered, Currently, there is 3 columns:

1) You will need to change the code section under #output csv

2) writer.writerow(['Potential XSS',line,'Pending'])


#Welcome to add in regex check, however it could decrease the speed of scanning. Do balance it out!