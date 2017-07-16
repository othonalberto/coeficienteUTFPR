#!/usr/bin/env python

import os
import rows
import document as d
import subject as s
import gpa

def main():
    grades = d.Document('t.ods')
    grades.open_doc()
    my = gpa.Gpa()

    # how to add a new subject
    example = s.Subject(6.6, 30)
    my.new_subject(example)

    my.set_gpa(grades) 

    print(my.get_gpa())

if __name__ == '__main__':
    main()
