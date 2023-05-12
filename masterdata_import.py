import csv
class MasterImport():
    
    @staticmethod
    def csv_import(master_name:str) -> dict:
        with open(file=f'./master_data/{master_name}.csv',mode='r',encoding='utf-8') as params_file:
            params = [row for row in csv.DictReader(params_file)]    
        return params