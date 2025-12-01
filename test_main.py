from .main import CsvParser


def test_wrong_report():
    parser = CsvParser(open('test1.csv'))
    res = parser.get_table(['wrong column'])
    assert res == None

def test_csv_parser():
    parser = CsvParser([open('test1.csv', 'r')])
    res = parser.get_table(['position'])
    print(res)
    with open('out1.txt') as file:
        test_out = [str.split(line[:-1:], ', ') for line in file.readlines()]
        print(test_out)
        
    assert res == test_out
