from lxml import etree
from bz2 import BZ2File
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

def textNode(elem):
    t = next(next(elem.iterchildren(tag='{http://www.mediawiki.org/xml/export-0.10/}revision')).iterchildren(tag='{http://www.mediawiki.org/xml/export-0.10/}text')).text
    t = re.sub("<[^<]+>", "", t)
    return t

wikipediaDataFile = "E:/Downloads/WikiData/wiki.xml"

with BZ2File(wikipediaDataFile) as wiki, open('E:/Downloads/WikiData/workfile.xml', 'w', encoding='utf-8') as output_file:
    context = etree.iterparse(wikipediaDataFile, events=('end',), tag='{http://www.mediawiki.org/xml/export-0.10/}page')
    fast_iter(context, lambda elem: output_file.write(textNode(elem)))
