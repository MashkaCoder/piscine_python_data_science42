def read_and_write() -> None:
    file_r = open("ds.csv", "r")
    file_w = open("ds.tsv", "w")
    text = file_r.read() \
        .replace("\",", "\"\t") \
        .replace(",\"", "\t\"") \
        .replace("true,", "true\t") \
        .replace("false,", "false\t")
    file_w.write(text)
    file_r.close()
    file_w.close()

if __name__ == "__main__":
    read_and_write()