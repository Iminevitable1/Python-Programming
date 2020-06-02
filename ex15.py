from sys import argv

#Two arguments..
script, filename, file_name = argv

#The following line opens the file.
txt1 = open(filename)

#Then it read the file and prints it out.
print(f"Here's your file {filename} : ")
print(txt1.read())

txt1.close()

print(f"Type filename again : ")
filename = input("> ")

#Opening of file.
txt = open(file_name)

#Reading of file.
print(txt.read())

txt.close()
