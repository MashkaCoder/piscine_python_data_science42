class Research:
    def file_reader(self) -> str:
        file = open('data.csv', 'r')
        text = file.read()
        file.close()
        return text


def main():
    res = Research()
    print(res.file_reader())


if __name__ == "__main__":
    main()
