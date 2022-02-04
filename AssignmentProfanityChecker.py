import argparse
import docx2txt
from pdfminer.high_level import extract_text

# adds an argument to the program requiring a file name at run.
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
filename = args.filename

# opens file with profanity and turns it into a profanity word list.
profanityFile = open('WordList.txt','r')
words = profanityFile.readlines()
wordList = [x[:-1] for x in words]

# function to check file for profanity.
def profanityCheck(text2parse):
    pass

# function to process plain text files.
def filterTxt():
    openFile = open(filename,'r')
    textRead = openFile.readlines()
    print(textRead)

# function to process Word documents.
def filterDocx():
    text = docx2txt.process(filename)
    print(text)

# function to process PDF files.
def filterPdf():
    text = extract_text(filename)
    print(text)

# function to process Excel or CSV files.
def filterXlsx():
    print(filename)

# if statements to check incoming file for filetype.
if filename.endswith('.txt'):
    filterTxt()
elif filename.endswith('.docx') or filename.endswith('.doc'):
    filterDocx()
elif filename.endswith('.pdf'):
    filterPdf()
elif filename.endswith('xlsx') or filename.endswith('.xls') or filename.endswith('.csv'):
    filterXlsx()