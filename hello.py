import sys
import os
os.system('clear')

print("Hello",end=" ") # print "Hello" and adds a space instead of the new line
if len(sys.argv)>1: # checks whether the received user name
    print(sys.argv[1].title()+"!") # if true, print user name with uppercased
else:                              # first letter and adds "!"
    print("World!") # if false, print "World!"
