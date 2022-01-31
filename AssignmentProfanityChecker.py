import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename',type=argparse.FileType('r'))
args = parser.parse_args()

print(args.filename.readlines())