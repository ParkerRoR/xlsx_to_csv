import csv
class Csv_generator:
    def __init__(self, nomes, telefones):
        self.nome_csv = input('Diga o nome do arquivo CSV que deseja criar: ')
        self.csvfile = open('{}.csv'.format(self.nome_csv), 'w')
        self.nomes = nomes
        self.telefones = telefones
    def criar_csv(self):
        self.csvfile.writelines('Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,Phone 1 - Type,Phone 1 - Value,Phone 2 - Type,Phone 2 - Value,Address 1 - Type,Address 1 - Formatted,Address 1 - Street,Address 1 - City,Address 1 - PO Box,Address 1 - Region,Address 1 - Postal Code,Address 1 - Country,Address 1 - Extended Address,Organization 1 - Type,Organization 1 - Name,Organization 1 - Yomi Name,Organization 1 - Title,Organization 1 - Department,Organization 1 - Symbol,Organization 1 - Location,Organization 1 - Job Description \n')
        for i in range(len(self.nomes)):
            self.csvfile.writelines('{},{},,,,,,,,,,,,,,,,,,,,,,,,,,,* myContacts,Mobile,{},,,,,,,,,,,,,,,,,,,\n'.format(self.nomes[i], self.nomes[i], self.telefones[i]))
