#!/usr/bin/python

import PyPDF2
import sys
import os
import time


def merge(input_files, output_file):
    """
    merges given input pdf files into single pdf file
    """

    output = PyPDF2.PdfFileWriter()
    
    for input_file in input_files:
        input = PyPDF2.PdfFileReader( open(input_file, "rb") )

        rotate = 0
        if input_file.lower().endswith('-rotate-90.pdf'):
            rotate = 90
        elif input_file.lower().endswith('-rotate-180.pdf'):
            rotate = 180
        elif input_file.lower().endswith('-rotate-270.pdf'):
            rotate = 270
        
        for i in range(input.numPages):
            page = input.getPage(i)
            if rotate > 0:
                page = page.rotate(rotate)
            output.addPage(page)

    with open(output_file, "wb") as outputStream:
        output.write(outputStream)

    return True


def main(args):
    # if there is no argument provided, find pdfs automatically from input/ dir
    if len(args) == 1:
        root_dir = os.path.dirname(__file__)
        input_dir = os.path.join(root_dir, 'input')

        if os.path.isdir(input_dir):
            pdfs = [f for f in os.listdir(input_dir) if f.lower().endswith('.pdf')]
            args.extend([os.path.join(input_dir, f) for f in pdfs])

        output_filename = "output-%s.pdf" % int(time.time())
        args.append(os.path.join(root_dir, output_filename))

    # at least 3 arguments are needed: program name itself, input, output
    if len(args) < 3:
        print("Usage: Put all PDFs inside \"input/\" directory.")
        print("       If you want to rotate pages of a PDF file, append \"-rotate-{angle}\" to file name.")
        print("       Ex: scan-rotate-180.pdf will be rotated 180 degrees before merge")
        print("")
        print("Command line usage: %s input1... output" % args[0])
        return
    
    input_files = args[1:-1]
    output_file = args[-1]
    
    if merge(input_files, output_file):
        print('Merged PDF created: ' + output_file)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except Exception as e:
        print(e)

    input('\nPress any key to continue')
