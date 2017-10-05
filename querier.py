from lxml import etree

def find():
    pass

filePath = "E:/Downloads/WikiData/workfile.xml"

with open(filePath, "w", encoding='utf-8') as file:
    query = input("Enter query to search for: ")
    print("Here's your query: ", query)
