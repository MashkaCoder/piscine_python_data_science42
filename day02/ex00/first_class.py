class Must_read:
    file=open('data.csv', 'r')
    text = file.read()
    print(text)
    file.close()

if __name__ == "__main__":
    Must_read