# Working with files in html format

# Importing library lxml
from lxml import etree
import requests

# Creating a request
respond = requests.get('http://docs.python.org/3')

# Showing the results
print(respond.status_code)
print(respond.headers['Content-Type'])

# Obtaining tree from the web page with the help of 'HTMLParser'
parser = etree.HTMLParser()
root = etree.fromstring(respond.text, parser)

# Showing the elements of the tree with tag 'a'
for element in root.iter('a'):
    print(element, element.attrib)
