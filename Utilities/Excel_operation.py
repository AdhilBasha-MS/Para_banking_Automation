import openpyxl


class ExcelUtil():
    def loadfile(self, path):
        self.path = path
        self.wb_obj = openpyxl.load_workbook(path)
        self.sheet = self.wb_obj.active

    def readData(self, row, col):
        return self.sheet.cell(row=row, column=col).value

