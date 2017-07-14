#!usr/bin/env python
import os
import rows

class Document(object):
    def __init__(self, documentName):
        self.doc = rows.import_from_xls(documentName)

    def get_doc(self):
        return self.doc

    def show_doc_fields(self):
        x = self.doc

        for row in x.fields.item():
            print(row)
