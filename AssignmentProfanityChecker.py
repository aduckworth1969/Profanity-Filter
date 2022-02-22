import argparse
# from types import NoneType
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
        with open(filename,'r') as openFile:
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
        assignmentList = list(sheet.values)
        assignmentText = []
        for item in assignmentList:
            for w in item:
                assignmentText.append(w)
    elif filename.endswith('.csv'):
        with open(filename, 'r') as openFile:
            csv_reader = csv.reader(openFile)
            assignmentText = list(csv_reader)
            print(assignmentText)

    return assignmentText

def checkProfanity(assignmentText):
    # opens file with profanity and turns it into a profanity word list.
    with open('WordList.json') as wordList:
        wordListDict = json.load(wordList)
        if isinstance(assignmentText,str):
            assignmentTextLower = assignmentText.lower()
            assignmentTextProcess = assignmentTextLower.split()
        elif isinstance(assignmentText,list):
            assignmentTextProcess = []
            for item in assignmentText:
                if isinstance(item,str):
                    itemLower = item.lower()
                    assignmentTextProcess.append(itemLower)
                if isinstance(item,list):
                    assignmentTextMap = (map(lambda x: x.lower(), item))
                    assignmentTextProcess.append(list(assignmentTextMap))
            print(assignmentTextProcess)
        textMatch = [x for x in assignmentTextProcess if x in wordListDict.keys()]
        print(textMatch)
        return textMatch

def evaluateProfanity(profanityCheck):
    # print(len(profanityCheck))
    pass
if __name__ == '__main__':
    main()