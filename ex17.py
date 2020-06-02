from sys import argv
#from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long.")

#NOT necessary....
#print(f"Does the output file exist ? {exists(to_file)}")
#print("Ready, hit Return to continue, hit Ctrl-C to abort.")
#input()

open(to_file, 'w').write(indata)

print("Alright. All done.")

open(from_file).close()
open(to_file).close()
