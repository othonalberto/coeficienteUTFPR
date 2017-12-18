#!/usr/bin/env python


class Coeficiente(object):
    def __init__(self):
        self.horas= 0
        self.notasVezesHoras = []
        self.coeficiente = 0

    def registrarDoc(self, Documento):
        x = Documento.doc

        for item in x:
            if item.cht_3 is not None and item.media is not None:
                self.notasVezesHoras.append(item.media*item.cht_3)
                self.horas += item.cht_3

    def inserir_materia(self, Materia):
        self.notasVezesHoras.append(Materia.nota * Materia.horas)
        self.horas += Materia.horas

    def gerar_coeficiente(self, Documento=None):
        if Documento is not None:
            Documento.abre_doc()
            self.registrarDoc(Documento)

        self.coeficiente = (sum(self.notasVezesHoras) / (10*self.horas))
        
    def retorna_coeficiente(self):
        return round(self.coeficiente, 4)
