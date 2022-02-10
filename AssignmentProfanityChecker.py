import argparse
import docx2txt
from pdfminer.high_level import extract_text

def main():
    # adds an argument to the program requiring a file name at run.
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    filename = args.filename

    assignmentText = processFileType(filename)
    checkProfanity(assignmentText)

def processFileType(filename):
    # if statements to check incoming file for filetype.
    if filename.endswith('.txt'):
        openFile = open(filename,'r')
        assignmentText = openFile.readlines()
        # print(assignmentText)
    elif filename.endswith('.docx') or filename.endswith('.doc'):
        assignmentText = docx2txt.process(filename)
        print(assignmentText)
    elif filename.endswith('.pdf'):
        assignmentText = extract_text(filename)
        print(assignmentText)
    elif filename.endswith('xlsx') or filename.endswith('.xls') or filename.endswith('.csv'):
        print(filename)

    return assignmentText

def checkProfanity(assignmentText):
    # opens file with profanity and turns it into a profanity word list.
    profanityFile = open('WordList.txt','r')
    words = profanityFile.readlines()
    wordList = [x[:-1] for x in words]

    print(assignmentText)

if __name__ == '__main__':
    main()