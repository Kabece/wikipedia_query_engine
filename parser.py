import time
from lxml import etree
import re

def fast_iter(context, func):
        for event, elem in context:
            if elem is not None:
                func(elem)
            elem.clear()
            for ancestor in elem.xpath('ancestor-or-self::*'):
                while ancestor.getprevious() is not None:
                    del ancestor.getparent()[0]
        del context

def safeWrite(output_file, elem):
    textWithoutXML = next(next(elem.iterchildren(tag='{http://www.mediawiki.org/xml/export-0.10/}revision'))
                          .iterchildren(tag='{http://www.mediawiki.org/xml/export-0.10/}text')).text
    if textWithoutXML is not None:
        textWithoutXML = re.sub("<[^<]+>", "", textWithoutXML)
        output_file.write(textWithoutXML)

wikipediaDataFile = "E:/Downloads/WikiData/wiki.xml"

with open("D:/WikiData/workfile.xml", 'w', encoding='utf-8') as output_file:
    start_time = time.clock()
    context = etree.iterparse(wikipediaDataFile, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}page')
    fast_iter(context, lambda elem: safeWrite(output_file, elem))
    print(time.clock() - start_time, "seconds")
