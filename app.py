from datetime import datetime
from db_functions import getTopPosts, getTopAuthors, getTopErrorDays

def printLine(text):
    with open("logFile.txt", "a+") as logFile:
        logFile.write(str(datetime.now()) + ": " + text)
    print(text)


printLine("Getting the most popular three articles of all time")
printLine(getTopPosts())

printLine("Getting the most popular article authors of all time")
printLine(getTopAuthors())

printLine("Getting which days did more than 1% of requests lead to errors")
printLine(getTopErrorDays())