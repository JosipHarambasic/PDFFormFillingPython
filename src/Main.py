import inspect
import CheckIfFileExists
import pdfrw
from pdfrw import PdfReader
import csv
import io
import pdfforms
from reportlab.pdfgen import canvas
import importlib.resources as pkg
import os
import argparse
import os.path

"""We use the parser to pass arguments to the code with the command line and also to show help if necessary"""
parser = argparse.ArgumentParser(description="Fill a PDF with formfields using a CSV file")
parser.add_argument("PDFRootPath", help="Enter the root path of your PDF which has to be filled")
parser.add_argument("CSVRootPath", help="Enter the root path of the CSV document")
parser.add_argument("SavingDirectory",help="Enter the saving directory where to store the filled out PDF's")
args = parser.parse_args()

def main(PDF, CSV, SavingDirectory):
    #"C:\\Users\\41786\\OneDrive\\Desktop\\FormField.pdf"
    check = CheckIfFileExists.CheckIfFileExists().check(PDF,CSV,SavingDirectory)

    if check:
        template = PdfReader(PDF)
        #"C:\\Users\\41786\\OneDrive\\Desktop\\Daten.csv"
        with open(CSV, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            formfieldlength = len(template.Root.Pages.Kids[0].Annots)
            counter = 0
            for row in spamreader:
                if len(row) < formfieldlength:
                    print("Row number: " + str(counter) + " is to short it can cause errors filling the PDF")
                counter+=1
                for i in range(0,len(row)):
                    template.Root.Pages.Kids[0].Annots[i].update(pdfrw.PdfDict(V=(row[i]),AS=(row[i])))
                #"C:\\Users\\41786\\OneDrive\\Desktop\\"
                pdfrw.PdfWriter().write(SavingDirectory+row[0]+".pdf", template)

    else:
        print("have a look at --help if something is not clear")


if __name__ == '__main__':
    main(args.PDFRootPath, args.CSVRootPath, args.SavingDirectory)