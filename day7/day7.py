TOTAL_AVAILABLE_DISK_SPACE = 70000000
UPDATE_REQUIRED_DISK_SPACE = 30000000

class FileObject:
    def __init__(self, name, path, size=0):
        self.name = name
        self.path = path
        self.size = size

class FolderObject(FileObject):
    def __init__(self, name, path, size=0):
        super().__init__(name, path, size)
        self.contents = []

    def add_item(self, item):
        self.contents.append(item)

    def increment_size(self, size):
        self.size += size
        if self.path == '/':
            return

        folder = next(
                (item for item in directory_list if item.path == ascend_directory(self.path) and isinstance(item, FolderObject)),
                None
                )
        folder.increment_size(size)


def ascend_directory(directory: str) -> str:
    temporary_split = directory.split('/')
    directory = '/'.join(temporary_split[0:-2])+'/'
    return directory

input_data = []

with open('input') as file:
    input_data = [l.splitlines()[0].split() for l in file]

current_directory_locator = ''
directory_list = [FolderObject('/', '/')]

for line in input_data:
    if line[0] == '$':
        if line[1] == "cd":
            cd = line[2]
            if cd == "..":
                current_directory_locator = ascend_directory(current_directory_locator)
            else:
                current_directory_locator += cd + '/' if cd != '/' else '/'
    else:
        if line[0] == "dir":
            folder = FolderObject(line[1], current_directory_locator+line[1]+'/')
            directory_list.append(folder)
            
        elif line[0].isdigit():
            file = FileObject(line[1], current_directory_locator, int(line[0]))
            folder = next(
                (item for item in directory_list if item.path == current_directory_locator and isinstance(item, FolderObject)),
                None
                )
            folder.add_item(file)
            folder.increment_size(file.size)


current_size = 0
for x in directory_list:
    if x.size < 100000:
        current_size+=x.size

UNUSED_SPACE = TOTAL_AVAILABLE_DISK_SPACE - directory_list[0].size

size_list = [item.size for item in directory_list]
valid_size_list = [size for size in size_list if size > (UPDATE_REQUIRED_DISK_SPACE - UNUSED_SPACE)]
print(current_size)             # Part 1
print(min(valid_size_list))     # Part 2
