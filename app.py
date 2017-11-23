from datetime import datetime
from db_functions import getTopPosts, getTopAuthors, getTopErrorDays

def printLine(text):
    with open("logFile.txt", "a+") as logFile:
        logFile.write(str(datetime.now()) + ": " + text)
    print(text)


printLine("Getting the most popular three articles of all time")
postsList = getTopPosts()
for post in postsList:
    printLine("- " + post[0] + " - " + str(post[1]) + " views")

printLine("Getting the most popular article authors of all time")
authorsList = getTopAuthors()
for author in authorsList:
    printLine("- " + author[0] + " - " + str(author[1]) + " views")

printLine("Getting which days did more than 1% of requests lead to errors")
datesList = getTopErrorDays()
for date in datesList:
    printLine("- " + str(date[0].now().date()) + " - " + str(date[1]) + " %")