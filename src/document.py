#!usr/bin/env python

import rows

TYPES = ['xls', 'xlsx', 'ods']


class Document(object):
    def __init__(self, documentName):
        self.doc = documentName
        self.doc_type = None
        self.doc_name = None
        self.define_type(documentName)

    def get_doc(self):
        return self.doc

    def show_doc_fields(self):
        x = self.doc

        for row in x.fields.item():
            print(row)

    def define_type(self, documentName):
        splitted = documentName.split('.')
        doc_name = splitted[0]
        doc_type = splitted[1]

        if doc_type in TYPES:
            self.doc_type = doc_type
            self.doc_name = doc_name
        else:
            raise ValueError('Arquivos do tipo {} não são suportados. '.format(doc_type))

    def get_doc_type(self):
        return self.doc_type

    def get_doc_name(self):
        return self.doc_name

    def open_doc(self):
        if self.doc_type == 'xls':
            self.doc = rows.import_from_xls(self.doc)
        elif self.doc_type == 'xlsx':
            self.doc = rows.import_from_xlsx(self.doc)
        elif self.doc_type == 'ods':
            self.doc = rows.import_from_ods(self.doc)
        else:
            raise Exception('Erro ao abrir o arquivo.')
