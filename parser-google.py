from lxml import etree
from copy import deepcopy

def fast_iter(context, func):
        for event, elem in context:
            func(elem)
            elem.clear()
            for ancestor in elem.xpath('ancestor-or-self::*'):
                while ancestor.getprevious() is not None:
                    del ancestor.getparent()[0]
        del context

def serialize(elem):
    r = etree.Element('SimplerRecord')
    t = etree.SubElement(r, 'Title')
    t.text = next(elem.iterchildren(tag='Title')).text

    # for c in elem.iterchildren(tag='Copyright'):
    #     r.append(deepcopy(c))
    return r


googleDataFile = "E:/Downloads/GoogleData/google.xml"
wikipediaDataFile = "E:/Downloads/WikiData/wiki.xml"


context = etree.iterparse(googleDataFile, events=('end',), tag='Record')
out = open('E:/Downloads/WikiData/workfile.xml', 'wb', 16777216)

fast_iter(context, lambda elem: out.write(etree.tostring(serialize(elem), encoding='utf-8')))
out.close()
