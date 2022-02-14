import argparse
import docx2txt
from pdfminer.high_level import extract_text
import openpyxl
import csv
import json

def main():
    # adds an argument to the program requiring a file name at run.
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename

    assignmentText = processFileType(filename)
    profanityCheck = checkProfanity(assignmentText)
    evaluateProfanityResults = evaluateProfanity(profanityCheck)

def processFileType(filename):
    # if statements to check incoming file for filetype.
    if filename.endswith('.txt'):
        openFile = open(filename,'r')
        assignmentText = openFile.read()
        # print(assignmentText)
    elif filename.endswith('.docx') or filename.endswith('.doc'):
        assignmentText = docx2txt.process(filename)
        # print(assignmentText)
    elif filename.endswith('.pdf'):
        assignmentText = extract_text(filename)
        # print(assignmentText)
    elif filename.endswith('xlsx') or filename.endswith('.xls'):
        workBook = openpyxl.load_workbook(filename)
        sheet = workBook.active
        assignmentText = list(sheet.values)
    elif filename.endswith('.csv'):
        pass

    return assignmentText

def checkProfanity(assignmentText):
    # opens file with profanity and turns it into a profanity word list.
    with open('WordList.json') as wordList:
        wordListDict = json.load(wordList)
        wordListDictKeys = wordListDict.keys()
        assignmentTextLower = assignmentText.lower()
        assignmentTextProcess = assignmentTextLower.split()
        textMatch = []
        for i in assignmentTextProcess:
            for w in wordListDictKeys:
                if i == w:
                    textMatch.append(i)
        print(textMatch)
        return textMatch

def evaluateProfanity(profanityCheck):
    print(len(profanityCheck))

if __name__ == '__main__':
    main()