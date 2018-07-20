
# Example: python html_parser.py Example img2.jpg

# need to install beautifulsoup4 using command "pip install beautifulsoup4"
from bs4 import BeautifulSoup
import urllib2
import sys
import socket 

# group number shown on website and image name 
group = sys.argv[1]
image = sys.argv[2]

# retrive html
url = "http://demo.caffe.berkeleyvision.org/classify_url?imageurl=http%3A%2F%2F35.173.122.2%2F" + group +"%2F" + image

try:
	response = urllib2.urlopen(url)
	
except urllib2.URLError, e:
    print "There was an error: %r" % e
    sys.exit(1)

html = response.read()

# show caffe result
soup = BeautifulSoup(html,"html5lib")

error = soup.find_all("div", ["alert", "alert-danger"])
if error != []:
	print error[0].text
	sys.exit(1)

li_tags = soup.select('li')

for item in li_tags[2:7]:
	print (item.select("a")[0].text,item.select("span")[0].text)

