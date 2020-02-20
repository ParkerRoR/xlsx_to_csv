import csv, xlrd
from stocsv import Csv_generator as scsv
ctt_file_name = 'contatos.xlsx'
sh = xlrd.open_workbook(ctt_file_name).sheet_by_index(0)

class Excel:
    def __init__(self, sh):
        self.sh = sh
        self.nomes = []
        self.tel1 = []

        self.nlinhas = self.sh.nrows

    def armazenarValores(self):
        for i in range(self.nlinhas):
            if i == 0:
                pass
            else:
                self.nomes.append(str(self.sh.cell_value(i,0)))
                self.tel1.append(str(self.sh.cell_value(i,1)))
                self.nomes[i-1] = self.nomes[i-1].replace('.0','')
                self.tel1[i-1] = self.tel1[i-1].replace('.0','')

    def criarCsv(self):
        csv = scsv(self.nomes, self.tel1)
        csv.criar_csv()

ex = Excel(sh)
ex.armazenarValores()
ex.criarCsv()