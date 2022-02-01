import csv


class Machine:
    def __init__(self, name):
        self.name = name

    def create_machine(self):
        with open(self.name + ".csv", 'w') as csv_file:
            fieldnames = ["text","CH","MV", "material","PRIX" ,"PPV", "PPCP", "PMCP", "PPCT","PMCT", "PPMF", "TPCP", "TPCT"]

            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()

            with open("machines.csv",'a') as csv_list:
                fieldnames = ["name"]
                csv_writer = csv.DictWriter(csv_list, fieldnames=fieldnames)
                csv_writer.writerow({'name':self.name})

    def add_material(self, CH,MV,material,PRIX, PPV, PPCP, PMCP, PPCT,PMCT ,PPMF, TPCP, TPCT):
        with open(self.name + ".csv", 'a') as csv_file:
            fieldnames = ["name", "material", "PPV", "PPCP", "PMCP", "PPCT", "PPMF", "TPCP", "TPCT"]
            csv_writer = csv.DictWriter(csv_file, fieldnames)
            csv_writer.writerow(
                {'text': self.name,'CH':CH ,'MV':MV,'PRIX':PRIX,'material': material, 'PPV': PPV, 'PPCP': PPCP, 'PMCP': PMCP, 'PPCT': PPCT,
                 'PMCT':PMCT,'PPMF': PPMF, 'TPCP': TPCP, 'TPCT': TPCT})

    def get_material_list(self):
        list = []
        with open(self.name + ".csv", 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                list.append(line)
            return list

    def get_material(self, material):
        with open(self.name + ".csv", 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                if line['text'] == material:
                    print(line)
                    return line

def load_machines():
    list = []
    with open("machines.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            list.append(line)
        return list
