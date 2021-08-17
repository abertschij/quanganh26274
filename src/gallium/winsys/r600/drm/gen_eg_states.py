import os
import re

def main():
    fileIN = open('eg_states.h', 'r')
    line = fileIN.readline()
    next_is_reg = False
    count = 0

    print "/* This file is autogenerated from eg_states.h - do not edit directly */"
    print "/* autogenerating script is gen_eg_states.py */"
    print ""
    while line:
        if line[0:2] == "};":
            if next_is_reg == True:
                print "#define " + name + "_SIZE\t\t", count
                print "#define " + name + "_PM4 128\t\t"
            next_is_reg = False
            count = 0
            print ""
    
        if line[0:6] == "static":
            name = line.rstrip("\n")
            cline = name.split()
            name = cline[4].split('[')
            name = name[0].replace("_names", "")
            print "/* " + name + " */"
            next_is_reg = True
        elif next_is_reg == True:
            reg = line.split();
            reg = reg[3].replace("},", "")
            reg = reg.replace("\"", "")
            print "#define " + name + "__" + reg + "\t\t", count
            count = count + 1

        line = fileIN.readline()

if __name__ == "__main__":
    main()
