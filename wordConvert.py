from docx import Document
import glob
import os

doc = Document()

files = glob.glob("readme.txt")
print(files)
file = input("enter text file name ") + ".txt"

with open(file, 'r', encoding='utf-8') as openfile:
    line = openfile.read()
    doc.add_paragraph(line)
    doc.save(file + ".docx")

os.system(file + ".docx")