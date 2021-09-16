from pdfrw import PdfReader
import os

class PDFFileValidation:

    def __init__(self):
        return

    """make check of the -o flag, and the PDF file"""
    def checkPDFWithOFlag(self,PDFPath):
        if not os.path.isfile(PDFPath):
            print("The PDF could not be found, please use a valid PDf")

        elif os.path.isfile(PDFPath) and (PDFPath.endswith(".pdf")):
            pdf = PdfReader(PDFPath)
            for i in pdf.Root.Pages.Kids[0].Annots:
                print(i.T)
        else:
            print("The -flag don't match the file please use -o or --ordtype with a PDF file, else have a look at --help")

    """make check of the -f flag, and the PDF file"""
    def checkPDFWithFFlag(self,PDFPath):
        if not os.path.isfile(PDFPath):
            print("The PDF could not be found, please use a valid PDF")

        elif os.path.isfile(PDFPath) and (PDFPath.endswith(".pdf")):
            pdf = PdfReader(PDFPath)
            for i in pdf.Root.Pages.Kids[0].Annots:
                print(i.T)
                print(i.FT)
        else:
            print("the -flag don't match the file please use -f or --fieldord with a PDF file, else have a look at --help")


    """make check of the T flag, and the PDF file"""
    def checkPDFWithTFlag(self,PDFPath):
        if not os.path.isfile(PDFPath):
            print("The PDF could not be found, please use a valid PDF")

        elif os.path.isfile(PDFPath) and (PDFPath.endswith(".pdf")):
            pdf = PdfReader(PDFPath)
            for i in pdf.Root.Pages.Kids[0].Annots:
                print(i.FT)
        else:
            print("the -flag don't match the file please use -t or --fieldtype with a PDF file, else have a look at --help")
