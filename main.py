import argparse

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

if __name__=='__main__':
    args = ArgsParser()

    print(args.get_files())
    print(args.get_report_types())