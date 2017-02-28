# Apache-Log-Parser
Vulnerability Scanner for Apache log files

#Ensure that python 2.7.x is installed

1) Open command line and browse to the root folder (Apache Log Parser)

2) Rename the log file that you want to scan to "CTF1.log"

2) Run command python runthis.py

3) Output will be in the output.csv file in the format of |Vulnerability|Content Log|False Positive?|

#Example Regex for different vulnerabilities:

SQL injection:
(\'|%27|%22)\d.*(SELECT|TRUNCATE|DELETE|INSERT|DROP|UNION|OR)

XSS:
(<|%3c).*(%3e|>)

File Inclusion:
(..|%2e%2e)(/|%2f)
