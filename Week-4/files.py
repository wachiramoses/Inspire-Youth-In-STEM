#exception handling
try:
    file_name =open(r"C:\\Users\\HP\\Documents\\Inspire-Youth-In-STEM\\Week-4\\test.txt")
    print(file_name.readlines())
except FileNotFoundError:
    msg = "sorry the file does not exist"
    print(msg)