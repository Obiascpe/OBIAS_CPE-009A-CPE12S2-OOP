class FileHandler:
    def read(self):
        pass

    def write(self, text):
        pass


class TextFileReaderWriter(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def write(self, text):
        file = open(self.filename, "w")
        file.write(text)
        file.close()

    def read(self):
        file = open(self.filename, "r")
        data = file.read()
        file.close()
        return data


if __name__ == "__main__":
    obj = TextFileReaderWriter("sample.txt")

    obj.write("This is my text file.\nSecond line.")
    print(obj.read())