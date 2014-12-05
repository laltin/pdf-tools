#!/usr/bin/python

import pyPdf
import sys


def single_overlay (input_file):
    """
    returns a page object that is overlay of pages of a single pdf file
    """
    
    input = pyPdf.PdfFileReader( open(input_file, "rb") )
    page = input.getPage(0)
    
    for i in range(1, input.getNumPages()):
        page.mergePage( input.getPage(i) )
        
    return page


def multiple_overlay (input_files):
    """
    returns a page object that is overlay of first pages of given pdf files.
    this function doesn't check if overlayed pages are same size
    """
    
    input = pyPdf.PdfFileReader( open(input_files[0], "rb") )
    page = input.getPage(0)
    
    for i in range(1, len(input_files)):
        input = pyPdf.PdfFileReader( open(input_files[i], "rb") )
        page.mergePage( input.getPage(0) )
        
    return page


def main (args):
    # at least 4 arguments are needed
    if len(args) < 4:
        print "Usage: %s input1 input2... output" % args[0]
        print "Usage: %s -s input output" % args[0]
        return
    
    page = None
    if args[1] == "-s":
        # -s option: overlay pages of single pdf file
        if len(args) != 4:
            # exactly 4 arguments needed
            print "Usage: %s -s input output" % args[0]
            return
        
        input_name = args[2]
        page = single_overlay(input_name)
        
    else:
        # overlay first pages 
        input_names = args[1:-1]
        page = multiple_overlay(input_names)
    
    # output file name is last argument
    output_name = args[-1]
    
    output = pyPdf.PdfFileWriter()
    output.addPage( page )
    output.write( open(output_name, "wb") )


if __name__ == "__main__":
    main(sys.argv)
