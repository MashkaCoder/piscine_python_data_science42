class Must_read:
    file = open('data.csv', 'r')
    text = file.read()
    print(text)
    file.close()


def main():
    Must_read()


if __name__ == "__main__":
    main()
