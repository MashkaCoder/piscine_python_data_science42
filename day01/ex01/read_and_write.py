def read_and_write() -> None:
    res = ''
    file_w = open("ds.tsv", 'w')
    with open("ds.csv", 'r') as file:
        for line in file:
            res = line.replace('false,', 'false\t')
            res = res.replace('true,', 'true\t')
            res = res.replace("\",", "\"\t")
            file_w.write(res)
    file_w.close()

if __name__ == "__main__":
    read_and_write()
