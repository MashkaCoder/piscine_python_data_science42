import sys
import os


class Research:
    def __init__(self, path: str) -> None:
        self.path = path

    def __chech_header(self, header: str) -> bool:
        if not header:
            return False
        header_list = header.split(",")
        if (len(header_list)) != 2:
            return False
        if len(header_list[0].replace(" ", "")) == 0 or header_list[1] == '\n':
            return False
        return True

    def __chek_lines(self, line: str) -> bool:
        valid = [['1', '0'], ['0', '1']]
        line_list = line.replace("\n", '').split(',')
        if len(line_list) != 2:
            return False
        return line_list in valid

    def file_reader(self, has_header=True) -> list:
        if not os.access(self.path, os.F_OK):
            raise FileNotFoundError(self.path)
        if not os.access(self.path, os.R_OK):
            raise PermissionError("Permission denied ", self.path)
        res_list = []
        count_csv_lines = 0
        with open(self.path, 'r') as file:
            if has_header:
                header = file.readline()
                if self.__chek_lines(header):
                    has_header = False
                else:
                    if not self.__chech_header(header):
                        raise ValueError("Incorrect format header")
                    if header.replace('\n', '') == "0,1" or header.replace('\n', '') == "1,0":
                        has_header = False
            if not has_header:
                numbers = []
                header = header.split(",")
                for ch in header:
                    numbers.append(int(ch))
                res_list.append(numbers)
                count_csv_lines = 1
            for line in file:
                if not self.__chek_lines(line):
                    raise ValueError("Incorrect format csv line")
                numbers = []
                line = line.replace('\n', '').split(',')
                for ch in line:
                    numbers.append(int(ch))
                res_list.append(numbers)
                count_csv_lines += 1
            if count_csv_lines == 0:
                raise ValueError("Incorrect format csv line")
        file.close()
        return res_list

    class Calculations:
        def counts(self, data: list) -> tuple:
            heads = 0
            tails = 0
            for num in data:
                heads += num[0]
                tails += num[1]
            return heads, tails

        def fractions(self, data: tuple) -> tuple:
            amount = sum(data)
            fract_head = data[0]/amount * 100
            fract_tail = data[1] / amount * 100
            return fract_head, fract_tail


def main():
    if (len(sys.argv)) == 2:
        try:
            res = Research(sys.argv[1])
            data = res.file_reader()
            calc = res.Calculations()
            count = calc.counts(data)
            fract = calc.fractions(count)
            print(data)
            print(count[0], count[1])
            print(fract[0], fract[1])
        except Exception as err:
            print(type(err).__name__, err, sep=': ')

    else:
        print("Wrong number of parameters")


if __name__ == "__main__":
    main()
