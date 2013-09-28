#-------------------------------------------------------------------------------
# Name:        SpiderManLinks
# Purpose:	   Finding and logging links of a URL.
# Author:      Sarath Kumar
# Web    :     www.iamsarath.blogspot.com
# Created:     01/Septemper/2012
# Copyright:   (c) Sarath Kumar 2012
# Licence:     Free and open source
#-------------------------------------------------------------------------------
#!/usr/bin/env python

# Project Restarted on March 5 2013
version="1.0.1."
def main():
    pass

if __name__ == '__main__':
    main()
import urllib2
from bs4 import BeautifulSoup
import sys
import re

url="";
outfile="links.txt"
if(len(sys.argv)==2):
    url=sys.argv[1]
elif(len(sys.argv)==3):
    url=sys.argv[1]
    outfile=sys.argv[2]


print '[Spider-Man Links ', version ,' Developed and maintained by Sarath Kumar]'
print 'Specify the URL were you want to extract links(eg:http://google.com)'
if(url==""):
    url=raw_input("Enter a URL:")
    print '>>>'
try:
     html = urllib2.urlopen(url).read()
     soup = BeautifulSoup(html)
#print soup.body.get_text()
#print(soup.get_text())
     f=open(outfile,'w')
     print 'Site', soup.title.name
     for link in soup.find_all('a'):
         print '[',link.text,"] \t--> \t:",(link.get('href'))
         f.write((link.get('href')+ '\n'))
     f.close();
except:
     print 'Problem connecting URL'
print ''
print 'Developed and maintained by sarath ,www.fb.com/sarathtvmala;'
raw_input()
#Too many bugs
