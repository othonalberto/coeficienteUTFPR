#!usr/bin/env python

import rows

TIPOS = ['xls', 'xlsx', 'ods']


class Documento(object):
    def __init__(self, nomeDocumento):
        self.doc = nomeDocumento 
        self.doc_tipo = None
        self.doc_nome = None
        self.define_tipo(nomeDocumento)

    def retorna_doc(self):
        return self.doc

    def define_tipo(self, nomeDocumento):
        splitted = nomeDocumento.split('.')
        doc_nome = splitted[0]
        doc_tipo = splitted[1]

        if doc_tipo in TIPOS:
            self.doc_tipo = doc_tipo
            self.doc_nome = doc_nome
        else:
            raise ValueError(
                    'Arquivos do tipo {} não são suportados.' .format(doc_type)
            )

    def abre_doc(self):
        if self.doc_tipo == 'xls':
            self.doc = rows.import_from_xls(self.doc)
        elif self.doc_tipo == 'xlsx':
            self.doc = rows.import_from_xlsx(self.doc)
        elif self.doc_tipo == 'ods':
            self.doc = rows.import_from_ods(self.doc)
        else:
            raise Exception('Erro ao abrir o arquivo.')
