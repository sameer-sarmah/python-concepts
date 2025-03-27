import xml.etree.ElementTree as ET

# Parsing XML
tree = ET.parse('./resources/bookstore.xml')
root = tree.getroot()

# Print all book titles
for book in root.findall('book'):
    title = book.find('title').text
    print(title)

# Creating XML
new_bookstore = ET.Element('bookstore')
new_book = ET.SubElement(new_bookstore, 'book', category='Physics')
title = ET.SubElement(new_book, 'title', lang='en')
title.text = 'Fundamentals of Physics'
author = ET.SubElement(new_book, 'author')
author.text = 'David Halliday'

# Convert to string and print
new_tree = ET.ElementTree(new_bookstore)
ET.dump(new_bookstore)