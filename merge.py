#!/usr/bin/python

import PyPDF2
import sys


def merge (input_files, output_file):
    """
    merges given input pdf files into single pdf file
    """

    output = PyPDF2.PdfFileWriter()
    
    for input_file in input_files:
        input = PyPDF2.PdfFileReader( open(input_file, "rb") )
        
        for i in range(input.numPages):
            output.addPage(input.getPage(i))

    with open(output_file, "wb") as outputStream:
        output.write(outputStream)

    return True


def main (args):
    # at least 3 arguments are needed: program name itself, input, output
    if len(args) < 3:
        print("Usage: %s input1... output" % args[0])
        return
    
    input_files = args[1:-1]
    output_file = args[-1]
    
    merge(input_files, output_file)


if __name__ == "__main__":
    main(sys.argv)
