import sys
import argparse


def print_file_content(file):
    with open(file, 'r') as file_object:
        lines = file_object.readlines()
        print(lines)


print_file_content('commaSheet.csv')

tup = ("Hello", "please", "don't", "delete", "me")


def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as file_object:
        for line in lst:
            file_object.write("%s\n" % line)


write_list_to_file("commaSheet.csv", tup)


def write_strings_to_file(output_file, *someLines):
    with open(output_file, 'w') as file_object:
        for line in someLines:
            file_object.write("%s\n" % line)


write_strings_to_file("commaSheet.csv", "hello", "hi", "hey", "yolo")


def read_csv(input_file):
    with open(input_file) as file_object:
        lines = file_object.readlines()
        for line in lines:
            tup = tuple(line.rstrip().split(','))
            print(tup)


read_csv("commaSheet.csv")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='A program that read, writes and/or stores text locally')
    parser.add_argument('file',
                        help='The file to process')
    parser.add_argument('destination',
                        help='The destination of a file to store the data in')

    args = parser.parse_args()
    print('File:', args.file)
    print('Destination:', args.destination)