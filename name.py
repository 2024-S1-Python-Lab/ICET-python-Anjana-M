filename=input("name.txt")
try:
    with open(name.txt,'r')as file1:
        lines=file1.readlines()
    lines=[line.strip()for line in lines]
    print("Lines from the file:",lines)
except FileNotFoundError:
    print(f"Error:The file'{name.txt}' does not exist,")
