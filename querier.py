import re
import time

filePath = r"D:/WikiData/workfile_good_one.txt"

# Compile a Regular Expression pattern from user input
def makeRegexp(query):
    # Clean user input and transcribe it to RegEx notation
    query = re.sub("\"", "", query)
    query = re.sub("\[", ".{", query)
    query = re.sub("\]", "}", query)
    pattern = re.compile(query.encode())
    return pattern


# Read file in batches
def partialRead(file, i, seek_size):
    if i > 0:
        # Move file pointer back seek_size of bits in order
        # to catch search phrases spanning between two batches of data
        file.seek(-seek_size, 1)
    while True:
        data = file.read(1024 * 1024)
        if not data:
            break
        # Use lazy generation
        yield data


with open(filePath, "rb") as file:
    query = input("Enter query to search for: ")
    start_time = time.clock()
    pattern = makeRegexp(query)
    i = 0
    for piece in partialRead(file, i, len(query.encode())): # Use size of pattern in bytes as seek_size
        for match in re.findall(pattern, piece):
            print("Match! : %s " % match.decode())
            print(time.clock() - start_time, "seconds")
        i += 1
    print("Total execution time: ", time.clock() - start_time, "seconds")
