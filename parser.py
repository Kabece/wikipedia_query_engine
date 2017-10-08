from lxml import etree
import time
import re


# Iterate over XML file tag by tag in order to avoid loading whole file into memory
def iterateOverXml(context, func):
        for event, elem in context:
            # If element exists apply specified function to it
            if elem is not None:
                func(elem)
            # Clear the element after using it to free memory
            elem.clear()
            # elem.clear() doesn't take care of clearing its root
            # so we use xpath to search for all empty ancestors and delete them
            for ancestor in elem.xpath('ancestor-or-self::*'):
                while ancestor.getprevious() is not None:
                    del ancestor.getparent()[0]
        del context

# Extract <text> tag value, clear all remaining XML tags, change new lines to spaces, lowercase
# and write to file
def extractAndWrite(output_file, elem):
    # First, iterate over children of <page> tag to find <revision> tag, then find <text> tag and extract
    # its value
    textWithoutXML = next(next(elem.iterchildren(tag='{http://www.mediawiki.org/xml/export-0.10/}revision'))
                          .iterchildren(tag='{http://www.mediawiki.org/xml/export-0.10/}text')).text
    if textWithoutXML is not None:
        # Get rid of XML / HTML tags
        textWithoutXML = re.sub("<[^<]+>", "", textWithoutXML)
        # Change new lines to spaces
        textWithoutXML = re.sub("\n", " ", textWithoutXML)
        # Lowercase and write to file
        output_file.write(textWithoutXML.lower())

wikipediaDataFile = "E:/Downloads/WikiData/wiki.xml"

with open("D:/WikiData/workfile.txt", 'w', encoding='utf-8') as output_file:
    start_time = time.clock()
    # We're interested only in contents of <page> tags
    context = etree.iterparse(wikipediaDataFile, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}page')
    iterateOverXml(context, lambda elem: extractAndWrite(output_file, elem))
    print("Total execution time: ", time.clock() - start_time, "seconds")
