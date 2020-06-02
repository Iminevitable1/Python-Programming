from sys import argv

script, filename, = argv
ice = "{} {} {}"

print(f"We are going to erase {filename}.")
print("If you don't want that press Ctrl-C.")
print("If you want that, hit RETURN.")

input("What do you wanna do ? ")

print("Opening the file....")
txt = open(filename, 'w')

print("Truncating the file.... Now don't regret that.")
txt.truncate()

print("Now please state 3 lines to put it in the txt file.")

line1 = input("line1 : ")
line2 = input("line2 : ")
line3 = input("line3 : ")
#Here there is repetition of file so we try it with other options.....
#txt.write(line1)
#txt.write('\n')
#txt.write(line2)
#txt.write('\n')
#txt.write(line3)
#txt.write('\n')

#Trying it with format feature....
#line = "{}\n{}\n{}\n" .format(line1, line2, line3)
#txt.write(line)

#Trying with join() function..
#line = (line1, line2, line3)
#txt.write('\n'.join(line) +'\n')

#Another way of doing this....
txt.write("%s\n%s\n%s\n" %(line1,line2,line3))

print("Now we are closing the file...")
txt.close()

#You can use any of the above methods for writing to the file....
