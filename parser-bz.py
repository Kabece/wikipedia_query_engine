from lxml import etree

wikipediaDataFile = "E:/Downloads/WikiData/wiki.xml"

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
    t = etree.SubElement(r, 'text')
    t.text = next(elem.iterchildren(tag='text')).text
    return r

context = etree.iterparse(wikipediaDataFile, events=('end',), tag='page')
out = open('E:/Downloads/WikiData/workfile.xml', 'wb', 16777216)

fast_iter(context, lambda elem: out.write(etree.tostring(serialize(elem), encoding='utf-8')))
out.close
