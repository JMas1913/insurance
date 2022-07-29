import csv

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

def load_list_data(list, insurance, column_name):
    with open('insurance.csv') as insurance:
        csv_dict = csv.DictReader(insurance)
        for row in csv_dict:
            list.append(row[column_name])
        return list

load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')

class PatientsInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, 
                patients_smoker_statuses, patients_regions, patients_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_charges = patients_charges

    def analyze_ages(self):
        total_age = 0
        for age in self.patients_ages:
            total_age += int(age)
        return (f"Average Patient Age: {str(round(total_age/len(self.patients_ages), 2))} years")

    def analyze_sexes(self):
        females = 0
        males = 0
        for sex in self.patients_sexes:
            if sex == 'female':
                females += 1
            elif sex == 'male':
                males += 1
        print(f"Count for female: {females}")
        print(f"Count for male: {males}")

    def unique_regions(self):
        unique_regions = []
        for region in self.patients_regions:
            if region not in unique_regions: 
                unique_regions.append(region)
        return unique_regions

    def average_charges(self):
        total_charges = 0
        for charge in self.patients_charges:
            total_charges += float(charge)
        return (f"Average Yearly Medical Insurance Charges: {str(round(total_charges/len(self.patients_charges), 2))} dollars.")
    
    def create_dictionary(self):
        self.patients_dictionary = {}
        self.patients_dictionary["age"] = [int(age) for age in self.patients_ages]
        self.patients_dictionary["sex"] = self.patients_sexes
        self.patients_dictionary["bmi"] = self.patients_bmis
        self.patients_dictionary["children"] = self.patients_num_children
        self.patients_dictionary["smoker"] = self.patients_smoker_statuses
        self.patients_dictionary["regions"] = self.patients_regions
        self.patients_dictionary["charges"] = self.patients_charges
        return self.patients_dictionary

patient_info = PatientsInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)

patient_info.analyze_ages()
patient_info.analyze_sexes()
patient_info.unique_regions()
patient_info.average_charges()
patient_info.create_dictionary()