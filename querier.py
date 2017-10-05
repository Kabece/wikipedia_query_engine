import re

filePath = "E:/Downloads/WikiData/workfile.xml"

def makeRegexp(query):
    query = re.sub("\"", "", query)
    query = re.sub("\[", ".{", query)
    query = re.sub("\]", "}", query)
    pattern = re.compile(query)
    return pattern

with open(filePath, "r", encoding='utf-8') as file:
    query = input("Enter query to search for: ")
    makeRegexp(query)
    for i, line in enumerate(file):
        pattern = makeRegexp(query)
        for match in re.findall(pattern, line):
            print("Found on line %s: %s" % (i + 1, match))


# The '*', '+', and '?' qualifiers are all greedy; they match as much text as possible.
    # Sometimes this behaviour isn’t desired; if the RE <.*> is matched against <a> b <c>, it
    # will match the entire string, and not just <a>. Adding ? after the qualifier makes it perform
    # the match in non-greedy or minimal fashion; as few characters as possible will be matched.
    # Using the RE <.*?> will match only <a>.
