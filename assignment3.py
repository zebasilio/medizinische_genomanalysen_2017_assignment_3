#! /usr/bin/env python2

'''
Before running the script, change the path of the vcf files in the files variable (line 16, 17 and 18)
to run the script, in the command line:
$chmod +x assignment3.py
$./assignment3.py > assignment3.txt
'''

import vcf
from vcf import utils
import hgvs

__author__ = 'Jose Basilio'

file_mother = "/home/jose/MedGenAn/medizinische_genomanalysen_2017_assignment_3/AmpliseqExome.20141120.NA24143.vcf"
file_father = "/home/jose/MedGenAn/medizinische_genomanalysen_2017_assignment_3/AmpliseqExome.20141120.NA24149.vcf"
file_son = "/home/jose/MedGenAn/medizinische_genomanalysen_2017_assignment_3/AmpliseqExome.20141120.NA24385.vcf"

class Assignment3:
    
    def __init__(self):
        ## Check if pyvcf is installed
        print "PyVCF version: %s" % vcf.VERSION
        ## Check if hgvs is installed
        print "HGVS version: %s" % hgvs.__version__


    def get_total_number_of_variants_mother(self):
        print "\n+++++++++++++++++++\nReturn the total number of identified variants in the mother:"
        count = 0
        for line in vcf.Reader(open(file_mother, "r")):
            count += 1
        print count
        return count
            
        
    def get_total_number_of_variants_father(self):
       print "\n+++++++++++++++++++\nReturn the total number of identified variants in the father:"
       count = 0
       for line in vcf.Reader(open(file_father, "r")):
            count += 1
       print count
       return count
       
        
    def get_variants_shared_by_father_and_son(self):
       print "\n+++++++++++++++++++\nReturn the number of identified variants shared by father and son:"
       count = 0
       lines = utils.walk_together(vcf.Reader(open(file_father, "r")), vcf.Reader(open(file_son, "r")))
       for entry in lines:
           if not entry[0] is None and not entry[1] is None:
               count += 1
       print count
       return count
        
        
    def get_variants_shared_by_mother_and_son(self):
        print "\n+++++++++++++++++++\nReturn the number of identified variants shared by mother and son:"
        count = 0
        lines = utils.walk_together(vcf.Reader(open(file_mother, "r")), vcf.Reader(open(file_son, "r")))
        for entry in lines:
           if not entry[0] is None and not entry[1] is None:
               count += 1
        print count
        return count
        
    def get_variants_shared_by_trio(self):
        print "\n+++++++++++++++++++\nReturn the number of identified variants shared by father, mother and son:"
        count = 0
        lines = utils.walk_together(vcf.Reader(open(file_mother, "r")), vcf.Reader(open(file_father, "r")), vcf.Reader(open(file_son, "r")))
        for entry in lines:
           if not entry[0] is None and not entry[1] is None and not entry[2] is None:
               count += 1
        print count
        return count
        

    def merge_mother_father_son_into_one_vcf(self):
        
        print "\n+++++++++++++++++++\nCreates one VCF containing all variants of the trio (merge VCFs):"
       
        merge = open ("merge.vcf", "w")
        writer = vcf.Writer(merge, vcf.Reader(open(file_mother, "r")), "\n")
        for lines in utils.walk_together(vcf.Reader(open(file_mother, "r")), vcf.Reader(open(file_father, "r")), vcf.Reader(open(file_son, "r"))):
            for entry in lines:
                if entry is not None:
                    writer.write_record(entry)
        print "merge files ok"
        
        
    def convert_first_variants_of_son_into_HGVS(self):
        '''
        Convert the first 100 variants identified in the son into the corresponding transcript HGVS.
        Each variant should be mapped to all corresponding transcripts. Pointer:
        - https://hgvs.readthedocs.io/en/master/examples/manuscript-example.html#project-genomic-variant-to-a-new-transcript
        :return: 
        '''
        print "do not know how to do it"
        
    
    def print_summary(self):
        self.get_total_number_of_variants_mother()
        self.get_total_number_of_variants_father()
        self.get_variants_shared_by_father_and_son()
        self.get_variants_shared_by_mother_and_son()
        self.get_variants_shared_by_trio()
        self.merge_mother_father_son_into_one_vcf()
        self.convert_first_variants_of_son_into_HGVS()
    
        
if __name__ == '__main__':
    print("Assignment 3")
    assignment1 = Assignment3()
    assignment1.print_summary()
    
    

