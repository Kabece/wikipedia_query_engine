from lxml import etree

def fast_iter(context, func):
        for event, elem in context:
            func(elem.text)
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]
        del context


googleDataFile = "E:/Downloads/GoogleData/google.xml"
wikipediaDataFile = "E:/Downloads/WikiData/wiki.xml"


context = etree.iterparse(wikipediaDataFile, events=('end',), tag='title')

# with open('E:/Downloads/WikiData/workfile.xml', 'w') as f:
fast_iter(context, print)
