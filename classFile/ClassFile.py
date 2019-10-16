import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


class File:
    def __init__(self, filepath='', start=0, end=None):
        self.filepath = filepath
        self.start = start
        self.current = start
        self.end = end

    def __str__(self):
        return self.filepath

    def write(self, line):
        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as file:
                file.write(line)
        else:
            with open(self.filepath, 'a') as file:
                file.write(line)

    def __add__(self, other):
        file = File(storage_path)
        with open(self.filepath, 'r') as file_1, open(other.filepath, 'r') as file_2:
            file.write(file_1.read())
            file.write(file_2.read())
        return file

    def __iter__(self):
        with open(self.filepath, 'r') as f:
            self.lines = f.readlines()
        if self.end is None:
            self.end = len(self.lines)
        return self

    def __next__(self):
        if self.current >= self.end or self.current >= len(self.lines):
            raise StopIteration

        line = self.lines[self.current]
        self.current += 1
        return line

#for line in File('123.txt'):
    #print(line)

add_1 = File('111.txt')
add_1.write('123412412\n')
add_2 = File('321.txt')
add_3 = add_1 + add_2

for line in add_3:
    print(line)

print(open(storage_path).read())
print(add_1)