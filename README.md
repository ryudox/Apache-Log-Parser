# Apache-Log-Parser
Vulnerability Scanner for Apache log files

#Ensure that python 2.7.x is installed

1) Open command line and browse to the root folder (Apache Log Parser)

2) Run the command "python runthis.py <log_filename>"

3) Output will be in the output.csv file in the format of |Vulnerability|Content Log|False Positive?|

#Example Regex for different vulnerabilities:

SQL injection:
(\'|%27|%22)\d.*(SELECT|TRUNCATE|DELETE|INSERT|DROP|UNION|OR)

XSS:
(<|%3c)\w\w\w\w\w\w(%3e|>)

File Inclusion:
(..|%2e%2e)(/|%2f)
