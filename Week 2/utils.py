import sys
import argparse
import os


def get_file_names(folderpath, out='output.txt'):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    with open(out, 'w') as file_object:
        for files in os.listdir("."):
            print(files)
            file_object.write("%s\n" % files)


def get_all_file_names(folderpath, out='output.txt'):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    with open(out, 'w') as file_object:
        for root, subdirs, files in os.walk("."):
            for filename in files:
                print(filename)
                file_object.write("%s\n" % filename)


def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    for fNames in file_names:
        with open(fNames, 'r') as file_object:
            line = file_object.readline()
            print(line.rstrip())


def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    for fNames in file_names:
        with open(fNames, 'r') as file_object:
            lines = file_object.readlines()
            for line in lines:
                if '@' in line:
                    print(line)


def write_headlines(md_files, out='headLinesFromMD.md'):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    for fNames in md_files:
        if '.md' in fNames:
            print(fNames)
            with open(fNames, 'r') as file_object1:
                lines = file_object1.readlines()
                with open(out, 'w') as file_object2:
                    for line in lines:
                        if line.startswith('#'):
                            file_object2.write("%s\n" % line)