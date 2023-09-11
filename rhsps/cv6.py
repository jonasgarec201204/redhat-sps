class file_editor:
    def __init__(self, file:str):
        self.file = file
    def read_content(self) -> str:
        content = ""
        with open(self.file, encoding="utf-8") as file:
            content = file.read()
        return content
    def write_into_file(self, content):
        with open(self.file, mode="w", encoding="utf-8") as file:
            print(f"{content}", file=file)
    def append_into_file(self, content):
        with open(self.file, mode="a", encoding="utf-8") as file:
            print(f"{content}", file=file)
file_editor1 = file_editor("text.txt")
print(file_editor1.read_content())
file_editor1.write_into_file("Ahoj! ")
print(file_editor1.read_content())
file_editor1.append_into_file("Ahoj! ")
print(file_editor1.read_content())
