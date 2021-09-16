import csv
class CSVInformations:
    def __init__(self):
        return

    """Show the CSV files content"""
    def showCSVContent(self,CSVPath):
        with open(CSVPath, newline='') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for i in csvreader:
                print(i)