import argparse
import csv
from tabulate import tabulate

class ArgsParser:
    def __init__(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('--files', type=argparse.FileType('r'), nargs='+')
        arg_parser.add_argument('--report', type=str, nargs='+')
        self.args = arg_parser.parse_args()

    def get_files(self):
        return self.args.files
    
    def get_report_types(self):
        return self.args.report

class CsvParser:
    def __init__(self, files):
        self.data = []
        for file in files:
            reader = csv.DictReader(file, delimiter=',', fieldnames = ['name','position','completed_tasks','performance','skills','team','experience_years'])
            reader.__next__()
            for i in reader:
                self.data.append(i)

    def get_table(self, columns:list[str], with_nums=True):
        try:
            head = columns
            result = [head]
            for row in self.data:
                result.append([row[i] for i in columns])

            if with_nums:
                result[0].insert(0,'')
                for i in range(1, len(result)):
                    result[i].insert(0, str(i))

            return result
        except KeyError:
            print("invalid report")
            return None

class Printer:
    @staticmethod
    def print_table(table, with_header=True):
        print(tabulate(tabular_data=table[1::], headers=table[0]))
            

if __name__=='__main__':
    args = ArgsParser()
    parser = CsvParser(args.get_files())
    table = parser.get_table(["position", *args.get_report_types()])
    if not table is None:
        Printer.print_table(table)