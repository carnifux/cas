reads in a bunch of files in the eu ecig format or whatever and grabs just the unique cas numbers from all the files

usage:
python3 cas.py [directory containing multiple xml files in this format] [output file]
eg
python3 cas.py ~/work/xmls ~/cas-numbers.xml
