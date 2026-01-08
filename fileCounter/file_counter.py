# Programmer: Anish Yarrakonda
# Lab 5: Files and Lists

# imports
from printMeFirst import print_me_first

#function count will open the file fileName and counts how many lines, words and chars
# in the file, and place each line of the file in the lineList parameter.
# The function must RETURN numOfLine, numOfWords, numOfChars as return value,
# and lineList as parameter
#
# numOfLine: number of lines in the file
# numOfWords: number of words in the file
# numOfChars: number of characters in the file
#@parm: fileName - this is the filename to be opened
#@parm: lineList - this list contains all the text in each of lines
# from the file. Each line of text is added to the list.
# Need to remove the new line feed '\n' from the line
# before adding to the list.
#@return numOfLine, numOfWords, numOfChars

def count(fileName, lineList):
    
    # Declare variables
    line = ""
    numOfLine = 0
    numOfWords = 0
    numOfChar = 0

    # Open the specified file for reading
    infile = open(fileName, 'r')

    # Priming read
    line = infile.readline()

    # While the line is not empty:
    while line != '':
        # increment numOfLine
        numOfLine += 1
        # Strip newline character
        line = line.rstrip('\n')
        # Add line to lineList
        lineList.append(line)

        # Adds number of char in line to numOfChar
        for ch in line:
            numOfChar += 1
        
        # Splits line into words which are saved in listOfWords
        listOfWords = line.split()

        # Counts the number of words in listOfWords and adds it to numOfWords
        wordsOnLine = len(listOfWords)
        numOfWords += wordsOnLine
        
        # Set line to the next line
        line = infile.readline()

    # Close file
    infile.close()

    # Returns
    return numOfLine, numOfWords, numOfChar


if __name__ == "__main__":
    # print me first
    print_me_first.print_me_first(
        lab_info = "CNET-142 Lab 5 File & List - Anish Yarrakonda",
        program_name = "file_counter.py"
        )

    # list storing lines
    actualLineList = []

    #unpack tuple to store number of lines, words, and characters
    actualNumOfLine, actualNumOfWords, actualNumOfChar = count(fileName="/Users/anish/Documents/Python Coding Practice/Intro_to_Python_Course_@Ohlone/fileCounter/test.txt", lineList=actualLineList)

    # set counters for uppercase, lowercase, spaces, digits, and sentences to 0
    numOfUpper = 0
    numOfLower = 0
    numOfSpaces = 0
    numOfDigits = 0
    numOfSentences = 0

    # check the following conditions to increment one of the above counters
    for line in actualLineList:
        for ch in line:
            if ch.isupper():
                numOfUpper+=1
            elif ch.islower():
                numOfLower+=1
            elif ch == " ":
                numOfSpaces+=1
            elif ch.isdigit():
                numOfDigits+=1
            elif ch == "." or ch == "?" or ch == "!":
                numOfSentences+=1
    
    # Loop to print out all the lines in actualLineList
    for i in range(len(actualLineList)):
        print(f"Line {i+1} : {actualLineList[i]}")
    
    # Print all of the counters
    print(f"Total number of lines: {actualNumOfLine}")
    print(f"Total number of words: {actualNumOfWords}")
    print(f"Total number of characters: {actualNumOfChar}")
    print(f"Total number of uppercase letters: {numOfUpper}")
    print(f"Total number of lowercase letters: {numOfLower}")
    print(f"Total number of spaces: {numOfSpaces}")
    print(f"Total number of digits: {numOfDigits}")
    print(f"Total number of sentences: {numOfSentences}")