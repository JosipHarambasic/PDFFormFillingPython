import pdfrw
from pdfrw import PdfReader
import csv
import io
import pdfforms
from reportlab.pdfgen import canvas

def main():
    x = PdfReader("C:\\Users\\41786\\OneDrive\\Desktop\\FormField.pdf")
    with open("C:\\Users\\41786\\OneDrive\\Desktop\\test.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        formfieldlength = len(x.Root.Pages.Kids[0].Annots)
        for p in x.Root.Pages.Kids:
            for field in p.Annots:
                print(field.T)
        for row in spamreader:
            print(row)
            for i in range(0,formfieldlength-1):
                x.Root.Pages.Kids[0].Annots[i].update(pdfrw.PdfDict(V=str(row[i])))
            pdfrw.PdfWriter().write("C:\\Users\\41786\\OneDrive\\Desktop\\"+row[0]+".pdf", x)




if __name__ == '__main__':
    main()