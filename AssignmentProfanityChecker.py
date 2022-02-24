import argparse
import docx2txt
from pdfminer.high_level import extract_text
import openpyxl
import csv
import json
import string

def main():
    # adds an argument to the program requiring a file name at run.
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename

    assignmentText = processFileType(filename)
    profanityCheck = checkProfanity(assignmentText)
    evaluateProfanityResults = evaluateProfanity(profanityCheck,filename)

def processFileType(filename):
    # if statements to check incoming file for filetype.
    if filename.endswith('.txt'):
        with open(filename,'r') as openFile:
            assignmentText = openFile.read()
    elif filename.endswith('.docx') or filename.endswith('.doc'):
        assignmentText = docx2txt.process(filename)
    elif filename.endswith('.pdf'):
        assignmentText = extract_text(filename)
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
            csvTuple = list(csv_reader)
            assignmentText = []
            for item in csvTuple:
                for tupleItem in item:
                    assignmentText.append(tupleItem)

    return assignmentText

def checkProfanity(assignmentText):
    # opens file with profanity and turns it into a profanity word list.
    with open('WordList.json') as wordList:
        wordListDict = json.load(wordList)
        if isinstance(assignmentText,str):
            assignmentTextProcess = assignmentText.lower().split()
        elif isinstance(assignmentText,list):
            assignmentTextProcess = []
            for item in assignmentText:
                if isinstance(item,str):
                    itemLower = item.lower()
                    assignmentTextProcess.append(itemLower)
                if isinstance(item,list):
                    assignmentTextMap = (map(lambda x: x.lower(), item))
                    assignmentTextProcess.append(list(assignmentTextMap))
        assignmentTextProcessPunc = [''.join(letter for letter in word if letter not in string.punctuation) for word in assignmentTextProcess]
        textMatch = [x for x in assignmentTextProcessPunc if x in wordListDict.keys()]

        return wordListDict,textMatch

def evaluateProfanity(profanityCheck,filename):
    wordListDict = profanityCheck[0]
    textMatch = profanityCheck[1]
    dictMatch = []

    for i in textMatch:
        for k,v in wordListDict.items():
            if i == k:
                dictMatch.append(v)

if __name__ == '__main__':
    main()