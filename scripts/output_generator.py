#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:56:48 2020

@author: srihariravi
"""

from sys import argv
import getpass



def output_gen(file, input_file_name):
    username = getpass.getuser()
    file1 = open(file, 'r') 
    Lines = file1.readlines() 
    result = []
    for line in Lines:       
        if "%" in line.strip():
            if line.strip().split(":")[0].lower() not in [x.lower() for x in result]:
                result.append(line.strip().split(":")[0])
    with open('/home/'+username+'/out_' + input_file_name + '.txt', 'w') as filehandle:
        if len(result) == 0:
	    filehandle.write('no object detected')
	else:
	    for listitem in result:
                filehandle.write('%s\n' % listitem)

    print(result)
if __name__ == '__main__':
    output_gen(argv[1], argv[2])
