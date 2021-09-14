import os
class CheckIfFileExists:
    def __init__(self):
        return

    def check(self, PDF, CSV, SavingLocation):
        if not os.path.isfile(PDF) or not PDF.endswith(".pdf"):
            print("The PDF root path does not exist, please use a Valid PDF")
            return False
        if not os.path.isfile(CSV) or not CSV.endswith(".csv"):
            print("The CSV root path does not exist, please use a Valid CSV file")
            return False
        if not os.path.isdir(SavingLocation):
            print("The Saving location does not exist, please use a valid Directory to save the files")
            return False
        return True