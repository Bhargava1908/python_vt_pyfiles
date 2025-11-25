"""
OS Module:
OS => Operating System
Used to perform Operation on file system.

OS:
1. Windows (OS)
2. Mac OS
3. Linux (Ubuntu, Linux Mint, Puppy Linux, Elementary OS, Kali Linux, Parrot OS)
"""
import os



"""
1. path.dirname()
2. path.basename()
3. path.splitext()

4. path.sep()
5. path.join()
6. path.exists()
7. isdir()
7. path.abspath()
8. path.relpath()

os.mkdir()
os.makedirs()
os.rename()
7. walk()
os.getcwd()
"""
print(__file__) # Absolute Path
print(__name__) # If run directly, value will be __main__. If run from a module, value will be modulename.

# filepath = "./file1.txt"
filepath = ".\\demo.csv"
if os.path.exists(filepath):
    print("File Exists!!!")
else:
    print("File Doesn't Exist!!!")


# filepath = ".\\demo.csv"
filepath = ".\\Folder1"
if os.path.isdir(filepath):
    print("It is a Folder...")
else:
    print("It is a File...")


filepath = ".\\demo.csv"
print(os.path.abspath(filepath))

# filepath = ".\\demo.csv"
filepath = r"D:\Full Stack\Backend\Python\PythonJune2025\demo.csv"
print(os.path.isabs(filepath))

filepath = r"D:\Full Stack\Backend\Python\PythonJune2025\demo.csv"
print(os.path.dirname(filepath))

filepath = r"D:\Full Stack\Backend\Python\PythonJune2025\demo.csv"
print(os.path.basename(filepath))

path_to_folder = os.path.dirname(filepath)
folder_name = os.path.basename(path_to_folder)
print(folder_name)

filepath = r"D:\Full Stack\Backend\Python\PythonJune2025\demo.csv"
folders = os.path.split(filepath)
print(folders)

folder, filename = os.path.split(filepath)
print(folder)
print(filename)

filename_without_extension, file_extension = os.path.splitext(filename)
print(filename_without_extension, " ***************** ", file_extension)

# os.mkdir("Folder3")

# os.mkdir("Folder4\\Folder5")

# os.makedirs("Folder4\\Folder5", exist_ok=True)

# os.rename(".\\output5.txt", ".\\output5_renamed.txt")

print(os.path.join("Folder1", "Folder2", "Folder3", "Folder4"))

filename = os.path.join("Folder4", "Folder5", "my_file.txt")
my_filepath = os.path.join((os.path.dirname(__file__)), filename)
print(my_filepath)

print(os.getcwd())
