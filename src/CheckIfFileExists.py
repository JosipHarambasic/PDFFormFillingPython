import os

class CheckIfFileExists:
    def __init__(self):
        return

    """Check if all the args are correct and if they exist"""
    def check(self, PDF, CSV, SavingLocation):
        if not os.path.isfile(PDF) or not PDF.endswith(".pdf"):
            print("The PDF root path does not exist, please use a Valid PDF, if something is not clear have a look at --help")
            return False
        if not os.path.isfile(CSV) or not CSV.endswith(".csv"):
            print("The CSV root path does not exist, please use a Valid CSV file, if something is not clear have a look at --help")
            return False
        if not os.path.isdir(SavingLocation):
            print("The Saving location does not exist, please use a valid Directory to save the files, if something is not clear have a look at --help")
            return False
        return True