import CSVInformations
import CheckIfFileExists
import PDFFileValidation
import PDFFilling
from pdfrw import PdfReader
import csv
import io
import pdfforms
from reportlab.pdfgen import canvas
import os
import argparse
import pdfrw
import sys


def main():

    """Check the cmd inputs make the correct commands"""

    if len(sys.argv) == 1:
        print("have a look at --help to get more informations")

    elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
        print("""\nThis is an application that takes 3 arguments to fill out a PDF with a CSV files data
        Run the code as explained below to make a correct PDF form field filling with a CSV
        ---------------------------------------------------------------------------------------------------
        python Main.py csvPath pdfPath savingLocation
        ---------------------------------------------------------------------------------------------------
        1. path to CSV file (example C:\\Users\\Desktop\\Data.csv)
        2. path to PDF with form fields (example C:\\Users\\Desktop\\PDFwithFormFields.pdf)
        3. path to location you want to save the filled out PDF's (example C:\\Users\\Desktop)
        --------------------------------------------------------------------------------------------------
        Other commands that you can use:
        --------------------------------------------------------------------------------------------------
        -c or --pntcsv & pathToCsvFile      shows what was read from the CSV file
                                            second argument is the path to your CSV file
                                
        -o or --ordtype & pathToPDFFile     shows the order and the type of the form field
                                            second argument is path to your PDF file
                                        
        -f or --fieldord & pathToPDFFile    shows the order of the form fields, you have to order the
                                            rows of your CSV file in the same order from left to right
                                            second argument is the path to your PDF file
                                                                                                               
        -t or --fieldtype & pathToPDFFile   it shows the type of each form field
                                            second argument is the path to your PDF file
        """)

    elif sys.argv[1].endswith(".pdf") and sys.argv[2].endswith(".csv") and len(sys.argv)==4:
        PDFFilling.PDFFilling().createFilledPDF(PDF,CSV,SavingDirectory)

    elif sys.argv[1] == "-c" or sys.argv[1] == "--pntcsv" and sys.argv[2].endswith(".csv") and len(sys.argv)==3:
        CSVInformations.CSVInformations().showCSVContent(sys.argv[2])

    elif sys.argv[1] == "-o" or sys.argv[1] == "--ordtype" and sys.argv[2].endswith(".pdf") and os.path.isfile(sys.argv[2]) and len(sys.argv)==3:
        PDFFileValidation.PDFFileValidation().checkPDFWithOFlag(sys.argv[2])

    elif sys.argv[1] == "-f" or sys.argv[1] == "--fieldord" and sys.argv[2].endswith(".pdf") and os.path.isfile(sys.argv[2]) and len(sys.argv)==3:
        PDFFileValidation.PDFFileValidation().checkPDFWithFFlag(sys.argv[2])

    elif sys.argv[1] == "-t" or sys.argv[1] == "--fieltype" and sys.argv[2].endswith(".pdf") and os.path.isfile(sys.argv[2]) and len(sys.argv)==3:
        PDFFileValidation.PDFFileValidation().checkPDFWithTFlag(sys.argv[2])

if __name__ == '__main__':
    main()