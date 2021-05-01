import csv


class CSVtools():

    def infoToCSV(self, info, header):
        data = [header, *info]
        with open('GRADO_CAREERS.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(data)
