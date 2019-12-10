# Created by: Luke Heary
# Date: 12/9/19
import sys

def main():
    file = sys.argv[1]
    n = int(sys.argv[2])

    # Fastest way to input a text file, reads one line into memory at once
    uniqueNames = set()
    uniqueFirstNames = set()
    uniqueLastNames = set()
    mostCommonFirstNames = dict()
    mostCommonLastNames = dict()

    alreadyHaveSeen = set()
    specificallyUnique = set()

    with open(file) as FileObj:
        for count, line in enumerate(FileObj, start=1):
            # Gets every other line (because every other line is a name)
            if count % 2 == 1:
                cleanedLine = line.replace(" ","")
                cleanedLine = cleanedLine.split("--")
                cleanedLine = cleanedLine[0].split(",")
                firstName = cleanedLine[1]
                lastName = cleanedLine[0]
                uniqueNames.add(firstName + " " + lastName)
                uniqueFirstNames.add(firstName)
                uniqueLastNames.add(lastName)

                # These two if statements figure out the most common First and Last names
                if firstName not in mostCommonFirstNames:
                    mostCommonFirstNames[firstName] = 0
                else:
                    mostCommonFirstNames[firstName] += 1

                if lastName not in mostCommonLastNames:
                    mostCommonLastNames[lastName] = 0
                else:
                    mostCommonLastNames[lastName] += 1

                # This set of if statements figures out if the names are specifically unique
                if firstName not in alreadyHaveSeen:
                    if lastName not in alreadyHaveSeen:
                        specificallyUnique.add(firstName + " " + lastName)
                    else:
                        alreadyHaveSeen.add(lastName)
                else:
                    alreadyHaveSeen.add(firstName)

    # Gets the most common first name, and the how many times it shows up
    mostCommonFirstName = max(mostCommonFirstNames, key=mostCommonFirstNames.get)
    mostCommonFirstNameCount = str(mostCommonFirstNames[mostCommonFirstName])

    # Gets the most common last name, and the how many times it shows up
    mostCommonLastName = max(mostCommonLastNames, key=mostCommonLastNames.get)
    most_common_last_name_count = str(mostCommonLastNames[mostCommonLastName])

    # Gets the n amount of specifically unique names and appends them to a string for printing
    specificallyUniqueList = list(specificallyUnique)
    specificallyUniqueString = ""
    for i in range(n):
        specificallyUniqueString += specificallyUniqueList[i] + ", "

    print "1. Unique Count of Full Names: " + str(len(uniqueNames))
    print "2. Unique Count of First Names: " + str(len(uniqueFirstNames))
    print "3. Unique Count of Last Names: " + str(len(uniqueLastNames))
    print "4. Most Common First Name: " + mostCommonFirstName + " (appears " + mostCommonFirstNameCount + " times)"
    print "5. Most Common Last Name: " + mostCommonLastName + " (appears " + most_common_last_name_count + " times)"


    print "6. " + str(n) + " Specifically Unique Names: " + specificallyUniqueString
    print "7. "

main()