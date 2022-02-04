import argparse
import docx2txt
from pdfminer.high_level import extract_text

parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
filename = args.filename

def profanityCheck(text2parse):
    pass

def filterTxt():
    openFile = open(filename,'r')
    textRead = openFile.readlines()
    print(textRead)

def filterDocx():
    text = docx2txt.process(filename)
    print(text)

def filterPdf():
    text = extract_text(filename)
    print(text)

def filterXlsx():
    print(filename)

if filename.endswith('.txt'):
    filterTxt()
elif filename.endswith('.docx') or filename.endswith('.doc'):
    filterDocx()
elif filename.endswith('.pdf'):
    filterPdf()
elif filename.endswith('xlsx') or filename.endswith('.xls') or filename.endswith('.csv'):
    filterXlsx()
