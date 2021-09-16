import inspect
import CheckIfFileExists
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

class PDFFilling:
    def __init__(self):
        return

    def createFilledPDF(self,PDF, CSV, SavingDirectory):
        check = CheckIfFileExists.CheckIfFileExists().check(PDF, CSV, SavingDirectory)

        """If the check passed, then we can open those files and fill the PDF with the CSV's data"""
        if check:

            """open the PDF file and create a template which gets overwritten to a new filled out PDF"""
            template = PdfReader(PDF)

            # "C:\\Users\\41786\\OneDrive\\Desktop\\Daten.csv"
            """open the CSV file and set the delimiters"""
            with open(CSV, newline='') as csvfile:
                csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')

                """check the length of the form fields so we can check if everything is correctly"""
                formfieldlength = len(template.Root.Pages.Kids[0].Annots)

                """set a counter to inform the user about problems that can occur and in which row and to skip the first row"""
                counter = 1

                """iterate though the csvreader and check if the length of the row is the same as the length of the fomr fields"""
                for row in csvreader:
                    if len(row) < formfieldlength:
                        print("Row number: " + str(
                            counter) + " is shorter than there actual form fields exists --> Required: " + str(
                            formfieldlength) + ", Acctual: " + str(len(row)))
                    if len(row) > formfieldlength:
                        print("Row number: " + str(
                            counter) + " is longer than there actual form fields exists --> Required: " + str(
                            formfieldlength) + ", Acctual: " + str(len(row)))

                    """fill the form fields with the rows data"""
                    for i in range(0, len(row)):
                        template.Root.Pages.Kids[0].Annots[i].update(pdfrw.PdfDict(V=(row[i]), AS=(row[i])))
                    # "C:\\Users\\41786\\OneDrive\\Desktop\\"

                    """save the filled out PDFs with the first name of the csv + the row number"""
                    if counter != 1:
                        pdfrw.PdfWriter().write(SavingDirectory + "\\" + row[0] + str(counter) + ".pdf", template)
                    counter += 1
